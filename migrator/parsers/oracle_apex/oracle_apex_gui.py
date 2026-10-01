"""Oracle APEX page SQL exports -> BESSER B-UML GUIModel parser.

Pages remain Screens; native and legacy form pages contain Form widgets with
InputFields. One primary submit button is represented by Form.submit_label.

Fixed version of oracle_apex_gui.py that uses the correct constructor
signatures for the installed BESSER package version:

  - GUIModel(name, package, versionCode, versionName, modules, description)
  - DataSourceElement(name, ...)
  - DataList(name, description, list_sources)
  - Screen(name, description, view_elements, ...)
  - Button(name, description, label, buttonType, actionType)
"""

import glob
import os
import re
from besser.BUML.metamodel.gui.binding import DataBinding

from besser.BUML.metamodel.gui.graphical_ui import (
    Button,
    ButtonActionType,
    ButtonType,
    DataList,
    DataSourceElement,
    Form,
    GUIModel,
    InputField,
    InputFieldType,
    Module,
    Screen,
)

# Pages to unconditionally skip
_SKIP_PAGE_IDS   = {0, 1, 9999}
_SKIP_PAGE_NAMES = {"global page", "home", "login", "desktop", "landing"}

# Regex parameter extractors
_STR_RE  = re.compile(r"[,\s]p_(\w+)\s*=>\s*N?'((?:''|[^'])*)'", re.IGNORECASE)
_NUM_RE  = re.compile(r"[,\s]p_(\w+)\s*=>\s*(\d+)\b")
_BOOL_RE = re.compile(r"[,\s]p_(\w+)\s*=>\s*(true|false)\b", re.IGNORECASE)
_ID_RE = re.compile(r"[,\s]p_(\w+)\s*=>\s*wwv_flow_imp\.id\(\s*(\d+)\s*\)", re.IGNORECASE)


def _extract_params(proc_block: str) -> dict:
    params: dict = {}
    text = " " + proc_block
    for m in _STR_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2).replace("''", "'"))
    for m in _NUM_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2))
    for m in _BOOL_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2).lower() == "true")
    for m in _ID_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2))
    # Read complete top-level expressions, including modern SQL/plugin wrappers.
    arguments, start, depth, index = [], 0, 0, 0
    while index < len(proc_block):
        char = proc_block[index]
        if char == "'":
            index += 1
            while index < len(proc_block):
                if proc_block[index] == "'":
                    index += 1
                    if index < len(proc_block) and proc_block[index] == "'":
                        index += 1
                        continue
                    break
                index += 1
            continue
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == ',' and depth == 0:
            arguments.append(proc_block[start:index])
            start = index + 1
        index += 1
    arguments.append(proc_block[start:])
    for argument in arguments:
        match = re.match(r'\s*p_(\w+)\s*=>\s*(.*)', argument, re.DOTALL | re.IGNORECASE)
        if not match:
            continue
        key, expression = match[1].lower(), match[2].strip()
        strings = [value.replace("''", "'") for value in re.findall(r"'((?:''|[^'])*)'", expression)]
        if key == 'plug_source' and expression.lower().startswith('wwv_flow_string.join('):
            params[key] = '\n'.join(strings)
        elif key == 'attributes' and expression.lower().startswith('wwv_flow_t_plugin_attributes('):
            params['plugin_attributes'] = dict(zip(strings[::2], strings[1::2]))
    return params


def _all_calls(sql: str, proc_name: str) -> list:
    """Return list of param dicts for every call to proc_name in sql."""
    pattern = re.compile(
        r'wwv_flow_imp_page\.' + re.escape(proc_name) + r'\s*\(',
        re.IGNORECASE,
    )
    results = []
    for m in pattern.finditer(sql):
        start  = m.end()
        depth  = 1
        i      = start
        while i < len(sql) and depth > 0:
            # Parentheses inside SQL strings/comments do not delimit calls.
            if sql[i] == "'":
                i += 1
                while i < len(sql):
                    if sql[i] == "'":
                        i += 1
                        if i < len(sql) and sql[i] == "'":
                            i += 1
                            continue
                        break
                    i += 1
                continue
            if sql.startswith('--', i):
                end = sql.find('\n', i)
                i = len(sql) if end == -1 else end + 1
                continue
            if sql.startswith('/*', i):
                end = sql.find('*/', i + 2)
                i = len(sql) if end == -1 else end + 2
                continue
            if sql[i] == '(':
                depth += 1
            elif sql[i] == ')':
                depth -= 1
            i += 1
        block = sql[start:i - 1]
        results.append(_extract_params(block))
    return results


def _first_call(sql: str, proc: str) -> dict:
    calls = _all_calls(sql, proc)
    return calls[0] if calls else {}


# Button classification
_BUTTON_MAP = {
    "CREATE": (ButtonType.FloatingActionButton, ButtonActionType.Add),
    "SAVE":   (ButtonType.RaisedButton,          ButtonActionType.Save),
    "DELETE": (ButtonType.OutlinedButton,         ButtonActionType.Delete),
    "CANCEL": (ButtonType.TextButton,             ButtonActionType.Cancel),
}


def _classify_button(name: str, db_action: str, is_hot: bool, template_opts: str):
    upper = name.upper()
    if upper in _BUTTON_MAP:
        return _BUTTON_MAP[upper]
    db_upper = db_action.upper()
    if db_upper == "INSERT":
        return ButtonType.FloatingActionButton, ButtonActionType.Add
    if db_upper == "UPDATE":
        return ButtonType.RaisedButton, ButtonActionType.Save
    if db_upper == "DELETE":
        return ButtonType.OutlinedButton, ButtonActionType.Delete
    if "t-Button--danger" in template_opts:
        return ButtonType.OutlinedButton, ButtonActionType.Delete
    if is_hot:
        return ButtonType.RaisedButton, ButtonActionType.Save
    return ButtonType.TextButton, ButtonActionType.Cancel


def _safe_name(name):
    name = re.sub(r'[^A-Za-z0-9_]', '_', name)
    return ('_' + name if name[:1].isdigit() else name) or '_'


def _resolve_table(table, domain_model):
    """Resolve declared SQL identifiers against real domain classes; never invent one."""
    if not table or domain_model is None:
        return None
    table = table.split('.')[-1].strip('"')
    normalize = lambda name: name.replace('_', '').lower()
    matches = [cls for cls in domain_model.get_classes() if normalize(cls.name) == normalize(table)]
    return matches[0] if len(matches) == 1 else None


def _query_tables(query):
    """Read static FROM/JOIN tables, including comma joins and quoted schema names."""
    query = re.sub(r"'(?:''|[^'])*'|--[^\n]*|/\*[\s\S]*?\*/", ' ', query)
    tokens = re.findall(r'"[^\"]+"|[A-Za-z_$#][\w$#]*|[.,()]', query)
    ctes = {match[1].strip('"').lower() for match in re.finditer(
        r'(?:\bwith|,)\s*("[^"]+"|[\w$#]+)\s+as\s*\(', query, re.IGNORECASE)}
    tables, in_from, expect_table = [], False, False
    index = 0
    while index < len(tokens):
        token, word = tokens[index], tokens[index].lower()
        if word in {'from', 'join'}:
            in_from, expect_table = True, True
        elif word in {'where', 'group', 'having', 'order', 'connect', 'union', 'minus', 'intersect', 'select'}:
            in_from, expect_table = False, False
        elif token == ',' and in_from:
            expect_table = True
        elif expect_table:
            expect_table = False
            if token != '(':
                table = token
                if index + 2 < len(tokens) and tokens[index + 1] == '.':
                    table += '.' + tokens[index + 2]
                    index += 2
                if table.strip('"').lower() not in ctes and table not in tables:
                    tables.append(table)
        index += 1
    return tables


def _region_classes(region, domain_model):
    declared = region.get('query_table') or region.get('plugin_attributes', {}).get('table_name')
    if not declared and region.get('process_type', '').startswith('NATIVE_FORM_'):
        declared = region.get('attribute_02')
    tables = [declared] if declared else _query_tables(region.get('plug_source', ''))
    classes = []
    for table in tables:
        cls = _resolve_table(table, domain_model)
        if cls is not None and cls not in classes:
            classes.append(cls)
    return classes


_FIELD_TYPES = {
    'NATIVE_TEXT_FIELD': InputFieldType.Text,
    'NATIVE_TEXTAREA': InputFieldType.TextArea,
    'NATIVE_RICH_TEXT_EDITOR': InputFieldType.RichText,
    'NATIVE_PASSWORD': InputFieldType.Password,
    'NATIVE_NUMBER_FIELD': InputFieldType.Number,
    'NATIVE_SELECT_LIST': InputFieldType.Dropdown,
    'NATIVE_POPUP_LOV': InputFieldType.Dropdown,
    'NATIVE_RADIOGROUP': InputFieldType.RadioGroup,
    'NATIVE_CHECKBOX': InputFieldType.CheckboxGroup,
    'NATIVE_SINGLE_CHECKBOX': InputFieldType.Checkbox,
    'NATIVE_YES_NO': InputFieldType.Toggle,
    'NATIVE_DATE_PICKER': InputFieldType.Date,
    'NATIVE_DATE_PICKER_APEX': InputFieldType.Date,
    'NATIVE_DATE_PICKER_JET': InputFieldType.Date,
    'NATIVE_FILE': InputFieldType.File,
    'NATIVE_FILE_UPLOAD': InputFieldType.File,
    'NATIVE_HIDDEN': InputFieldType.Hidden,
}


def _form_elements(page_name, is_modal, plugs, items, processes, buttons, domain_model=None):
    """Return forms and indices of submit buttons represented by Form.submit_label.

    Native form regions own their items by item_plug_id. Older exports use
    static regions plus form processes, or modal custom forms with submit
    controls. Modal pages without editable items are not implicitly forms.
    """
    items = [item for item in items if item.get('name') and item.get('display_as')]
    editable = [item for item in items
                if item['display_as'] not in {'NATIVE_HIDDEN', 'NATIVE_DISPLAY_ONLY'}]
    regions = [plug for plug in plugs if plug.get('plug_source_type') == 'NATIVE_FORM']
    native_process = any(process.get('process_type', '').startswith('NATIVE_FORM_')
                         for process in processes)
    submits = [index for index, button in enumerate(buttons)
               if button.get('button_name') and button.get('button_action') == 'SUBMIT']
    if not regions and (native_process or (editable and (is_modal or submits))):
        regions = [{'plug_name': page_name}]
    forms = set()
    consumed = set()
    for index, region in enumerate(regions):
        fields = items if 'id' not in region else [
            item for item in items if item.get('item_plug_id') == region['id']]
        candidates = [button_index for button_index in submits if button_index not in consumed
                      and (buttons[button_index].get('button_plug_id') == region.get('id') or
                           (len(regions) == 1 and (not region.get('id') or
                                                  not buttons[button_index].get('button_plug_id'))))]
        # A Form has one primary submit control; other APEX buttons remain Button objects.
        candidates.sort(key=lambda button_index: (
            buttons[button_index].get('button_name', '').upper() not in {'SAVE', 'CREATE', 'APPLY'},
            buttons[button_index].get('button_is_hot') != 'Y', button_index))
        submit = buttons[candidates[0]] if candidates else None
        if candidates:
            consumed.add(candidates[0])
        form = Form(
            name=f"{_safe_name(region.get('plug_name') or page_name)}_fields_{index + 1}",
            description='', title=region.get('plug_name') or page_name,
            inputFields={InputField(
                name=_safe_name(item['name']), description='',
                field_type=_FIELD_TYPES.get(item['display_as'], InputFieldType.Text),
                label=item.get('prompt', ''), required=item.get('is_required') is True,
                placeholder=item.get('placeholder', ''),
                default_value=item.get('item_default') if item.get('item_default_type') == 'STATIC' else None,
                readonly=item['display_as'] == 'NATIVE_DISPLAY_ONLY',
            ) for item in fields},
            submit_label=(submit.get('button_image_alt') or submit['button_name'].title())
                         if submit else 'Submit',
        )
        classes = _region_classes(region, domain_model)
        if not classes:
            for process in processes:
                if not process.get('process_type', '').startswith('NATIVE_FORM_'):
                    continue
                process_region = process.get('form_region_id') or process.get('region_id')
                if 'id' in region and process_region and process_region != region['id']:
                    continue
                if len(regions) > 1 and process_region is None:
                    continue
                for cls in _region_classes(process, domain_model):
                    if cls not in classes:
                        classes.append(cls)
        if len(classes) == 1:
            form.data_binding = DataBinding(domain_concept=classes[0])
        forms.add(form)
    return forms, consumed


def _parse_page_file(sql_path: str, domain_model=None):
    """Parse one APEX page SQL file; return (page_id, Screen) or None to skip."""
    with open(sql_path, "r", encoding="utf-8") as fh:
        sql = fh.read()

    page_params = _first_call(sql, "create_page")
    if not page_params:
        return None

    try:
        page_id = int(page_params.get("id", "-1"))
    except (ValueError, TypeError):
        page_id = -1

    if page_id in _SKIP_PAGE_IDS:
        return None

    page_name: str = page_params.get("name", "").strip()
    if not page_name or page_name.lower() in _SKIP_PAGE_NAMES:
        return None

    page_mode: str = page_params.get("page_mode", "NORMAL").upper()
    is_modal = page_mode == "MODAL"

    # Region detection
    plug_calls    = _all_calls(sql, "create_page_plug")
    entity_name   = None
    is_list_page  = False
    item_calls = _all_calls(sql, "create_page_item")
    button_calls = _all_calls(sql, "create_page_button")
    forms, consumed_submits = _form_elements(
        page_name, is_modal, plug_calls, item_calls,
        _all_calls(sql, "create_page_process"), button_calls, domain_model)
    is_form_page = bool(forms)

    for p in plug_calls:
        src_type = p.get("plug_source_type", "")
        tbl      = p.get("query_table", "")
        if src_type == "NATIVE_IR":
            is_list_page = True
            if tbl:
                entity_name = tbl.capitalize()
        if src_type == "NATIVE_FORM":
            is_form_page = True
            if tbl:
                entity_name = tbl.capitalize()

    if entity_name is None:
        entity_name = page_name.strip().replace(' ', '_').replace('-', '_')
    else:
        entity_name = entity_name.replace(' ', '_').replace('-', '_')

    # Build view elements
    view_elements: set = set(forms)

    if is_list_page and entity_name:
        # Fixed: DataSourceElement(name=...) — no 'source' keyword arg
        classes = []
        for region in plug_calls:
            if region.get('plug_source_type') == 'NATIVE_IR':
                for cls in _region_classes(region, domain_model):
                    if cls not in classes:
                        classes.append(cls)
        sources = {DataSourceElement(name=cls.name, dataSourceClass=cls) for cls in classes}
        if not sources:
            sources = {DataSourceElement(name=entity_name)}
        # Fixed: DataList(name, description, list_sources)
        data_list = DataList(
            name=f"{entity_name}_List",
            description="",
            list_sources=sources,
        )
        if classes:
            data_list.data_binding = DataBinding(domain_concept=classes[0])
        view_elements.add(data_list)

    for button_index, btn_p in enumerate(button_calls):
        if button_index in consumed_submits:
            continue
        btn_name: str = btn_p.get("button_name", "").strip()
        if not btn_name:
            continue

        btn_action  = btn_p.get("button_action", "")
        is_hot      = btn_p.get("button_is_hot", "N") == "Y"
        tmpl_opts   = btn_p.get("button_template_options", "")
        db_action   = btn_p.get("database_action", "")

        btn_type, act_type = _classify_button(btn_name, db_action, is_hot, tmpl_opts)

        # Fixed: Button requires (name, description, label, buttonType, actionType)
        # Names cannot contain spaces or hyphens in this BESSER version
        safe_name = _safe_name(btn_name.title())
        view_elements.add(
            Button(
                name=safe_name,
                description="",
                label=btn_p.get('button_image_alt') or btn_name.title(),
                buttonType=btn_type,
                actionType=act_type,
            )
        )

    # Screen name (no spaces or hyphens allowed in BESSER names)
    def _safe(s: str) -> str:
        result = re.sub(r'[^A-Za-z0-9_]', '_', s)
        if result and result[0].isdigit():
            result = "_" + result
        return result or '_'

    safe_entity = _safe(entity_name) if entity_name else _safe(page_name)
    if is_list_page:
        screen_name = f"{safe_entity}_List"
    elif is_form_page or is_modal:
        screen_name = f"{safe_entity}_Form"
    else:
        screen_name = _safe(page_name)

    # Fixed: Screen requires (name, description, view_elements, ...)
    screen = Screen(
        name=screen_name,
        description="",
        view_elements=view_elements,
        is_main_page=not is_modal,
    )
    return page_id, screen


def oracle_apex_to_gui(pages_dir: str, module_name: str = None, domain_model=None) -> GUIModel:
    """Parse Oracle APEX page SQL files and return a BESSER B-UML GUIModel.

    Args:
        pages_dir  : directory containing page_000XX.sql files
        module_name: optional name for the GUIModel and its Module
        domain_model: parsed DomainModel used to resolve declared table bindings
    """
    if not os.path.isdir(pages_dir):
        print(f"Pages directory not found: {pages_dir}")
        return None

    name = module_name or "OracleApexGUI"

    gui_model = GUIModel(
        name=name,
        package="",
        versionCode="",
        versionName="",
        modules=set(),
        description="",
    )

    page_files = sorted(glob.glob(os.path.join(pages_dir, "page_*.sql")))
    if not page_files:
        print(f"No page_*.sql files found in: {pages_dir}")

    screens: set = set()
    seen_names: set = set()
    print(f"Parsing {len(page_files)} APEX page files in: {os.path.basename(pages_dir)}")

    for path in page_files:
        result = _parse_page_file(path, domain_model)
        if result is not None:
            page_id, screen = result
            if screen.name in seen_names:
                screen.name = f"{screen.name}_p{page_id}"
            seen_names.add(screen.name)
            screens.add(screen)
            print(
                f"  Screen '{screen.name}'"
                f" | main={screen.is_main_page}"
                f" | elements={len(screen.view_elements)}"
            )
        else:
            print(f"  Skipped: {os.path.basename(path)}")

    module = Module(name=name, screens=screens)
    gui_model.modules.add(module)

    print(f"  Total: {len(screens)} screens extracted")
    return gui_model


# ---------------------------------------------------------------------------
# Monolithic SQL export parser
# ---------------------------------------------------------------------------

import re as _re
import tempfile as _tempfile

_PAGE_MARKER_RE = _re.compile(
    r'^prompt\s+--application/pages/(page_\d+)\s*$',
    _re.IGNORECASE | _re.MULTILINE,
)
_PNAME_RE = _re.compile(r"(,\s*p_name\s*=>\s*N?')(.*?)(')", _re.IGNORECASE | _re.DOTALL)


def _sanitize_section(text: str) -> str:
    """Replace spaces/hyphens inside p_name values to avoid BESSER parse errors."""
    def _fix(m):
        safe = _re.sub(r"[\s\-]+", "_", m.group(2))
        return m.group(1) + safe + m.group(3)
    return _PNAME_RE.sub(_fix, text)


def oracle_apex_gui_from_sql(sql_path: str, module_name: str = None, domain_model=None) -> GUIModel:
    """Parse a monolithic Oracle APEX SQL export and return a GUIModel.

    Oracle APEX can export an application as a single SQL file.  Each page
    section is delimited by a ``prompt --application/pages/page_NNNNN`` line.
    This function splits the file on those markers, writes each section to a
    temporary file, and delegates to the existing :func:`_parse_page_file`
    helper.

    Args:
        sql_path   : path to the monolithic ``.sql`` export file.
        module_name: optional name for the GUIModel and its Module.
        domain_model: parsed DomainModel used to resolve declared table bindings.

    Returns:
        A populated ``GUIModel``, or ``None`` if the file is missing or contains
        no page markers.
    """
    if not os.path.isfile(sql_path):
        print(f"  SQL file not found: {sql_path}")
        return None

    with open(sql_path, "r", encoding="utf-8", errors="replace") as fh:
        content = fh.read()

    markers = list(_PAGE_MARKER_RE.finditer(content))
    if not markers:
        print(f"  No page markers found in: {os.path.basename(sql_path)}")
        return None

    name = module_name or os.path.splitext(os.path.basename(sql_path))[0]
    print(f"  Found {len(markers)} page sections in {os.path.basename(sql_path)}")

    screens: set = set()
    with _tempfile.TemporaryDirectory() as tmp_dir:
        for i, m in enumerate(markers):
            page_id = m.group(1)
            start   = m.start()
            end     = markers[i + 1].start() if i + 1 < len(markers) else len(content)
            section = _sanitize_section(content[start:end])

            tmp_file = os.path.join(tmp_dir, f"{page_id}.sql")
            with open(tmp_file, "w", encoding="utf-8") as fh:
                fh.write(section)

            result = _parse_page_file(tmp_file, domain_model)
            if result is not None:
                _, screen = result
                existing_names = {s.name for s in screens}
                if screen.name in existing_names:
                    screen.name = f"{screen.name}_{page_id}"
                screens.add(screen)

    gui_model = GUIModel(name=name, package="", versionCode="",
                         versionName="", modules={Module(name=name, screens=screens)}, description="")
    print(f"  Total: {len(screens)} screens extracted from monolithic SQL")
    return gui_model
