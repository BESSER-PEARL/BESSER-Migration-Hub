"""
Retool RSX App Generator — builds a Retool zip-import package from scratch.

Generates the Toolscript (RSX) zip format that Retool accepts for app import:

  <app_name>/
    metadata.json          — app metadata + rootScreen
    main.rsx               — top-level <App> with <Include> entries
    lib/
      query1.sql           — SELECT * FROM <table1>;
      query2.sql           — ...
    src/
      <entity1>.rsx        — Screen + SqlQueryUnified + Frame + Table
      <entity2>.rsx        — ...
    .positions/
      .<entity1>.positions.json   — grid positions for each widget
      ...

If a GUIModel is provided the generator also:
  - Filters/orders table columns to match the model's DataList fields
  - Adds Back/Add <Button> elements above the table (direct Frame children)
  - Adds Edit/Delete <RowAction> elements inside the table
  - Sets button colours from ActionType / ButtonType

Without a GUIModel every entity gets a plain table with all domain-model
columns plus standard Filter / Download / Refresh toolbar buttons.
"""

import hashlib
import json
import os
import re
import shutil
import uuid as _uuid_mod
import zipfile

from besser.BUML.metamodel.structural import DomainModel, Enumeration
from besser.generators.structural_utils import get_foreign_keys

try:
    from besser.BUML.metamodel.gui.graphical_ui import (
        GUIModel, DataList, Button as GUIButton,
    )
    _HAS_GUI = True
except ImportError:
    GUIModel = None
    DataList = None
    GUIButton = None
    _HAS_GUI = False


# ── Type & colour tables ───────────────────────────────────────────────────────

BUML_TO_RETOOL_FORMAT = {
    'int': 'decimal', 'float': 'decimal', 'bool': 'decimal',
    'str': 'string',  'date': 'string',   'datetime': 'string',
    'time': 'string', 'timedelta': 'decimal', 'any': 'string',
}

_ACTION_COLOR = {
    'Add': 'blue',    'Create': 'blue',   'Save': 'green',
    'Edit': 'yellow', 'Update': 'yellow', 'Delete': 'red',
    'Back': 'gray',   'Cancel': 'gray',   'Navigate': 'gray',
    'Next': 'blue',   'Login': 'blue',    'Logout': 'gray',
}
_BTNTYPE_COLOR = {
    'FloatingActionButton': 'blue',  'RaisedButton': 'yellow',
    'OutlinedButton': 'red',         'TextButton': 'gray',
    'IconButton': 'gray',            'DropdownButton': 'blue',
}

_DEFAULT_RESOURCE_ID = "2a86a318-80a0-4803-95d8-409396e41af2"


# ── Helpers ────────────────────────────────────────────────────────────────────

def _camel_to_snake(name: str) -> str:
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def _col_id(seed: str) -> str:
    """Deterministic 5-char hex column ID."""
    return hashlib.md5(seed.encode()).hexdigest()[:5]


def _resolve_color(action: str, btn_type: str) -> str:
    return _ACTION_COLOR.get(action) or _BTNTYPE_COLOR.get(btn_type, 'gray')


# ── Domain model analysis ──────────────────────────────────────────────────────

def _collect_entities_info(domain_model: DomainModel) -> list:
    """Return [(entity_name, table_name, columns), ...]
    where columns = [(col_name, retool_format), ...]."""
    try:
        fkeys = get_foreign_keys(domain_model)
    except Exception:
        fkeys = {}

    fk_map: dict = {}
    for assoc in domain_model.associations:
        ends = list(assoc.ends)
        if len(ends) != 2:
            continue
        e0, e1 = ends[0], ends[1]
        if e0.multiplicity.max > 1 and e1.multiplicity.max > 1:
            continue
        if assoc.name not in fkeys:
            continue
        class_with_fk, ref_prop_name = fkeys[assoc.name]
        fk_col = _camel_to_snake(ref_prop_name) + '_id'
        fk_map.setdefault(class_with_fk, []).append(fk_col)

    try:
        classes = list(domain_model.classes_sorted_by_inheritance())
    except Exception:
        classes = list(domain_model.get_classes())

    result = []
    for cls in classes:
        table_name = _camel_to_snake(cls.name)
        columns = [('id', 'decimal')]
        for attr in sorted(cls.attributes, key=lambda a: a.name):
            col_name = _camel_to_snake(attr.name)
            type_name = getattr(attr.type, 'name', 'str')
            fmt = 'string' if isinstance(attr.type, Enumeration) else \
                  BUML_TO_RETOOL_FORMAT.get(type_name, 'string')
            columns.append((col_name, fmt))
        for fk_col in fk_map.get(cls.name, []):
            columns.append((fk_col, 'decimal'))
        result.append((cls.name, table_name, columns))
    return result


# ── GUI model analysis ─────────────────────────────────────────────────────────

class _ButtonInfo:
    __slots__ = ('btn_id', 'label', 'color', 'action')

    def __init__(self, btn_id: str, label: str, color: str, action: str):
        self.btn_id = btn_id
        self.label  = label
        self.color  = color
        self.action = action


class _ScreenInfo:
    __slots__ = ('gui_fields', 'header_buttons', 'row_actions')

    def __init__(self):
        self.gui_fields: list     = []   # [(col_name, fmt)]
        self.header_buttons: list = []   # _ButtonInfo (Back + Add)
        self.row_actions: list    = []   # _ButtonInfo (Edit + Delete)


def _analyse_gui_model(gui_model, domain_model: DomainModel) -> dict:
    """Return {table_name_lower: _ScreenInfo} for every DataList screen."""
    if gui_model is None or not _HAS_GUI:
        return {}

    dm_attr_fmt: dict = {}
    for cls in list(domain_model.get_classes()):
        attr_map = {}
        for attr in cls.attributes:
            sn = _camel_to_snake(attr.name)
            type_name = getattr(attr.type, 'name', 'str')
            fmt = BUML_TO_RETOOL_FORMAT.get(type_name, 'string')
            attr_map[sn] = fmt
            attr_map[attr.name.lower()] = fmt
        dm_attr_fmt[cls.name.lower()] = attr_map

    all_screens = []
    modules = gui_model.modules
    if isinstance(modules, dict):
        for mod in modules.values():
            scr = getattr(mod, 'screens', None)
            all_screens.extend(scr if isinstance(scr, (set, list)) else
                               scr.values() if isinstance(scr, dict) else [])
    else:
        for mod in (modules or []):
            all_screens.extend(getattr(mod, 'screens', None) or [])

    result = {}
    for screen in all_screens:
        ves       = getattr(screen, 'view_elements', None) or set()
        dl_list   = [ve for ve in ves if isinstance(ve, DataList)]
        if not dl_list:
            continue

        info = _ScreenInfo()
        info.gui_fields.append(('id', 'decimal'))

        for dl in dl_list:
            for ds in (getattr(dl, 'list_sources', None) or set()):
                fields     = getattr(ds, 'fields', [])
                entity_obj = getattr(ds, 'dataSourceClass', None)
                entity_str = (
                    (getattr(entity_obj, 'name', str(entity_obj)) or '')
                    if entity_obj is not None
                    else (getattr(ds, 'name', '') or '')
                ).lower()
                attr_map = dm_attr_fmt.get(entity_str, {})
                seen = {'id'}
                for field_ref in fields:
                    raw      = (field_ref if isinstance(field_ref, str)
                                else getattr(field_ref, 'name', str(field_ref)))
                    col_name = _camel_to_snake(raw.split('.')[-1])
                    if col_name in seen:
                        continue
                    seen.add(col_name)
                    info.gui_fields.append((col_name, attr_map.get(col_name, 'string')))

        ctr = [0]
        for ve in ves:
            if not isinstance(ve, GUIButton):
                continue
            at     = getattr(ve, 'actionType', None)
            action = getattr(at, 'name', str(at)) if at is not None else ''
            bt     = getattr(ve, 'buttonType', None)
            b_type = getattr(bt, 'name', str(bt)) if bt is not None else ''
            label  = getattr(ve, 'label', '') or getattr(ve, 'name', '')

            _UNK = ('', '?', 'None')
            _PH  = ('', 'Unnamed Button', 'unnamed button')
            if action in _UNK and label in _PH:
                continue
            if label in _PH:
                label = action

            ctr[0] += 1
            binfo = _ButtonInfo(
                btn_id=f"btn_{action.lower()}_{ctr[0]}",
                label=label,
                color=_resolve_color(action, b_type),
                action=action,
            )
            if action in ('Back', 'Cancel', 'Navigate'):
                info.header_buttons.insert(0, binfo)
            elif action in ('Add', 'Create'):
                info.header_buttons.append(binfo)
            elif action in ('Edit', 'Update', 'Delete'):
                info.row_actions.append(binfo)
            else:
                info.header_buttons.append(binfo)

        for dl in dl_list:
            for ds in (getattr(dl, 'list_sources', None) or set()):
                entity_obj = getattr(ds, 'dataSourceClass', None)
                tname      = (
                    (getattr(entity_obj, 'name', str(entity_obj)) or '')
                    if entity_obj is not None
                    else (getattr(ds, 'name', '') or '')
                ).lower()
                if tname:
                    result[tname] = info
    return result


# ── RSX content builders ───────────────────────────────────────────────────────

def _column_rsx(col_name: str, fmt: str, indent: str = '      ') -> str:
    col_id = _col_id(col_name)
    label  = col_name.replace('_', ' ').title()
    if fmt == 'decimal':
        align     = 'right'
        editable  = '{{ showStepper: true }}'
        fmt_extra = f'\n{indent}  formatOptions={{{{ showSeparators: true, notation: "standard" }}}}'
        agg       = 'sum'
    else:
        align     = 'left'
        editable  = '{{ spellCheck: false }}'
        fmt_extra = ''
        agg       = 'none'
    lines = [
        f'{indent}<Column',
        f'{indent}  id="{col_id}"',
        f'{indent}  alignment="{align}"',
        f'{indent}  editableOptions={editable}',
        f'{indent}  format="{fmt}"{fmt_extra}',
        f'{indent}  groupAggregationMode="{agg}"',
        f'{indent}  key="{col_name}"',
        f'{indent}  label="{label}"',
        f'{indent}  placeholder="Enter value"',
        f'{indent}  position="center"',
        f'{indent}  size={{100}}',
        f'{indent}  summaryAggregationMode="none"',
        f'{indent}/>',
    ]
    return '\n'.join(lines)


def _button_rsx(btn_id: str, text: str, color: str,
                indent: str = '    ') -> str:
    return (
        f'{indent}<Button\n'
        f'{indent}  id="{btn_id}"\n'
        f'{indent}  text="{text}"\n'
        f'{indent}  colorScheme="{color}"\n'
        f'{indent}/>'
    )


def _row_action_rsx(action_id: str, label: str,
                    indent: str = '      ') -> str:
    return (
        f'{indent}<RowAction\n'
        f'{indent}  id="{action_id}"\n'
        f'{indent}  label="{label}"\n'
        f'{indent}/>'
    )


_TOOLBAR_RSX = '''\
      <ToolbarButton
        id="1a"
        icon="bold/interface-text-formatting-filter-2"
        label="Filter"
        type="filter"
      />
      <ToolbarButton
        id="3c"
        icon="bold/interface-download-button-2"
        label="Download"
        type="custom"
      />
      <ToolbarButton
        id="4d"
        icon="bold/interface-arrows-round-left"
        label="Refresh"
        type="custom"
      />'''


def _build_screen_rsx(entity_name: str, table_name: str, idx: int,
                      columns: list, gui_info, resource_id: str) -> str:
    screen_id  = table_name
    query_id   = f'query{idx + 1}'
    frame_id   = f'$main{idx + 1}'
    table_id   = f'table{idx + 1}'
    screen_uuid = str(_uuid_mod.uuid4())

    # Use GUI-specified fields when they go beyond just 'id'; otherwise use
    # all domain model columns (which includes FK cols — APEX shows all fields)
    gui_has_fields = gui_info and len(gui_info.gui_fields) > 1
    display_cols = gui_info.gui_fields if gui_has_fields else columns
    pk_col_id = _col_id(display_cols[0][0]) if display_cols else 'id'

    cols_rsx = '\n'.join(_column_rsx(cn, fmt) for cn, fmt in display_cols)

    row_actions_rsx = ''
    if gui_info and gui_info.row_actions:
        row_actions_rsx = '\n' + '\n'.join(
            _row_action_rsx(b.btn_id, b.label) for b in gui_info.row_actions
        )

    header_btns_rsx = ''
    if gui_info and gui_info.header_buttons:
        header_btns_rsx = '\n' + '\n'.join(
            _button_rsx(b.btn_id, b.label, b.color) for b in gui_info.header_buttons
        ) + '\n'

    # Manually build to avoid f-string brace escaping issues
    lines = [
        f'<Screen',
        f'  id="{screen_id}"',
        f'  _customShortcuts={{[]}}',
        f'  _hashParams={{[]}}',
        f'  _order={{{idx}}}',
        f'  _searchParams={{[]}}',
        f'  browserTitle={{null}}',
        f'  title={{null}}',
        f'  urlSlug={{null}}',
        f'  uuid="{screen_uuid}"',
        f'>',
        f'  <SqlQueryUnified',
        f'    id="{query_id}"',
        f'    query={{include("../lib/{query_id}.sql", "string")}}',
        f'    resourceDisplayName="retool_db"',
        f'    resourceName="{resource_id}"',
        f'    warningCodes={{[]}}',
        f'  />',
        f'  <Frame',
        f'    id="{frame_id}"',
        f'    enableFullBleed={{false}}',
        f'    isHiddenOnDesktop={{false}}',
        f'    isHiddenOnMobile={{false}}',
        f'    padding="8px 12px"',
        f'    sticky={{null}}',
        f'    type="main"',
        f'  >{header_btns_rsx}',
        f'    <Table',
        f'      id="{table_id}"',
        f'      cellSelection="none"',
        f'      clearChangesetOnSave={{true}}',
        '      data="{{ ' + query_id + '.data }}"',
        '      defaultSelectedRow={{ mode: "index", indexType: "display", index: 0 }}',
        f'      emptyMessage="No rows found"',
        f'      enableSaveActions={{true}}',
        f'      primaryKeyColumnId="{pk_col_id}"',
        f'      rowHeight="medium"',
        f'      showBorder={{true}}',
        f'      showFooter={{true}}',
        f'      showHeader={{true}}',
        f'      toolbarPosition="bottom"',
        f'    >',
        cols_rsx + row_actions_rsx,
        _TOOLBAR_RSX,
        f'    </Table>',
        f'  </Frame>',
        f'</Screen>',
        '',
    ]
    return '\n'.join(lines)


def _build_positions(table_id: str, gui_info) -> dict:
    pos = {table_id: {'row': 3, 'col': 0, 'height': 10, 'width': 12}}
    if gui_info:
        back_col = 0
        for b in gui_info.header_buttons:
            if b.action in ('Back', 'Cancel', 'Navigate'):
                pos[b.btn_id] = {'row': 0, 'col': back_col, 'height': 2, 'width': 2}
                back_col += 2
        add_col = 9
        for b in gui_info.header_buttons:
            if b.action not in ('Back', 'Cancel', 'Navigate'):
                pos[b.btn_id] = {'row': 0, 'col': add_col, 'height': 2, 'width': 3}
                add_col += 3
    return pos


# ── Public generator class ─────────────────────────────────────────────────────

class RetoolRsxAppGenerator:
    """
    Generates a Retool RSX (Toolscript) zip-import package from a BESSER
    DomainModel and an optional GUIModel.

    Args:
        domain_model : BESSER DomainModel (required)
        gui_model    : BESSER GUIModel — adds buttons and column filtering
        app_name     : folder / zip name inside output_dir
        output_dir   : where to write output (default: ./retool_rsx_output)
        resource_id  : Retool DB resource UUID (leave as default for demo)
    """

    def __init__(self, domain_model: DomainModel,
                 gui_model=None,
                 app_name: str = 'retool_app',
                 output_dir: str = None,
                 resource_id: str = _DEFAULT_RESOURCE_ID):
        self.domain_model = domain_model
        self.gui_model    = gui_model
        self.app_name     = app_name
        self.output_dir   = output_dir or os.path.join(os.getcwd(), 'retool_rsx_output')
        self.resource_id  = resource_id

    def generate(self) -> str:
        """Build the RSX app folder and zip. Returns the path to the zip file."""
        entities_info = _collect_entities_info(self.domain_model)
        screen_infos  = _analyse_gui_model(self.gui_model, self.domain_model)

        # ── Create directory structure ─────────────────────────────────────────
        app_folder = os.path.join(self.output_dir, self.app_name)
        if os.path.exists(app_folder):
            shutil.rmtree(app_folder)
        src_dir = os.path.join(app_folder, 'src')
        lib_dir = os.path.join(app_folder, 'lib')
        pos_dir = os.path.join(app_folder, '.positions')
        for d in (src_dir, lib_dir, pos_dir):
            os.makedirs(d)

        # ── 1. SQL queries ─────────────────────────────────────────────────────
        for i, (_, table_name, _cols) in enumerate(entities_info):
            with open(os.path.join(lib_dir, f'query{i + 1}.sql'),
                      'w', encoding='utf-8', newline='\n') as f:
                f.write(f'SELECT * FROM {table_name};')

        # ── 2. Screen RSX files + positions ───────────────────────────────────
        screen_ids = []
        for i, (entity_name, table_name, columns) in enumerate(entities_info):
            gui_info   = screen_infos.get(table_name)
            rsx_content = _build_screen_rsx(
                entity_name, table_name, i, columns, gui_info, self.resource_id,
            )
            with open(os.path.join(src_dir, f'{table_name}.rsx'),
                      'w', encoding='utf-8', newline='\n') as f:
                f.write(rsx_content)

            table_id = f'table{i + 1}'
            positions = _build_positions(table_id, gui_info)
            with open(os.path.join(pos_dir, f'.{table_name}.positions.json'),
                      'w', encoding='utf-8') as f:
                json.dump(positions, f, indent=2)

            screen_ids.append(table_name)
            gui_has = gui_info and len(gui_info.gui_fields) > 1
            used_cols = [c[0] for c in (gui_info.gui_fields if gui_has else columns)]
            btn_labels = [b.label for b in gui_info.header_buttons] if gui_info else []
            print(f'  Screen  : {entity_name}  cols={used_cols}  buttons={btn_labels}')

        # ── 3. main.rsx ───────────────────────────────────────────────────────
        includes = '\n'.join(
            f'  <Include src="./src/{sid}.rsx" />' for sid in screen_ids
        )
        with open(os.path.join(app_folder, 'main.rsx'),
                  'w', encoding='utf-8', newline='\n') as f:
            f.write(f'<App>\n{includes}\n</App>\n')

        # ── 4. metadata.json ──────────────────────────────────────────────────
        metadata = {
            'toolscriptVersion': '1.0.0',
            'version': '43.0.9',
            'pageUuid': str(_uuid_mod.uuid4()),
            'appTemplate': {
                'pubAppDecoupledQueriesDisabled': True,
                'pageCodeFolders': {
                    'object': {sid: {'array': []} for sid in screen_ids},
                },
                'rootScreen': screen_ids[0] if screen_ids else '',
                'version': '4.36.0',
            },
        }
        with open(os.path.join(app_folder, 'metadata.json'),
                  'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)

        # ── 5. Create ZIP ─────────────────────────────────────────────────────
        zip_path = os.path.join(self.output_dir, f'{self.app_name}.zip')
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(app_folder):
                dirs.sort()
                for file in sorted(files):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.output_dir)
                    # Ensure forward slashes in zip archive
                    arcname = arcname.replace('\\', '/')
                    zf.write(file_path, arcname)

        print(f'  Folder  : {app_folder}')
        print(f'  ZIP     : {zip_path}')
        return zip_path
