"""Render B-UML screens directly, without guessing their contents from names."""
from besser.BUML.metamodel.gui import Button, DataList, Form, InputField, Screen
import re


def sql_string(value):
    return "'" + str(value).replace("'", "''") + "'"


def call(procedure, **params):
    """Parameters contain SQL expressions, including explicitly quoted strings."""
    return f'wwv_flow_imp_page.{procedure}(\n ' + '\n,'.join(
        f'p_{key}=>{value}' for key, value in params.items()) + '\n);'


def assign_pages(generator):
    modules = generator.gui_model.modules
    modules = modules.values() if isinstance(modules, dict) else modules
    screens = [screen for module in sorted(modules, key=lambda module: module.name)
               for screen in sorted(module.screens, key=lambda screen: screen.name)]
    assignments = []
    page = 2
    for screen in screens:
        if not isinstance(screen, Screen):
            raise ValueError(f'GUI module contains a non-Screen: {screen.name}')
        while page in {101, 9999}:
            page += 1
        widgets = screen.view_elements
        kind = 'form' if any(isinstance(widget, Form) for widget in widgets) else (
            'list' if any(isinstance(widget, DataList) for widget in widgets) else 'other')
        assignments.append((screen, page, screen.name, kind))
        page += 1
    return assignments


def render_page(generator, screen, page, assignments):
    """Export actual forms, fields, reports and buttons, including unbound forms.

    Unbound forms use a SQL row from DUAL and have no invented persistence.
    Class-backed forms expose DML only for fields matched to real columns.
    """
    wid, uid = generator._wid, generator._uid
    lines = [f'prompt --application/pages/page_{page:05d}', generator._comp_begin(),
             call('create_page', id=page, name=sql_string(screen.name),
                  step_title=sql_string(screen.name), page_mode=sql_string(
                      'NORMAL' if screen.is_main_page else 'MODAL'),
                  autocomplete_on_off="'OFF'", page_template_options="'#DEFAULT#'",
                  protection_level="'C'")]
    page_numbers = {entry[0]: entry[1] for entry in assignments}
    used_items, used_buttons = set(), set()

    def identifier(name, used):
        base = re.sub(r'[^A-Za-z0-9_]', '_', name).upper() or 'ELEMENT'
        if base[0].isdigit():
            base = 'ELEMENT_' + base
        candidate, index = base, 2
        while candidate in used:
            candidate = f'{base}_{index}'
            index += 1
        used.add(candidate)
        return candidate

    def emit_item(field, region, sequence, column=None, source_type=None):
        item = identifier(f'P{page}_' + re.sub(r'^P\d+_', '', field.name, flags=re.I), used_items)
        types = {'Hidden': 'NATIVE_HIDDEN', 'Number': 'NATIVE_NUMBER_FIELD',
                 'TextArea': 'NATIVE_TEXTAREA', 'Password': 'NATIVE_PASSWORD',
                 'Date': 'NATIVE_DATE_PICKER_APEX', 'DateTime': 'NATIVE_DATE_PICKER_APEX',
                 'Checkbox': 'NATIVE_SINGLE_CHECKBOX'}
        field_type = field.field_type.name
        if field_type not in types and field_type != 'Text':
            generator.warnings.append(f"Input type {field_type} on '{field.name}' uses a text fallback.")
        params = dict(id=wid(uid()), name=sql_string(item), item_sequence=sequence,
                      item_plug_id=wid(region), prompt=sql_string(field.label or ''),
                      display_as=sql_string(types.get(field_type, 'NATIVE_TEXT_FIELD')),
                      field_template=generator._FIELD_TMPL, item_template_options="'#DEFAULT#'",
                      is_required='true' if field.required else 'false')
        if field.readonly or field.disabled:
            params['read_only_when_type'] = "'ALWAYS'"
        if field.placeholder:
            params['placeholder'] = sql_string(field.placeholder)
        if field.default_value is not None:
            params.update(item_default=sql_string(field.default_value), item_default_type="'STATIC'")
        if column is not None:
            params.update(source=sql_string(column), source_type=sql_string(source_type))
        lines.append(call('create_page_item', **params))
        return item

    def emit_button(name, label, region, sequence, action_type=None, widget=None):
        name = identifier(name, used_buttons)
        button_id = uid()
        params = dict(id=wid(button_id), button_sequence=sequence, button_plug_id=wid(region),
                      button_name=sql_string(name), button_image_alt=sql_string(label or ''),
                      button_template_id=generator._BTN_TMPL, button_template_options="'#DEFAULT#'",
                      button_position="'BOTTOM'", button_action="'SUBMIT'")
        transitions = [action for event in getattr(widget, 'events', []) for action in event.actions
                       if type(action).__name__ == 'Transition']
        if len(transitions) == 1 and transitions[0].target_screen in page_numbers:
            params.update(button_action="'REDIRECT_PAGE'", button_redirect_url=sql_string(
                f'f?p=&APP_ID.:{page_numbers[transitions[0].target_screen]}:&SESSION.::&DEBUG.::::'))
        elif transitions:
            generator.warnings.append(f"Button '{name}' has ambiguous or unresolved navigation.")
            params['button_action'] = "'DEFINED_BY_DA'"
        elif action_type in {'Add', 'Create', 'Save', 'Update', 'Delete'}:
            params['database_action'] = sql_string(
                {'Add': 'INSERT', 'Create': 'INSERT', 'Save': 'UPDATE', 'Update': 'UPDATE', 'Delete': 'DELETE'}[action_type])
        elif action_type is not None:
            params['button_action'] = "'DEFINED_BY_DA'"
            generator.warnings.append(f"Button '{name}' has no executable action binding.")
        lines.append(call('create_page_button', **params))
        return name

    body_region = uid()
    # Every screen remains a page, including screens with no entity-backed widget.
    lines.append(call('create_page_plug', id=wid(body_region), plug_name=sql_string(screen.name),
                      plug_display_sequence=10, region_template_options="'#DEFAULT#'"))
    for index, widget in enumerate(sorted(screen.view_elements, key=lambda widget: widget.name), start=1):
        sequence = (index + 1) * 10
        if isinstance(widget, Form):
            region = uid()
            fields = sorted(widget.inputFields, key=lambda field: field.name)
            binding = getattr(widget, 'data_binding', None)
            concept = getattr(binding, 'domain_concept', None)
            cls = generator._find_class_for_entity(concept.name) if concept else None
            params = dict(id=wid(region), plug_name=sql_string(widget.title or widget.name),
                          plug_display_sequence=sequence, region_template_options="'#DEFAULT#'",
                          plug_source_type="'NATIVE_FORM'")
            columns = {field: generator._col(re.sub(r'^P\d+_', '', field.name, flags=re.I)) for field in fields}
            if cls:
                params.update(query_type="'TABLE'", query_table=sql_string(generator._tbl(cls.name)),
                              include_rowid_column='false')
            else:
                aliases = []
                used_aliases = set()
                for field in fields:
                    column = identifier(columns[field], used_aliases)
                    columns[field] = column
                    sql_type = {'Number': 'number', 'Date': 'date', 'DateTime': 'timestamp'}.get(
                        field.field_type.name, 'varchar2(4000)')
                    aliases.append(f'cast(null as {sql_type}) as {column}')
                params.update(query_type="'SQL'", plug_source=sql_string(
                    'select ' + ', '.join(aliases or ['1 as FORM_ROW']) + ' from dual'))
                generator.warnings.append(f"Form '{widget.name}' has no persistence binding.")
            lines.append(call('create_page_plug', **params))
            real_columns = {generator._col(attribute.name) for attribute in cls.attributes} | {'ID'} if cls else set()
            pk_item = None
            for position, field in enumerate(fields, start=1):
                column = columns[field]
                matched = not cls or column in real_columns
                item = emit_item(field, region, position * 10,
                                 column if matched else None, 'DB_COLUMN' if cls else 'REGION_SOURCE_COLUMN')
                if cls and column == 'ID':
                    pk_item = item
                elif cls and not matched:
                    generator.warnings.append(f"Field '{field.name}' has no matching column in '{cls.name}'.")
            submit = emit_button(f'FORM_{index}_SUBMIT', widget.submit_label, region, 1000)
            if widget.show_cancel:
                emit_button(f'FORM_{index}_CANCEL', widget.cancel_label, region, 1010, 'Cancel')
            if not cls:
                lines.append(call('create_page_process', id=wid(uid()), process_sequence=sequence,
                                  process_point="'BEFORE_HEADER'", process_type="'NATIVE_FORM_INIT'",
                                  process_name=sql_string(f'Initialize {widget.name}'), form_region_id=wid(region)))
            if cls:
                if pk_item is None:
                    pk_item = identifier(f'P{page}_FORM_{index}_ID', used_items)
                    lines.append(call('create_page_item', id=wid(uid()), name=sql_string(pk_item),
                                      item_sequence=1, item_plug_id=wid(region), display_as="'NATIVE_HIDDEN'",
                                      source="'ID'", source_type="'DB_COLUMN'"))
                for process_type, point, operation in [('NATIVE_FORM_FETCH', 'AFTER_HEADER', 'Fetch'),
                                                        ('NATIVE_FORM_PROCESS', 'AFTER_SUBMIT', 'Process')]:
                    params = dict(id=wid(uid()), process_sequence=sequence, process_point=sql_string(point),
                                  process_type=sql_string(process_type), process_name=sql_string(f'{operation} {widget.name}'),
                                  form_region_id=wid(region),
                                  attributes="wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(" +
                                  "'primary_key_column','ID','primary_key_item'," + sql_string(pk_item) +
                                  ",'table_name'," + sql_string(generator._tbl(cls.name)) +
                                  ",'supported_operations','I:U:D')).to_clob")
                    if operation == 'Process':
                        params.update(process_when=sql_string(submit), process_when_type="'REQUEST_IN_CONDITION'")
                    lines.append(call('create_page_process', **params))
        elif isinstance(widget, DataList):
            for source in sorted(widget.list_sources, key=lambda source: source.name):
                cls = getattr(source, 'dataSourceClass', None)
                if cls is None and len(widget.list_sources) == 1:
                    cls = getattr(getattr(widget, 'data_binding', None), 'domain_concept', None)
                cls = generator._find_class_for_entity(cls.name) if cls else None
                region = uid()
                if not cls:
                    lines.append(call('create_page_plug', id=wid(region), plug_name=sql_string(widget.name),
                                      plug_display_sequence=sequence))
                    generator.warnings.append(f"Data source '{source.name}' has no class binding.")
                    continue
                lines.append(call('create_page_plug', id=wid(region), plug_name=sql_string(widget.name + '_' + source.name),
                                  plug_display_sequence=sequence, query_type="'TABLE'",
                                  query_table=sql_string(generator._tbl(cls.name)), include_rowid_column='false',
                                  plug_source_type="'NATIVE_IR'"))
                lines.append(call('create_worksheet', id=wid(uid()), name=sql_string(widget.name),
                                  internal_uid=uid(), base_pk1="'ID'", show_detail_link="'N'",
                                  owner='USER', pagination_type="'ROWS_X_TO_Y'", report_list_mode="'TABS'"))
                report_columns = ['ID'] + sorted({generator._col(attribute.name) for attribute in cls.attributes} - {'ID'})
                column_types = {generator._col(attribute.name): (
                    'NUMBER' if attribute.type.name in {'int', 'float', 'bool'} else
                    'DATE' if attribute.type.name in {'date', 'datetime', 'time'} else 'STRING')
                    for attribute in cls.attributes}
                column_types['ID'] = 'NUMBER'
                for position, column in enumerate(report_columns, start=1):
                    # APEX uses spreadsheet-style identifiers, including AA after Z.
                    number, letters = position, ''
                    while number:
                        number, remainder = divmod(number - 1, 26)
                        letters = chr(65 + remainder) + letters
                    lines.append(call('create_worksheet_column', id=wid(uid()), db_column_name=sql_string(column),
                                      display_order=position, column_identifier=sql_string(letters),
                                      column_label=sql_string(column), column_type=sql_string(column_types[column])))
                lines.append(call('create_worksheet_rpt', id=wid(uid()), application_user="'APXWS_DEFAULT'",
                                  report_seq=10, report_alias=sql_string(str(region)), status="'PUBLIC'",
                                  is_default="'Y'", report_columns=sql_string(':'.join(report_columns))))
        elif isinstance(widget, Button):
            emit_button(widget.name, widget.label, body_region, sequence, widget.actionType.name, widget)
        elif isinstance(widget, InputField):
            emit_item(widget, body_region, sequence)
        else:
            generator.warnings.append(f"Widget '{widget.name}' ({type(widget).__name__}) is not supported.")
    lines.append(generator._comp_end())
    return '\n'.join(lines)
