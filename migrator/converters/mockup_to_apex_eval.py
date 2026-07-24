"""
Extended pipeline: UI page images -> B-UML structural + GUI models -> Oracle APEX application pages.

This script extends mendix_to_apex_eval.py for the case where no low-code
platform JSON export is available (e.g. Power Apps, or any app for which only
UI screenshots exist).  The user provides a folder of UI page screenshots;
the mockup_to_buml module uses GPT-4o to derive both the structural B-UML
model and the GUI B-UML model from those images.  The two models are then
passed to the same downstream generators used in the Mendix path:
  - OracleApexSQLGenerator       -> SQL table DDL script
  - generate_pages_for_gui_model -> Oracle APEX application page SQL files

Pipeline steps
--------------
1. Collect inputs interactively (UI page images folder, API key, APEX details).
2. mockup_to_buml  ->  output_folder/buml/model.py
                   ->  output_folder/gui_model/generated_gui_model.py
3. Dynamically load domain_model and gui_model from the generated files.
4. Emit a readable B-UML code snapshot via domain_model_to_code.
5. OracleApexSQLGenerator -> SQL table definitions.
6. generate_pages_for_gui_model -> APEX application pages.
"""

import sys
import os
import re
import importlib.util
from pathlib import Path

# ---------------------------------------------------------------------------
# Path bootstrap – allows running this script directly from converters/
# ---------------------------------------------------------------------------
_CONVERTERS_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT   = _CONVERTERS_DIR.parents[1]          # BESSER-Migration-Hub root
_BESSER_ROOT    = _PROJECT_ROOT.parent / "BESSER"      # BESSER library root

for _p in (str(_PROJECT_ROOT), str(_BESSER_ROOT)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
# ---------------------------------------------------------------------------

from besser.BUML.metamodel.gui.graphical_ui import GUIModel
from besser.BUML.metamodel.structural import DomainModel
from besser.BUML.notations.mockup_to_buml.mockup_to_buml import mockup_to_buml
from besser.utilities.buml_code_builder import domain_model_to_code
import besser.BUML.notations.mockup_to_buml.multiple_images as _mult_images
import besser.BUML.notations.structuralPlantUML as _ptu_mod

from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator
from migrator.converters.besser_to_apex import (
    generate_pages_for_gui_model,
    get_apex_pages_dir,
    extract_apex_info_from_file,
)
from migrator.converters.fix_gui_model import fix_generated_gui_model

# ---------------------------------------------------------------------------
# Monkey-patch plantuml_to_buml so invalid LLM-generated multiplicities are
# fixed before the ANTLR parser sees them.
# ---------------------------------------------------------------------------

def _sanitize_plantuml_file(path: str) -> None:
    """
    Fix common LLM mistakes in a generated PlantUML file:
      • Multiplicity labels containing plain English words, e.g.
          "many libraries"  ->  "*"
          "many"            ->  "*"
          "one"             ->  "1"
          "zero or more"    ->  "*"
          "one or more"     ->  "+"
          "zero or one"     ->  "0..1"
      • Leading blank line before @startuml (causes 'extraneous input' warning).
    """
    _MULT_RE = re.compile(
        r'"((?:zero\s+or\s+more|zero\s+or\s+one|one\s+or\s+more|many\s+\w+|many|one))"',
        re.IGNORECASE,
    )
    _MULT_MAP = {
        "zero or more": "*",
        "zero or one":  "0..1",
        "one or more":  "+",
        "many":         "*",
        "one":          "1",
    }

    def _replace_mult(m: re.Match) -> str:
        raw = m.group(1).strip().lower()
        # Check exact-phrase map first
        for phrase, replacement in _MULT_MAP.items():
            if raw == phrase:
                return f'"{replacement}"'
        # "many <word>" → "*"
        if raw.startswith("many"):
            return '"*"'
        return m.group(0)

    with open(path, "r", encoding="utf-8") as fh:
        source = fh.read()

    # Strip leading blank lines before @startuml
    patched = re.sub(r"^\s*\n(?=@startuml)", "", source)
    patched = _MULT_RE.sub(_replace_mult, patched)

    # Normalize association labels (after ':'), converting quoted phrases
    # like : "has authors" -> : has_authors so the PlantUML parser sees a
    # single ID token instead of free text which it cannot parse.
    def _label_to_id(m: re.Match) -> str:
        raw = m.group(1)
        # keep only alphanum and spaces, then replace spaces with underscores
        cleaned = re.sub(r"[^0-9a-zA-Z ]+", " ", raw).strip()
        ident = re.sub(r"\s+", "_", cleaned)
        if not ident:
            ident = "assoc"
        return f": {ident}"

    patched = re.sub(r':\s*"([^"]+)"', _label_to_id, patched)

    # (Do not strip surrounding quotes: the PlantUML parser expects multiplicities
    # to remain quoted, but we already normalize their contents above.)

    if patched != source:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(patched)
        print("  [sanitize-puml] Fixed invalid multiplicities in PlantUML file.")


_original_plantuml_to_buml = _ptu_mod.plantuml_to_buml


def _patched_plantuml_to_buml(plantUML_model_path, buml_file_path):
    _sanitize_plantuml_file(plantUML_model_path)
    return _original_plantuml_to_buml(plantUML_model_path, buml_file_path)


_mult_images.plantuml_to_buml = _patched_plantuml_to_buml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_apex_app_info(apex_export_dir: str) -> dict:
    """
    Scan the APEX export directory and return workspace_name and apex_user
    extracted from the first page SQL file that contains those fields.
    Reuses get_apex_pages_dir / extract_apex_info_from_file from besser_to_apex.
    """
    pages_dir = get_apex_pages_dir(apex_export_dir)
    for file_name in sorted(os.listdir(pages_dir)):
        if not file_name.lower().endswith('.sql'):
            continue
        info = extract_apex_info_from_file(os.path.join(pages_dir, file_name))
        workspace_name = info.get('p_default_owner') or info.get('p_owner')
        apex_user      = info.get('p_owner') or info.get('p_default_owner')
        if workspace_name and apex_user:
            return {'workspace_name': workspace_name, 'apex_user': apex_user}
    raise RuntimeError(
        f"Could not extract workspace_name / apex_user from APEX export at '{apex_export_dir}'. "
        "Ensure the export contains page SQL files with p_default_owner / p_owner fields."
    )


def _ask(label: str, default: str = "") -> str:
    """Prompt the user for a value; return default if the user presses Enter."""
    if default:
        raw = input(f"  {label} [{default}]: ").strip()
        return raw if raw else default
    raw = input(f"  {label}: ").strip()
    return raw


def _sanitize_generated_py(py_file: str) -> None:
    """
    Rewrite a generated B-UML Python file in-place so that it can be loaded
    without errors regardless of whether the LLM used keyword or positional
    arguments for names.

    Patches applied
    ---------------
    1. name='...' / name="..." keyword arguments: spaces → underscores.
    2. First positional string argument of known BESSER constructors that
       contain spaces (Button, Screen, Module, GUIModel, DataList, etc.):
       spaces → underscores.  This covers generated files that call e.g.
       Button("Library Add Button", ...) instead of Button(name=...).
    """
    # --- pass 1: keyword  name='...' -----------------------------------------
    _KW_RE = re.compile(
        r"""((?:^|[,(\s])name\s*=\s*)(['"])(.*?)\2""",
        re.MULTILINE,
    )

    def _fix_kw(m: re.Match) -> str:
        prefix, quote, value = m.group(1), m.group(2), m.group(3)
        fixed = value.replace(" ", "_")
        if fixed != value:
            print(f"  [sanitize] name= '{value}' -> '{fixed}'")
        return f"{prefix}{quote}{fixed}{quote}"

    # --- pass 2: first positional string of known constructors ---------------
    # Matches:  ConstructorName("value with spaces", ...
    #       or  ConstructorName('value with spaces', ...
    _CONSTRUCTORS = (
        "Button", "Screen", "Module", "GUIModel",
        "DataList", "DataSourceElement",
        "InputField", "Label", "TextField",
    )
    _POS_RE = re.compile(
        r"""(?<!\w)(?:"""
        + "|".join(re.escape(c) for c in _CONSTRUCTORS)
        + r""")\s*\(\s*(['"])([^'"]*\s+[^'"]*)\1""",
    )

    def _fix_pos(m: re.Match) -> str:
        quote, value = m.group(1), m.group(2)
        fixed = value.replace(" ", "_")
        full = m.group(0)
        if fixed != value:
            print(f"  [sanitize] positional name '{value}' -> '{fixed}'")
            return full[: m.start(2) - m.start(0)] + fixed + quote
        return full

    with open(py_file, "r", encoding="utf-8") as fh:
        source = fh.read()

    patched = _KW_RE.sub(_fix_kw, source)
    patched = _POS_RE.sub(_fix_pos, patched)

    # --- pass 3: remove DjangoGenerator imports and generation blocks ------
    # Remove import lines that reference DjangoGenerator (e.g. "from ... import DjangoGenerator")
    patched = re.sub(r"(?m)^\s*from\s+.*\bDjangoGenerator\b.*\n", "", patched)
    patched = re.sub(r"(?m)^\s*import\s+.*\bDjangoGenerator\b.*\n", "", patched)

    # Remove explicit Django generation blocks like:
    #   # Django Generation
    #   django = DjangoGenerator(...)
    #   django.generate()
    patched = re.sub(
        r"(?ms)^\s*#\s*Django\s*Generation.*?django\.generate\(\)\s*",
        "",
        patched,
    )

    # Fallback: remove any standalone sequence that creates a DjangoGenerator
    patched = re.sub(
        r"(?ms)^\s*[^\n]*django\s*=\s*DjangoGenerator\([^\n]*\).*?django\.generate\(\)\s*",
        "",
        patched,
    )

    # --- pass 4: map invalid enum members to known values -----------------
    # Common LLM-generated enum members that don't exist in our enums
    _ENUM_REPLACEMENTS = {
        # ButtonType: FlatButton -> TextButton
        r"ButtonType\.FlatButton": "ButtonType.TextButton",
        # possible shorthand names -> full enum members
        r"ButtonType\.Flat": "ButtonType.TextButton",
        r"ButtonType\.FAB": "ButtonType.FloatingActionButton",
        r"ButtonType\.Floating_Action_Button": "ButtonType.FloatingActionButton",
    }
    for pat, repl in _ENUM_REPLACEMENTS.items():
        patched = re.sub(pat, repl, patched)

    if patched != source:
        with open(py_file, "w", encoding="utf-8") as fh:
            fh.write(patched)


def _reorder_generated_py(py_file: str) -> None:
    """
    Read a generated Python file and attempt to reorder top-level statements
    so that definitions (assignments to names) appear before uses. This is a
    conservative, best-effort pass that preserves the file if parsing fails or
    a safe topological order cannot be determined.
    """
    try:
        import ast
        from collections import deque
    except Exception:
        return

    try:
        with open(py_file, "r", encoding="utf-8") as fh:
            source = fh.read()
    except Exception:
        return

    try:
        tree = ast.parse(source)
    except Exception:
        return

    nodes = list(tree.body)
    node_sources = []
    for node in nodes:
        try:
            seg = ast.get_source_segment(source, node) or ""
        except Exception:
            seg = ""
        node_sources.append((node, seg))

    # map name -> defining node index
    def_names = {}
    for i, (node, src) in enumerate(node_sources):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    def_names[target.id] = i
                elif isinstance(target, ast.Tuple):
                    for elt in target.elts:
                        if isinstance(elt, ast.Name):
                            def_names[elt.id] = i
        elif isinstance(node, ast.AnnAssign):
            target = node.target
            if isinstance(target, ast.Name):
                def_names[target.id] = i

    # collect dependencies: node i depends on node j if i reads a name defined in j
    class NV(ast.NodeVisitor):
        def __init__(self):
            self.names = set()

        def visit_Name(self, n):
            if isinstance(n.ctx, ast.Load):
                self.names.add(n.id)

    deps = {i: set() for i in range(len(nodes))}
    for i, (node, src) in enumerate(node_sources):
        nv = NV()
        nv.visit(node)
        for name in nv.names:
            if name in def_names and def_names[name] != i:
                deps[i].add(def_names[name])

    indeg = {i: 0 for i in deps}
    for i in deps:
        for j in deps[i]:
            indeg[j] += 1

    q = deque([i for i, d in indeg.items() if d == 0])
    order = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in list(deps.keys()):
            if n in deps[m]:
                deps[m].remove(n)
                indeg[m] -= 1
                if indeg[m] == 0:
                    q.append(m)

    if len(order) != len(nodes):
        # couldn't find an acyclic order — bail out
        return

    parts = [node_sources[i][1] for i in order if node_sources[i][1].strip()]
    new_source = "\n\n".join(parts) + ("\n" if parts else "")

    if new_source != source:
        try:
            with open(py_file, "w", encoding="utf-8") as fh:
                fh.write(new_source)
            print(f"  [reorder] Reordered top-level statements in '{py_file}'.")
        except Exception:
            pass


class _ModuleAdapter:
    """
    Thin adapter that makes a duck-typed 'module' object look like the
    BESSER GUIModel module interface expected by generate_pages_for_gui_model:
      - module.screens  →  iterable of screen objects with a .name attribute
    """
    def __init__(self, raw_module):
        self._raw = raw_module
        raw_screens = getattr(raw_module, "screens", set())
        self.screens = list(raw_screens) if not isinstance(raw_screens, list) else raw_screens

    def __getattr__(self, item):
        return getattr(self._raw, item)


def _normalize_gui_model(obj):
    """
    Return an object that satisfies the interface expected by
    generate_pages_for_gui_model:
      gui_model.modules  →  dict  {name: module_obj}
    where each module has a .screens iterable.

    Handles two common shapes produced by mockup_to_buml:
      • BESSER GUIModel  – modules is already a dict
      • LLM custom class – modules may be a set or list of module objects
    """
    raw_modules = getattr(obj, "modules", {})

    if isinstance(raw_modules, dict):
        # Already the expected shape; wrap each module for safety
        normalized = {k: _ModuleAdapter(v) for k, v in raw_modules.items()}
    else:
        # set / list of module objects
        normalized = {}
        for m in raw_modules:
            key = getattr(m, "name", str(id(m)))
            normalized[key] = _ModuleAdapter(m)

    # Attach the normalised modules dict back onto a thin wrapper
    class _GUIModelAdapter:
        def __init__(self, inner, modules_dict):
            self._inner = inner
            self.modules = modules_dict
        def __getattr__(self, item):
            return getattr(self._inner, item)

    return _GUIModelAdapter(obj, normalized)


def _load_module_attribute(py_file: str, attr: str):
    """
    Dynamically execute a generated B-UML Python file and return the named
    module-level attribute.

    - mockup_to_buml writes <output_folder>/buml/model.py
      which exposes ``domain_model`` (a DomainModel instance).
    - mockup_to_buml writes <output_folder>/gui_model/generated_gui_model.py
      which exposes ``gui_model`` (a GUIModel instance).

    importlib executes each file in an isolated module namespace.  A fallback
    type-scan is performed when the expected variable name is absent, to
    tolerate minor naming variations in LLM-generated code.
    """
    # Patch spaces out of name='...' values before the module is executed.
    _sanitize_generated_py(py_file)

    module_name = f"_buml_gen_{attr}"
    spec   = importlib.util.spec_from_file_location(module_name, py_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    # Add the parent of the generated file's directory to sys.path so that
    # relative imports like "from buml.model import *" inside generated files
    # can resolve the sibling buml/ package in the same output folder.
    output_dir = str(Path(py_file).parent.parent)
    _path_added = output_dir not in sys.path
    if _path_added:
        sys.path.insert(0, output_dir)
    try:
        spec.loader.exec_module(module)
    finally:
        if _path_added and output_dir in sys.path:
            sys.path.remove(output_dir)

    # Direct attribute lookup (expected common case)
    if hasattr(module, attr):
        obj = getattr(module, attr)
        if attr == "gui_model":
            return _normalize_gui_model(obj)
        return obj

    # Fallback 1: scan namespace for an instance of BESSER's expected type
    type_map = {
        "domain_model": DomainModel,
        "gui_model":    GUIModel,
    }
    expected_type = type_map.get(attr)
    if expected_type is not None:
        for _name, value in vars(module).items():
            if isinstance(value, expected_type):
                print(
                    f"  [info] '{attr}' not found by name in '{py_file}'; "
                    f"using '{_name}' ({type(value).__name__})."
                )
                if attr == "gui_model":
                    return _normalize_gui_model(value)
                return value

    # Fallback 2 (gui_model only): duck-type – find any module-level object
    # that has a 'modules' attribute.  The LLM sometimes generates its own
    # local GUIModel class that shadows the BESSER import.
    if attr == "gui_model":
        candidates = [
            (n, v) for n, v in vars(module).items()
            if not n.startswith("_")
            and not isinstance(v, type)
            and not callable(v)
            and hasattr(v, "modules")
        ]
        if candidates:
            _name, value = candidates[0]
            print(
                f"  [info] '{attr}' not found by name or BESSER type in '{py_file}'; "
                f"using '{_name}' via duck-typing (has .modules)."
            )
            return _normalize_gui_model(value)

    raise AttributeError(
        f"The generated file '{py_file}' does not expose a '{attr}' variable "
        "and no fallback instance of the expected type was found.  "
        "Check mockup_to_buml output."
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print()
    print("=" * 70)
    print("  UI Page Images  ->  B-UML Models  ->  Oracle APEX Application Pages")
    print("=" * 70)
    print()
    print("Provide the required inputs below.")
    print("(Press Enter to accept the value shown in [brackets].)\n")

    # --- Collect inputs from the user --------------------------------------
    api_key = _ask("OpenAI API key")

    images_folder = _ask(
        "Folder containing UI page mockup / screenshot images"
    )

    nav_image = _ask(
        "Navigation diagram image path  [optional – Enter to skip]",
        default=""
    ) or None

    pages_order = _ask(
        "Pages-order text file path     [optional – Enter to skip]",
        default=""
    ) or None

    additional_info = _ask(
        "Additional info file path      [optional – Enter to skip]",
        default=""
    ) or None

    default_output = str(_CONVERTERS_DIR / "output" / "mockup_buml")
    output_folder = _ask(
        "Output folder for B-UML artefacts",
        default=default_output
    )

    apex_export_dir = _ask(
        "Oracle APEX export directory   (folder containing the APEX page SQL files)"
    )
    # -----------------------------------------------------------------------

    # Auto-extract workspace name and APEX user from the export directory.
    print("\n  [info] Extracting APEX application info from export directory …")
    apex_app_info  = _extract_apex_app_info(apex_export_dir)
    workspace_name = apex_app_info['workspace_name']
    apex_user      = apex_app_info['apex_user']
    print(f"  [info] workspace_name : {workspace_name}")
    print(f"  [info] apex_user      : {apex_user}")

    # Step 1 – run mockup_to_buml to generate both structural and GUI models
    print(f"\n[1/5]  Running mockup_to_buml on '{images_folder}' …")
    mockup_to_buml(
        api_key=api_key,
        input_folder=images_folder,
        navigation_image_path=nav_image,
        pages_order_file_path=pages_order,
        additional_info_path=additional_info,
        output_folder=output_folder,
    )

    structural_model_file = os.path.join(output_folder, "buml", "model.py")
    gui_model_file        = os.path.join(output_folder, "gui_model", "generated_gui_model.py")

    for path in (structural_model_file, gui_model_file):
        if not os.path.isfile(path):
            raise FileNotFoundError(
                f"Expected B-UML model file at '{path}' "
                "but mockup_to_buml did not create it.  "
                "Check the output for errors."
            )

    # Attempt to reorder generated files so definitions precede uses (avoids
    # import-time NameError from LLM-generated forward references).
    try:
        _reorder_generated_py(structural_model_file)
    except Exception:
        pass
    try:
        _reorder_generated_py(gui_model_file)
    except Exception:
        pass
    try:
        fix_generated_gui_model(gui_model_file)
    except Exception:
        pass

    # Mirror key generated/fixed artifacts into a single folder inside
    # converters for easy inspection in VS Code explorer. The folder name is
    # derived from the output folder provided by the user so multiple runs
    # with different outputs don't clobber each other.
    try:
        import shutil
        # derive a short, safe folder name from the output_folder path
        _base = os.path.basename(os.path.normpath(output_folder)) or "mockup_buml"
        _safe = re.sub(r"[^0-9A-Za-z._-]+", "_", _base)
        files_root = os.path.join(_CONVERTERS_DIR, f"mockup_to_apex_output_{_safe}")
        gui_out = os.path.join(files_root, "gui_model")
        buml_out = os.path.join(files_root, "buml")
        os.makedirs(gui_out, exist_ok=True)
        os.makedirs(buml_out, exist_ok=True)

        def _copy(src, dst_dir):
            try:
                if os.path.isfile(src):
                    dst = os.path.join(dst_dir, os.path.basename(src))
                    shutil.copy2(src, dst)
                    print(f"  [export] Copied {src} -> {dst}")
            except Exception:
                pass

        _copy(gui_model_file, gui_out)
        _copy(structural_model_file, buml_out)
    except Exception:
        pass

    # Step 2 – load domain model
    print(f"[2/5]  Loading domain model from '{structural_model_file}' …")
    domain_model: DomainModel = _load_module_attribute(structural_model_file, "domain_model")

    # Step 3 – load GUI model
    print(f"[3/5]  Loading GUI model from '{gui_model_file}' …")
    gui_model: GUIModel = _load_module_attribute(gui_model_file, "gui_model")

    # Step 4 – emit readable B-UML code snapshot
    buml_code_dir = os.path.join(output_folder, "buml_code")
    print(f"[4/5]  Writing B-UML code snapshot to '{buml_code_dir}' …")
    domain_model_to_code(model=domain_model, file_path=buml_code_dir)

    # Step 5 – generate Oracle APEX SQL DDL and application pages
    print(f"[5/5]  Generating Oracle APEX SQL table definitions …")
    sql_output_dir = os.path.join(output_folder, "sql")
    sql_generator = OracleApexSQLGenerator(
        domain_model,
        output_dir=sql_output_dir,
        output_filename="tables_oracle_apex.sql",
    )
    sql_generator.generate()

    print(f"        Generating Oracle APEX application pages …")
    generate_pages_for_gui_model(
        apex_export_dir,
        gui_model,
        domain_model,
        workspace_name,
        apex_user,
    )

    # Mirror SQL DDL and APEX page SQL files into converters output folder
    try:
        import shutil
        # reuse the same files_root derivation as above so all artifacts for
        # this output_folder end up in the same place.
        _base = os.path.basename(os.path.normpath(output_folder)) or "mockup_buml"
        _safe = re.sub(r"[^0-9A-Za-z._-]+", "_", _base)
        files_root = os.path.join(_CONVERTERS_DIR, f"mockup_to_apex_output_{_safe}")
        sql_out = os.path.join(files_root, "sql")
        apex_out = os.path.join(files_root, "apex_pages")
        os.makedirs(sql_out, exist_ok=True)
        os.makedirs(apex_out, exist_ok=True)

        def _copy_file(src, dst_dir):
            try:
                if os.path.isfile(src):
                    dst = os.path.join(dst_dir, os.path.basename(src))
                    shutil.copy2(src, dst)
                    print(f"  [export] Copied {src} -> {dst}")
            except Exception:
                pass

        # copy generated SQL DDL
        ddl = os.path.join(sql_output_dir, "tables_oracle_apex.sql")
        _copy_file(ddl, sql_out)

        # copy APEX page SQL files from the export (pages dir)
        try:
            pages_dir = get_apex_pages_dir(apex_export_dir)
        except Exception:
            pages_dir = apex_export_dir

        if os.path.isdir(pages_dir):
            for fn in sorted(os.listdir(pages_dir)):
                if fn.lower().endswith('.sql'):
                    _copy_file(os.path.join(pages_dir, fn), apex_out)
    except Exception:
        pass

    print()
    print("✅  Oracle APEX artefacts generated successfully!")
    print(f"📁  B-UML artefacts  : {os.path.abspath(output_folder)}")
    print(f"    SQL table DDL    : {os.path.abspath(sql_output_dir)}/tables_oracle_apex.sql")
    print(f"    APEX pages       : {os.path.abspath(apex_export_dir)}")


if __name__ == "__main__":
    main()

