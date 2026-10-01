"""Retool RSX Toolscript export -> BESSER B-UML GUIModel parser.

Parses a Retool RSX Toolscript export, either as a ``.zip`` file or as an
already-extracted directory. The export is a tree of files:

  - ``main.rsx``            entry point, ``<Include src="...">``s the rest
  - ``header.rsx`` / ``functions.rsx`` / ``src/*.rsx``  screens & fragments
  - ``lib/*.sql`` / ``lib/*.js``   query bodies bound to widgets via
    ``data="{{queryName.data}}"`` and ``<Event pluginId="queryName">``

RSX files use a JSX-like attribute syntax that is not valid XML (e.g.
``attr={[]}`` or ``{{ expr }}``). A small tokenizer respects quoted strings
and brace nesting without evaluating JavaScript.

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
import html
import posixpath

from besser.BUML.metamodel.structural import DomainModel
from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement,
    Form, InputField, InputFieldType, SelectOption,
    GUIModel, Module, Screen, Text, Image,
)

from migrator.parsers.retool._rsx_source import load_rsx_source
from migrator.parsers.retool._sql_source import sql_tables
from migrator.parsers.retool.retool_csv_parser import _normalize_stem, _to_pascal
from besser.BUML.metamodel.gui.binding import DataBinding
from besser.BUML.metamodel.gui.dashboard import BarChart, LineChart, PieChart, Chart, Series
from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition

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
    'DateRange':  InputFieldType.DateRange,
    'Tags':       InputFieldType.Tags,
    'DateTime':   InputFieldType.DateTime,
    'Time':       InputFieldType.Time,
    'FileButton': InputFieldType.File,
    'FileUpload': InputFieldType.File,
}


_DEFAULT_CLASSIFICATION = (ButtonType.TextButton, ButtonActionType.RunMethod)


def _classify(keyword_source: str):
    """Classify a (query name / button label) string into (ButtonType,
    ButtonActionType) via keyword match; default TextButton/Cancel."""
    if not keyword_source:
        return _DEFAULT_CLASSIFICATION
    lower = re.sub(r'([a-z])([A-Z])', r'\1 \2', keyword_source).lower().strip()
    for keyword, pair in _BUTTON_MAP:
        if re.search(rf'(?<![a-z]){keyword}(?![a-z])', lower):
            return pair
    return _DEFAULT_CLASSIFICATION


def _classify_best(*candidates: str):
    """Classify from several candidate strings (e.g. bound query name,
    then visible label), preferring the first one that actually matches a
    known keyword over a generic query name like "openModal" that would
    otherwise mask an informative label.
    """
    for candidate in candidates:
        if candidate:
            words = re.sub(r'([a-z])([A-Z])', r'\1 \2', candidate).lower()
            if any(re.search(rf'(?<![a-z]){keyword}(?![a-z])', words) for keyword, _ in _BUTTON_MAP):
                return _classify(candidate)
    return None


def _event_signal(inner: str):
    """Classify a button from its wired-up Events, when they conclusively
    signal an action type - this takes priority over guessing from the
    caption, since it reflects what the button actually does.

    A `type="datasource" method="trigger"` event runs a named query,
    and Retool query names are real ground truth for CRUD intent (e.g.
    `pluginId="deleteProduct"`), not a label-text guess. `type="widget"`
    events are structural, independent of either name: `show`/`open`
    reveals another widget (typically a modal) and `hide`/`close` dismisses
    one, regardless of what the button or target happens to be called -
    e.g. a "Setup Guide" button that only `show`s a modal is navigating,
    not cancelling, even though its caption matches no keyword.
    Returns None, not a default, when nothing conclusive is found, so the
    caller can still fall back to a caption-based guess before giving up.
    """
    trigger_plugin_id = None
    widget_methods = []
    for _, ev_attrs, _ in _find_all_tags(inner, {'Event'}):
        ev_type = _attr(ev_attrs, 'type')
        method = _attr(ev_attrs, 'method')
        if ev_type == 'datasource' and method == 'trigger' and trigger_plugin_id is None:
            trigger_plugin_id = _attr(ev_attrs, 'pluginId')
        elif ev_type == 'widget':
            widget_methods.append(method)
    if trigger_plugin_id:
        pair = _classify_best(trigger_plugin_id)
        if pair is not None:
            return pair
    if any(method in ('hide', 'close') for method in widget_methods):
        return (ButtonType.TextButton, ButtonActionType.Cancel)
    if any(method in ('show', 'open') for method in widget_methods):
        return (ButtonType.TextButton, ButtonActionType.Navigate)
    return None


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
_TAG_START = re.compile(r'<(/?)([A-Za-z][\w.$]*)\b')


def _scan_tags(text):
    """Tokenize tags while respecting quoted strings and JSX brace depth."""
    text = re.sub(r'<!--.*?-->|\{/\*.*?\*/\}', lambda m: ' ' * len(m[0]), text, flags=re.DOTALL)
    pos = 0
    while match := _TAG_START.search(text, pos):
        start, i = match.start(), match.end()
        attrs_start = i
        quote, depth = None, 0
        while i < len(text):
            char = text[i]
            if quote:
                if char == '\\':
                    i += 2
                    continue
                if char == quote:
                    quote = None
            elif char in '"\'`':
                quote = char
            elif char == '{':
                depth += 1
            elif char == '}':
                depth = max(0, depth - 1)
            elif char == '>' and depth == 0:
                attrs = text[attrs_start:i]
                self_close = attrs.rstrip().endswith('/')
                if self_close:
                    attrs = attrs.rstrip()[:-1]
                yield bool(match[1]), match[2], attrs, self_close, (start, i + 1)
                break
            i += 1
        pos = i + 1


def _iter_top_level_blocks(text: str, tag_names: set):
    """Return non-overlapping blocks for the requested tags."""
    tokens = list(_scan_tags(text))
    blocks, index = [], 0
    while index < len(tokens):
        close, tag, attrs, self_close, span = tokens[index]
        index += 1
        if close or tag not in tag_names:
            continue
        if self_close:
            blocks.append((tag, attrs, '', span))
            continue
        depth, inner_end, end = 1, len(text), len(text)
        while index < len(tokens):
            close2, tag2, _, self_close2, span2 = tokens[index]
            index += 1
            if tag2 == tag and not self_close2:
                depth += -1 if close2 else 1
                if depth == 0:
                    inner_end, end = span2
                    break
        blocks.append((tag, attrs, text[span[1]:inner_end], (span[0], end)))
    return blocks


def _find_all_tags(text: str, tag_names: set):
    return [(tag, attrs, span) for close, tag, attrs, _, span in _scan_tags(text)
            if not close and tag in tag_names]


def _attr(attrs: str, key: str) -> str:
    """Extract a simple string attribute value: key="value"."""
    match = re.search(rf"(?<![\w]){re.escape(key)}\s*=\s*([\"'])(.*?)\1", attrs, re.DOTALL)
    return html.unescape(match[2]) if match else None


def _bool_attr(attrs: str, key: str) -> bool:
    m = re.search(rf'\b{re.escape(key)}=\{{\s*(true|false)\s*\}}', attrs)
    return bool(m and m.group(1) == 'true')


def _resolve_include(src: str, base_dir: str) -> str:
    """Resolve a <Include src="./x.rsx"/> path against the including
    file's directory into a normalised app-root-relative posix path."""
    joined = posixpath.normpath(posixpath.join(base_dir, src))
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
        return _flatten_includes(target, source, _visited.copy())

    return re.sub(r'<Include\s+src="([^"]+)"\s*/>', _sub, text)


def _query_name_from_binding(binding: str):
    """Extract the query name from a `{{ queryName.data ... }}` binding."""
    if not binding:
        return None
    m = re.search(r'\b([A-Za-z_$][\w$]*)\.data\b', binding)
    return m.group(1) if m else None


def _submit_event_plugin(block_text: str):
    """Find the pluginId of an `<Event event="submit" .../>` inside a Form
    block, if present."""
    for tag, attrs, _span in _find_all_tags(block_text, {'Event'}):
        if _attr(attrs, 'event') == 'submit':
            return _attr(attrs, 'pluginId')
    return None


def _resolve_class(domain_model, table_name):
    if domain_model is None or not table_name:
        return None
    expected = _to_pascal(_normalize_stem(table_name)).lower()
    return next((cls for cls in domain_model.get_classes()
                 if cls.name.lower() == expected), None)


def _build_input(tag, attrs, inner, used_names):
    options = []
    for _, option_attrs, _ in _find_all_tags(inner, {'Option'}):
        value = _attr(option_attrs, 'value')
        if value is not None:
            options.append(SelectOption(label=_attr(option_attrs, 'label') or value, value=value))
    key = _attr(attrs, 'formDataKey') or _attr(attrs, 'id') or tag
    return InputField(
        name=_dedupe_name(_safe_name(key), used_names), description='',
        field_type=_FIELD_TAG_MAP[tag], label=_attr(attrs, 'label') or '',
        placeholder=_attr(attrs, 'placeholder') or '',
        required=_bool_attr(attrs, 'required'), default_value=_attr(attrs, 'value'),
        disabled=_bool_attr(attrs, 'disabled'), readonly=_bool_attr(attrs, 'readOnly'),
        options=options or None,
    )


def _build_chart(attrs, inner, query_primary_table, domain_model, used_names):
    series_tags = _find_all_tags(inner, {'Series'})
    chart_type = _attr(attrs, 'chartType')
    if not chart_type:
        match = re.search(r'chartType:\s*"([^"]+)"', attrs)
        chart_type = match[1] if match else None
    if not chart_type and series_tags:
        chart_type = _attr(series_tags[0][1], 'type')
    chart_class = {'line': LineChart, 'bar': BarChart, 'pie': PieChart}.get(chart_type, Chart)
    chart = chart_class(name=_dedupe_name(_safe_name(_attr(attrs, 'id') or 'chart'), used_names))
    query_name = _query_name_from_binding(_attr(attrs, 'datasourceJS') or _attr(attrs, 'data'))
    cls = _resolve_class(domain_model, query_primary_table.get(query_name))
    if cls is not None:
        label_name = _attr(attrs, 'xAxisDropdown')
        label_field = next((a for a in cls.attributes if a.name == label_name), None)
        chart.data_binding = DataBinding(domain_concept=cls, label_field=label_field)
        # Legacy Plotly widgets describe their fields in dataseries labels.
        fields = {a.name: a for a in cls.attributes}
        for field_name in dict.fromkeys(re.findall(r'label:\s*"([^"]+)"', attrs)):
            if field_name in fields and field_name != label_name:
                chart.series.append(Series(
                    name=_safe_name(field_name), label=field_name, styling=None,
                    data_binding=DataBinding(domain_concept=cls, label_field=label_field,
                                             data_field=fields[field_name]),
                ))
    for _, series_attrs, _ in series_tags:
        query_name = _query_name_from_binding(_attr(series_attrs, 'datasource'))
        series_cls = _resolve_class(domain_model, query_primary_table.get(query_name))
        if series_cls is None:
            continue
        def bound_field(key):
            match = re.search(r'\.data\.([\w]+)', _attr(series_attrs, key) or '')
            return next((a for a in series_cls.attributes if match and a.name == match[1]), None)
        binding = DataBinding(domain_concept=series_cls, label_field=bound_field('xData'),
                              data_field=bound_field('yData'))
        chart.series.append(Series(name=_safe_name(_attr(series_attrs, 'name') or 'Series'),
                                   label=_attr(series_attrs, 'name'), data_binding=binding, styling=None))
    return chart


def _build_data_list(tag: str, attrs: str, inner: str, query_primary_table: dict,
                      domain_model: DomainModel, used_names: set):
    widget_id = _attr(attrs, 'id') or tag
    data_binding = _attr(attrs, 'data') or ''
    query_name = _query_name_from_binding(data_binding)

    # Column list, used both for entity-name matching and as fallback fields.
    columns_m = re.search(r'_columns=\{\[(.*?)\]\}', attrs, re.DOTALL)
    columns = re.findall(r'"([^"]+)"', columns_m.group(1)) if columns_m else []

    if not columns:
        columns = [key for _, cattrs, _ in _find_all_tags(inner, {'Column'})
                   if (key := _attr(cattrs, 'key'))]

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
        resolved_cls = _resolve_class(domain_model, entity_name)
    if not columns and resolved_cls is not None:
        columns = sorted(a.name for a in resolved_cls.attributes)

    data_source = DataSourceElement(
        name=_safe_name(entity_name),
        dataSourceClass=resolved_cls,
        field_names=[c.lower() for c in columns] or None,
    )
    dl_name = _dedupe_name(_safe_name(f"{widget_id}_List"), used_names)
    data_list = DataList(name=dl_name, description="", list_sources={data_source})

    if resolved_cls is not None:
        data_source.fields = {a for a in resolved_cls.attributes if a.name in data_source.field_names}
        data_source.field_names = [c.lower() for c in columns]
        data_list.data_binding = DataBinding(domain_concept=resolved_cls)

    # Row-level action buttons embedded as JS object literals in the props.
    action_buttons = []
    for ab_m in re.finditer(
        r'\{\s*actionButtonText:\s*"([^"]*)".*?actionButtonQuery:\s*"([^"]*)"',
        attrs, re.DOTALL,
    ):
        label, query = ab_m.group(1), ab_m.group(2)
        btn_type, act_type = _classify_best(query, label) or _DEFAULT_CLASSIFICATION
        btn_name = _dedupe_name(_safe_name(f"{widget_id}_{label}"), used_names)
        action_buttons.append(Button(
            name=btn_name, description="", label=label,
            buttonType=btn_type, actionType=act_type,
        ))
    for _, action_attrs, action_inner, _ in _iter_top_level_blocks(inner, {'Action'}):
        btn = _build_button(action_attrs, action_inner, used_names)
        if btn is not None:
            action_buttons.append(btn)
    return data_list, action_buttons


def _build_button(attrs: str, inner: str, used_names: set):
    if _bool_attr(attrs, 'submit'):
        return None
    label = _attr(attrs, 'text') or _attr(attrs, 'label')
    widget_id = _attr(attrs, 'id') or label or 'button'
    if not label:
        label = widget_id
    # The button's wired-up Events are checked before its caption: what a
    # button actually does (runs a named delete/update query, opens a modal,
    # closes one) is real evidence, whereas the caption is only ever a guess.
    btn_type, act_type = (_event_signal(inner) or _classify_best(label)
                          or _DEFAULT_CLASSIFICATION)
    name = _dedupe_name(_safe_name(widget_id), used_names)
    try:
        button = Button(
            name=name, description="", label=label,
            buttonType=btn_type, actionType=act_type,
        )
        # Resolve direct dialog-opening events after every screen is known.
        button._retool_navigation = [
            (_attr(ev_attrs, 'event'), _attr(ev_attrs, 'pluginId'))
            for _, ev_attrs, _ in _find_all_tags(inner, {'Event'})
            if _attr(ev_attrs, 'type') == 'widget' and _attr(ev_attrs, 'method') == 'show'
        ]
        return button
    except ValueError:
        return None


def _build_form(attrs: str, inner: str, used_names: set, domain_model=None):
    form_id = _attr(attrs, 'id') or 'form'
    field_names_used = set()
    input_fields = {_build_input(tag, fattrs, field_inner, field_names_used)
                    for tag, fattrs, field_inner, _ in _iter_top_level_blocks(inner, set(_FIELD_TAG_MAP))}
    if not input_fields:
        return None
    submit_plugin = _submit_event_plugin(inner)
    submit_label = next((_attr(battrs, 'text') or _attr(battrs, 'label')
                         for _, battrs, _ in _find_all_tags(inner, {'Button'})
                         if _bool_attr(battrs, 'submit')), None)
    title_m = re.search(r'<Text\b[^>]*\bvalue="([^"]*)"', inner)
    name = _dedupe_name(_safe_name(form_id), used_names)
    form = Form(
        name=name,
        inputFields=input_fields,
        title=title_m.group(1) if title_m else None,
        submit_label=submit_label or "Submit",
        description=submit_plugin or "",
    )
    if domain_model is not None:
        names = {field.name for field in input_fields}
        candidates = [(len(names & {a.name for a in cls.attributes}), cls)
                      for cls in domain_model.get_classes()]
        candidates.sort(key=lambda item: (-item[0], item[1].name))
        if candidates and candidates[0][0] >= 2 and (len(candidates) == 1 or candidates[0][0] > candidates[1][0]):
            form.data_binding = DataBinding(domain_concept=candidates[0][1])
    return form



def _parse_screen_content(content: str, query_primary_table: dict,
                           domain_model: DomainModel):
    """Parse a screen's flattened RSX content into a set of view elements."""
    view_elements = set()
    used_names = set()

    for tag, attrs, inner, span in _iter_top_level_blocks(content, {'Table', 'TableLegacy'}):
        data_list, action_buttons = _build_data_list(
            tag, attrs, inner, query_primary_table, domain_model, used_names,
        )
        view_elements.add(data_list)
        view_elements.update(action_buttons)

    for tag, attrs, inner, span in _iter_top_level_blocks(content, {'Button'}):
        btn = _build_button(attrs, inner, used_names)
        if btn is not None:
            view_elements.add(btn)

    form_blocks = _iter_top_level_blocks(content, {'Form'})
    for tag, attrs, inner, span in form_blocks:
        form = _build_form(attrs, inner, used_names, domain_model)
        if form is not None:
            view_elements.add(form)
    outside_forms = content
    for _, _, _, (start, end) in reversed(form_blocks):
        outside_forms = outside_forms[:start] + outside_forms[end:]
    for tag, attrs, inner, _ in _iter_top_level_blocks(outside_forms, set(_FIELD_TAG_MAP)):
        view_elements.add(_build_input(tag, attrs, inner, used_names))
    for _, attrs, _ in _find_all_tags(content, {'Image'}):
        view_elements.add(Image(name=_dedupe_name(_safe_name(_attr(attrs, 'id') or 'image'), used_names),
                                description='', source=_attr(attrs, 'src')))
    for _, attrs, _ in _find_all_tags(content, {'Statistic'}):
        value = (_attr(attrs, 'prefix') or '') + (_attr(attrs, 'value') or '') + (_attr(attrs, 'suffix') or '')
        view_elements.add(Text(name=_dedupe_name(_safe_name(_attr(attrs, 'id') or 'statistic'), used_names),
                               content=value, description=_attr(attrs, 'label') or ''))
    for tag, attrs, inner, _ in _iter_top_level_blocks(content, {'PlotlyChart', 'Chart'}):
        view_elements.add(_build_chart(attrs, inner, query_primary_table, domain_model, used_names))

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
            primary, _, _ = sql_tables(text)
            if primary:
                query_primary_table[query_name] = primary

    for path, text in source.items():
        if not path.lower().endswith('.rsx'):
            continue
        for _, attrs, _ in _find_all_tags(text, {'SqlQueryUnified', 'SqlQuery'}):
            query_id = _attr(attrs, 'id')
            include = re.search(r'query=\{include\("([^"]+)"', attrs)
            sql = source.get(_resolve_include(include[1], posixpath.dirname(path)), '') if include else _attr(attrs, 'query')
            primary, _, _ = sql_tables(sql or '')
            if query_id and primary:
                query_primary_table[query_id] = primary

    screens: set = set()
    screen_targets = {}
    used_screen_names: set = {_safe_name(name)}

    if 'main.rsx' in source:
        flattened = _flatten_includes('main.rsx', source)

        def extract_screens(text, prefix=''):
            blocks = _iter_top_level_blocks(text, {'Screen', 'View', 'Modal', 'ModalFrame'})
            remaining = text
            for tag, attrs, inner, (start, end) in reversed(blocks):
                is_modal = tag in {'Modal', 'ModalFrame'}
                key = _attr(attrs, 'viewKey') or _attr(attrs, 'id') or tag
                if tag == 'View' and re.fullmatch(r'View\s+\d+', key):
                    remaining = remaining[:start] + extract_screens(inner, prefix) + remaining[end:]
                    continue
                screen_key = _safe_name(key)
                if prefix and not is_modal:
                    screen_key = f"{prefix}_{screen_key}"
                child_remaining = extract_screens(inner, screen_key)
                elements = _parse_screen_content(child_remaining, query_primary_table, domain_model)
                if elements or is_modal or tag in {'Screen', 'View'}:
                    screen_name = _dedupe_name(screen_key, used_screen_names)
                    screen = Screen(name=screen_name, description='', view_elements=elements,
                                    is_main_page=not is_modal)
                    screens.add(screen)
                    screen_targets.setdefault(_attr(attrs, 'id') or key, []).append(screen)
                    print(f"  Screen '{screen_name}' | elements={len(elements)}")
                remaining = remaining[:start] + remaining[end:]
            return remaining

        root_text = extract_screens(flattened)
        root_elements = _parse_screen_content(root_text, query_primary_table, domain_model)
        if root_elements:
            root_name = _dedupe_name(_safe_name(f'{name}_Main'), used_screen_names)
            screens.add(Screen(name=root_name, description='', view_elements=root_elements, is_main_page=True))
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

    for screen in screens:
        for component in screen.view_elements:
            for index, (event_name, target_id) in enumerate(getattr(component, '_retool_navigation', [])):
                targets = screen_targets.get(target_id, [])
                event_type = {'click': EventType.OnClick}.get(event_name)
                if len(targets) == 1 and event_type is not None:
                    action = Transition(name=f'{component.name}_open_{index}', target_screen=targets[0], triggered_by=component)
                    if not hasattr(component, 'events'):
                        component.events = set()
                    component.events.add(Event(name=f'{component.name}_{event_name}_{index}', event_type=event_type, actions={action}))

    gui_model = GUIModel(
        name=name,
        package="",
        versionCode="",
        versionName="",
        modules=set(),
        description="",
    )
    module = Module(name=name, screens=screens)
    gui_model.modules.add(module)
    print(f"  Total: {len(screens)} screen(s) extracted from RSX")
    return gui_model
