"""Render supported BUML GUI components as classic Retool Toolscript."""
import html
import json
import re

from besser.BUML.metamodel.gui.graphical_ui import (
    Button, DataList, Form, Image, InputField, Screen, Text, ViewContainer,
)
from besser.BUML.metamodel.gui.dashboard import BarChart, Chart, LineChart, PieChart, MetricCard
from besser.BUML.metamodel.gui.events_actions import Transition

from ._schema import snake_name, sql_identifier, values


def identifier(value):
    result = re.sub(r'[^A-Za-z0-9_$]', '_', value) or 'widget'
    return '_' + result if result[0].isdigit() else result


def attr(value):
    return html.escape(str(value), quote=True).replace('\n', '&#10;').replace('\r', '&#13;')


def tag(name, attrs, children=None):
    props = ' '.join(f'{key}={value}' for key, value in attrs.items() if value is not None)
    if children is None:
        return f'<{name} {props} />'
    return f'<{name} {props}>\n{children}\n</{name}>'


def quoted(value):
    return '"' + attr(value) + '"'


def literal(value):
    return '{' + json.dumps(value, ensure_ascii=False) + '}'


_INPUT_TAGS = {
    'Text': 'TextInput', 'Search': 'TextInput', 'Email': 'TextInput', 'URL': 'TextInput',
    'Tel': 'TextInput', 'Password': 'Password', 'TextArea': 'TextArea', 'RichText': 'RichText',
    'Number': 'NumberInput', 'Spinner': 'NumberInput', 'Slider': 'Slider', 'Checkbox': 'Checkbox',
    'Toggle': 'Switch', 'Dropdown': 'Select', 'MultiSelect': 'MultiSelect', 'RadioGroup': 'RadioGroup',
    'Date': 'Date', 'DateTime': 'DateTime', 'Time': 'Time', 'File': 'FileButton',
    'DateRange': 'DateRange', 'Tags': 'Tags',
}


class RsxWriter:
    def __init__(self, tables, resource_id):
        self.tables = tables
        self.resource_id = resource_id
        self.queries = {}
        self.query_ids = {}
        self.warnings = []
        self.used_ids = set()
        self.screen_ids = {}
        self.positions = {}
        self.rows = {}

    def reserve(self, name):
        base = identifier(name)
        result, suffix = base, 2
        while result in self.used_ids:
            result = f'{base}_{suffix}'
            suffix += 1
        self.used_ids.add(result)
        return result

    def warn(self, message):
        if message not in self.warnings:
            self.warnings.append(message)

    def table_for(self, cls_or_name):
        if cls_or_name is None:
            return None
        name = getattr(cls_or_name, 'name', cls_or_name)
        return next((t for t in self.tables
                     if (t.entity and t.entity.name.lower() == str(name).lower())
                     or t.name == snake_name(str(name))), None)

    def bound_table(self, component):
        binding = getattr(component, 'data_binding', None)
        return self.table_for(getattr(binding, 'domain_concept', None))

    def query(self, table):
        if table.name in self.query_ids:
            return self.query_ids[table.name]
        name = self.reserve('get_' + table.name)
        self.query_ids[table.name] = name
        self.queries[name] = f'SELECT * FROM {sql_identifier(table.name)};\n'
        return name

    def place(self, widget_id, screen_id, height=2, container=''):
        row_key = (screen_id, container)
        row = self.rows.get(row_key, 0)
        position = {'row': row, 'col': 0, 'height': height, 'width': 12}
        if container:
            position.update(container=container, rowGroup='body', subcontainer='')
        self.positions.setdefault(screen_id, {})[widget_id] = position
        self.rows[row_key] = row + height

    def events(self, component):
        events = []
        for event in sorted(values(getattr(component, 'events', None)), key=lambda e: e.name):
            event_name = {'OnClick': 'click', 'OnSubmit': 'submit', 'OnChange': 'change'}.get(event.event_type.name)
            for action in sorted(values(event.actions), key=lambda a: a.name):
                if isinstance(action, Transition) and action.target_screen in self.screen_ids and event_name:
                    target = action.target_screen
                    target_id = self.screen_ids[target]
                    props = {'event': quoted(event_name), 'type': quoted('widget'),
                             'pluginId': quoted(target_id), 'method': quoted('show')}
                    if target.is_main_page:
                        props.update(type=quoted('util'), pluginId=quoted(''), method=quoted('openPage'),
                                     params=literal({'map': {'pageName': target_id}}))
                    events.append(tag('Event', props))
                else:
                    self.warn(f'Action {action.name!r} on {component.name!r} needs manual wiring.')
        return '\n'.join(events)

    def render(self, component, screen_id, container=''):
        if isinstance(component, DataList):
            return self.data_list(component, screen_id, container)
        widget_id = self.reserve(component.name)
        height = 10 if isinstance(component, (Chart, ViewContainer)) else 2
        if isinstance(component, Form):
            height = max(6, 2 * (len(component.inputFields) + 1 + bool(component.title) + component.show_cancel))
        self.place(widget_id, screen_id, height=height, container=container)
        if isinstance(component, Text):
            return tag('Text', {'id': quoted(widget_id), 'value': quoted(component.content)})
        if isinstance(component, Image):
            return tag('Image', {'id': quoted(widget_id), 'src': quoted(component.source or '')})
        if isinstance(component, MetricCard):
            binding = component.data_binding
            table = self.table_for(getattr(binding, 'domain_concept', None))
            field = getattr(binding, 'data_field', None)
            value = ''
            if table and field:
                query = self.query(table)
                value = '{{ ' + query + '.data.' + snake_name(field.name) + '?.[0] }}'
            else:
                self.warn(f'Metric {component.name!r} needs a resolvable data field.')
            return tag('Statistic', {'id': quoted(widget_id), 'label': quoted(component.metric_title), 'value': quoted(value)})
        if isinstance(component, InputField):
            return self.input(component, widget_id)
        if isinstance(component, Button):
            events = self.events(component)
            if not events:
                self.warn(f'Button {component.name!r} has no executable action binding.')
            return tag('Button', {'id': quoted(widget_id), 'text': quoted(component.label)}, events or None)
        if isinstance(component, Form):
            title = ''
            if component.title:
                title_id = self.reserve(widget_id + '_title')
                self.place(title_id, screen_id, container=widget_id)
                title = tag('Text', {'id': quoted(title_id), 'value': quoted(component.title)})
            fields = '\n'.join(self.render(f, screen_id, widget_id)
                               for f in sorted(component.inputFields, key=lambda f: f.name))
            submit_id = self.reserve(widget_id + '_submit')
            self.place(submit_id, screen_id, container=widget_id)
            submit = tag('Button', {'id': quoted(submit_id), 'text': quoted(component.submit_label),
                                   'submit': '{true}', 'submitTargetId': quoted(widget_id)})
            events = self.events(component)
            if not events:
                self.warn(f'Form {component.name!r} has no executable submit action binding.')
            cancel = ''
            if component.show_cancel:
                cancel_id = self.reserve(widget_id + '_cancel')
                self.place(cancel_id, screen_id, container=widget_id)
                cancel = tag('Button', {'id': quoted(cancel_id), 'text': quoted(component.cancel_label)},
                             tag('Event', {'event': quoted('click'), 'method': quoted('reset'),
                                           'type': quoted('widget'), 'pluginId': quoted(widget_id)}))
            return tag('Form', {'id': quoted(widget_id), 'showBody': '{true}', 'showFooter': '{true}'},
                       title + '\n' + tag('Body', {}, fields) + '\n' + tag('Footer', {}, submit + '\n' + cancel) + '\n' + events)
        if isinstance(component, Chart):
            return self.chart(component, widget_id)
        if isinstance(component, ViewContainer):
            children = '\n'.join(self.render(child, screen_id, widget_id)
                                 for child in sorted(component.view_elements, key=lambda e: e.name))
            return tag('Container', {'id': quoted(widget_id), 'showBody': '{true}'},
                       tag('View', {'viewKey': quoted('View 1')}, children))
        self.warn(f'Unsupported component {type(component).__name__} {component.name!r} was omitted.')
        return ''

    def input(self, component, widget_id):
        kind = component.field_type.name
        input_tag = _INPUT_TAGS.get(kind)
        if input_tag is None:
            self.warn(f'Input type {kind} on {component.name!r} uses a TextInput fallback.')
            input_tag = 'TextInput'
        attrs = {'id': quoted(widget_id), 'formDataKey': quoted(component.name),
                 'label': quoted(component.label), 'placeholder': quoted(component.placeholder),
                 'required': literal(component.required), 'disabled': literal(component.disabled),
                 'readOnly': literal(component.readonly)}
        if component.default_value is not None:
            attrs['value'] = quoted(component.default_value)
        for prop, key in [('min_value', 'min'), ('max_value', 'max'), ('step', 'step')]:
            value = getattr(component, prop, None)
            if value is not None:
                attrs[key] = literal(value)
        options = '\n'.join(tag('Option', {'id': quoted(self.reserve(widget_id + '_option')),
                                          'value': quoted(option.value), 'label': quoted(option.label)})
                            for option in (component.options or []))
        if options:
            attrs['itemMode'] = quoted('static')
        return tag(input_tag, attrs, options or None)

    def data_list(self, component, screen_id, container):
        result = []
        sources = sorted(values(component.list_sources), key=lambda source: source.name)
        if not sources and self.bound_table(component):
            from besser.BUML.metamodel.gui.graphical_ui import DataSourceElement
            sources = [DataSourceElement(name=self.bound_table(component).name,
                                         dataSourceClass=self.bound_table(component).entity)]
        if not sources:
            self.warn(f'DataList {component.name!r} has no data source.')
        for index, source in enumerate(sources):
            base = component.name[:-5] if component.name.endswith('_List') else component.name
            widget_id = self.reserve(base if index == 0 else base + '_' + str(index + 1))
            self.place(widget_id, screen_id, 10, container)
            table = self.table_for(source.dataSourceClass or source.name) or self.bound_table(component)
            names = source.field_names or sorted(f.name for f in source.fields)
            if not names and table:
                names = [c.name for c in table.columns]
            names = list(dict.fromkeys(snake_name(name) for name in names))
            attrs = {'id': quoted(widget_id), 'showHeader': '{true}', 'showFooter': '{true}'}
            if table:
                attrs['data'] = quoted('{{ ' + self.query(table) + '.data }}')
                missing = set(names) - {c.name for c in table.columns}
                if missing:
                    self.warn(f'Table {component.name!r} has query-only columns {sorted(missing)}; provide their query logic.')
                if table.key.name in names:
                    attrs['primaryKeyColumnId'] = quoted(widget_id + '_' + table.key.name)
            else:
                attrs['data'] = '{[]}'
                self.warn(f'Table {component.name!r} has no domain class; data binding needs manual wiring.')
            columns = []
            for name in names:
                column = next((c for c in table.columns if c.name == name), None) if table else None
                columns.append(tag('Column', {'id': quoted(widget_id + '_' + name), 'key': quoted(name),
                                              'label': quoted(name.replace('_', ' ').title()),
                                              'format': quoted(column.format if column else 'string')}))
            result.append(tag('Table', attrs, '\n'.join(columns)))
        return '\n'.join(result)

    def chart(self, component, widget_id):
        kind = 'bar' if isinstance(component, BarChart) else 'pie' if isinstance(component, PieChart) else 'line' if isinstance(component, LineChart) else None
        if kind is None:
            self.warn(f'Unsupported chart type {type(component).__name__} on {component.name!r} uses an empty Chart.')
            return tag('Chart', {'id': quoted(widget_id)}, '')
        traces = []
        for series in component.series:
            binding = series.data_binding
            table = self.table_for(binding.domain_concept)
            if table is None or binding.label_field is None or binding.data_field is None:
                self.warn(f'Chart series {series.name!r} lacks a resolvable class or x/y fields.')
                continue
            query = self.query(table)
            x = '{{ ' + query + '.data.' + snake_name(binding.label_field.name) + ' }}'
            y = '{{ ' + query + '.data.' + snake_name(binding.data_field.name) + ' }}'
            traces.append(tag('Series', {'id': quoted(self.reserve(widget_id + '_series')), 'name': quoted(series.label or series.name),
                                         'type': quoted(kind), 'datasource': quoted('{{ ' + query + '.data }}'),
                                         'xData': quoted(x), 'yData': quoted(y)}))
        if not traces:
            self.warn(f'Chart {component.name!r} has no resolvable series; add its data binding in Retool.')
        if kind == 'pie':
            # Plotly's pie format uses labels/values instead of x/y.
            binding = component.series[0].data_binding if component.series else getattr(component, 'data_binding', None)
            table = self.table_for(getattr(binding, 'domain_concept', None))
            if table and binding.label_field and binding.data_field:
                query = self.query(table)
                trace = '{ type: "pie", labels: ' + query + '.data.' + snake_name(binding.label_field.name)
                trace += ', values: ' + query + '.data.' + snake_name(binding.data_field.name) + ' }'
                return tag('PlotlyChart', {'id': quoted(widget_id), 'chartType': quoted('pie'),
                                          'datasourceJS': quoted('{{ ' + query + '.data }}'),
                                          'xAxisDropdown': quoted(snake_name(binding.label_field.name)),
                                          'dataseries': '{{ label: "' + snake_name(binding.data_field.name) + '" }}',
                                          'data': quoted('{{ [' + trace + '] }}')})
        if not traces:
            traces.append(tag('Series', {'id': quoted(self.reserve(widget_id + '_series')), 'type': quoted(kind),
                                         'datasource': '{[]}', 'xData': '{[]}', 'yData': '{[]}'}))
        return tag('Chart', {'id': quoted(widget_id), 'title': quoted(component.title or '')}, '\n'.join(traces))

    def screen(self, screen, index):
        screen_id = self.screen_ids[screen]
        children = '\n'.join(self.render(element, screen_id)
                             for element in sorted(screen.view_elements,
                                                   key=lambda e: (getattr(e, 'display_order', None) or 0, e.name)))
        if screen.is_main_page:
            return tag('Screen', {'id': quoted(screen_id), 'title': quoted(screen.name), '_order': literal(index)},
                       tag('Frame', {'id': quoted('$main'), 'type': quoted('main'), 'padding': quoted('8px 12px')}, children))
        return tag('ModalFrame', {'id': quoted(screen_id), 'hidden': '{true}', 'showOverlay': '{true}'},
                   tag('Body', {}, children))
