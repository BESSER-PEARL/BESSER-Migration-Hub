"""FastAPI entry point for the BESSER Migration Hub interface.

Run from the repository root so the ``migrator`` package is importable:

    uvicorn webapp.backend.app.main:app --reload --port 8000

The sys.path bootstrap below also makes it work when launched from other
working directories.
"""
from __future__ import annotations

import sys
from pathlib import Path

# --- Ensure the repo root (which contains the `migrator` package) is importable.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# The migrator parsers print progress with emoji (e.g. "✅"). On Windows the
# default cp1252 console encoding can't encode those and raises
# UnicodeEncodeError mid-parse, so force UTF-8 on the standard streams.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass

from fastapi import FastAPI  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402

from .routers import migration  # noqa: E402

app = FastAPI(
    title="BESSER Migration Hub",
    description="Standalone interface for migrating applications across low-code platforms "
                "via the BESSER B-UML pivot model.",
    version="0.1.0",
)

# Dev-friendly CORS: the Vite frontend runs on a different port.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(migration.router)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok"}
