"""Shared loader for Retool RSX Toolscript exports.

An RSX export can arrive either as a ``.zip`` file or as an already
extracted directory. Both layouts are read into the same
``{relative_posix_path: text}`` shape so the RSX/GUI parser and the
CSV/data-model parser's optional SQL-mining step can share one
implementation instead of duplicating zip-vs-folder handling.
"""

import os
import zipfile

# Extensions worth decoding as text; anything else (images, etc.) is skipped.
_TEXT_EXTENSIONS = ('.rsx', '.sql', '.js', '.json')


def _find_app_root(paths: list) -> str:
    """Return the directory prefix (posix, '' or 'app_name/') that contains
    main.rsx / metadata.json, so nested "<app_name>/..." export layouts are
    normalised the same way flat ones are.
    """
    for p in paths:
        if p == 'main.rsx' or p.endswith('/main.rsx'):
            return p[: -len('main.rsx')]
    for p in paths:
        if p == 'metadata.json' or p.endswith('/metadata.json'):
            return p[: -len('metadata.json')]
    return ''


def load_rsx_source(path: str) -> dict:
    """Load an RSX export (zip file or directory) into a flat text map.

    Args:
        path: Path to either the RSX ``.zip`` file or the extracted
            RSX folder.

    Returns:
        A dict mapping app-root-relative POSIX paths (e.g. ``'main.rsx'``,
        ``'src/checkoutModal.rsx'``, ``'lib/getOrders.sql'``) to their
        decoded text content. Empty dict if the path doesn't exist or
        contains no readable files.
    """
    if not path or not os.path.exists(path):
        return {}

    raw: dict = {}
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path, 'r') as zf:
            for name in zf.namelist():
                if name.endswith('/') or not name.lower().endswith(_TEXT_EXTENSIONS):
                    continue
                with zf.open(name) as fh:
                    raw[name.replace(os.sep, '/')] = fh.read().decode('utf-8', errors='replace')
    elif os.path.isdir(path):
        for root, _dirs, files in os.walk(path):
            for fname in files:
                if not fname.lower().endswith(_TEXT_EXTENSIONS):
                    continue
                full = os.path.join(root, fname)
                rel = os.path.relpath(full, path).replace(os.sep, '/')
                with open(full, 'r', encoding='utf-8', errors='replace') as fh:
                    raw[rel] = fh.read()
    else:
        return {}

    root_prefix = _find_app_root(list(raw.keys()))
    if not root_prefix:
        return raw
    return {
        k[len(root_prefix):]: v
        for k, v in raw.items()
        if k.startswith(root_prefix)
    }
