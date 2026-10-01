"""Target generation shared by scripts and the web interface."""
from pathlib import Path
from typing import Any

class GenerationError(Exception):
    """A target generator could not be selected."""

def generate_target(target_generator: str, sql_dialect: str | None,
                   model: Any, output_dir: Path, gui_model=None) -> list[str]:
    out = str(output_dir)

    if target_generator == "oracle_apex":
        from migrator.generators.sql.oracle_apex_app_generator import OracleApexFullAppGenerator
        app_name = getattr(model, "name", None) or "Generated_App"
        OracleApexFullAppGenerator(
            model=model,
            gui_model=gui_model,
            output_dir=out,
            output_filename="oracle_apex_app.sql",
            app_name=app_name,
        ).generate()

    elif target_generator == "spreadsheet":
        from migrator.generators.spreadsheet import SpreadSheetGenerator
        SpreadSheetGenerator(model=model, output_dir=out).generate()

    elif target_generator == "sql":
        from besser.generators.sql.sql_generator import SQLGenerator
        SQLGenerator(model=model, output_dir=out, sql_dialect=sql_dialect).generate()

    elif target_generator == "retool":
        from migrator.generators.retool.retool_generator import RetoolGenerator
        generator = RetoolGenerator(
            model=model, gui_model=gui_model, output_dir=out,
            app_name=getattr(model, 'name', None) or getattr(gui_model, 'name', None) or 'retool_app',
        )
        generator.generate()
        return generator.warnings

    elif target_generator == "service_now":
        from migrator.generators.service_now.service_now_generator import ServiceNowGenerator
        ServiceNowGenerator(model=model, output_dir=out).generate()

    else:
        raise GenerationError(f"No generator wired for '{target_generator}'.")
    return []

