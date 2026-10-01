"""List the modules contained in a Mendix export JSON.

Mirrors the module-detection logic used by ``migrator/parsers/mendix.py``
(a module is the first ``.``-separated segment of an entity's
``$QualifiedName`` inside a ``DomainModels$DomainModel`` unit) so the UI can
offer a dropdown instead of asking the user to type the module name.
"""
from __future__ import annotations

import json
from pathlib import Path

_ENCODINGS = ["utf-8", "utf-16", "utf-16-le", "utf-16-be"]


def _load_json(json_path: str | Path) -> dict | None:
    for enc in _ENCODINGS:
        try:
            with open(json_path, "r", encoding=enc) as fh:
                return json.load(fh)
        except UnicodeDecodeError:
            continue
        except json.JSONDecodeError:
            return None
        except Exception:
            return None
    return None


def list_modules(json_path: str | Path) -> list[str]:
    """Return the sorted list of module names found in a Mendix export."""
    data = _load_json(json_path)
    if not data:
        return []

    modules: set[str] = set()
    for unit in data.get("units", []):
        if unit.get("$Type") == "DomainModels$DomainModel" and unit.get("entities"):
            qualified = unit["entities"][0].get("$QualifiedName", "")
            module = qualified.split(".")[0] if qualified else ""
            if module:
                modules.add(module)
    return sorted(modules)
