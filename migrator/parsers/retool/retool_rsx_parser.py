"""Retool RSX zip -> BESSER B-UML GUIModel parser.

Parses a Retool RSX Toolscript zip package.  The zip must contain
src/*.rsx files (one per screen).  Each file is XML; the parser extracts:

  - Table elements  -> DataList view elements
  - Button elements -> Button view elements

Returns None (with a diagnostic message) if the zip is missing, empty,
or contains no src/*.rsx files.
"""

import os
import re
import zipfile
from xml.etree import ElementTree as ET

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
    return re.sub(r'[^A-Za-z0-9_]', '_', text).strip('_') or 'Element'


def _parse_rsx_screen(entry_name: str, xml_content: str):
    """Parse one src/*.rsx file into a B-UML Screen, or return None."""
    stem        = os.path.splitext(os.path.basename(entry_name))[0]
    screen_name = _safe_name(stem)

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as exc:
        print(f"  XML parse error in {entry_name}: {exc}")
        return None

    view_elements: set = set()
    entity_name = screen_name

    # Extract entity name and DataList from Table elements
    for table_elem in root.iter('Table'):
        raw = (table_elem.get('name') or table_elem.get('id') or '').strip()
        raw = re.sub(r'[Tt]able', '', raw).strip()
        if raw:
            entity_name = _safe_name(raw)
        data_source = DataSourceElement(
            name=entity_name,
            dataSourceClass=entity_name,
        )
        view_elements.add(DataList(
            name=_safe_name(f"{entity_name}_List"),
            description="",
            list_sources={data_source},
        ))
        break  # one table per screen

    # Extract Button elements
    for btn_elem in root.iter('Button'):
        label = (btn_elem.get('name') or btn_elem.get('label') or '').strip()
        if not label:
            continue
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
            rsx_entries = sorted(
                n for n in zf.namelist()
                if n.startswith('src/') and n.endswith('.rsx')
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
