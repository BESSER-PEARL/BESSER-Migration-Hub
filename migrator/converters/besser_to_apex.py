import os
import re
import glob
from difflib import SequenceMatcher
from migrator.generators.sql import UIPagesSQLGenerator



def get_apex_pages_dir(apex_export_dir):
    """
    Dynamically find the pages directory inside the APEX export structure,
    which contains two nested folders starting with 'f', then 'application/pages'.
    """
    # Current APEX custom exports commonly contain:
    #   <export-name>/application/pages/*.sql
    # Support that layout as well as the older nested f*/f*/ layout.

    direct_pages = os.path.join(apex_export_dir, "application/pages/")
    if os.path.isdir(direct_pages):
        return direct_pages

    nested_pages = glob.glob(os.path.join(apex_export_dir, "*", "application", "pages"))
    if nested_pages:
        return nested_pages[0]

    # Look for the first folder starting with 'f'
    first_level_dirs = glob.glob(os.path.join(apex_export_dir, "f*"))
    if not first_level_dirs:
        raise FileNotFoundError("No folder starting with 'f' found in apex_export_dir")
    first_f = first_level_dirs[0]

    # Look for the second folder starting with 'f' inside the first one
    second_level_dirs = glob.glob(os.path.join(first_f, "f*"))
    if not second_level_dirs:
        raise FileNotFoundError("No folder starting with 'f' found inside the first 'f' folder")
    second_f = second_level_dirs[0]

    # Build the final pages path
    pages_dir = os.path.join(second_f, "application", "pages")
    if not os.path.exists(pages_dir):
        raise FileNotFoundError(f"Pages directory not found: {pages_dir}")

    return pages_dir


def extract_apex_info_from_file(sql_file_path):

    """
    Extract p_default_owner, p_default_application_id, p_owner, p_id, p_name,
    p_version_yyyy_mm_dd, and p_release from an APEX page SQL file.
    """
    info = {}
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

        # Extract p_default_owner
        m_owner = re.search(r"p_default_owner\s*=>\s*'([^']+)'", content)
        if m_owner:
            info['p_default_owner'] = m_owner.group(1)

        # Extract p_default_application_id
        m_app_id = re.search(r"p_default_application_id\s*=>\s*([0-9]+)", content)
        if m_app_id:
            info['p_default_application_id'] = m_app_id.group(1)

        # Extract p_owner
        m_owner2 = re.search(r"p_owner\s*=>\s*'([^']+)'", content)
        if m_owner2:
            info['p_owner'] = m_owner2.group(1)

        # Extract p_id and p_name from create_page
        m_page = re.search(r"wwv_flow_imp_page\.create_page\(\s*p_id\s*=>\s*([0-9]+).*?p_name\s*=>\s*'([^']+)'", content, re.DOTALL)
        if m_page:
            info['p_id'] = int(m_page.group(1))
            info['p_name'] = m_page.group(2)

        # Extract APEX version fields from wwv_flow_imp.import_begin header
        m_version = re.search(r"p_version_yyyy_mm_dd\s*=>\s*'([^']+)'", content)
        if m_version:
            info['p_version_yyyy_mm_dd'] = m_version.group(1)

        m_release = re.search(r"p_release\s*=>\s*'([^']+)'", content)
        if m_release:
            info['p_release'] = m_release.group(1)

        # Infer page type from known APEX region/process signatures.
        if "NATIVE_FORM" in content:
            info['page_type'] = "form"
        elif "NATIVE_IR" in content or "NATIVE_IG" in content:
            info['page_type'] = "list"
        else:
            info['page_type'] = "other"

    return info


def _normalize_page_name(name: str) -> str:
    """Normalize names so screen/APEX comparison tolerates separators and case."""
    if not name:
        return ""
    normalized = name.strip().lower()
    normalized = re.sub(r"[_\-\s]+", "", normalized)
    # Strip common suffixes produced by both Mendix (_page) and mockup
    # generators (*screen, *listscreen, *list).
    normalized = re.sub(r"(form)?page$", "", normalized)
    normalized = re.sub(r"(list)?(screen)$", "", normalized)
    normalized = re.sub(r"list$", "", normalized)
    return normalized


def _screen_is_list_page(screen_name: str) -> bool:
    """
    Return True for list/report screens; False for form/add/edit screens.

    Handles three naming conventions:
      • Oracle APEX path: names end with ``_List``
      • Mendix path     : names end with ``_page`` (but not ``_form_page``)
      • Mockup path     : names end with ``Screen`` or ``ListScreen``
                          (but not ``FormScreen``, ``AddScreen``, ``EditScreen``)
    """
    name = screen_name.lower()
    _FORM_KEYWORDS = ("form", "add", "edit", "new", "create", "detail")

    # Oracle APEX convention (*_List but not *_Form)
    if name.endswith("_list"):
        return True

    # Mendix convention
    if name.endswith("_page"):
        return not any(kw in name for kw in ("_form_page", "_from_page"))

    # Mockup convention  (*Screen / *ListScreen)
    if name.endswith("screen"):
        return not any(kw in name for kw in _FORM_KEYWORDS)

    return False


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def _build_page_generator(library_model, gui_model, app_id, screen, screen_number,
                          workspace_name, user_name,
                          apex_version='2024.11.30', apex_release='24.2.6',
                          output_dir=None):
    return UIPagesSQLGenerator(
        model=library_model,
        gui_model=gui_model,
        app_id=app_id,
        screen=screen,
        screen_number=screen_number,
        workspace_name=workspace_name,
        user_name=user_name,
        apex_version=apex_version,
        apex_release=apex_release,
        output_file_name=f"{screen.name}_generated.sql",
        output_dir=output_dir,
    )

def generate_pages_for_gui_model(apex_export_dir, gui_model, library_model, workspace_name, user_name,
                                 output_dir=None):
    """Generate APEX page SQL for every list screen in the GUI model.

    The app_id and version metadata are read from the uploaded APEX export;
    page IDs are assigned sequentially starting above the highest existing page
    so the generated SQL can be imported into the app without ID conflicts.
    """
    pages_dir = get_apex_pages_dir(apex_export_dir)
    print(f"  APEX pages directory detected: {pages_dir}")

    # Read all parseable pages from the export
    apex_pages = []
    for file_name in os.listdir(pages_dir):
        if not file_name.lower().endswith('.sql'):
            continue
        sql_file_path = os.path.join(pages_dir, file_name)
        apex_info = extract_apex_info_from_file(sql_file_path)
        if apex_info.get('p_id') is not None:
            apex_pages.append(apex_info)

    if not apex_pages:
        raise RuntimeError("No APEX pages found in export")

    # Pull app_id from the first page that has one
    app_id = None
    for info in apex_pages:
        if info.get('p_default_application_id'):
            app_id = str(info['p_default_application_id'])
            break
    if app_id is None:
        raise RuntimeError("Could not determine app_id from APEX export")

    # Pull APEX version metadata; fall back to safe defaults
    apex_version = '2024.11.30'
    apex_release = '24.2.6'
    for info in apex_pages:
        if info.get('p_version_yyyy_mm_dd'):
            apex_version = info['p_version_yyyy_mm_dd']
        if info.get('p_release'):
            apex_release = info['p_release']
        if info.get('p_version_yyyy_mm_dd') and info.get('p_release'):
            break

    print(f"  APEX version detected: {apex_version}  release: {apex_release}")

    # Assign fresh page IDs above the highest existing one (steps of 2 so that
    # the template's screen_number+1 form-page slot stays free between list pages)
    max_existing_id = max((p['p_id'] for p in apex_pages), default=0)
    # Round up to the next even number >= max+10 so IDs look tidy
    next_id = max_existing_id + 10
    if next_id % 2 != 0:
        next_id += 1

    generated_screens = []
    for module in gui_model.modules.values():
        for screen in sorted(module.screens, key=lambda s: s.name):
            if not _screen_is_list_page(screen.name):
                continue
            gen = _build_page_generator(
                library_model=library_model,
                gui_model=gui_model,
                app_id=app_id,
                screen=screen,
                screen_number=next_id,
                workspace_name=workspace_name,
                user_name=user_name,
                apex_version=apex_version,
                apex_release=apex_release,
                output_dir=output_dir,
            )
            gen.generate()
            print(f"  Generated page {next_id}: {screen.name}")
            generated_screens.append(screen.name)
            next_id += 2

    if not generated_screens:
        print("Warning: no list screens found in GUI model to generate.")




