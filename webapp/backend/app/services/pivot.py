"""Build the B-UML pivot model from uploaded source artifacts.

Wraps ``migrator.ModelMigrator`` / ``migrator.GUIModelMigrator`` and BESSER's
serialization helpers. Imports are done lazily so that the rest of the API
(e.g. /platforms) keeps working even if the heavy BESSER/migrator stack has an
import problem.
"""
from __future__ import annotations

from pathlib import Path
import shutil
from typing import Any

from ..platforms import get_source
from ..sessions import Session


class PivotError(Exception):
    """Raised when the pivot model cannot be produced."""


# --------------------------------------------------------------------------- #
# Summaries
# --------------------------------------------------------------------------- #

def _domain_summary(model: Any) -> dict:
    from besser.BUML.metamodel.structural import Class, Enumeration

    types = list(getattr(model, "types", []) or [])
    classes = [t for t in types if isinstance(t, Class)]
    enums = [t for t in types if isinstance(t, Enumeration)]
    associations = list(getattr(model, "associations", []) or [])

    attributes = 0
    for c in classes:
        attributes += len(list(getattr(c, "attributes", []) or []))

    return {
        "classes": len(classes),
        "attributes": attributes,
        "associations": len(associations),
        "enumerations": len(enums),
        "class_names": sorted(getattr(c, "name", "?") for c in classes),
    }


def _gui_summary(model: Any) -> dict:
    raw_modules = getattr(model, "modules", []) or []
    modules = list(raw_modules.values()) if isinstance(raw_modules, dict) else list(raw_modules)
    screens: list[Any] = []
    for m in modules:
        screens.extend(list(getattr(m, "screens", []) or []))

    widgets = 0
    screen_names = []
    for s in screens:
        screen_names.append(getattr(s, "name", "?"))
        # Screens expose their widgets under a few possible attribute names.
        for attr in ("view_elements", "elements", "view_components"):
            widgets += len(list(getattr(s, attr, []) or []))

    return {
        "modules": len(modules),
        "screens": len(screens),
        "widgets": widgets,
        "screen_names": sorted(screen_names),
    }


def _build_screenshot_gui(session: Session, openai_token: str) -> tuple[Any, str, str | None]:
    """Generate a GUI pivot model from uploaded screenshots with BESSER's LLM pipeline."""
    from besser.BUML.notations.mockup_to_buml.mockup_to_buml import mockup_to_buml
    from migrator.converters.fix_gui_model import fix_generated_gui_model
    from migrator.converters.mockup_to_apex_eval import _load_module_attribute

    output_dir = session.work_dir / "mockup_buml"
    mockup_to_buml(
        api_key=openai_token,
        input_folder=str(session.uploads_dir),
        output_folder=str(output_dir),
    )

    gui_file = output_dir / "gui_model" / "generated_gui_model.py"
    if not gui_file.is_file():
        raise PivotError(
            "The screenshot pipeline did not produce a GUI model. "
            "Check the screenshots and try again."
        )

    # LLM output can contain forward references and invalid enum names.
    fix_generated_gui_model(str(gui_file))
    try:
        gui_model = _load_module_attribute(str(gui_file), "gui_model")
    except Exception as exc:
        raise PivotError(f"Generated GUI model could not be loaded: {exc}") from exc

    filename = "gui_model.py"
    shutil.copy2(gui_file, session.pivot_dir / filename)
    return gui_model, filename, None


# --------------------------------------------------------------------------- #
# Serialization
# --------------------------------------------------------------------------- #

def _serialize_domain(model: Any, pivot_dir: Path) -> str:
    """Write a runnable buml_model.py; return the filename."""
    from besser.utilities.buml_code_builder import domain_model_to_code

    filename = "buml_model.py"
    domain_model_to_code(model=model, file_path=str(pivot_dir / filename))
    return filename


def _serialize_gui(model: Any, pivot_dir: Path) -> tuple[str, str | None]:
    """Serialize the GUI model. Returns (filename, note).

    Prefers a BESSER GUI code-builder if one exists; otherwise falls back to a
    readable text dump so the user still gets something to download.
    """
    from besser.utilities import buml_code_builder as bcb  # type: ignore

    builder = None
    for fn_name in ("gui_model_to_code", "gui_to_code", "guimodel_to_code"):
        fn = getattr(bcb, fn_name, None)
        if callable(fn):
            builder = fn
            break

    fallback_note: str | None = None
    if builder is not None:
        try:
            filename = "gui_model.py"
            builder(model=model, file_path=str(pivot_dir / filename))
            return filename, None
        except Exception as exc:
            fallback_note = (
                "The BESSER GUI code-builder could not serialize this model "
                f"({exc}); exported a readable text dump instead."
            )
    else:
        fallback_note = (
            "No BESSER GUI code-builder available; exported a readable text dump instead."
        )

    # Fallback: dump a readable representation so the user still gets a file.
    filename = "gui_model.txt"
    lines = ["# GUI pivot model (readable dump)\n"]
    for m in getattr(model, "modules", []) or []:
        lines.append(f"Module: {getattr(m, 'name', '?')}")
        for s in getattr(m, "screens", []) or []:
            lines.append(f"  Screen: {getattr(s, 'name', '?')}")
    (pivot_dir / filename).write_text("\n".join(lines), encoding="utf-8")
    return filename, fallback_note


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #

def _classify_uploads(session: Session) -> dict:
    """Split uploaded files by kind."""
    images, csvs, jsons, others = [], [], [], []
    for p in sorted(session.uploads_dir.iterdir()):
        suffix = p.suffix.lower()
        if suffix in (".png", ".jpg", ".jpeg"):
            images.append(p)
        elif suffix == ".csv":
            csvs.append(p)
        elif suffix == ".json":
            jsons.append(p)
        else:
            others.append(p)
    return {"images": images, "csvs": csvs, "jsons": jsons, "others": others}


def build_pivot(
    session: Session,
    source_lcp: str,
    scope: str,
    module_name: str | None,
    openai_token: str | None,
) -> dict:
    """Parse uploads into the pivot model(s), serialize, and summarize.

    Returns a dict shaped like schemas.PivotResponse (minus session_id).
    Stores the model objects on the session for later generation.
    """
    from migrator import ModelMigrator, GUIModelMigrator

    source = get_source(source_lcp)
    if source is None:
        raise PivotError(f"Unknown source platform '{source_lcp}'.")
    if not source.implemented:
        raise PivotError(f"Source platform '{source.label}' is not implemented yet.")

    files = _classify_uploads(session)
    warnings: list[str] = []
    want_data = scope in ("data", "both")
    want_gui = scope in ("gui", "both")

    # Resolve the primary model path per source type.
    if source_lcp == "mendix":
        if not files["jsons"]:
            raise PivotError("No Mendix JSON file was uploaded.")
        model_path = str(files["jsons"][0])
        if not module_name:
            raise PivotError("A Mendix module name is required.")
        mig_module: Any = module_name
    else:  # LLM path
        if not files["images"]:
            raise PivotError("An image/screenshot is required for LLM-based extraction.")
        model_path = str(files["images"][0])
        # The PowerApps parser reuses `module_name` to carry the CSV paths.
        mig_module = [str(p) for p in files["csvs"]]
        if source.needs_openai and not openai_token:
            raise PivotError("An OpenAI token is required for this LLM-based transformation.")

    summary: dict = {}
    downloads: list[dict] = []

    # ---- Domain model -----------------------------------------------------
    if want_data:
        if not source.supports_data:
            warnings.append(f"{source.label} does not support data-model extraction; skipped.")
        else:
            try:
                dm = ModelMigrator(
                    lcp=source_lcp,
                    model_path=model_path,
                    module_name=mig_module,
                    openai_token=openai_token or "",
                ).domain_model()
            except Exception as exc:  # surface parser errors cleanly
                raise PivotError(f"Data-model extraction failed: {exc}") from exc
            if dm is None:
                raise PivotError(
                    "Data-model extraction returned nothing. "
                    "Check the module name / uploaded file."
                )
            session.domain_model = dm
            summary.update(_domain_summary(dm))
            fname = _serialize_domain(dm, session.pivot_dir)
            downloads.append({"artifact": "domain", "filename": fname, "available": True})

    # ---- GUI model --------------------------------------------------------
    if want_gui:
        if not source.supports_gui:
            warnings.append(
                f"GUI extraction is not available for {source.label} yet; skipped."
            )
            downloads.append({
                "artifact": "gui", "filename": "", "available": False,
                "note": f"GUI extraction not implemented for {source.label}.",
            })
        elif source.transformation == "llm":
            try:
                gm, fname, note = _build_screenshot_gui(session, openai_token or "")
            except PivotError:
                raise
            except Exception as exc:
                raise PivotError(f"Screenshot GUI-model extraction failed: {exc}") from exc
            session.gui_model = gm
            summary.update(_gui_summary(gm))
            downloads.append({
                "artifact": "gui", "filename": fname, "available": True, "note": note,
            })
        else:
            try:
                gm = GUIModelMigrator(
                    lcp=source_lcp,
                    model_path=model_path,
                    module_name=mig_module,
                    openai_token=openai_token or "",
                ).gui_model()
            except Exception as exc:
                raise PivotError(f"GUI-model extraction failed: {exc}") from exc
            if gm is None:
                warnings.append("GUI-model extraction returned nothing; skipped.")
            else:
                session.gui_model = gm
                summary.update(_gui_summary(gm))
                fname, note = _serialize_gui(gm, session.pivot_dir)
                downloads.append({
                    "artifact": "gui", "filename": fname, "available": True, "note": note,
                })

    if not downloads or not any(d["available"] for d in downloads):
        raise PivotError("Nothing could be extracted from the provided inputs.")

    session.source_lcp = source_lcp
    session.scope = scope
    session.module_name = module_name

    return {"summary": summary, "downloads": downloads, "warnings": warnings}
