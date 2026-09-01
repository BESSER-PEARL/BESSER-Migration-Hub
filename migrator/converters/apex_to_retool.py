import io
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

from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui
from migrator.generators.retool.retool_generator import RetoolGenerator
from migrator.generators.retool.retool_rsx_app_generator import RetoolRsxAppGenerator

# ==============================================================================
# INPUT CONFIGURATION — edit these paths before running
# ==============================================================================

DDL_PATH    = Path(r"path/to/script.sql")       # Oracle APEX DDL SQL file
PAGES_DIR   = Path(r"path/to/apex/pages")       # folder with page_000XX.sql files
APP_NAME    = "my_retool_app"                   # name for the generated Retool app
MODULE_NAME = "App"                             # B-UML module name
OUTPUT_PATH = Path("output").resolve()          # output folder

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


# Step 1 — Parse DDL → DomainModel
print(f"[1/4] Parsing Oracle APEX DDL: {DDL_PATH.name}")
if not DDL_PATH.is_file():
    raise FileNotFoundError(f"DDL file not found: {DDL_PATH}")
with _silent():
    domain_model = oracle_apex_to_buml(ddl_path=str(DDL_PATH), module_name=MODULE_NAME)
if domain_model is None:
    raise RuntimeError(f"DDL parsing returned no model — check the file: {DDL_PATH}")

# Step 2 — Parse APEX pages → GUIModel
print(f"[2/4] Parsing APEX pages: {PAGES_DIR.name}")
if not PAGES_DIR.is_dir():
    raise FileNotFoundError(f"Pages directory not found: {PAGES_DIR}")
with _silent():
    gui_model = oracle_apex_to_gui(pages_dir=str(PAGES_DIR), module_name=MODULE_NAME)

# Step 3 — Generate CSV files (one per entity, for Retool DB import)
print(f"[3/4] Generating CSV files")
with _silent():
    csv_generator = RetoolGenerator(model=domain_model, app_name=APP_NAME, output_dir=str(OUTPUT_PATH))
    csv_generator.generate_csv()

# Step 4 — Generate Retool RSX app (folder + .zip)
print(f"[4/4] Generating Retool RSX app")
with _silent():
    rsx_generator = RetoolRsxAppGenerator(
        domain_model=domain_model, gui_model=gui_model,
        app_name=APP_NAME, output_dir=str(OUTPUT_PATH),
    )
    rsx_generator.generate()

print(f"\n✅ Migration finished.")
print(f"📂 Output generated at:\n{OUTPUT_PATH}")
