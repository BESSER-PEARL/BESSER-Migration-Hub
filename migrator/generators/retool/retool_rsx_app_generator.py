"""Generate classic Retool Toolscript folders and ZIPs from BUML models."""
import json
from pathlib import Path
import uuid
import zipfile

from besser.BUML.metamodel.gui.graphical_ui import DataList, DataSourceElement, Screen

from ._schema import collect_tables, entities_info, values
from ._rsx_writer import RsxWriter, identifier, quoted, tag

_DEFAULT_RESOURCE_ID = '2a86a318-80a0-4803-95d8-409396e41af2'
# Kept for callers that used the previous private schema helper.
_collect_entities_info = entities_info


class RetoolRsxAppGenerator:
    """Export a GUIModel, or scaffold one table page per domain entity.

    domain_model may be omitted for GUI-only export. Queries are generated
    for resolvable classes; missing bindings and unsupported behavior are
    reported in warnings and generation_report.json. generate() returns the ZIP.
    """

    def __init__(self, domain_model=None, gui_model=None, app_name='retool_app',
                 output_dir=None, resource_id=_DEFAULT_RESOURCE_ID):
        if domain_model is None and gui_model is None:
            raise ValueError('A domain model or GUI model is required')
        if app_name in {'.', '..'} or Path(app_name).name != app_name or '/' in app_name or '\\' in app_name:
            raise ValueError('app_name must be a single folder name')
        self.domain_model = domain_model
        self.gui_model = gui_model
        self.app_name = app_name
        self.output_dir = Path(output_dir or 'retool_rsx_output')
        self.resource_id = resource_id or _DEFAULT_RESOURCE_ID
        self.warnings = []

    def generate(self):
        tables = collect_tables(self.domain_model)
        writer = RsxWriter(tables, self.resource_id)
        if self.gui_model is not None:
            screens = [screen for module in sorted(values(self.gui_model.modules), key=lambda m: m.name)
                       for screen in sorted(values(module.screens), key=lambda s: s.name)]
            if not screens:
                raise ValueError('The GUI model has no screens')
        else:
            screens = [Screen(name=table.entity.name if table.entity else table.name,
                              description='', is_main_page=True, view_elements={
                                  DataList(name=table.name + '_List', description='', list_sources={
                                      DataSourceElement(name=table.name, dataSourceClass=table.entity,
                                                        field_names=[c.name for c in table.columns])})})
                       for table in tables]
            if not screens:
                raise ValueError('The domain model has no classes')
        # Preserve named wrapper pages without selecting an empty wrapper as
        # the generated landing page when a populated main page is available.
        screens.sort(key=lambda s: (not s.is_main_page, not bool(s.view_elements), s.name))
        for screen in screens:
            writer.screen_ids[screen] = writer.reserve(screen.name)
        files = {}
        for index, screen in enumerate(screens):
            screen_id = writer.screen_ids[screen]
            files[f'src/{screen_id}.rsx'] = writer.screen(screen, index)
            files[f'.positions/.{screen_id}.positions.json'] = json.dumps(writer.positions.get(screen_id, {}), indent=2)
        queries = []
        for query_name, sql in sorted(writer.queries.items()):
            files[f'lib/{query_name}.sql'] = sql
            queries.append(tag('SqlQueryUnified', {
                'id': quoted(query_name), 'query': '{include("./lib/' + query_name + '.sql", "string")}',
                'resourceDisplayName': quoted('retool_db'), 'resourceName': quoted(self.resource_id),
            }))
        files['functions.rsx'] = tag('GlobalFunctions', {}, '\n'.join(queries)) + '\n'
        includes = [tag('Include', {'src': quoted('./functions.rsx')})]
        includes.extend(tag('Include', {'src': quoted('./src/' + writer.screen_ids[s] + '.rsx')}) for s in screens)
        main_ids = [writer.screen_ids[s] for s in screens if s.is_main_page]
        if not main_ids:
            host_id = writer.reserve(identifier(self.app_name) + '_Main')
            includes.append(tag('Screen', {'id': quoted(host_id)},
                                tag('Frame', {'id': quoted('$main'), 'type': quoted('main')}, '')))
            main_ids.append(host_id)
        files['main.rsx'] = tag('App', {}, '\n'.join(includes)) + '\n'
        files['metadata.json'] = json.dumps({
            'toolscriptVersion': '1.0.0', 'version': '43.0.9',
            'pageUuid': str(uuid.uuid5(uuid.NAMESPACE_URL, 'buml-retool:' + self.app_name)),
            'appTemplate': {'appMaxWidth': '100%', 'rootScreen': main_ids[0], 'version': '4.67.0',
                            'pageCodeFolders': {'object': {sid: {'array': []} for sid in main_ids}}},
        }, indent=2)
        self.warnings = writer.warnings
        files['generation_report.json'] = json.dumps({
            'app': self.app_name, 'screens': [writer.screen_ids[s] for s in screens],
            'resource_id': self.resource_id, 'warnings': self.warnings,
        }, indent=2, ensure_ascii=False)
        folder = self.output_dir / self.app_name
        # Overwrite generated files only. Do not delete an existing app folder.
        for relative, content in files.items():
            destination = folder / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding='utf-8', newline='\n')
        self.output_dir.mkdir(parents=True, exist_ok=True)
        archive = self.output_dir / f'{self.app_name}.zip'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zf:
            for relative in sorted(files):
                zf.writestr(f'{self.app_name}/{relative}', files[relative].encode('utf-8'))
        return str(archive)
