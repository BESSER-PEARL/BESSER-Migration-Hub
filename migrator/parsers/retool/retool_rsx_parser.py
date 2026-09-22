"""Retool RSX zip -> BESSER B-UML GUIModel parser.

Parses a Retool RSX Toolscript zip package.  The zip must contain
src/*.rsx files (one per screen), either at the root level (src/*.rsx)
or under an app-name prefix (<app_name>/src/*.rsx).

RSX files use a JSX-like attribute syntax that is NOT valid XML
(e.g. ``attr={[]}`` or ``{{ expr }}``).  All element detection is
therefore done with regular expressions rather than an XML parser.

The parser extracts:
  - Table elements  -> DataList view elements
  - Button elements -> Button view elements

Returns None (with a diagnostic message) if the zip is missing, empty,
or contains no src/*.rsx files.
"""

import os
import re
import zipfile

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

# Keyword → (ButtonType, ButtonActionType) for button classification
_BUTTON_MAP = {
    'add':    (ButtonType.FloatingActionButton, ButtonActionType.Add),
    'create': (ButtonType.FloatingActionButton, ButtonActionType.Add),
    'new':    (ButtonType.FloatingActionButton, ButtonActionType.Add),
    'save':   (ButtonType.RaisedButton,         ButtonActionType.Save),
    'edit':   (ButtonType.RaisedButton,         ButtonActionType.Save),
    'update': (ButtonType.RaisedButton,         ButtonActionType.Save),
    'delete': (ButtonType.OutlinedButton,       ButtonActionType.Delete),
    'remove': (ButtonType.OutlinedButton,       ButtonActionType.Delete),
    'back':   (ButtonType.TextButton,           ButtonActionType.Cancel),
    'cancel': (ButtonType.TextButton,           ButtonActionType.Cancel),
}


def _classify_button(label: str):
    lower = label.lower().strip()
    for keyword, pair in _BUTTON_MAP.items():
        if keyword in lower:
            return pair
    return ButtonType.TextButton, ButtonActionType.Cancel


def _safe_name(text: str) -> str:
    """Replace non-identifier characters with underscores."""
    result = re.sub(r'[^A-Za-z0-9_]', '_', text).strip('_') or 'Element'
    if result[0].isdigit():
        result = "_" + result
    return result


# Regex patterns for RSX element detection (no XML parser — RSX uses JSX syntax)
_TABLE_NAME_RE  = re.compile(r'<Table\b[^>]*\bname="([^"]+)"',  re.DOTALL)
_TABLE_ID_RE    = re.compile(r'<Table\b[^>]*\bid="([^"]+)"',    re.DOTALL)
_TABLE_RE       = re.compile(r'<Table\b')
_BTN_TEXT_RE    = re.compile(r'<Button\b[^>]*\btext="([^"]+)"', re.DOTALL)
_BTN_NAME_RE    = re.compile(r'<Button\b[^>]*\bname="([^"]+)"', re.DOTALL)


def _parse_rsx_screen(entry_name: str, rsx_content: str):
    """Parse one src/*.rsx file into a B-UML Screen using regex.

    RSX uses JSX-like attribute syntax (e.g. ``attr={[]}`` or
    ``{{ expr }}``) that is not valid XML, so ElementTree is not used.
    """
    stem        = os.path.splitext(os.path.basename(entry_name))[0]
    screen_name = _safe_name(stem)

    view_elements: set = set()
    entity_name = screen_name

    # ── Table → DataList ──────────────────────────────────────────────────────
    m = _TABLE_NAME_RE.search(rsx_content) or _TABLE_ID_RE.search(rsx_content)
    if _TABLE_RE.search(rsx_content):
        if m:
            raw = re.sub(r'[Tt]able', '', m.group(1)).strip()
            if raw:
                entity_name = _safe_name(raw)
        data_source = DataSourceElement(name=entity_name)
        view_elements.add(DataList(
            name=_safe_name(f"{entity_name}_List"),
            description="",
            list_sources={data_source},
        ))

    # ── Button elements ───────────────────────────────────────────────────────
    labels_seen: set = set()
    for pat in (_BTN_TEXT_RE, _BTN_NAME_RE):
        for label in pat.findall(rsx_content):
            label = label.strip()
            if not label or label in labels_seen:
                continue
            labels_seen.add(label)
            safe = _safe_name(label)
            btn_type, act_type = _classify_button(label)
            try:
                view_elements.add(Button(
                    name=safe,
                    description="",
                    label=label,
                    buttonType=btn_type,
                    actionType=act_type,
                ))
            except ValueError:
                pass

    is_modal = bool(re.search(r'(form|modal|detail)', screen_name.lower()))
    return Screen(
        name=screen_name,
        description="",
        view_elements=view_elements,
        is_main_page=not is_modal,
    )


def retool_rsx_to_gui(zip_path: str, module_name: str = None) -> GUIModel:
    """Parse a Retool RSX zip and return a BESSER B-UML GUIModel.

    Args:
        zip_path:    Path to the Retool RSX .zip file (or None / missing).
        module_name: Optional name for the GUIModel and its Module.

    Returns:
        A populated GUIModel, or None if the zip is missing, empty,
        or contains no src/*.rsx files.
    """
    if not zip_path or not os.path.isfile(zip_path):
        print(f"RSX zip not found: {zip_path!r}")
        return None

    name = module_name or 'RetoolGUI'
    print(f"Parsing RSX zip: {os.path.basename(zip_path)}")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            # Accept both  src/*.rsx  and  <app_name>/src/*.rsx  layouts
            _RSX_ENTRY_RE = re.compile(r'(?:^|/)src/[^/]+\.rsx$')
            rsx_entries = sorted(
                n for n in zf.namelist()
                if _RSX_ENTRY_RE.search(n)
            )
            if not rsx_entries:
                print("  No src/*.rsx files found in zip — skipping GUI extraction")
                return None

            screens: set = set()
            for entry in rsx_entries:
                with zf.open(entry) as fh:
                    content = fh.read().decode('utf-8', errors='replace')
                screen = _parse_rsx_screen(entry, content)
                if screen is not None:
                    screens.add(screen)
                    print(
                        f"  Screen '{screen.name}'"
                        f" | elements={len(screen.view_elements)}"
                    )

    except zipfile.BadZipFile as exc:
        print(f"  Bad zip file: {exc}")
        return None

    if not screens:
        print("  No screens extracted from RSX zip")
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
