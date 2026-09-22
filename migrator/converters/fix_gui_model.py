"""
Fixer (v2) for LLM-generated GUI model Python files.

Strategy
--------
Circular dependency problem: list Screens need buttons/datalists in
view_elements, but nav Buttons need list Screens as targetScreen.

Solution (two-phase Screen creation):
  Phase 1 – Create list Screens with view_elements={} so nav Buttons
             can reference them by name.
  Phase 2 – After all buttons/datasources/datalists are defined, patch
             each Screen's view_elements back:
             LibraryListScreen.view_elements = {libraryAddingButton, libraryList}

Final order in the output file:
  1. Imports (buml.model, structural, gui – always at top)
  2. List Screens with view_elements={}
  3. Nav Buttons (targetScreen=<list screen>)
  4. Home Screen (is_main_page=True, view_elements={nav buttons})
  5. Add Buttons (no targetScreen)
  6. DataSourceElements
  7. DataLists
  8. ViewComponent / other GUI constructors
  9. Scalar field-name assignments (only those referenced above)
 10. Screen.view_elements patch lines
 11. Modules
 12. GUIModel

Also:
  - Strips local class re-definitions of BESSER metamodel classes.
  - Strips stub domain classes (class Author: pass).
  - Strips junk code (with-blocks, for-loops, print calls, etc.).
  - Normalises imports: forces the three required imports at top,
    drops redundant ones.
"""
import ast
import re
from typing import Dict, List, Optional, Set, Tuple

_REQUIRED_IMPORTS = [
    "from buml.model import *",
    "from besser.BUML.metamodel.gui import *",
    "from besser.BUML.metamodel.structural import *",
]

_GUI_CONSTRUCTORS: Set[str] = {
    "Button", "Screen", "Module", "GUIModel",
    "DataList", "DataSourceElement", "ViewComponent",
    "InputField", "Label", "TextField",
}

_BESSER_GUI_CLASSES: Set[str] = {
    "ScreenType", "NamedElement", "ViewElement", "ViewComponent",
    "DataSourceElement", "DataList", "Button", "Screen", "Module",
    "GUIModel", "ButtonType", "ButtonActionType",
}

_SKIP_IMPORT_PREFIXES = (
    "from enum import",
    "from typing import",
)


# ---------------------------------------------------------------------------
# AST helpers
# ---------------------------------------------------------------------------

def _node_src(source: str, node: ast.AST) -> str:
    try:
        return ast.get_source_segment(source, node) or ""
    except Exception:
        return ""


def _is_besser_class_def(node: ast.AST) -> bool:
    return isinstance(node, ast.ClassDef) and node.name in _BESSER_GUI_CLASSES


def _is_stub_class(node: ast.AST) -> bool:
    if not isinstance(node, ast.ClassDef):
        return False
    if len(node.body) != 1:
        return False
    stmt = node.body[0]
    if isinstance(stmt, ast.Pass):
        return True
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
        return True
    return False


def _import_text(node: ast.AST) -> str:
    if isinstance(node, ast.ImportFrom):
        names = ", ".join(
            (f"{a.name} as {a.asname}" if a.asname else a.name)
            for a in node.names
        )
        level = "." * (node.level or 0)
        return f"from {level}{node.module or ''} import {names}"
    if isinstance(node, ast.Import):
        names = ", ".join(
            (f"{a.name} as {a.asname}" if a.asname else a.name)
            for a in node.names
        )
        return f"import {names}"
    return ""


def _assigned_name(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Assign) and node.targets:
        t = node.targets[0]
        if isinstance(t, ast.Name):
            return t.id
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    return None


def _rhs_call(node: ast.AST) -> Optional[ast.Call]:
    if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
        return node.value
    if isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Call):
        return node.value
    return None


def _rhs_constructor(node: ast.AST) -> Optional[str]:
    call = _rhs_call(node)
    if call is None:
        return None
    func = call.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _is_scalar_assignment(node: ast.AST) -> bool:
    if not isinstance(node, ast.Assign):
        return False
    if not node.targets or not isinstance(node.targets[0], ast.Name):
        return False
    return isinstance(node.value, ast.Constant)


def _kw_value(call: ast.Call, kwname: str):
    for kw in call.keywords:
        if kw.arg == kwname:
            return kw.value
    return None


def _set_names_from_expr(expr) -> List[str]:
    """Extract Name ids from a Set or List literal."""
    names = []
    if expr is None:
        return names
    elts = []
    if isinstance(expr, ast.Set):
        elts = expr.elts
    elif isinstance(expr, ast.List):
        elts = expr.elts
    for elt in elts:
        if isinstance(elt, ast.Name):
            names.append(elt.id)
    return names


def _rewrite_screen_empty_view_elements(seg: str) -> str:
    """Return a copy of the Screen(...) assignment with view_elements={}."""
    # Replace the view_elements keyword argument value with {}
    # We do this via regex on the source segment for safety.
    result = re.sub(
        r'(view_elements\s*=\s*)\{[^}]*\}',
        r'\1{}',
        seg,
        count=1,
    )
    # Also handle list form
    result = re.sub(
        r'(view_elements\s*=\s*)\[[^\]]*\]',
        r'\1{}',
        result,
        count=1,
    )
    return result


# ---------------------------------------------------------------------------
# Core rewriter
# ---------------------------------------------------------------------------

def fix_generated_gui_model(py_file: str) -> None:
    try:
        with open(py_file, "r", encoding="utf-8") as fh:
            src = fh.read()
    except Exception:
        return

    try:
        tree = ast.parse(src)
    except SyntaxError:
        return

    nodes = list(tree.body)

    # ------------------------------------------------------------------
    # Pass 1: categorise all top-level nodes
    # ------------------------------------------------------------------
    extra_imports: List[str] = []
    seen_imports: Set[str] = set()

    # ------------------------------------------------------------------
    # Pre-scan: find home screen variable names (is_main_page=True)
    # so we can classify back-buttons correctly in the main pass.
    # ------------------------------------------------------------------
    home_screen_varnames: Set[str] = set()
    for node in nodes:
        ctor = _rhs_constructor(node)
        if ctor == "Screen":
            call = _rhs_call(node)
            if call:
                mp = _kw_value(call, "is_main_page")
                if mp and isinstance(mp, ast.Constant) and mp.value is True:
                    name = _assigned_name(node)
                    if name:
                        home_screen_varnames.add(name)

    # categorised assignment buckets
    forward_nav_buttons: List[Tuple[str, str]] = []  # (name, seg) – targetScreen is a list screen
    back_buttons: List[Tuple[str, str]] = []          # (name, seg) – targetScreen is the home screen
    add_buttons: List[Tuple[str, str]] = []           # (name, seg) – no targetScreen
    home_screens: List[Tuple[str, str, str]] = []     # (name, seg, original_seg) is_main_page=True
    list_screens: List[Tuple[str, str, List[str]]] = []  # (name, empty_seg, [view_elem_names])
    datasources: List[Tuple[str, str]] = []
    datalists: List[Tuple[str, str]] = []
    view_components: List[Tuple[str, str]] = []
    modules: List[Tuple[str, str]] = []
    guimodels: List[Tuple[str, str]] = []
    scalar_candidates: List[Tuple[str, str]] = []  # filtered later

    for node in nodes:
        seg = _node_src(src, node)
        if not seg.strip():
            continue

        if _is_besser_class_def(node) or _is_stub_class(node):
            continue

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            txt = _import_text(node)
            lower = txt.lower()
            # Drop imports superseded by our required set
            if any(lower.startswith(p.lower()) for p in _SKIP_IMPORT_PREFIXES):
                continue
            if txt in _REQUIRED_IMPORTS:
                continue
            # Drop buml/model relative imports – our required imports cover them
            if re.match(r'from\s+buml\b', txt, re.I) or re.match(r'import\s+buml\b', txt, re.I):
                continue
            if txt not in seen_imports:
                seen_imports.add(txt)
                extra_imports.append(txt)
            continue

        ctor = _rhs_constructor(node)

        if ctor == "Screen":
            name = _assigned_name(node)
            if not name:
                continue
            call = _rhs_call(node)
            is_main = False
            view_elem_names: List[str] = []
            if call:
                mp = _kw_value(call, "is_main_page")
                if mp and isinstance(mp, ast.Constant) and mp.value is True:
                    is_main = True
                ve = _kw_value(call, "view_elements")
                view_elem_names = _set_names_from_expr(ve)

            if is_main:
                home_screens.append((name, seg, seg))
            else:
                empty_seg = _rewrite_screen_empty_view_elements(seg)
                list_screens.append((name, empty_seg, view_elem_names))
            continue

        if ctor == "Button":
            name = _assigned_name(node)
            if not name:
                continue
            call = _rhs_call(node)
            target_screen_name = None
            if call:
                for kw in call.keywords:
                    if kw.arg == "targetScreen" and isinstance(kw.value, ast.Name):
                        target_screen_name = kw.value.id
                        break
            if target_screen_name is None:
                add_buttons.append((name, seg))
            elif target_screen_name in home_screen_varnames:
                back_buttons.append((name, seg))
            else:
                forward_nav_buttons.append((name, seg))
            continue

        if ctor in ("DataSourceElement", "DataSource"):
            name = _assigned_name(node) or f"__anon_{id(node)}"
            datasources.append((name, seg))
            continue

        if ctor == "DataList":
            name = _assigned_name(node) or f"__anon_{id(node)}"
            datalists.append((name, seg))
            continue

        if ctor in ("ViewComponent", "InputField", "Label", "TextField"):
            name = _assigned_name(node) or f"__anon_{id(node)}"
            view_components.append((name, seg))
            continue

        if ctor == "Module":
            name = _assigned_name(node) or f"__anon_{id(node)}"
            modules.append((name, seg))
            continue

        if ctor == "GUIModel":
            name = _assigned_name(node) or f"__anon_{id(node)}"
            guimodels.append((name, seg))
            continue

        # Unknown GUI constructor – keep it
        if ctor in _GUI_CONSTRUCTORS:
            name = _assigned_name(node) or f"__anon_{id(node)}"
            view_components.append((name, seg))
            continue

        # Scalar candidate (e.g. Library_name = "name")
        if _is_scalar_assignment(node):
            name = _assigned_name(node)
            if name:
                scalar_candidates.append((name, seg))
            continue

        # Everything else (with-blocks, for-loops, print(), attribute
        # assignments, dict/list literals, junk code) is dropped silently.

    # ------------------------------------------------------------------
    # Filter scalar candidates: only keep those referenced by kept nodes
    # ------------------------------------------------------------------
    kept_segs = (
        [seg for _, seg in forward_nav_buttons]
        + [seg for _, seg in back_buttons]
        + [seg for _, seg in add_buttons]
        + [seg for _, seg, _ in list_screens]
        + [seg for _, seg, _ in home_screens]
        + [seg for _, seg in datasources]
        + [seg for _, seg in datalists]
        + [seg for _, seg in view_components]
        + [seg for _, seg in modules]
        + [seg for _, seg in guimodels]
    )
    all_kept_src = "\n".join(kept_segs)
    scalar_kept = [(n, s) for n, s in scalar_candidates if n in all_kept_src]

    # ------------------------------------------------------------------
    # Build view_elements patch lines
    # (only for list screens that originally had non-empty view_elements)
    # ------------------------------------------------------------------
    patch_lines: List[str] = []
    for screen_name, _, view_elem_names in list_screens:
        if view_elem_names:
            elems = ", ".join(view_elem_names)
            patch_lines.append(f"{screen_name}.view_elements = {{{elems}}}")

    # ------------------------------------------------------------------
    # Assemble final source
    # ------------------------------------------------------------------
    parts: List[str] = []

    # 1. Imports
    parts.extend(_REQUIRED_IMPORTS)
    parts.extend(extra_imports)

    # 2. List screens with empty view_elements
    for _, empty_seg, _ in list_screens:
        parts.append(empty_seg)

    # 3. Forward nav buttons (targetScreen = list screen, now defined)
    for _, seg in forward_nav_buttons:
        parts.append(seg)

    # 4. Home screen (is_main_page=True, references forward nav buttons)
    for _, seg, _ in home_screens:
        parts.append(seg)

    # 5. Back buttons (targetScreen = home screen, now defined)
    for _, seg in back_buttons:
        parts.append(seg)

    # 6. Add buttons (no deps)
    for _, seg in add_buttons:
        parts.append(seg)

    # 7. DataSourceElements
    for _, seg in datasources:
        parts.append(seg)

    # 8. DataLists
    for _, seg in datalists:
        parts.append(seg)

    # 9. ViewComponent etc.
    for _, seg in view_components:
        parts.append(seg)

    # 10. Scalar field-name assignments
    for _, seg in scalar_kept:
        parts.append(seg)

    # 11. Patch list screen view_elements (back buttons now defined too)
    if patch_lines:
        parts.append("\n".join(patch_lines))

    # 12. Modules
    for _, seg in modules:
        parts.append(seg)

    # 13. GUIModel
    for _, seg in guimodels:
        parts.append(seg)

    new_src = "\n\n".join(p for p in parts if p.strip()) + "\n"

    if new_src != src:
        try:
            with open(py_file, "w", encoding="utf-8") as fh:
                fh.write(new_src)
            print(
                f"  [fix_gui_model_v2] Rewrote '{py_file}': "
                "two-phase Screen creation, stripped junk, sorted definitions."
            )
        except Exception:
            pass

