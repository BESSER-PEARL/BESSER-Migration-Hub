"""Oracle APEX page SQL exports -> BESSER B-UML GUIModel parser (fixed).

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

from besser.BUML.metamodel.gui.graphical_ui import (
    Button,
    ButtonActionType,
    ButtonType,
    DataList,
    DataSourceElement,
    GUIModel,
    Module,
    Screen,
)

# Pages to unconditionally skip
_SKIP_PAGE_IDS   = {0, 1, 9999}
_SKIP_PAGE_NAMES = {"global page", "home", "login", "desktop", "landing"}

# Regex parameter extractors
_STR_RE  = re.compile(r"[,\s]p_(\w+)\s*=>\s*N?'([^']*)'")
_NUM_RE  = re.compile(r"[,\s]p_(\w+)\s*=>\s*(\d+)\b")
_BOOL_RE = re.compile(r"[,\s]p_(\w+)\s*=>\s*(true|false)\b", re.IGNORECASE)


def _extract_params(proc_block: str) -> dict:
    params: dict = {}
    text = " " + proc_block
    for m in _STR_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2))
    for m in _NUM_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2))
    for m in _BOOL_RE.finditer(text):
        params.setdefault(m.group(1), m.group(2).lower() == "true")
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


def _parse_page_file(sql_path: str):
    """Parse one APEX page SQL file; return a Screen or None to skip."""
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
    is_form_page  = False

    for p in plug_calls:
        src_type = p.get("plug_source_type", "")
        tbl      = p.get("query_table", "")
        if src_type == "NATIVE_IR":
            is_list_page = True
            if tbl:
                entity_name = tbl.capitalize()
            break
        if src_type == "NATIVE_FORM":
            is_form_page = True
            if tbl:
                entity_name = tbl.capitalize()
            break

    if entity_name is None:
        entity_name = page_name.strip()

    # Build view elements
    view_elements: set = set()

    if is_list_page and entity_name:
        # Fixed: DataSourceElement(name=...) — no 'source' keyword arg
        data_source = DataSourceElement(name=entity_name)
        # Fixed: DataList(name, description, list_sources)
        data_list = DataList(
            name=f"{entity_name}_List",
            description="",
            list_sources={data_source},
        )
        view_elements.add(data_list)

    for btn_p in _all_calls(sql, "create_page_button"):
        btn_name: str = btn_p.get("button_name", "").strip()
        if not btn_name:
            continue

        btn_action  = btn_p.get("button_action", "")
        is_hot      = btn_p.get("button_is_hot", "N") == "Y"
        tmpl_opts   = btn_p.get("button_template_options", "")
        db_action   = btn_p.get("database_action", "")

        btn_type, act_type = _classify_button(btn_name, db_action, is_hot, tmpl_opts)

        # Fixed: Button requires (name, description, label, buttonType, actionType)
        # Names cannot contain spaces in this BESSER version
        safe_name = btn_name.title().replace(' ', '_')
        view_elements.add(
            Button(
                name=safe_name,
                description="",
                label=btn_name.title(),   # label may contain spaces
                buttonType=btn_type,
                actionType=act_type,
            )
        )

    # Screen name (no spaces allowed in BESSER names)
    safe_entity = entity_name.replace(' ', '_') if entity_name else page_name.replace(' ', '_')
    if is_list_page:
        screen_name = f"{safe_entity}_List"
    elif is_form_page or is_modal:
        screen_name = f"{safe_entity}_Form"
    else:
        screen_name = page_name.replace(' ', '_')

    # Fixed: Screen requires (name, description, view_elements, ...)
    screen = Screen(
        name=screen_name,
        description="",
        view_elements=view_elements,
        is_main_page=not is_modal,
    )
    return screen


def oracle_apex_to_gui(pages_dir: str, module_name: str = None) -> GUIModel:
    """Parse Oracle APEX page SQL files and return a BESSER B-UML GUIModel.

    Args:
        pages_dir  : directory containing page_000XX.sql files
        module_name: optional name for the GUIModel and its Module
    """
    if not os.path.isdir(pages_dir):
        print(f"Pages directory not found: {pages_dir}")
        return None

    name = module_name or "OracleApexGUI"

    # Fixed: GUIModel requires all positional args
    gui_model = GUIModel(
        name=name,
        package="",
        versionCode="",
        versionName="",
        modules={},
        description="",
    )

    page_files = sorted(glob.glob(os.path.join(pages_dir, "page_*.sql")))
    if not page_files:
        print(f"No page_*.sql files found in: {pages_dir}")

    screens: set = set()
    print(f"Parsing {len(page_files)} APEX page files in: {os.path.basename(pages_dir)}")

    for path in page_files:
        screen = _parse_page_file(path)
        if screen is not None:
            screens.add(screen)
            print(
                f"  Screen '{screen.name}'"
                f" | main={screen.is_main_page}"
                f" | elements={len(screen.view_elements)}"
            )
        else:
            print(f"  Skipped: {os.path.basename(path)}")

    # Fixed: Module(name, screens) - no gui_model kwarg in this BESSER version
    module = Module(name=name, screens=screens)
    # Fixed: modules is a dict, use update()
    gui_model.modules.update({module.name: module})

    print(f"  Total: {len(screens)} screens extracted")
    return gui_model
