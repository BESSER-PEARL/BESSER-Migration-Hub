"""In-memory migration session store.

A session holds the parsed pivot model(s) between the /pivot and /generate
calls, plus a temporary working directory where uploads and generated
artifacts live. This is deliberately simple (single process, memory only);
swap for a persistent store when embedding into the BESSER editor.
"""
from __future__ import annotations

import shutil
import tempfile
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class Session:
    id: str
    work_dir: Path
    source_lcp: str = ""
    module_name: Optional[str] = None
    scope: str = "data"                 # data | gui | both
    domain_model: Any = None            # besser DomainModel
    gui_model: Any = None               # besser GUIModel
    # Files generated for a chosen target: filename -> {path, description}.
    artifacts: dict[str, dict] = field(default_factory=dict)
    target_lcp: Optional[str] = None

    @property
    def uploads_dir(self) -> Path:
        d = self.work_dir / "uploads"
        d.mkdir(parents=True, exist_ok=True)
        return d

    @property
    def pivot_dir(self) -> Path:
        d = self.work_dir / "pivot"
        d.mkdir(parents=True, exist_ok=True)
        return d

    @property
    def output_dir(self) -> Path:
        d = self.work_dir / "output"
        d.mkdir(parents=True, exist_ok=True)
        return d


class SessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}
        self._root = Path(tempfile.gettempdir()) / "besser_migration_hub"
        self._root.mkdir(parents=True, exist_ok=True)

    def create(self) -> Session:
        sid = uuid.uuid4().hex[:12]
        work_dir = self._root / sid
        work_dir.mkdir(parents=True, exist_ok=True)
        session = Session(id=sid, work_dir=work_dir)
        self._sessions[sid] = session
        return session

    def get(self, session_id: str) -> Optional[Session]:
        return self._sessions.get(session_id)

    def delete(self, session_id: str) -> None:
        session = self._sessions.pop(session_id, None)
        if session is not None:
            shutil.rmtree(session.work_dir, ignore_errors=True)


# Module-level singleton used by the routers.
store = SessionStore()
