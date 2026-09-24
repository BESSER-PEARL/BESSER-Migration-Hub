import json
import os
from typing import Optional

from besser.BUML.metamodel.structural import Class, DomainModel, Property

from besser.BUML.metamodel.gui.graphical_ui import (
    Button,
    ButtonActionType,
    ButtonType,
    DataList,
    DataSourceElement,
    Form,
    GUIModel,
    Image,
    InputField,
    InputFieldType,
    Module,
    Screen,
    Text,
    ViewContainer,
    ViewElement,
)
from besser.BUML.metamodel.gui.dashboard import ExpressionColumn, FieldColumn, LookupColumn, Table

from besser.BUML.metamodel.gui import (
    DataBinding, Styling, Color, Layout, LayoutType, Position, PositionType, JustificationType
)

def extract_main_pages(unit) -> set[str]:
    """Extracts main pages from a NavigationDocument unit."""
    main_pages = set()

    def recurse(node):
        if isinstance(node, dict):
            node_type = node.get("$Type")

            # Check direct homePage
            if node_type == "Navigation$NavigationProfile":
                main_page = node.get("homePage", {}).get("page", {}).split('.')[1]
                if main_page:
                    main_pages.add(main_page)

            # Recurse deeper
            for value in node.values():
                recurse(value)

        elif isinstance(node, list):
            for item in node:
                recurse(item)

    recurse(unit)
    return main_pages



def mendix_to_buml_button_type(mendix_button_type: str) -> ButtonType:
    """Converts Mendix button type to B-UML button type.

    ``Button`` requires a non-null ``buttonType``, so any unmapped/unknown
    Mendix action falls back to ``ButtonType.RaisedButton`` instead of ""
    (an empty string previously left generated code with a missing
    constructor argument).
    """
    type_mapping = {
        "Pages$PageClientAction": ButtonType.RaisedButton,
        "Pages$DeleteClientAction": ButtonType.OutlinedButton,
        "Pages$CreateObjectClientAction": ButtonType.FloatingActionButton,
        "Pages$NoClientAction": ButtonType.TextButton,
        "Pages$CancelChangesClientAction": ButtonType.TextButton,
        "Pages$MicroflowClientAction": ButtonType.RaisedButton,
        "Pages$SaveChangesClientAction": ButtonType.RaisedButton

    }
    return type_mapping.get(mendix_button_type, ButtonType.RaisedButton)


def mendix_to_buml_action_type(mendix_action_type: str) -> ButtonActionType:
    """Converts Mendix button type to B-UML action type for button.

    ``Button`` requires a non-null ``actionType``, so any unmapped/unknown
    Mendix action (e.g. ``NoClientAction``, ``MicroflowClientAction``) falls
    back to ``ButtonActionType.RunMethod`` instead of "" (an empty string
    previously left generated code with a missing constructor argument).
    """
    type_mapping = {
        "Pages$DeleteClientAction": ButtonActionType.Delete,
        "Pages$CancelChangesClientAction": ButtonActionType.Cancel,
        "Pages$PageClientAction": ButtonActionType.Navigate,
        "Pages$CreateObjectClientAction": ButtonActionType.Add,
        "Pages$SaveChangesClientAction": ButtonActionType.Save,
        "Pages$MicroflowClientAction": ButtonActionType.RunMethod,
        "Pages$CallNanoflowClientAction": ButtonActionType.RunMethod,
        "Pages$NoClientAction": ButtonActionType.RunMethod,
        "Pages$ClosePageClientAction": ButtonActionType.Back,
        "Pages$SignOutClientAction": ButtonActionType.Logout,
        "Pages$OpenLinkClientAction": ButtonActionType.Navigate,
    }
    return type_mapping.get(mendix_action_type, ButtonActionType.RunMethod)


# for styling for buttons
def map_button_style_to_color(style: str) -> Color:
    """Map Mendix 'buttonStyle' to a BUML Color."""
    style_map = {
        "Danger": Color(
            background_color="#EF4444",
            text_color="#FFFFFF",
            border_color="#DC2626"),     # Red
        "Primary": Color(
            background_color="#3B82F6",
            text_color="#FFFFFF",
            border_color="#2563EB"),    # Blue
        "Success": Color(
            background_color="#0C4B33",
            text_color="#FFFFFF",
            border_color="#0056b3"),    # Green
        "Secondary": Color(
            background_color="#6C757D",
            text_color="#FFFFFF",
            border_color="#5A6268"),  # Gray
        "Warning": Color(
            background_color="#FFC107",
            text_color="#000000",
            border_color="#FFA000"),     # Amber/Yellow
        "Info": Color(
            background_color="#17A2B8",
            text_color="#FFFFFF",
            border_color="#117A8B"),        # Cyan/Teal
        "Inverse": Color(
            background_color="#343A40",
            text_color="#FFFFFF",
            border_color="#1D2124"),     # Dark/Contrast
        "Default": Color(
            background_color="#E0E0E0",
            text_color="#000000",
            border_color="#B0B0B0")      # Neutral
    }

    # Fallback color if style not found
    style_color = Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0")

    return style_map.get(style, style_color)

def extract_css_classes(node: dict) -> list[str]:
    """Return CSS classes including Mendix buttonStyle."""
    appearance = node.get("appearance", {})
    raw_classes = appearance.get("class", "")
    button_style = node.get("buttonStyle", "")

    classes = []

    # classes from appearance
    if isinstance(raw_classes, str):
        classes.extend([cls for cls in raw_classes.split() if cls])

    # convert Mendix buttonStyle to CSS class
    if button_style:
        classes.append(f"btn-{button_style.lower()}")

    return classes


def extract_styling(node: dict) -> Styling:
    """Extract styling from a Mendix widget node.

    The only visual information we currently care about is the Mendix
    ``buttonStyle`` (present on action buttons) which is mapped to a
    ``Color``; other widget types simply fall back to the neutral default
    color plus a relative position.
    """
    button_style = node.get("buttonStyle", "")  # like 'Danger', 'Primary', etc.
    #size = css_class if css_class else ""

    color = map_button_style_to_color(button_style)
    position = Position(p_type=PositionType.RELATIVE)

    return Styling(size="", color=color, position=position)


def _translated_text(template_node, prefer_lang: str = "en_US") -> str:
    """Extract translated display text from a Mendix ``Pages$ClientTemplate``-shaped node.

    Mendix stores one ``Texts$Translation`` per language under
    ``template.translations``. We prefer ``prefer_lang`` (English by default)
    but fall back to the first non-empty translation in any other language
    rather than returning "" (a page authored only in ``nl_NL`` would
    otherwise produce blank labels/content everywhere).
    """
    if not isinstance(template_node, dict):
        return ""
    templates = template_node.get("template", [])
    if not isinstance(templates, list):
        templates = [templates]

    fallback_text = ""
    for template in templates:
        if not isinstance(template, dict) or template.get("$Type") != "Texts$Text":
            continue
        translations = template.get("translations", [])
        if isinstance(translations, dict):
            translations = [translations]
        for translation in translations:
            if not isinstance(translation, dict) or translation.get("$Type") != "Texts$Translation":
                continue
            text = translation.get("text", "")
            if not text:
                continue
            if translation.get("languageCode") == prefer_lang:
                return text
            if not fallback_text:
                fallback_text = text
    return fallback_text


def _resolve_attribute_name(attribute_ref) -> Optional[str]:
    """Return the bare attribute name from a ``DomainModels$AttributeRef`` node.

    Mendix stores the fully qualified path (``Module.Entity.Attribute``,
    or an association-hop attribute when ``entityRef`` is an
    ``IndirectEntityRef``); we keep only the final segment, matching the
    convention already used for list/gallery columns in this parser.
    """
    if not isinstance(attribute_ref, dict):
        return None
    attribute = attribute_ref.get("attribute", "")
    if not attribute or "." not in attribute:
        return None
    return attribute.split(".")[-1]


def _entity_qname_from_ref(entity_ref) -> Optional[str]:
    """Extract the qualified entity name (``"Module.Entity"``) from either
    shape of Mendix entity reference: a ``DomainModels$DirectEntityRef``
    (plain ``entity`` field) or a ``DomainModels$IndirectEntityRef`` (an
    association-hop ``steps`` list, whose *last* step's ``destinationEntity``
    is the entity actually reached, e.g. a Data Grid 2 shown via an
    association from the page's own context entity).
    """
    if isinstance(entity_ref, str):
        return entity_ref or None
    if not isinstance(entity_ref, dict):
        return None
    if entity_ref.get("$Type") == "DomainModels$IndirectEntityRef":
        steps = entity_ref.get("steps") or []
        if steps and isinstance(steps[-1], dict):
            return steps[-1].get("destinationEntity") or None
        return None
    return entity_ref.get("entity") or None


def _resolve_entity_class(domain_model: Optional[DomainModel], entity_ref) -> Optional[object]:
    """Resolve a ``DomainModels$...EntityRef``-shaped node (or a bare qualified
    name string) to the matching BUML ``Class`` in ``domain_model``.

    Returns ``None`` when no domain model was supplied (e.g. only the GUI model
    was requested, so no ``DomainModel`` exists to resolve against), the
    reference is missing/malformed, or the entity isn't part of the migrated
    module (e.g. a Mendix built-in like ``System.FileDocument``).
    """
    if domain_model is None or not entity_ref:
        return None
    qualified_name = _entity_qname_from_ref(entity_ref)
    if not qualified_name or "." not in qualified_name:
        return None
    entity_name = qualified_name.split(".")[-1]
    return domain_model.get_class_by_name(entity_name)


def _build_action_button(node: dict) -> Button:
    """Build a ``Button`` from a ``Pages$ActionButton`` node."""
    label = _translated_text(node.get("caption"))
    action = node.get("action", {}) or {}
    button_type_str = action.get("$Type", "")
    button_type = mendix_to_buml_button_type(button_type_str)
    action_type = mendix_to_buml_action_type(button_type_str)

    target_screen = None
    page_settings = action.get("pageSettings", {})
    if isinstance(page_settings, dict) and page_settings.get("page"):
        screen_name = page_settings.get("page", "").split(".")[1]
        target_screen = Screen(
            name=screen_name,
            description="",
            x_dpi="",
            y_dpi="",
            screen_size="Small",
            view_elements=set(),
        )

    if button_type == ButtonType.TextButton and label in {"Back", "Return", "←"}:
        action_type = ButtonActionType.Back

    button = Button(
        label=label or "Unnamed Button",
        buttonType=button_type,
        actionType=action_type,
        description="",
        name=node.get("name", ""),
        visibility="",
        targetScreen=target_screen,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    return button


# Mendix InputFieldType -> BUML InputFieldType for simple, directly-bound editable widgets.
_MENDIX_INPUT_WIDGET_TYPES = {
    "Pages$TextBox": InputFieldType.Text,
    "Pages$TextArea": InputFieldType.TextArea,
    "Pages$CheckBox": InputFieldType.Checkbox,
    "Pages$DatePicker": InputFieldType.Date,
}


def _build_input_field(node: dict, field_type: InputFieldType) -> InputField:
    """Build an ``InputField`` from a simple bound editable widget

    (``Pages$TextBox`` / ``Pages$TextArea`` / ``Pages$CheckBox`` / ``Pages$DatePicker``).
    All four share the same ``attributeRef`` / ``labelTemplate`` /
    ``placeholderTemplate`` / ``editable`` shape.
    """
    label = _translated_text(node.get("labelTemplate"))
    placeholder = _translated_text(node.get("placeholderTemplate"))
    attr_name = _resolve_attribute_name(node.get("attributeRef"))

    field = InputField(
        name=node.get("name", ""),
        description="",
        field_type=field_type,
        label=label,
        placeholder=placeholder,
        readonly=node.get("editable", "Always") != "Always",
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    if attr_name:
        field.custom_attributes["data-mendix-attribute"] = attr_name
    return field


def _build_reference_selector(node: dict) -> InputField:
    """Build a dropdown/radio-group ``InputField`` from a ``Pages$ReferenceSelector``.

    Reference selectors bind to an attribute on an *associated* entity
    (``attributeRef.entityRef`` is an ``IndirectEntityRef`` describing the
    association hop) rather than a plain attribute of the page's own entity.
    """
    label = _translated_text(node.get("labelTemplate")) or _translated_text(node.get("screenReaderLabel"))
    attr_name = _resolve_attribute_name(node.get("attributeRef"))
    render_mode = node.get("renderMode", "DropDown")
    field_type = InputFieldType.RadioGroup if render_mode == "RadioButtons" else InputFieldType.Dropdown

    field = InputField(
        name=node.get("name", ""),
        description="",
        field_type=field_type,
        label=label,
        readonly=node.get("editable", "Always") != "Always",
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    if attr_name:
        field.custom_attributes["data-mendix-attribute"] = attr_name
    return field


def _build_file_manager(node: dict) -> InputField:
    """Build a file-upload ``InputField`` from a ``Pages$FileManager`` widget."""
    attr_name = _resolve_attribute_name(node.get("attributeRef"))
    field = InputField(
        name=node.get("name", "fileManager"),
        description="",
        field_type=InputFieldType.File,
        label=_translated_text(node.get("labelTemplate")),
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    if attr_name:
        field.custom_attributes["data-mendix-attribute"] = attr_name
    return field


def _build_text(node: dict) -> Text:
    """Build a ``Text`` component from ``Pages$DynamicText`` or ``Pages$Label``."""
    content_node = node.get("content") or node.get("caption")
    content = _translated_text(content_node)
    return Text(
        name=node.get("name", ""),
        content=content,
        description="",
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _build_title(node: dict) -> Text:
    """Build a placeholder ``Text`` for a page's dynamic ``Pages$Title`` slot.

    Mendix renders the page's own (dynamic) title here; there is no static
    caption on the node itself, so we emit a recognizable placeholder.
    """
    return Text(
        name=node.get("name", "pageTitle"),
        content="{PageTitle}",
        description="Dynamic page title placeholder",
        css_classes=extract_css_classes(node),
    )


def _build_static_image(node: dict) -> Image:
    """Build an ``Image`` from a ``Pages$StaticImageViewer`` widget."""
    return Image(
        name=node.get("name", "image"),
        description=_translated_text(node.get("alternativeText")),
        source=node.get("image") or None,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _build_group_box(node: dict, domain_model: Optional[DomainModel] = None) -> ViewContainer:
    """Build a ``ViewContainer`` from a ``Pages$GroupBox`` (a titled panel)."""
    caption = _translated_text(node.get("caption"))
    children = _build_children(node.get("widgets", []), domain_model)
    if caption:
        box_name = node.get("name", "groupBox")
        children.add(Text(name=f"{box_name}_title", content=caption, description=""))
    return ViewContainer(
        name=node.get("name", "groupBox"),
        description="",
        view_elements=children,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _build_div_container(node: dict, domain_model: Optional[DomainModel] = None) -> ViewContainer:
    """Build a plain ``ViewContainer`` from a ``Pages$DivContainer``."""
    return ViewContainer(
        name=node.get("name", "container"),
        description="",
        view_elements=_build_children(node.get("widgets", []), domain_model),
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _build_data_view(node: dict, domain_model: Optional[DomainModel] = None) -> ViewContainer:
    """Build a ``ViewContainer`` from a ``Pages$DataView`` (a single-object entity form).

    Nested widgets' own ``attributeRef`` values are already fully-qualified
    (``Module.Entity.Attribute``), so we don't need to thread the DataView's
    entity context down for attribute resolution.

    BUML has a dedicated ``Form`` component (submit/cancel semantics), so any
    ``InputField``s found *directly* under this DataView (i.e. not already
    nested inside a further sub-container such as a GroupBox, which builds
    its own children independently) are grouped into a ``Form`` instead of
    sitting loose in the container; its submit/cancel labels are inferred
    from sibling Save/Cancel action buttons when present. Fields nested
    inside a GroupBox within the DataView are a known follow-up -- they
    currently stay as plain ``InputField``s inside that GroupBox's own
    container rather than being folded into this Form.

    When a ``domain_model`` is supplied (i.e. the data model was also
    extracted in this run), the Form's ``data_binding`` is set to the
    resolved domain ``Class`` from the DataView's own ``dataSource``, so the
    "bound entity" isn't just implicit in each field's attribute name.
    """
    widgets = list(node.get("widgets", []) or []) + list(node.get("footerWidgets", []) or [])
    flat_widgets = _flatten_layout_containers(widgets)

    children = set()
    input_fields = []
    names_seen = set()
    for raw_widget in flat_widgets:
        built = _build_widget(raw_widget, domain_model)
        if built is None:
            continue
        if built.name in names_seen:
            built.name = f"{built.name}_{len(names_seen)}"
        names_seen.add(built.name)
        if isinstance(built, InputField):
            input_fields.append(built)
        else:
            children.add(built)

    if input_fields:
        submit_label, cancel_label, show_cancel = "Submit", "Cancel", False
        for raw_widget in flat_widgets:
            if raw_widget.get("$Type") != "Pages$ActionButton":
                continue
            action = raw_widget.get("action", {}) or {}
            label = _translated_text(raw_widget.get("caption"))
            if action.get("$Type") == "Pages$SaveChangesClientAction" and label:
                submit_label = label
            elif action.get("$Type") == "Pages$CancelChangesClientAction" and label:
                cancel_label = label
                show_cancel = True

        form = Form(
            name=f"{node.get('name', 'dataView')}_form",
            description="",
            inputFields=set(input_fields),
            submit_label=submit_label,
            cancel_label=cancel_label,
            show_cancel=show_cancel,
        )
        data_source = node.get("dataSource", {}) or {}
        entity_class = _resolve_entity_class(domain_model, data_source.get("entityRef"))
        if entity_class is not None:
            form.data_binding = DataBinding(domain_concept=entity_class)
        children.add(form)

    return ViewContainer(
        name=node.get("name", "dataView"),
        description="",
        view_elements=children,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _build_tab_container(node: dict, domain_model: Optional[DomainModel] = None) -> ViewContainer:
    """Build a ``ViewContainer`` from a ``Pages$TabContainer``.

    BUML has no tab concept, so all tab pages' widgets are merged into one
    container (tab separation is lost -- a documented simplification).
    """
    children = set()
    for tab_page in node.get("tabPages", []) or []:
        if isinstance(tab_page, dict):
            children.update(_build_children(tab_page.get("widgets", []), domain_model))
    return ViewContainer(
        name=node.get("name", "tabContainer"),
        description="",
        view_elements=children,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


def _resolve_custom_widget_properties(node: dict) -> dict:
    """Resolve a ``CustomWidgets$CustomWidget`` node's properties by key.

    Modern Mendix widget-plugins (Data Grid 2, Combobox, Gallery, Image, ...)
    self-describe their schema: ``type.objectType.propertyTypes`` is a list of
    ``{"$ID": ..., "key": ...}`` entries, and ``object.properties`` holds the
    actual values as ``{"type": <propertyType $ID>, "value": {...}}``. We
    build the id -> key map once and return ``{key: value}`` for easy lookup.
    """
    widget_type = node.get("type", {})
    object_type = widget_type.get("objectType", {}) if isinstance(widget_type, dict) else {}
    prop_types = object_type.get("propertyTypes", []) if isinstance(object_type, dict) else []
    id_to_key = {
        pt.get("$ID"): pt.get("key")
        for pt in prop_types
        if isinstance(pt, dict) and pt.get("$ID")
    }

    resolved = {}
    obj = node.get("object", {})
    properties = obj.get("properties", []) if isinstance(obj, dict) else []
    for prop in properties:
        if not isinstance(prop, dict):
            continue
        key = id_to_key.get(prop.get("type"))
        if key:
            resolved[key] = prop.get("value", {}) or {}
    return resolved


def _build_gallery(node: dict, props: dict, domain_model: Optional[DomainModel] = None) -> DataList:
    """Build a ``DataList`` from a Gallery widget-plugin ("Data containers > Gallery").

    Structurally equivalent to a classic ``Pages$ListView``: a ``datasource``
    property gives the bound entity, and a ``content`` property holds the
    per-item widget template whose ``attributeRef``-bound fields we collect.
    """
    datasource_value = props.get("datasource", {})
    data_source_node = datasource_value.get("dataSource") if isinstance(datasource_value, dict) else None
    entity_ref = data_source_node.get("entityRef") if isinstance(data_source_node, dict) else None
    entity_qname = _entity_qname_from_ref(entity_ref)
    entity_name = entity_qname.split(".")[-1] if entity_qname else ""

    content_value = props.get("content", {})
    content_widgets = content_value.get("widgets", []) if isinstance(content_value, dict) else []
    fields = extract_fields_from_listview_widgets(content_widgets)

    source_name = entity_name or node.get("name", "Gallery")
    data_source = DataSourceElement(name=source_name, dataSourceClass=entity_name, fields=fields)
    data_list = DataList(
        name=node.get("name", "gallery"),
        description="",
        list_sources={data_source},
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    entity_class = _resolve_entity_class(domain_model, entity_ref)
    if entity_class is not None:
        data_list.data_binding = DataBinding(domain_concept=entity_class)
    return data_list


def _resolve_nested_object_list(node: dict, list_property_key: str) -> tuple[list, dict]:
    """Resolve a widget-plugin property that holds a *list of nested objects*
    (e.g. Data Grid 2's "columns"), returning ``(objects, id_to_key)``.

    Each item in such a list (a ``CustomWidgets$WidgetObject``) has its own
    independent property schema, described by the *list property's own*
    ``valueType.objectType.propertyTypes`` -- separate from the parent
    widget's top-level schema that ``_resolve_custom_widget_properties``
    already resolves. ``id_to_key`` is that nested schema's id -> key map, for
    use with ``_resolve_widget_object`` on each returned object.
    """
    widget_type = node.get("type", {})
    object_type = widget_type.get("objectType", {}) if isinstance(widget_type, dict) else {}
    prop_types = object_type.get("propertyTypes", []) if isinstance(object_type, dict) else []
    target_prop_type = next(
        (pt for pt in prop_types if isinstance(pt, dict) and pt.get("key") == list_property_key),
        None,
    )
    if target_prop_type is None:
        return [], {}

    value_type = target_prop_type.get("valueType", {}) or {}
    item_object_type = value_type.get("objectType") or {}
    item_prop_types = item_object_type.get("propertyTypes", []) if isinstance(item_object_type, dict) else []
    id_to_key = {
        pt.get("$ID"): pt.get("key")
        for pt in item_prop_types
        if isinstance(pt, dict) and pt.get("$ID")
    }

    resolved = _resolve_custom_widget_properties(node)
    list_value = resolved.get(list_property_key, {})
    objects = list_value.get("objects", []) if isinstance(list_value, dict) else []
    return objects, id_to_key


def _resolve_widget_object(widget_object: dict, id_to_key: dict) -> dict:
    """Resolve one nested ``CustomWidgets$WidgetObject`` (e.g. one Data Grid 2
    column) into a ``{key: value}`` dict, using the id -> key map for that
    object's own schema (see ``_resolve_nested_object_list``)."""
    resolved = {}
    for prop in widget_object.get("properties", []) or []:
        if not isinstance(prop, dict):
            continue
        key = id_to_key.get(prop.get("type"))
        if key:
            resolved[key] = prop.get("value", {}) or {}
    return resolved


def _build_data_grid(node: dict, props: dict, domain_model: Optional[DomainModel] = None) -> Table:
    """Build a ``Table`` from the "Data Grid 2" widget-plugin.

    Unlike Gallery/ListView (generic repeaters), Data Grid 2 is a genuine
    column-based table -- each column is bound to an attribute, possibly
    reached through an association hop from the grid's own entity (a lookup
    column, e.g. showing a related Vendor's name in a ProductLine grid) --
    so columns are modeled as ``FieldColumn``/``LookupColumn`` rather than
    flattened into a plain field-name list.

    ``FieldColumn``/``LookupColumn`` only generate valid code when the
    table's own bound entity (and, for a lookup column, the associated
    entity too) resolves to a real ``Class`` -- BESSER's code-builder
    references a variable named after that class, and silently emits a
    bare/undefined name otherwise (a ``NameError`` at import time). So
    whenever that resolution fails (most commonly a Mendix built-in like
    ``System.WorkflowUserTask``, absent from the export), we fall back to
    ``ExpressionColumn`` for that column instead, which is always safe since
    it just carries the attribute name as a literal string.
    """
    datasource_value = props.get("datasource", {})
    data_source_node = datasource_value.get("dataSource") if isinstance(datasource_value, dict) else None
    grid_entity_ref = data_source_node.get("entityRef") if isinstance(data_source_node, dict) else None
    grid_entity_class = _resolve_entity_class(domain_model, grid_entity_ref)

    column_objects, col_id_to_key = _resolve_nested_object_list(node, "columns")

    columns = []
    for col_obj in column_objects:
        col_props = _resolve_widget_object(col_obj, col_id_to_key)
        attribute_value = col_props.get("attribute", {})
        attribute_ref = attribute_value.get("attributeRef") if isinstance(attribute_value, dict) else None
        attr_name = _resolve_attribute_name(attribute_ref)
        if not attr_name:
            continue

        header_value = col_props.get("header", {})
        header_text = ""
        if isinstance(header_value, dict):
            header_text = _translated_text(header_value.get("textTemplate"))
        header_text = header_text or attr_name

        if grid_entity_class is None:
            columns.append(ExpressionColumn(label=header_text, expression=attr_name))
            continue

        col_entity_ref = attribute_ref.get("entityRef") if isinstance(attribute_ref, dict) else None
        if col_entity_ref:
            # Lookup column: the field lives on an entity reached through an
            # association hop from the grid's own entity, not on the grid's
            # own entity directly. The lookup is resolved at runtime by
            # matching an association end's name, so it also needs that
            # target entity to be a real, resolved Class.
            col_entity_qname = _entity_qname_from_ref(col_entity_ref)
            col_entity_name = col_entity_qname.split(".")[-1] if col_entity_qname else ""
            col_entity_class = _resolve_entity_class(domain_model, col_entity_ref)
            if col_entity_class is None:
                columns.append(ExpressionColumn(label=header_text, expression=attr_name))
                continue
            path_property = Property(
                name=col_entity_name.lower(),
                type=Class(name=col_entity_name, attributes=set()),
            )
            columns.append(LookupColumn(
                label=header_text,
                path=path_property,
                field=Property(name=attr_name, type=""),
            ))
        else:
            columns.append(FieldColumn(label=header_text, field=Property(name=attr_name, type="")))

    page_size_value = props.get("pageSize", {})
    rows_per_page = 5
    if isinstance(page_size_value, dict):
        try:
            rows_per_page = int(page_size_value.get("primitiveValue") or 5)
        except (TypeError, ValueError):
            rows_per_page = 5

    table = Table(
        name=node.get("name", "dataGrid"),
        show_header=True,
        show_pagination=True,
        rows_per_page=rows_per_page,
        columns=columns,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    if grid_entity_class is not None:
        table.data_binding = DataBinding(domain_concept=grid_entity_class)
    return table


def _build_custom_image(node: dict, props: dict) -> Image:
    """Build an ``Image`` from the "Image" widget-plugin."""
    image_url_value = props.get("imageUrl", {})
    source = ""
    if isinstance(image_url_value, dict):
        source = _translated_text(image_url_value.get("textTemplate"))

    alt_value = props.get("alternativeText", {})
    description = ""
    if isinstance(alt_value, dict):
        description = _translated_text(alt_value.get("textTemplate"))

    return Image(
        name=node.get("name", "image"),
        description=description,
        source=source or None,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )


# widgetId -> builder for the widget-plugins ("CustomWidgets$CustomWidget") we can
# confidently resolve. Anything else (Combobox, maps, charts, ...) is skipped
# rather than guessed at, since its internal property schema hasn't been
# verified against real exported data yet.
_CUSTOM_WIDGET_BUILDERS = {
    "com.mendix.widget.web.gallery.Gallery": _build_gallery,
    "com.mendix.widget.web.image.Image": _build_custom_image,
    "com.mendix.widget.web.datagrid.Datagrid": _build_data_grid,
}
# Builders that need the domain model (to resolve a bound entity/Class), as
# opposed to ones that only work off the raw widget JSON (e.g. Image).
_CUSTOM_WIDGET_BUILDERS_NEEDING_DOMAIN_MODEL = {_build_gallery, _build_data_grid}


def _build_custom_widget(node: dict, domain_model: Optional[DomainModel] = None) -> Optional[ViewElement]:
    """Build a BUML view element from a ``CustomWidgets$CustomWidget`` (widget-plugin)."""
    widget_type = node.get("type", {})
    widget_id = widget_type.get("widgetId", "") if isinstance(widget_type, dict) else ""
    builder = _CUSTOM_WIDGET_BUILDERS.get(widget_id)
    if builder is None:
        return None
    props = _resolve_custom_widget_properties(node)
    if builder in _CUSTOM_WIDGET_BUILDERS_NEEDING_DOMAIN_MODEL:
        return builder(node, props, domain_model)
    return builder(node, props)


def _extract_attributes(attributes_node, fields: set):
    """Extract attribute names from attributeRef nodes.

    The same bound field is often rendered more than once inside a single
    list/gallery item template (e.g. shown in both a title and a subtitle
    widget); ``DataSourceElement.fields`` rejects two entries with the same
    name, so duplicates are skipped here rather than added twice.
    """
    if isinstance(attributes_node, dict):
        attributes_node = [attributes_node]

    if not isinstance(attributes_node, list):
        return

    existing_names = {f.name for f in fields}
    for attr in attributes_node:
        if not isinstance(attr, dict):
            continue

        if attr.get("$Type") != "DomainModels$AttributeRef":
            continue

        attribute = attr.get("attribute", "")
        if not attribute or "." not in attribute:
            continue

        attribute = ".".join(attribute.split(".")[1:])
        if attribute in existing_names:
            continue
        fields.add(Property(name=attribute, type=""))
        existing_names.add(attribute)


def extract_fields_from_listview_widgets(widgets_node: list) -> set:
    """
    Extracts field names (attributes) from ClientTemplateParameter widgets inside a ListView.
    Returns a set of Property objects.
    """
    fields = set()

    def recurse(node):
        if isinstance(node, dict):
            node_type = node.get("$Type")

            if node_type == "Pages$ClientTemplateParameter":
                _extract_attributes(node.get("attributeRef", []), fields)

            for value in node.values():
                recurse(value)

        elif isinstance(node, list):
            for item in node:
                recurse(item)

    for widget in widgets_node:
        recurse(widget)

    return fields


def _build_list_view(node: dict, domain_model: Optional[DomainModel] = None) -> DataList:
    """Build a ``DataList`` from a classic ``Pages$ListView`` node."""
    name = node.get("name", "UnnamedListView")
    widgets = node.get("widgets", []) or []
    fields = extract_fields_from_listview_widgets(widgets)

    list_sources = set()
    entity_class = None
    data_source_node = node.get("dataSource", {}) or {}
    if data_source_node.get("$Type") == "Pages$ListViewXPathSource":
        entity_ref = data_source_node.get("entityRef")
        entity_qname = _entity_qname_from_ref(entity_ref)
        entity_name = entity_qname.split(".")[-1] if entity_qname else ""

        source_name = entity_name or name or "DataSource"
        data_source = DataSourceElement(
            name=source_name,
            dataSourceClass=entity_name,
            fields=fields,
        )
        list_sources.add(data_source)
        entity_class = _resolve_entity_class(domain_model, entity_ref)

    data_list = DataList(
        name=name,
        description="",
        list_sources=list_sources,
        styling=extract_styling(node),
        css_classes=extract_css_classes(node),
    )
    if entity_class is not None:
        data_list.data_binding = DataBinding(domain_concept=entity_class)
    return data_list


def _build_widget(node: dict, domain_model: Optional[DomainModel] = None) -> Optional[ViewElement]:
    """Build a single BUML view element from one raw Mendix widget JSON node.

    Returns ``None`` for action-less/unsupported nodes (e.g. ``Pages$NoClientAction``
    sentinels, unresolved widget-plugins) rather than raising, so one
    unfamiliar/malformed widget never aborts the whole page's extraction.

    ``domain_model`` is optional (``None`` when only the GUI model was
    requested, with no domain model built in this run) and is forwarded to
    the handful of builders that resolve a bound entity (``Form``, ``DataList``).
    """
    if not isinstance(node, dict):
        return None
    node_type = node.get("$Type")

    try:
        if node_type == "Pages$ActionButton":
            return _build_action_button(node)
        if node_type in _MENDIX_INPUT_WIDGET_TYPES:
            return _build_input_field(node, _MENDIX_INPUT_WIDGET_TYPES[node_type])
        if node_type == "Pages$ReferenceSelector":
            return _build_reference_selector(node)
        if node_type == "Pages$FileManager":
            return _build_file_manager(node)
        if node_type in ("Pages$DynamicText", "Pages$Label"):
            return _build_text(node)
        if node_type == "Pages$Title":
            return _build_title(node)
        if node_type == "Pages$StaticImageViewer":
            return _build_static_image(node)
        if node_type == "Pages$GroupBox":
            return _build_group_box(node, domain_model)
        if node_type == "Pages$DivContainer":
            return _build_div_container(node, domain_model)
        if node_type == "Pages$DataView":
            return _build_data_view(node, domain_model)
        if node_type == "Pages$TabContainer":
            return _build_tab_container(node, domain_model)
        if node_type == "Pages$ListView":
            return _build_list_view(node, domain_model)
        if node_type == "CustomWidgets$CustomWidget":
            return _build_custom_widget(node, domain_model)
    except Exception as exc:  # never let one malformed widget break the whole page
        print(f"Warning: skipping unsupported/malformed '{node_type}' widget "
              f"'{node.get('name', '?')}': {exc}")
        return None

    # Unknown widget type: if it still carries a nested widget list (e.g. a
    # snippet call, or a future Mendix widget we haven't special-cased yet),
    # don't silently drop its contents -- surface them in a plain container.
    nested = node.get("widgets")
    if isinstance(nested, list) and nested:
        children = _build_children(nested, domain_model)
        if not children:
            return None
        return ViewContainer(
            name=node.get("name") or f"{node_type or 'container'}",
            description="",
            view_elements=children,
        )

    return None


# Purely-visual Mendix grid wrappers that carry no data bindings of their own --
# only responsive column weights -- so flattening them loses nothing meaningful.
_PASS_THROUGH_LAYOUT_TYPES = {"Pages$LayoutGrid", "Pages$LayoutGridRow", "Pages$LayoutGridColumn"}


def _flatten_layout_containers(nodes: list) -> list:
    """Flatten LayoutGrid > LayoutGridRow > LayoutGridColumn wrappers into the
    plain, ordered list of real widgets they contain."""
    flat = []
    for node in nodes or []:
        if not isinstance(node, dict):
            continue
        node_type = node.get("$Type")
        if node_type == "Pages$LayoutGrid":
            for row in node.get("rows", []) or []:
                if isinstance(row, dict):
                    flat.extend(_flatten_layout_containers(row.get("columns", [])))
        elif node_type == "Pages$LayoutGridRow":
            flat.extend(_flatten_layout_containers(node.get("columns", [])))
        elif node_type == "Pages$LayoutGridColumn":
            flat.extend(_flatten_layout_containers(node.get("widgets", [])))
        else:
            flat.append(node)
    return flat


def _build_children(widget_nodes: list, domain_model: Optional[DomainModel] = None) -> set:
    """Build the set of BUML view elements for a list of raw Mendix widget nodes."""
    result = set()
    names_seen = set()
    for node in _flatten_layout_containers(widget_nodes):
        built = _build_widget(node, domain_model)
        if built is None:
            continue
        # A container rejects two children with the same name; flattening can
        # occasionally bring same-named siblings together (e.g. repeated item
        # templates), so disambiguate defensively rather than crash.
        if built.name in names_seen:
            built.name = f"{built.name}_{len(names_seen)}"
        names_seen.add(built.name)
        result.add(built)
    return result


# for styling for buttons
def map_mendix_screen_layout_to_besser(layout_type: str) -> Layout:
    """Map Mendix screen layout type to besser."""
    layout_map = {
        # General Web Layouts
        "Atlas_Core.Atlas_Default": Layout(
            layout_type =LayoutType.FLEX,
            orientation="vertical",
            padding="10px",
            margin="10px",
            gap="15px",
            alignment=JustificationType.CENTER,
            wrap=True),
        "Atlas_Core.Atlas_TopBar": Layout(
            layout_type=LayoutType.FLEX,
            orientation="horizontal",
            padding="5px",
            margin="5px",
            gap="10px",
            alignment=JustificationType.SPACE_BETWEEN,
            wrap=False),
    }

    # Fallback color if style not found
    screen_layout = Layout(
        layout_type="",
        orientation="vertical",
        padding="",
        margin="",
        gap="",
        alignment="",
        wrap=True)

    return layout_map.get(layout_type, screen_layout)



# for extarcting the layout for screen
def extract_screen_layout(page_node: dict) -> Styling:
    """Extracts screen layout from a Pages$Page node."""

    layout_type = ""
    screen_layout = None

    layout_call = page_node.get("layoutCall")
    if isinstance(layout_call, dict):
        layout_type = layout_call.get("layout")
        screen_layout = map_mendix_screen_layout_to_besser(layout_type)
    return screen_layout


def build_screens(gui_screens: set, main_pages, _gui_model: GUIModel,
                   domain_model: Optional[DomainModel] = None) -> set[Screen]:
    """Convert a list of raw screen nodes into ``Screen`` objects.

    ``_gui_model`` is unused and only kept for compatibility with callers.
    """
    screens = set()
    for scr in gui_screens:
        raw_widgets = []
        layout_call = scr.get("layoutCall", {}) or {}
        for argument in layout_call.get("arguments", []) or []:
            if isinstance(argument, dict):
                raw_widgets.extend(argument.get("widgets", []) or [])

        view_elements = _build_children(raw_widgets, domain_model)

        screen_name = scr.get("$QualifiedName").split(".")[1]
        is_main = screen_name in main_pages

        screen_layout = None
        extracted = extract_screen_layout(scr)
        if extracted:
            screen_layout = extracted

        screen = Screen(
            name=screen_name,
            description="",
            x_dpi="",
            y_dpi="",
            screen_size="Small",
            view_elements=view_elements,
            is_main_page=is_main,
            layout=screen_layout,
        )
        screens.add(screen)
    return screens


def build_modules(gui_screens, main_pages, gui_model: GUIModel,
                   domain_model: Optional[DomainModel] = None) -> set[Module]:
    """Create a single ``Module`` for the supplied screens.

    The returned set currently contains exactly one module named after
    ``gui_model.name``.
    """
    modules = set()
    screens = set()
    for scr in gui_screens:
        single_screen_set = build_screens(
            gui_screens=[scr],
            main_pages=main_pages,
            _gui_model=gui_model,
            domain_model=domain_model,
        )
        screens.update(single_screen_set)
    modules.add(Module(name=gui_model.name, screens=set(screens)))
    return modules


def mendix_to_gui(json_path: str, module_name: str,
                  _encoding: str = "utf-16",
                  domain_model: Optional[DomainModel] = None) -> Optional[GUIModel]:
    """Load a Mendix GUI JSON and return the corresponding ``GUIModel``.

    The ``_encoding`` parameter is retained for compatibility but ignored; the
    implementation probes several common encodings.  Numerous early returns keep
    the control flow simple.

    ``domain_model`` is optional: when the caller already built the
    ``DomainModel`` for this same module (i.e. both data model and GUI model
    are being extracted together), passing it in lets Forms/DataLists resolve
    their bound entity as a real ``Class`` reference via ``DataBinding``
    instead of just a name string. If omitted, GUI extraction still works
    exactly as before -- ``data_binding`` is simply left unset.
    """
    if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
        print("❌ The JSON file is empty or does not exist.")
        return None

    tried_encodings = ["utf-8", "utf-16", "utf-16-le", "utf-16-be"]
    data = None
    for enc in tried_encodings:
        try:
            with open(json_path, "r", encoding=enc) as json_file:
                data = json.load(json_file)
            #print(f"✅ Successfully loaded JSON using encoding: {enc}")
            break
        except UnicodeDecodeError as e:
            print(f"⚠️ UnicodeDecodeError for {enc}: {e}")
        except json.JSONDecodeError as e:
            print(f"❌ JSONDecodeError with {enc}: {e}")
            return None
        except Exception as e:  # broad-exception-caught
            print(f"❌ Unknown error with {enc}: {e}")
            return None

    if data is None:
        print("❌ Failed to decode the JSON file with all tried encodings.")
        return None

    main_pages = set()
    for unit in data.get("units", []):
        if unit.get("$Type") == "Navigation$NavigationDocument":
            main_pages.update(extract_main_pages(unit))

    gui_screens = []
    for unit in data.get("units", []):
        if (
            unit.get("$Type") == "Pages$Page"
            and unit.get("$QualifiedName", "").split('.')[0] == module_name
        ):
            gui_screens.append(unit)

    if not gui_screens:
        return None

    gui_model = GUIModel(
        name=module_name,
        package="",
        versionCode="",
        versionName="",
        modules=set(),
        description="",
    )
    modules_set = build_modules(
        gui_screens=gui_screens, gui_model=gui_model, main_pages=main_pages,
        domain_model=domain_model,
    )
    gui_model.modules.update(modules_set)

    return gui_model
