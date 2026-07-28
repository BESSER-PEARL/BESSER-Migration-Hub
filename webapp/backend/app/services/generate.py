"""Generate target-platform artifacts from the stored pivot model.

Dispatches to the right BESSER / migrator generator based on the target
platform's ``generator`` field. Instead of hard-coding output filenames, we
snapshot the session output directory before and after ``generate()`` and
register whatever new files appear.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from ..platforms import get_target
from ..sessions import Session


class GenerateError(Exception):
    """Raised when target artifacts cannot be produced."""


def _snapshot(output_dir: Path) -> set[Path]:
    return {p for p in output_dir.rglob("*") if p.is_file()}


def _run_generator(target_generator: str, sql_dialect: str | None,
                   model: Any, output_dir: Path) -> None:
    out = str(output_dir)

    if target_generator == "oracle_apex":
        from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator
        OracleApexSQLGenerator(
            model=model,
            output_dir=out,
            output_filename="tables_oracle_apex.sql",
        ).generate()

    elif target_generator == "spreadsheet":
        from migrator.generators.spreadsheet import SpreadSheetGenerator
        SpreadSheetGenerator(model=model, output_dir=out).generate()

    elif target_generator == "sql":
        from besser.generators.sql.sql_generator import SQLGenerator
        SQLGenerator(model=model, output_dir=out, sql_dialect=sql_dialect).generate()

    else:
        raise GenerateError(f"No generator wired for '{target_generator}'.")


def _run_apex_gui_generator(session: Session) -> list[Path]:
    """Generate APEX page SQL from the stored GUI pivot and uploaded export."""
    if session.apex_export_dir is None:
        raise GenerateError(
            "Upload a split Oracle APEX custom export before generating GUI pages."
        )
    if session.gui_model is None:
        return []

    from migrator.converters.besser_to_apex import generate_pages_for_gui_model
    from migrator.converters.mockup_to_apex_eval import _extract_apex_app_info

    info = _extract_apex_app_info(str(session.apex_export_dir))
    page_output_dir = session.output_dir / "apex_pages"
    page_output_dir.mkdir(parents=True, exist_ok=True)
    generate_pages_for_gui_model(
        str(session.apex_export_dir),
        session.gui_model,
        session.domain_model,
        info["workspace_name"],
        info["apex_user"],
        output_dir=str(page_output_dir),
    )

    generated = sorted(p for p in page_output_dir.glob("*_generated.sql") if p.is_file())
    if not generated:
        raise GenerateError("No generated APEX page SQL files were produced.")
    return generated


def generate_artifacts(session: Session, target_lcp: str) -> dict:
    """Produce artifacts for the chosen target. Returns a dict shaped like
    schemas.GenerateResponse (minus session_id)."""
    target = get_target(target_lcp)
    if target is None:
        raise GenerateError(f"Unknown target platform '{target_lcp}'.")
    if not target.implemented or not target.generator:
        raise GenerateError(f"Target platform '{target.label}' is not implemented yet.")

    if target.supports_data and session.domain_model is None:
        raise GenerateError(
            "No domain model available in this session. "
            "Generate the pivot model with the data-model scope first."
        )

    warnings: list[str] = []
    output_dir = session.output_dir
    before = _snapshot(output_dir)

    try:
        _run_generator(target.generator, target.sql_dialect, session.domain_model, output_dir)
    except Exception as exc:
        raise GenerateError(f"Generation failed: {exc}") from exc

    apex_pages: list[Path] = []
    if target_lcp == "oracle_apex" and session.gui_model is not None:
        if session.apex_export_dir is None:
            warnings.append(
                "The table script is ready. After importing it into APEX and exporting "
                "the app as a split ZIP, upload that ZIP to generate GUI page SQL."
            )
        else:
            try:
                apex_pages = _run_apex_gui_generator(session)
            except Exception as exc:
                raise GenerateError(f"APEX GUI page generation failed: {exc}") from exc

    after = _snapshot(output_dir)
    new_files = sorted(after - before, key=lambda p: p.name)

    if not new_files:
        # Some generators may overwrite existing files; fall back to all files.
        new_files = sorted(after, key=lambda p: p.name)
    if not new_files:
        raise GenerateError("The generator produced no output files.")

    artifacts = []
    for p in new_files:
        rel = p.relative_to(output_dir).as_posix()
        session.artifacts[rel] = {"path": str(p), "description": target.output_desc}
        artifacts.append({"name": rel, "description": target.output_desc})

    session.target_lcp = target_lcp
    return {"artifacts": artifacts, "tutorial": target.tutorial, "warnings": warnings}
