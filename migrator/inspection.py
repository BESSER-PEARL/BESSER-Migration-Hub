"""Model summaries and source-file inspection."""
from pathlib import Path
from typing import Any

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


def _classify_uploads(directory: Path) -> dict:
    """Split uploaded files in a directory by extension."""
    images, csvs, jsons, sqls, zips, others = [], [], [], [], [], []
    if not directory.is_dir():
        return {"images": images, "csvs": csvs, "jsons": jsons, "sqls": sqls, "zips": zips, "others": others}
    for p in sorted(directory.iterdir()):
        if p.is_dir():
            continue
        suffix = p.suffix.lower()
        if suffix in (".png", ".jpg", ".jpeg"):
            images.append(p)
        elif suffix == ".csv":
            csvs.append(p)
        elif suffix == ".json":
            jsons.append(p)
        elif suffix == ".sql":
            sqls.append(p)
        elif suffix == ".zip":
            zips.append(p)
        else:
            others.append(p)
    return {"images": images, "csvs": csvs, "jsons": jsons, "sqls": sqls, "zips": zips, "others": others}


domain_summary = _domain_summary
gui_summary = _gui_summary
classify_files = _classify_uploads
