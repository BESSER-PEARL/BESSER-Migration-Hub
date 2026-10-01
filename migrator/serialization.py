"""B-UML source serialization and compatibility repairs."""
from pathlib import Path
from typing import Any
import re

def _fix_digit_leading_vars(file_path: Path) -> None:
    """Rename Python identifiers that start with a digit in a generated BUML file.

    BESSER's code builder emits names like ``100_transactions_generated = Screen(...)``
    which are invalid Python identifiers.  This scans for every such LHS name and
    prepends ``_`` to all standalone occurrences, leaving quoted string values untouched.
    """
    content = file_path.read_text(encoding="utf-8")
    # Find identifiers starting with a digit used as assignment targets or attribute bases.
    bad_names = set(re.findall(r'^(\d\w+)\s*[=.]', content, re.MULTILINE))
    if not bad_names:
        return
    for name in bad_names:
        # Replace only standalone occurrences (not inside strings or longer identifiers).
        content = re.sub(
            r'(?<![A-Za-z0-9_"\'])' + re.escape(name) + r'(?![A-Za-z0-9_"\'])',
            '_' + name,
            content,
        )
    file_path.write_text(content, encoding="utf-8")


_GLOBALS_DOMAIN_MODEL_REF = (
    "domain_model_ref = globals().get('domain_model') or "
    "next((v for k, v in globals().items() if k.startswith('domain_model') "
    "and hasattr(v, 'get_class_by_name')), None)"
)


_SAFE_DOMAIN_MODEL_REF = (
    "try:\n"
    "    domain_model_ref = domain_model\n"
    "except NameError:\n"
    "    domain_model_ref = None"
)


def _fix_globals_domain_model_ref(file_path: Path) -> None:
    """Replace BESSER's ``globals()``-based domain-model lookup with a direct reference.

    ``besser.utilities.buml_code_builder`` emits ``domain_model_ref = globals().get(...)``
    for DataList/data-binding resolution. Some BUML BESSER-editor consumers execute
    generated content in a restricted namespace without ``globals``/``__builtins__``,
    which makes the import fail with ``name 'globals' is not defined``. Since the
    combined project always defines ``domain_model`` as a top-level name before the
    GUI section, a plain (builtin-free) name lookup is equivalent and safe everywhere.
    """
    content = file_path.read_text(encoding="utf-8")
    if _GLOBALS_DOMAIN_MODEL_REF not in content:
        return
    content = content.replace(_GLOBALS_DOMAIN_MODEL_REF, _SAFE_DOMAIN_MODEL_REF)
    file_path.write_text(content, encoding="utf-8")


def _collect_constructor_variables(content: str, class_name: str) -> dict[str, list[str]]:
    """Map ``target_name -> [variable names, in file order]`` for every
    ``var = ClassName(..., name="target_name", ...)`` call in generated code,
    whether written on one line or spread across several (``_write_constructor``
    picks single- vs multi-line purely based on how many parameters it has).

    Mendix widget names are only unique *within one page*, not across the
    whole app (e.g. many pages independently have their own "listView1"), so
    the same ``name=`` value can legitimately appear many times; BESSER's own
    ``created_vars`` dedup then assigns each a distinct Python variable
    (``listview1``, ``listview1_1``, ``listview1_2``, ...). Returning every
    occurrence (not just the first) lets the caller pair them up positionally
    instead of always grabbing the first match.
    """
    occurrences: dict[str, list[str]] = {}
    lines = content.splitlines()
    start_pattern = re.compile(rf'^(\w+) = {re.escape(class_name)}\(')
    name_pattern = re.compile(r'name="((?:[^"\\]|\\.)*)"')
    i = 0
    while i < len(lines):
        match = start_pattern.match(lines[i])
        if match:
            var_name = match.group(1)
            block_lines = [lines[i]]
            j = i
            if not lines[i].rstrip().endswith(')'):
                j += 1
                while j < len(lines) and lines[j].strip() != ')':
                    block_lines.append(lines[j])
                    j += 1
                if j < len(lines):
                    block_lines.append(lines[j])
            name_match = name_pattern.search("\n".join(block_lines))
            if name_match:
                occurrences.setdefault(name_match.group(1), []).append(var_name)
            i = j
        i += 1
    return occurrences


def _fix_gui_data_bindings(file_path: Path, gui_model: Any) -> None:
    """Append ``<var>.data_binding = DataBinding(domain_concept=<ClassVar>)`` lines
    for every ``Form``/``DataList`` whose ``data_binding`` the Mendix parser
    resolved to a domain ``Class``.

    Unlike charts/``MetricCard``, BESSER's own ``gui_model_to_code`` never
    serializes ``data_binding`` for ``Form``/``DataList`` at all (verified
    against the installed package), so it would otherwise be silently dropped
    from the generated file even though the in-memory BUML object has it set.
    This assumes the domain model was already emitted earlier in the same
    file (true for the combined "download BUML project" file), so each class
    is referenced by the exact variable name ``domain_model_to_code`` gave it.
    """
    from besser.BUML.metamodel.gui.graphical_ui import Form, DataList
    from besser.utilities.buml_code_builder.common import safe_class_name

    def walk(elems):
        # Sort at every level the same way gui_model_to_code does (by
        # (display_order, name), which reduces to plain name-order here since
        # our parser never sets display_order) so that same-named elements
        # across different screens are visited in the same relative order the
        # code-builder emitted them in.
        collected = []
        for e in sorted(elems, key=lambda x: (getattr(x, "display_order", None) or 0, x.name)):
            collected.append(e)
            if hasattr(e, "view_elements") and e.view_elements:
                collected.extend(walk(e.view_elements))
        return collected

    modules = sorted(getattr(gui_model, "modules", []) or [], key=lambda m: m.name)
    screens = [s for m in modules for s in sorted(getattr(m, "screens", []) or [], key=lambda s: s.name)]
    all_elements = walk(screens)
    bound = [
        e for e in all_elements
        if isinstance(e, (Form, DataList)) and getattr(e, "data_binding", None) is not None
        and getattr(e.data_binding, "domain_concept", None) is not None
    ]
    if not bound:
        return

    content = file_path.read_text(encoding="utf-8")
    form_vars = _collect_constructor_variables(content, "Form")
    datalist_vars = _collect_constructor_variables(content, "DataList")
    next_index: dict[tuple[str, str], int] = {}

    new_lines = []
    for element in bound:
        is_form = isinstance(element, Form)
        occurrences = form_vars.get(element.name) if is_form else datalist_vars.get(element.name)
        if not occurrences:
            continue
        key = ("Form" if is_form else "DataList", element.name)
        idx = next_index.get(key, 0)
        if idx >= len(occurrences):
            continue
        next_index[key] = idx + 1
        var_name = occurrences[idx]
        class_var = safe_class_name(element.data_binding.domain_concept.name)
        new_lines.append(f"{var_name}.data_binding = DataBinding(domain_concept={class_var})\n")

    if not new_lines:
        return
    # gui_model_to_code always emits `from besser.BUML.metamodel.gui.binding import
    # DataBinding` unconditionally, so it's already available here.
    content = (
        content.rstrip("\n") + "\n\n"
        "# Bound-entity data bindings resolved by the Mendix parser\n"
        + "".join(new_lines)
    )
    file_path.write_text(content, encoding="utf-8")


def _serialize_domain(model: Any, pivot_dir: Path) -> str:
    """Write a runnable buml_model.py; return the filename."""
    from besser.utilities.buml_code_builder import domain_model_to_code

    filename = "buml_model.py"
    out_path = pivot_dir / filename
    domain_model_to_code(model=model, file_path=str(out_path))
    _fix_digit_leading_vars(out_path)
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
        out_path = pivot_dir / "gui_model.py"
        try:
            builder(model=model, file_path=str(out_path))
            _fix_digit_leading_vars(out_path)
            _fix_globals_domain_model_ref(out_path)
            _fix_gui_data_bindings(out_path, model)
            return "gui_model.py", None
        except Exception as exc:
            # The builder may have written a partial file before failing; remove it so
            # the project-download endpoint doesn't silently bundle broken code instead
            # of the fallback text dump produced below.
            out_path.unlink(missing_ok=True)
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


serialize_domain = _serialize_domain
serialize_gui = _serialize_gui
