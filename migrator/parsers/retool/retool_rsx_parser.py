"""Retool RSX Toolscript export -> BESSER B-UML GUIModel parser.

Parses a Retool RSX Toolscript export, either as a ``.zip`` file or as an
already-extracted directory. The export is a tree of files:

  - ``main.rsx``            entry point, ``<Include src="...">``s the rest
  - ``header.rsx`` / ``functions.rsx`` / ``src/*.rsx``  screens & fragments
  - ``lib/*.sql`` / ``lib/*.js``   query bodies bound to widgets via
    ``data="{{queryName.data}}"`` and ``<Event pluginId="queryName">``

RSX files use a JSX-like attribute syntax that is NOT valid XML (e.g.
``attr={[]}`` or ``{{ expr }}``), so a small regex-based tag tokenizer is
used instead of an XML parser. This is still a heuristic reader, not a
real JSX parser: a literal ``>`` inside a ``{{ }}`` binding expression can
in principle confuse tag-boundary detection, though this has not been
observed in practice.

The parser extracts, per logical page (each top-level ``<View>``/``<Modal>``
under ``main.rsx``'s include tree):

  - Table / TableLegacy elements  -> DataList view elements
  - their row-level actionButtons -> extra Button view elements
  - Button elements (+ bound Event/pluginId) -> Button view elements
  - Form elements + their input widgets -> Form/InputField view elements
  - top-level markdown Text elements -> Text view elements

Returns None (with a diagnostic message) if the export is missing, empty,
or contains no parseable RSX screens.
"""

import os
import re
import zipfile

from besser.BUML.metamodel.structural import DomainModel
from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement,
    Form, InputField, InputFieldType, SelectOption,
    GUIModel, Module, Screen, Text,
)

from migrator.parsers.retool._rsx_source import load_rsx_source

# Keyword -> (ButtonType, ButtonActionType) for button/query classification.
# Order matters: first matching keyword wins.
_BUTTON_MAP = [
    ('add',    (ButtonType.FloatingActionButton, ButtonActionType.Add)),
    ('create', (ButtonType.FloatingActionButton, ButtonActionType.Add)),
    ('new',    (ButtonType.FloatingActionButton, ButtonActionType.Add)),
    ('insert', (ButtonType.FloatingActionButton, ButtonActionType.Add)),
    ('save',   (ButtonType.RaisedButton,         ButtonActionType.Save)),
    ('edit',   (ButtonType.RaisedButton,         ButtonActionType.Save)),
    ('update', (ButtonType.RaisedButton,         ButtonActionType.Save)),
    ('checkout', (ButtonType.RaisedButton,       ButtonActionType.Save)),
    ('submit', (ButtonType.RaisedButton,         ButtonActionType.Save)),
    ('delete', (ButtonType.OutlinedButton,       ButtonActionType.Delete)),
    ('remove', (ButtonType.OutlinedButton,       ButtonActionType.Delete)),
    ('back',   (ButtonType.TextButton,           ButtonActionType.Cancel)),
    ('cancel', (ButtonType.TextButton,            ButtonActionType.Cancel)),
    ('close',  (ButtonType.TextButton,           ButtonActionType.Cancel)),
]

# RSX widget tag -> InputFieldType for Form-contained fields.
_FIELD_TAG_MAP = {
    'TextInput':  InputFieldType.Text,
    'TextArea':   InputFieldType.TextArea,
    'RichText':   InputFieldType.RichText,
    'Password':   InputFieldType.Password,
    'NumberInput': InputFieldType.Number,
    'Slider':     InputFieldType.Slider,
    'Checkbox':   InputFieldType.Checkbox,
    'Switch':     InputFieldType.Toggle,
    'Select':     InputFieldType.Dropdown,
    'RadioGroup': InputFieldType.RadioGroup,
    'MultiSelect': InputFieldType.MultiSelect,
    'Date':       InputFieldType.Date,
    'DateTime':   InputFieldType.DateTime,
    'Time':       InputFieldType.Time,
    'FileButton': InputFieldType.File,
    'FileUpload': InputFieldType.File,
}


_DEFAULT_CLASSIFICATION = (ButtonType.TextButton, ButtonActionType.Cancel)


def _classify(keyword_source: str):
    """Classify a (query name / button label) string into (ButtonType,
    ButtonActionType) via keyword match; default TextButton/Cancel."""
    if not keyword_source:
        return _DEFAULT_CLASSIFICATION
    lower = keyword_source.lower().strip()
    for keyword, pair in _BUTTON_MAP:
        if keyword in lower:
            return pair
    return _DEFAULT_CLASSIFICATION


def _classify_best(*candidates: str):
    """Classify from several candidate strings (e.g. bound query name,
    then visible label), preferring the first one that actually matches a
    known keyword over a generic query name like "openModal" that would
    otherwise mask an informative label.
    """
    for candidate in candidates:
        result = _classify(candidate)
        if result != _DEFAULT_CLASSIFICATION:
            return result
    return _DEFAULT_CLASSIFICATION


def _safe_name(text: str) -> str:
    """Replace non-identifier characters with underscores."""
    result = re.sub(r'[^A-Za-z0-9_]', '_', text).strip('_') or 'Element'
    if result[0].isdigit():
        result = "_" + result
    return result


def _dedupe_name(base: str, used: set) -> str:
    """Return `base`, or `base_2`/`base_3`/... if already used."""
    name = base
    i = 2
    while name in used:
        name = f"{base}_{i}"
        i += 1
    used.add(name)
    return name


# ── Tag tokenizer ───────────────────────────────────────────────────────────
# A JSX-ish tag: <Name ...attrs.../>  or  <Name ...attrs...>  or  </Name>
# Attribute values may contain arbitrarily nested {{ }} / {} expressions,
# but never a literal '<' or '>' in the RSX seen so far, so a single
# non-greedy [^<>]* is both sufficient and avoids the catastrophic
# backtracking that an alternation like (?:[^<>]|\{[^{}]*\})* causes on the
# very large multi-KB attribute blocks Retool emits for table widgets.
_TAG_RE = re.compile(r'<(/?)([A-Za-z][\w.$]*)([^<>]*?)(/?)>', re.DOTALL)


def _iter_top_level_blocks(text: str, tag_names: set):
    """Yield (tag_name, attrs_str, inner_text, full_match_span) for every
    top-level (non-nested-in-another-matched-tag-of-interest) occurrence of
    any tag in `tag_names`, matching nested same-tag opens/closes by depth
    so the inner_text is exactly the block's content.
    """
    blocks = []
    pos = 0
    n = len(text)
    while pos < n:
        m = _TAG_RE.search(text, pos)
        if not m:
            break
        is_close, tag, attrs, self_close = m.groups()
        if is_close or tag not in tag_names:
            pos = m.end()
            continue
        if self_close:
            blocks.append((tag, attrs, '', m.span()))
            pos = m.end()
            continue
        # Depth-count further opens/closes of this same tag to find the
        # matching close tag, so nested occurrences don't end the block early.
        depth = 1
        inner_start = m.end()
        search_pos = inner_start
        inner_end = n
        close_end = n
        while True:
            m2 = _TAG_RE.search(text, search_pos)
            if not m2:
                break
            is_close2, tag2, _attrs2, self_close2 = m2.groups()
            if tag2 == tag and not self_close2:
                depth += -1 if is_close2 else 1
                if depth == 0:
                    inner_end = m2.start()
                    close_end = m2.end()
                    break
            search_pos = m2.end()
        blocks.append((tag, attrs, text[inner_start:inner_end], (m.start(), close_end)))
        pos = close_end
    return blocks


def _find_all_tags(text: str, tag_names: set):
    """Flat scan for every self-closing or open tag matching `tag_names`,
    ignoring nesting -- used for widgets we only need attrs from (Table,
    Button, form fields) rather than their (possibly absent) children.
    """
    out = []
    for m in _TAG_RE.finditer(text):
        is_close, tag, attrs, _self_close = m.groups()
        if not is_close and tag in tag_names:
            out.append((tag, attrs, m.span()))
    return out


def _attr(attrs: str, key: str) -> str:
    """Extract a simple string attribute value: key="value"."""
    m = re.search(rf'\b{re.escape(key)}="([^"]*)"', attrs)
    return m.group(1) if m else None


def _bool_attr(attrs: str, key: str) -> bool:
    m = re.search(rf'\b{re.escape(key)}=\{{\s*(true|false)\s*\}}', attrs)
    return bool(m and m.group(1) == 'true')


def _resolve_include(src: str, base_dir: str) -> str:
    """Resolve a <Include src="./x.rsx"/> path against the including
    file's directory into a normalised app-root-relative posix path."""
    joined = os.path.normpath(os.path.join(base_dir, src)).replace(os.sep, '/')
    return joined.lstrip('/')


def _flatten_includes(entry: str, source: dict, _visited=None) -> str:
    """Recursively substitute <Include src="X"/> with the resolved content
    of X, producing one flattened document for `entry`."""
    if _visited is None:
        _visited = set()
    if entry in _visited or entry not in source:
        return ''
    _visited.add(entry)
    text = source[entry]
    base_dir = os.path.dirname(entry)

    def _sub(m):
        src = m.group(1)
        target = _resolve_include(src, base_dir)
        return _flatten_includes(target, source, _visited)

    return re.sub(r'<Include\s+src="([^"]+)"\s*/>', _sub, text)


def _query_name_from_binding(binding: str):
    """Extract the query name from a `{{ queryName.data ... }}` binding."""
    if not binding:
        return None
    m = re.search(r'\{\{\s*([A-Za-z_$][\w$]*)\.data', binding)
    return m.group(1) if m else None


def _submit_event_plugin(block_text: str):
    """Find the pluginId of an `<Event event="submit" .../>` inside a Form
    block, if present."""
    for tag, attrs, _span in _find_all_tags(block_text, {'Event'}):
        if _attr(attrs, 'event') == 'submit':
            return _attr(attrs, 'pluginId')
    return None


def _build_data_list(tag: str, attrs: str, query_primary_table: dict,
                      domain_model: DomainModel, used_names: set):
    widget_id = _attr(attrs, 'id') or tag
    data_binding = _attr(attrs, 'data') or ''
    query_name = _query_name_from_binding(data_binding)

    # Column list, used both for entity-name matching and as fallback fields.
    columns_m = re.search(r'_columns=\{\[(.*?)\]\}', attrs, re.DOTALL)
    columns = re.findall(r'"([^"]+)"', columns_m.group(1)) if columns_m else []

    entity_name = None
    resolved_cls = None
    if query_name and query_name in query_primary_table:
        entity_name = query_primary_table[query_name]
    elif domain_model is not None and columns:
        best_cls, best_score = None, 0.0
        for cls in domain_model.get_classes():
            attr_names = {a.name for a in cls.attributes}
            overlap = len(attr_names & {c.lower() for c in columns})
            score = overlap / max(len(attr_names), 1)
            if score > best_score:
                best_cls, best_score = cls, score
        if best_cls is not None and best_score > 0.3:
            entity_name = best_cls.name
            resolved_cls = best_cls
    if entity_name is None:
        entity_name = _safe_name(re.sub(r'Table$', '', widget_id, flags=re.IGNORECASE) or widget_id)
    if resolved_cls is None and domain_model is not None:
        resolved_cls = domain_model.get_class_by_name(entity_name)

    data_source = DataSourceElement(
        name=_safe_name(entity_name),
        dataSourceClass=resolved_cls,
        field_names=[c.lower() for c in columns] or None,
    )
    dl_name = _dedupe_name(_safe_name(f"{widget_id}_List"), used_names)
    data_list = DataList(name=dl_name, description="", list_sources={data_source})

    # Row-level action buttons embedded as JS object literals in the props.
    action_buttons = []
    for ab_m in re.finditer(
        r'\{\s*actionButtonText:\s*"([^"]*)".*?actionButtonQuery:\s*"([^"]*)"',
        attrs, re.DOTALL,
    ):
        label, query = ab_m.group(1), ab_m.group(2)
        btn_type, act_type = _classify_best(query, label)
        btn_name = _dedupe_name(_safe_name(f"{widget_id}_{label}"), used_names)
        action_buttons.append(Button(
            name=btn_name, description="", label=label,
            buttonType=btn_type, actionType=act_type,
        ))
    return data_list, action_buttons


def _build_button(attrs: str, inner: str, used_names: set):
    if _bool_attr(attrs, 'submit'):
        return None
    label = _attr(attrs, 'text') or _attr(attrs, 'label')
    widget_id = _attr(attrs, 'id') or label or 'button'
    if not label:
        label = widget_id
    plugin_id = None
    for tag, ev_attrs, _span in _find_all_tags(inner, {'Event'}):
        if _attr(ev_attrs, 'method') == 'trigger':
            plugin_id = _attr(ev_attrs, 'pluginId')
            break
    btn_type, act_type = _classify_best(plugin_id, label)
    name = _dedupe_name(_safe_name(widget_id), used_names)
    try:
        return Button(
            name=name, description="", label=label,
            buttonType=btn_type, actionType=act_type,
        )
    except ValueError:
        return None


def _build_form(attrs: str, inner: str, used_names: set):
    form_id = _attr(attrs, 'id') or 'form'
    input_fields = set()
    field_names_used = set()
    for tag, fattrs, _span in _find_all_tags(inner, set(_FIELD_TAG_MAP)):
        field_type = _FIELD_TAG_MAP[tag]
        key = _attr(fattrs, 'formDataKey') or _attr(fattrs, 'id') or tag
        options = []
        for opt_m in re.finditer(r'<Option\b[^>]*\bvalue="([^"]*)"', inner):
            options.append(SelectOption(label=opt_m.group(1), value=opt_m.group(1)))
        field_name = _dedupe_name(_safe_name(key), field_names_used)
        input_fields.add(InputField(
            name=field_name,
            description="",
            field_type=field_type,
            label=_attr(fattrs, 'label') or '',
            placeholder=_attr(fattrs, 'placeholder') or '',
            required=_bool_attr(fattrs, 'required'),
            default_value=_attr(fattrs, 'value'),
            options=options if (field_type == InputFieldType.Dropdown and options) else None,
        ))
    if not input_fields:
        return None
    submit_plugin = _submit_event_plugin(inner)
    title_m = re.search(r'<Text\b[^>]*\bvalue="([^"]*)"', inner)
    name = _dedupe_name(_safe_name(form_id), used_names)
    return Form(
        name=name,
        description="",
        inputFields=input_fields,
        title=title_m.group(1) if title_m else None,
        submit_label=submit_plugin or "Submit",
    )


def _parse_screen_content(content: str, query_primary_table: dict,
                           domain_model: DomainModel):
    """Parse a screen's flattened RSX content into a set of view elements."""
    view_elements = set()
    used_names = set()

    for tag, attrs, span in _find_all_tags(content, {'Table', 'TableLegacy'}):
        data_list, action_buttons = _build_data_list(
            tag, attrs, query_primary_table, domain_model, used_names,
        )
        view_elements.add(data_list)
        view_elements.update(action_buttons)

    for tag, attrs, inner, span in _iter_top_level_blocks(content, {'Button'}):
        btn = _build_button(attrs, inner, used_names)
        if btn is not None:
            view_elements.add(btn)

    for tag, attrs, inner, span in _iter_top_level_blocks(content, {'Form'}):
        form = _build_form(attrs, inner, used_names)
        if form is not None:
            view_elements.add(form)

    for tag, attrs, span in _find_all_tags(content, {'Text'}):
        value = _attr(attrs, 'value')
        if not value or not value.strip().lstrip('#').strip():
            continue
        widget_id = _attr(attrs, 'id') or 'text'
        name = _dedupe_name(_safe_name(widget_id), used_names)
        view_elements.add(Text(name=name, content=value, description=""))

    return view_elements


def retool_rsx_to_gui(zip_path: str, module_name: str = None,
                       domain_model: DomainModel = None) -> GUIModel:
    """Parse a Retool RSX export and return a BESSER B-UML GUIModel.

    Args:
        zip_path:     Path to the RSX export, either a ``.zip`` file or an
            already-extracted directory (parameter name kept for backward
            compatibility with existing call sites).
        module_name:  Optional name for the GUIModel and its Module.
        domain_model: Optional DomainModel for the same app; when given,
            DataList entities resolve to real Class references and better
            table->entity name matching is possible.

    Returns:
        A populated GUIModel, or None if the export is missing, empty,
        or contains no parseable screens.
    """
    if not zip_path or not os.path.exists(zip_path):
        print(f"RSX export not found: {zip_path!r}")
        return None

    name = module_name or 'RetoolGUI'
    print(f"Parsing RSX export: {os.path.basename(str(zip_path).rstrip('/\\'))}")

    source = load_rsx_source(zip_path)
    if not source:
        print("  RSX export is empty or unreadable")
        return None

    # Map query name -> primary FROM table, from lib/*.sql files.
    query_primary_table: dict = {}
    for path, text in source.items():
        if path.startswith('lib/') and path.lower().endswith('.sql'):
            query_name = os.path.splitext(os.path.basename(path))[0]
            m = re.search(r'\bFROM\s+([A-Za-z_][\w]*)', text, re.IGNORECASE)
            if m:
                query_primary_table[query_name] = m.group(1).lower()

    screens: set = set()
    used_screen_names: set = set()

    if 'main.rsx' in source:
        flattened = _flatten_includes('main.rsx', source)

        view_blocks = _iter_top_level_blocks(flattened, {'View', 'Modal'})
        consumed_spans = []
        for tag, attrs, inner, span in view_blocks:
            consumed_spans.append(span)
            is_modal = tag == 'Modal'
            screen_key = _attr(attrs, 'viewKey') or _attr(attrs, 'id') or ('Modal' if is_modal else 'View')
            screen_name = _dedupe_name(_safe_name(screen_key), used_screen_names)
            elements = _parse_screen_content(inner, query_primary_table, domain_model)
            screens.add(Screen(
                name=screen_name,
                description="",
                view_elements=elements,
                is_main_page=not is_modal,
            ))
            print(f"  Screen '{screen_name}' | elements={len(elements)}")

        # Anything not inside a consumed View/Modal block belongs to the
        # implicit root screen (e.g. the app title, top-level buttons).
        root_text = flattened
        for start, end in sorted(consumed_spans, reverse=True):
            root_text = root_text[:start] + root_text[end:]
        root_elements = _parse_screen_content(root_text, query_primary_table, domain_model)
        if root_elements:
            root_name = _dedupe_name(_safe_name(name), used_screen_names)
            screens.add(Screen(
                name=root_name,
                description="",
                view_elements=root_elements,
                is_main_page=True,
            ))
            print(f"  Screen '{root_name}' (root) | elements={len(root_elements)}")

    else:
        # Fall back to the legacy behaviour: one screen per src/*.rsx file
        # (keeps working for older exports that only contain a bare src/
        # folder without a real main.rsx).
        rsx_entries = sorted(p for p in source if re.search(r'(?:^|/)src/[^/]+\.rsx$', p))
        if not rsx_entries:
            print("  No main.rsx or src/*.rsx files found — skipping GUI extraction")
            return None
        for entry in rsx_entries:
            stem = os.path.splitext(os.path.basename(entry))[0]
            screen_name = _dedupe_name(_safe_name(stem), used_screen_names)
            elements = _parse_screen_content(source[entry], query_primary_table, domain_model)
            is_modal = bool(re.search(r'(form|modal|detail)', stem.lower()))
            screens.add(Screen(
                name=screen_name,
                description="",
                view_elements=elements,
                is_main_page=not is_modal,
            ))
            print(f"  Screen '{screen_name}' | elements={len(elements)}")

    if not screens:
        print("  No screens extracted from RSX export")
        return None

    gui_model = GUIModel(
        name=name,
        package="",
        versionCode="",
        versionName="",
        modules={},
        description="",
    )
    module = Module(name=name, screens=screens)
    gui_model.modules.update({module.name: module})
    print(f"  Total: {len(screens)} screen(s) extracted from RSX")
    return gui_model
