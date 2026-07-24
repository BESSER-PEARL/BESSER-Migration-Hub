"""
Extended pipeline: UI page images -> B-UML structural model -> Oracle APEX SQL DDL.

Pipeline steps
--------------
1. User provides: UI page images folder, optional navigation/order/info files,
   OpenAI API key, and output folder.
2. mockup_to_buml  ->  output_folder/buml/model.py   (structural B-UML model)
                   ->  output_folder/gui_model/generated_gui_model.py  (not used here)
3. Dynamically load domain_model from the generated model.py.
4. OracleApexSQLGenerator  ->  output_folder/sql/tables_oracle_apex.sql
"""

import sys
import os
import importlib.util
from pathlib import Path

# ---------------------------------------------------------------------------
# Path bootstrap – allows running this script directly from converters/
# ---------------------------------------------------------------------------
_CONVERTERS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT   = _CONVERTERS_DIR.parents[1]          # BESSER-Migration-Hub root
_BESSER_ROOT    = _PROJECT_ROOT.parent / "BESSER"      # BESSER library root

for _p in (str(_PROJECT_ROOT), str(_BESSER_ROOT)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
# ---------------------------------------------------------------------------

from besser.BUML.notations.mockup_to_buml.mockup_to_buml import mockup_to_buml
from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ask(label: str, default: str = "") -> str:
    """Prompt the user for a value; return default if the user presses Enter."""
    if default:
        raw = input(f"  {label} [{default}]: ").strip()
        return raw if raw else default
    raw = input(f"  {label}: ").strip()
    return raw


def _load_domain_model(model_py_path: str):
    """
    Dynamically execute a generated B-UML model.py file and return the
    ``domain_model`` object it defines.

    mockup_to_buml writes a Python script to
    ``<output_folder>/buml/model.py`` whose last statement assigns a
    DomainModel instance to a module-level variable named ``domain_model``.
    importlib executes the file in an isolated module namespace to avoid
    polluting the caller's environment.
    """
    spec   = importlib.util.spec_from_file_location("_buml_structural_model", model_py_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["_buml_structural_model"] = module
    spec.loader.exec_module(module)

    if not hasattr(module, "domain_model"):
        raise AttributeError(
            f"The generated file '{model_py_path}' does not expose a "
            "'domain_model' variable.  Check mockup_to_buml output."
        )
    return module.domain_model


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print()
    print("=" * 65)
    print("  UI Page Images  ->  B-UML Structural Model  ->  Oracle APEX SQL")
    print("=" * 65)
    print()
    print("Provide the required inputs below.")
    print("(Press Enter to accept the value shown in [brackets].)\n")

    # --- Collect inputs from the user --------------------------------------
    api_key = _ask("OpenAI API key")

    images_folder = _ask(
        "Folder containing UI page mockup / screenshot images"
    )

    nav_image = _ask(
        "Navigation diagram image path  [optional – Enter to skip]",
        default=""
    ) or None

    pages_order = _ask(
        "Pages-order text file path     [optional – Enter to skip]",
        default=""
    ) or None

    additional_info = _ask(
        "Additional info file path      [optional – Enter to skip]",
        default=""
    ) or None

    default_output = str(_CONVERTERS_DIR / "output" / "mockup_buml")
    output_folder = _ask(
        "Output folder for B-UML artefacts",
        default=default_output
    )
    # -----------------------------------------------------------------------

    # Step 1 – run mockup_to_buml on the UI page images
    print(f"\n[1/3]  Running mockup_to_buml on '{images_folder}' …")
    mockup_to_buml(
        api_key=api_key,
        input_folder=images_folder,
        navigation_image_path=nav_image,
        pages_order_file_path=pages_order,
        additional_info_path=additional_info,
        output_folder=output_folder,
    )

    # Step 2 – load the generated structural B-UML model
    structural_model_file = os.path.join(output_folder, "buml", "model.py")
    if not os.path.isfile(structural_model_file):
        raise FileNotFoundError(
            f"Expected structural B-UML model at '{structural_model_file}' "
            "but mockup_to_buml did not create it.  "
            "Check the output for errors."
        )

    print(f"[2/3]  Loading domain model from '{structural_model_file}' …")
    domain_model = _load_domain_model(structural_model_file)

    # Step 3 – generate Oracle APEX SQL DDL
    sql_output_dir = os.path.join(output_folder, "sql")
    print(f"[3/3]  Generating Oracle APEX SQL into '{sql_output_dir}' …")

    sql_generator = OracleApexSQLGenerator(
        domain_model,
        output_dir=sql_output_dir,
        output_filename="tables_oracle_apex.sql",
    )
    sql_generator.generate()

    print()
    print("✅  Oracle APEX SQL generated successfully!")
    print(f"📁  Output directory : {os.path.abspath(sql_output_dir)}")
    print(f"    SQL file         : tables_oracle_apex.sql")


if __name__ == "__main__":
    main()

