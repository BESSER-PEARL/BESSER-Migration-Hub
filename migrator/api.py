"""Parse source applications with shared domain and GUI bindings."""
from pathlib import Path


def parse_source(source: str, data_path: str | Path, gui_path: str | Path | None = None,
                 module_name: str | None = None):
    """Return (domain_model, gui_model); omit gui_path for data-only extraction."""
    data_path = str(data_path)
    gui_path = str(gui_path) if gui_path is not None else None
    if source == 'mendix':
        from migrator.parsers.mendix.mendix import mendix_to_buml
        from migrator.parsers.mendix.mendix_gui import mendix_to_gui
        if not module_name:
            raise ValueError('Mendix extraction requires a module name.')
        domain = mendix_to_buml(data_path, module_name)
        gui = mendix_to_gui(gui_path, module_name, domain_model=domain) if gui_path else None
    elif source == 'oracle_apex':
        from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
        from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui, oracle_apex_gui_from_sql
        domain = oracle_apex_to_buml(data_path, module_name=module_name)
        gui_parser = oracle_apex_gui_from_sql if gui_path and Path(gui_path).is_file() else oracle_apex_to_gui
        gui = gui_parser(gui_path, module_name=module_name, domain_model=domain) if gui_path else None
    elif source == 'retool':
        from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
        from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui
        domain = retool_csv_to_buml(data_path, module_name=module_name, rsx_dir=gui_path)
        gui = retool_rsx_to_gui(gui_path, module_name=module_name, domain_model=domain) if gui_path else None
    else:
        raise ValueError(f'Unsupported deterministic source platform: {source}')
    if domain is None:
        raise ValueError('No domain model extracted. Check the export and module selection.')
    return domain, gui
