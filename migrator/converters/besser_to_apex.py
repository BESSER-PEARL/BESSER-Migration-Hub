import os
import re
import glob
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
    Extract p_default_owner, p_default_application_id, p_owner, p_id, and p_name from an APEX page SQL file.
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

    return info

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

    for file_name in os.listdir(pages_dir):
        if not file_name.lower().endswith('.sql'):
            continue

        sql_file_path = os.path.join(pages_dir, file_name)
        apex_info = extract_apex_info_from_file(sql_file_path)

        if not apex_info.get('p_name'):
            continue

        apex_page_name = apex_info['p_name']

        for module, remaining_screens in module_screens.items():

            for screen in remaining_screens[:]:

                if (
                    screen.name.startswith(apex_page_name)
                    and screen.name.endswith("_page")
                ):

                    sql_list_page_file = UIPagesSQLGenerator(
                        model=library_model,
                        gui_model=gui_model,
                        app_id=apex_info['p_default_application_id'],
                        screen=screen,
                        screen_number=apex_info['p_id'],
                        workspace_name=workspace_name,
                        user_name=user_name,
                        output_file_name=f"{screen.name}_generated.sql"
                    )
                    sql_list_page_file.generate()

                    # ✅ Remove screen after first successful match
                    remaining_screens.remove(screen)

                    # ✅ Stop searching for this APEX file
                    break




