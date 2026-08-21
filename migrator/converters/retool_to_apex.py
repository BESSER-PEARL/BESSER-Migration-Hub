import io
import os
import sys
from contextlib import contextmanager
from pathlib import Path

# UTF-8 stdout on Windows
if hasattr(sys.stdout, 'buffer') and sys.stdout.encoding.lower() not in ('utf-8', 'utf8'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Project root on sys.path
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui
from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator
from migrator.generators.sql.sql_generator_ui import UIPagesSQLGenerator
from migrator.converters.besser_to_apex import (
    get_apex_pages_dir,
    extract_apex_info_from_file,
    _normalize_page_name,
    _screen_is_list_page,
    _similarity,
)
from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement,
    GUIModel, Module, Screen,
)

# ==============================================================================
# INPUT CONFIGURATION — edit these paths before running
# ==============================================================================

CSV_DIR         = Path(r"path/to/retool/csv")         # folder with .csv files from Retool DB
ZIP_PATH        = Path(r"path/to/app.zip")  # Path(r"path/to/app.zip") or None
APEX_EXPORT_DIR = Path(r"path/to/apex/export")        # exported APEX app folder (or None)
APP_NAME        = "my_apex_app"                        # name for generated artefacts
MODULE_NAME     = "App"                                # B-UML module name
WORKSPACE_NAME  = "MYWORKSPACE"                        # APEX workspace name
USER_NAME       = "ADMIN"                              # APEX user name
OUTPUT_PATH     = Path("output").resolve()             # output folder

# ==============================================================================


@contextmanager
def _silent():
    """Suppress stdout from internal library calls."""
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = old


OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# Step 1 — Parse CSV files → DomainModel
if not CSV_DIR.is_dir():
    raise FileNotFoundError(f"CSV directory not found: {CSV_DIR}")
csv_count = len(list(CSV_DIR.glob('*.csv')))
print(f"[1/4] Parsing {csv_count} CSV file(s)")
with _silent():
    domain_model = retool_csv_to_buml(csv_dir=str(CSV_DIR), module_name=MODULE_NAME)
if domain_model is None:
    raise RuntimeError(f"CSV parsing returned no model — check the directory: {CSV_DIR}")

# Step 2 — Parse RSX zip → GUIModel (optional)
gui_model = None
if ZIP_PATH:
    with _silent():
        gui_model = retool_rsx_to_gui(zip_path=str(ZIP_PATH), module_name=MODULE_NAME)

# If no RSX zip (or it yielded no screens), build a minimal GUIModel from the DomainModel
if gui_model is None:
    gui_model = GUIModel(name=MODULE_NAME, package="", versionCode="",
                         versionName="", modules={}, description="")
    screens = set()
    for cls in domain_model.get_classes():
        safe = cls.name.replace(' ', '_')
        screens.add(Screen(
            name=f"{safe}_List",
            description="",
            view_elements={
                DataList(name=f"{safe}_List", description="",
                         list_sources={DataSourceElement(name=cls.name, dataSourceClass=cls.name)}),
                Button(name="Create", description="", label="Create",
                       buttonType=ButtonType.FloatingActionButton,
                       actionType=ButtonActionType.Add),
            },
            is_main_page=True,
        ))
    gui_model.modules[MODULE_NAME] = Module(name=MODULE_NAME, screens=screens)

# Step 3 — Generate Oracle APEX DDL
ddl_filename = f"{APP_NAME}_tables.sql"
with _silent():
    OracleApexSQLGenerator(
        model=domain_model,
        output_dir=str(OUTPUT_PATH),
        output_filename=ddl_filename,
    ).generate()

# Step 4 — Generate APEX page scripts
pages_dir = OUTPUT_PATH / "apex_pages"
pages_dir.mkdir(exist_ok=True)

apex_export = str(APEX_EXPORT_DIR) if APEX_EXPORT_DIR and APEX_EXPORT_DIR.is_dir() else None

if apex_export:
    # Mode A — read app_id / workspace / version from the existing APEX export
    export_pages_dir = get_apex_pages_dir(apex_export)
    apex_pages = [
        extract_apex_info_from_file(os.path.join(export_pages_dir, f))
        for f in os.listdir(export_pages_dir) if f.lower().endswith('.sql')
    ]
    apex_pages = [p for p in apex_pages if p.get('p_name') and p.get('p_id') is not None]
    list_pages  = [p for p in apex_pages if p.get('page_type') == 'list']

    app_id         = str(list_pages[0]['p_default_application_id'])
    workspace_nm   = list_pages[0].get('p_default_owner', 'WKSP_APP')
    workspace_name = workspace_nm.replace('WKSP_', '') if workspace_nm.startswith('WKSP_') else workspace_nm
    apex_version   = next((p['p_version_yyyy_mm_dd'] for p in apex_pages if p.get('p_version_yyyy_mm_dd')), '2024.11.30')
    apex_release   = next((p['p_release']            for p in apex_pages if p.get('p_release')),            '24.2.6')

    list_screens = [s for m in gui_model.modules.values() for s in m.screens
                    if _screen_is_list_page(s.name) or s.is_main_page]
    matched_ids  = set()

    # Pass 1 — exact / prefix match
    for apex_info in list_pages:
        apex_norm = _normalize_page_name(apex_info['p_name'])
        for screen in list_screens[:]:
            screen_norm = _normalize_page_name(screen.name)
            if screen_norm == apex_norm or screen_norm.startswith(apex_norm) or apex_norm.startswith(screen_norm):
                with _silent():
                    UIPagesSQLGenerator(
                        model=domain_model, gui_model=gui_model,
                        app_id=app_id, screen=screen,
                        screen_number=apex_info['p_id'],
                        workspace_name=workspace_name, user_name=USER_NAME,
                        apex_version=apex_version, apex_release=apex_release,
                        output_file_name=f"{screen.name}_generated.sql",
                        output_dir=str(pages_dir),
                    ).generate()
                matched_ids.add(apex_info['p_id'])
                list_screens.remove(screen)
                break

    # Pass 2 — fuzzy match for remaining screens
    remaining = [p for p in list_pages if p['p_id'] not in matched_ids]
    for screen in list_screens:
        screen_norm = _normalize_page_name(screen.name)
        best = max(remaining, key=lambda p: _similarity(screen_norm, _normalize_page_name(p['p_name'])), default=None)
        if best and _similarity(screen_norm, _normalize_page_name(best['p_name'])) >= 0.85:
            with _silent():
                UIPagesSQLGenerator(
                    model=domain_model, gui_model=gui_model,
                    app_id=app_id, screen=screen,
                    screen_number=best['p_id'],
                    workspace_name=workspace_name, user_name=USER_NAME,
                    apex_version=apex_version, apex_release=apex_release,
                    output_file_name=f"{screen.name}_generated.sql",
                    output_dir=str(pages_dir),
                ).generate()
            remaining = [p for p in remaining if p['p_id'] != best['p_id']]

else:
    # Mode B — fallback: sequential page numbering
    all_screens = sorted(
        (s for m in gui_model.modules.values() for s in m.screens if s.is_main_page),
        key=lambda s: s.name,
    )
    for idx, screen in enumerate(all_screens):
        page_num = idx + 2
        with _silent():
            UIPagesSQLGenerator(
                model=domain_model, gui_model=gui_model,
                app_id='100', screen=screen,
                screen_number=page_num,
                workspace_name=WORKSPACE_NAME, user_name=USER_NAME,
                apex_version='2024.11.30', apex_release='24.2.6',
                output_file_name=f'page_{page_num:05d}.sql',
                output_dir=str(pages_dir),
            ).generate()

print(f"✅ Migration finished.")
print(f"📂 Output generated at:\n{OUTPUT_PATH}")
