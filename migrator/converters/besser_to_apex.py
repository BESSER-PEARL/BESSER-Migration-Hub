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

    Handles two naming conventions:
      • Mendix path  : names end with ``_page`` (but not ``_form_page``)
      • Mockup path  : names end with ``Screen`` or ``ListScreen``
                       (but not ``FormScreen``, ``AddScreen``, ``EditScreen``)
    """
    name = screen_name.lower()
    _FORM_KEYWORDS = ("form", "add", "edit", "new", "create", "detail")

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
                          apex_version='2024.11.30', apex_release='24.2.6'):
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
        output_file_name=f"{screen.name}_generated.sql"
    )

def generate_pages_for_gui_model(apex_export_dir, gui_model, library_model, workspace_name, user_name):
    """
    Walk through pages folder in exported APEX app, match screens in GUI model,
    generate SQL ONCE per screen, then remove it from further matching.
    """


    pages_dir = get_apex_pages_dir(apex_export_dir)

    # Build mutable screen lists per module
    module_screens = {
        module: list(module.screens)
        #for module in gui_model.modules
        for module in gui_model.modules.values()

    }

    apex_pages = []
    for file_name in os.listdir(pages_dir):
        if not file_name.lower().endswith('.sql'):
            continue

        sql_file_path = os.path.join(pages_dir, file_name)
        apex_info = extract_apex_info_from_file(sql_file_path)
        if apex_info.get('p_name') and apex_info.get('p_id') is not None:
            apex_pages.append(apex_info)

    if not apex_pages:
        raise RuntimeError("No APEX pages found in export")

    list_apex_pages = [p for p in apex_pages if p.get('page_type') == 'list']
    if not list_apex_pages:
        raise RuntimeError("No APEX list pages found in export")

    app_id = str(list_apex_pages[0]['p_default_application_id'])

    # Extract APEX version from the first page that carries it; fall back to
    # the template defaults when the export does not include those fields.
    apex_version = '2024.11.30'
    apex_release = '24.2.6'
    for page_info in apex_pages:
        if page_info.get('p_version_yyyy_mm_dd'):
            apex_version = page_info['p_version_yyyy_mm_dd']
        if page_info.get('p_release'):
            apex_release = page_info['p_release']
        if page_info.get('p_version_yyyy_mm_dd') and page_info.get('p_release'):
            break

    print(f"  APEX version detected: {apex_version}  release: {apex_release}")

    generated_screens = set()
    matched_apex_ids = set()

    for apex_info in list_apex_pages:

        if not apex_info.get('p_name'):
            continue

        apex_page_name = _normalize_page_name(apex_info['p_name'])

        for module, remaining_screens in module_screens.items():

            for screen in remaining_screens[:]:
                if not _screen_is_list_page(screen.name):
                    continue

                screen_page_name = _normalize_page_name(screen.name)

                if (
                    screen_page_name == apex_page_name
                    or screen_page_name.startswith(apex_page_name)
                    or apex_page_name.startswith(screen_page_name)
                ):

                    sql_list_page_file = _build_page_generator(
                        library_model=library_model,
                        gui_model=gui_model,
                        app_id=app_id,
                        screen=screen,
                        screen_number=apex_info['p_id'],
                        workspace_name=workspace_name,
                        user_name=user_name,
                        apex_version=apex_version,
                        apex_release=apex_release,
                    )
                    sql_list_page_file.generate()
                    generated_screens.add(screen.name)
                    matched_apex_ids.add(apex_info['p_id'])

                    # ✅ Remove screen after first successful match
                    remaining_screens.remove(screen)

                    # ✅ Stop searching for this APEX file
                    break

    # Second pass: resolve minor naming differences (e.g., Operational vs Operations).
    unmatched_screens = []
    for module, remaining_screens in module_screens.items():
        for screen in remaining_screens:
            if _screen_is_list_page(screen.name):
                unmatched_screens.append(screen)

    remaining_apex_pages = [
        p for p in list_apex_pages
        if p.get('p_id') not in matched_apex_ids
    ]

    for screen in unmatched_screens:
        screen_page_name = _normalize_page_name(screen.name)
        best = None
        best_score = 0.0
        for apex_info in remaining_apex_pages:
            apex_page_name = _normalize_page_name(apex_info['p_name'])
            score = _similarity(screen_page_name, apex_page_name)
            if score > best_score:
                best_score = score
                best = apex_info

        if best and best_score >= 0.85:
            sql_list_page_file = _build_page_generator(
                library_model=library_model,
                gui_model=gui_model,
                app_id=app_id,
                screen=screen,
                screen_number=best['p_id'],
                workspace_name=workspace_name,
                user_name=user_name,
                apex_version=apex_version,
                apex_release=apex_release,
            )
            sql_list_page_file.generate()
            generated_screens.add(screen.name)
            matched_apex_ids.add(best['p_id'])
            remaining_apex_pages = [p for p in remaining_apex_pages if p['p_id'] != best['p_id']]

    # Keep the output list-page-only: do not synthesize new IDs for unmatched pages.
    unmatched_list_pages = []
    for module in module_screens.values():
        for screen in module:
            if _screen_is_list_page(screen.name) and screen.name not in generated_screens:
                unmatched_list_pages.append(screen.name)

    if unmatched_list_pages:
        print("Warning: unmatched list screens were skipped:", ", ".join(sorted(unmatched_list_pages)))




