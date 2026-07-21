"""HTTP API for the Migration Hub wizard."""
from __future__ import annotations

import io
import re
import tempfile
import zipfile
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, StreamingResponse

from .. import platforms
from ..schemas import (
    GenerateRequest,
    GenerateResponse,
    ModulesResponse,
    PivotResponse,
    PlatformsResponse,
)
from ..services import generate as generate_service
from ..services import mendix_inspect
from ..services import pivot as pivot_service
from ..sessions import store

router = APIRouter(prefix="/api")

_SAFE_NAME = re.compile(r"[^A-Za-z0-9._-]+")


def _safe_filename(name: str) -> str:
    name = Path(name or "upload").name
    return _SAFE_NAME.sub("_", name) or "upload"


# --------------------------------------------------------------------------- #
# Registry
# --------------------------------------------------------------------------- #

@router.get("/platforms", response_model=PlatformsResponse)
def get_platforms() -> PlatformsResponse:
    return PlatformsResponse(
        sources=platforms.sources_public(),
        targets=platforms.targets_public(),
    )


# --------------------------------------------------------------------------- #
# Mendix module discovery
# --------------------------------------------------------------------------- #

@router.post("/mendix/modules", response_model=ModulesResponse)
async def mendix_modules(file: UploadFile = File(...)) -> ModulesResponse:
    suffix = Path(file.filename or "model.json").suffix or ".json"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        modules = mendix_inspect.list_modules(tmp_path)
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    if not modules:
        raise HTTPException(
            status_code=422,
            detail="No modules found. Is this a valid Mendix export JSON?",
        )
    return ModulesResponse(modules=modules)


# --------------------------------------------------------------------------- #
# Pivot model
# --------------------------------------------------------------------------- #

@router.post("/pivot", response_model=PivotResponse)
async def create_pivot(
    source_lcp: str = Form(...),
    scope: str = Form("data"),
    module_name: Optional[str] = Form(None),
    openai_token: Optional[str] = Form(None),
    files: list[UploadFile] = File(...),
) -> PivotResponse:
    if scope not in ("data", "gui", "both"):
        raise HTTPException(status_code=422, detail="scope must be 'data', 'gui' or 'both'.")

    session = store.create()
    # Persist uploads.
    for f in files:
        dest = session.uploads_dir / _safe_filename(f.filename or "upload")
        dest.write_bytes(await f.read())

    try:
        result = pivot_service.build_pivot(
            session=session,
            source_lcp=source_lcp,
            scope=scope,
            module_name=module_name,
            openai_token=openai_token,
        )
    except pivot_service.PivotError as exc:
        store.delete(session.id)
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except ModuleNotFoundError as exc:
        store.delete(session.id)
        raise HTTPException(
            status_code=503,
            detail=(
                "The migration engine is not installed. Run `pip install -r requirements.txt` "
                f"before retrying. Missing module: {exc.name}."
            ),
        ) from exc

    return PivotResponse(
        session_id=session.id,
        source_lcp=source_lcp,
        scope=scope,
        summary=result["summary"],
        downloads=result["downloads"],
        warnings=result["warnings"],
    )


@router.get("/sessions/{session_id}/download/pivot")
def download_pivot(session_id: str, artifact: str = "all"):
    session = store.get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found.")

    pivot_dir = session.pivot_dir
    files = sorted(p for p in pivot_dir.iterdir() if p.is_file())
    if not files:
        raise HTTPException(status_code=404, detail="No pivot artifacts available.")

    if artifact in ("domain", "gui"):
        prefix = "buml_model" if artifact == "domain" else "gui_model"
        match = next((p for p in files if p.stem.startswith(prefix)), None)
        if match is None:
            raise HTTPException(status_code=404, detail=f"No {artifact} artifact available.")
        return FileResponse(str(match), filename=match.name, media_type="application/octet-stream")

    # Default: zip everything in the pivot dir.
    return _zip_response(files, pivot_dir, "pivot_model.zip")


# --------------------------------------------------------------------------- #
# Target generation
# --------------------------------------------------------------------------- #

@router.post("/sessions/{session_id}/generate", response_model=GenerateResponse)
def generate(session_id: str, body: GenerateRequest) -> GenerateResponse:
    session = store.get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found.")

    try:
        result = generate_service.generate_artifacts(session, body.target_lcp)
    except generate_service.GenerateError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    return GenerateResponse(
        session_id=session.id,
        target_lcp=body.target_lcp,
        artifacts=result["artifacts"],
        tutorial=result["tutorial"],
        warnings=result["warnings"],
    )


@router.get("/sessions/{session_id}/download/artifacts")
def download_artifacts(session_id: str, name: str = "all"):
    session = store.get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found.")
    if not session.artifacts:
        raise HTTPException(status_code=404, detail="No generated artifacts available.")

    if name != "all":
        info = session.artifacts.get(name)
        if info is None:
            raise HTTPException(status_code=404, detail=f"Artifact '{name}' not found.")
        path = Path(info["path"])
        return FileResponse(str(path), filename=path.name, media_type="application/octet-stream")

    files = [Path(info["path"]) for info in session.artifacts.values()]
    return _zip_response(files, session.output_dir, "artifacts.zip")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _zip_response(files: list[Path], base_dir: Path, download_name: str) -> StreamingResponse:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            if p.is_file():
                try:
                    arcname = p.relative_to(base_dir).as_posix()
                except ValueError:
                    arcname = p.name
                zf.write(p, arcname)
    buffer.seek(0)
    return StreamingResponse(
        buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{download_name}"'},
    )
