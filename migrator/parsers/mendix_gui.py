import json
import os
from typing import Optional

from besser.BUML.metamodel.structural import Property

from besser.BUML.metamodel.gui.graphical_ui import (
    Button,
    ButtonActionType,
    ButtonType,
    DataList,
    DataSourceElement,
    GUIModel,
    Module,
    Screen,
)

from besser.BUML.metamodel.gui import (
    Styling, Color, Layout, LayoutType, Position, PositionType, JustificationType
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



def mendix_to_buml_button_type(mendix_button_type: str) -> str:
    """Converts Mendix button type to B-UML button type."""
    type_mapping = {
        "Pages$PageClientAction": ButtonType.RaisedButton,
        "Pages$DeleteClientAction": ButtonType.OutlinedButton,
        "Pages$CreateObjectClientAction": ButtonType.FloatingActionButton,
        "Pages$NoClientAction": ButtonType.TextButton,
        "Pages$CancelChangesClientAction": ButtonType.TextButton,
        "Pages$MicroflowClientAction": ButtonType.RaisedButton,
        "Pages$SaveChangesClientAction": ButtonType.RaisedButton

    }
    return type_mapping.get(mendix_button_type, "")


def mendix_to_buml_action_type(mendix_action_type: str) -> str:
    """Converts Mendix button type to B-UML action type for button."""
    type_mapping = {
        "Pages$DeleteClientAction": ButtonActionType.Delete,
        "Pages$CancelChangesClientAction": ButtonActionType.Cancel,
        "Pages$PageClientAction": ButtonActionType.Edit,
        "Pages$CreateObjectClientAction": ButtonActionType.Add,
        "Pages$SaveChangesClientAction": ButtonActionType.Save
    }
    return type_mapping.get(mendix_action_type, "")


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
    """Extract styling from a Pages$ActionButton node.

    The only visual information we currently care about is the Mendix
    ``buttonStyle`` which is mapped to a ``Color``.  Size used to be taken from
    the ``class`` string; we keep that behaviour for backwards compatibility,
    but the caller is responsible for also storing the raw classes on the
    element itself via ``extract_css_classes``.
    """
    button_style = node.get("buttonStyle", "")  # like 'Danger', 'Primary', etc.
    #size = css_class if css_class else ""

    color = map_button_style_to_color(button_style)
    position = Position(p_type=PositionType.RELATIVE)

    return Styling(size="", color=color, position=position)





def extract_action_buttons(unit):
    """Extracts action buttons from a Pages$Page unit."""
    action_buttons = set()

    def _label_from_caption(caption_node):
        if not isinstance(caption_node, dict):
            return ""
        templates = caption_node.get("template", [])
        if not isinstance(templates, list):
            templates = [templates]
        for template in templates:
            if isinstance(template, dict) and template.get("$Type") == "Texts$Text":
                translations = template.get("translations", [])
                if isinstance(translations, dict):
                    translations = [translations]
                for translation in translations:
                    if (
                        isinstance(translation, dict)
                        and translation.get("$Type") == "Texts$Translation"
                    ):
                        text = translation.get("text", "")
                        if text:
                            return text
        return ""

    def recurse(node):
        if isinstance(node, dict):
            if node.get("$Type") == "Pages$ActionButton":
                label = _label_from_caption(node.get("caption"))
                action = node.get("action", {})
                button_type_str = action.get("$Type", "")
                button_type = mendix_to_buml_button_type(button_type_str)
                action_type = mendix_to_buml_action_type(button_type_str)

                target_screen = None
                if action_type == ButtonActionType.Navigate:
                    page_settings = action.get("pageSettings", {})
                    if isinstance(page_settings, dict):
                        screen_name = page_settings.get("page", "").split(".")[1]
                        target_screen = Screen(
                            name=screen_name,
                            description="",
                            x_dpi="",
                            y_dpi="",
                            screen_size="Small",
                            view_elements={},
                        )

                if button_type == ButtonType.TextButton and label in {"Back", "Return", "←"}:
                    action_type = ButtonActionType.Back

                styling = extract_styling(node)
                css_classes = extract_css_classes(node)
                button = Button(
                    label=label or "Unnamed Button",
                    buttonType=button_type,
                    actionType=action_type,
                    description="",
                    name=node.get("name", ""),
                    visibility="",
                    targetScreen=target_screen,
                    styling=styling,
                )
                # attach any discovered CSS classes (may be empty)
                button.css_classes = css_classes
                action_buttons.add(button)

            for value in node.values():
                recurse(value)
        elif isinstance(node, list):
            for item in node:
                recurse(item)
    recurse(unit)
    return action_buttons


def _extract_attributes(attributes_node, fields: set):
    """Extract attribute names from attributeRef nodes."""
    if isinstance(attributes_node, dict):
        attributes_node = [attributes_node]

    if not isinstance(attributes_node, list):
        return

    for attr in attributes_node:
        if not isinstance(attr, dict):
            continue

        if attr.get("$Type") != "DomainModels$AttributeRef":
            continue

        attribute = attr.get("attribute", "")
        if not attribute or "." not in attribute:
            continue

        attribute = ".".join(attribute.split(".")[1:])
        fields.add(Property(name=attribute, type=""))


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

def extract_list_sources(unit):
    """Extracts data sources from Pages$ListViewXPathSource nodes inside a ListView."""
    list_sources = set()

    def recurse(node):
        if isinstance(node, dict):
            if node.get("$Type") == "Pages$ListViewXPathSource":
                widgets = node.get("widgets", [])
                fields = extract_fields_from_listview_widgets(widgets)

                data_source = DataSourceElement(
                    name=node.get("entityRef", {}).get("entity", "UnnamedDataSource"),
                    dataSourceClass="",
                    fields=fields
                )
                list_sources.add(data_source)

            for value in node.values():
                recurse(value)

        elif isinstance(node, list):
            for item in node:
                recurse(item)

    recurse(unit)
    return list_sources


def extract_data_lists(unit):
    """Extracts data lists from Pages$ListView nodes."""
    data_lists = set()

    def recurse(node):
        if isinstance(node, dict):
            if node.get("$Type") == "Pages$ListView":
                name = node.get("name", "UnnamedListView")
                widgets = node.get("widgets", [])

                # Extract fields from widgets
                fields = extract_fields_from_listview_widgets(widgets)

                list_sources = set()

                data_source_class_name = ""
                # Extract data source (must be under "dataSource")
                data_source_node = node.get("dataSource", {})
                if data_source_node.get("$Type") == "Pages$ListViewXPathSource":
                    if not data_source_node.get("entityRef") == "null":
                        entity_name = data_source_node.get(
                            "entityRef", {}).get("entity", "UnnamedEntity")
                        if not entity_name == "UnnamedEntity":
                            data_source_class_name = entity_name.split('.')[1]

                    data_source = DataSourceElement(
                        name="",
                        dataSourceClass=data_source_class_name,
                        fields=fields
                    )
                    list_sources.add(data_source)



                # Build DataList instance
                data_list = DataList(
                    name=name,
                    description="",
                    list_sources=list_sources,
                    styling=""
                )

                # capture classes on the element itself for later code generation
                data_list.css_classes = extract_css_classes(node)

                data_lists.add(data_list)

            # Recurse deeper
            for value in node.values():
                recurse(value)

        elif isinstance(node, list):
            for item in node:
                recurse(item)

    recurse(unit)
    return data_lists


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


def build_screens(gui_screens: set, main_pages, _gui_model: GUIModel) -> set[Screen]:
    """Convert a list of raw screen nodes into ``Screen`` objects.

    ``_gui_model`` is unused and only kept for compatibility with callers.
    """
    screens = set()
    for scr in gui_screens:
        view_elements = set()
        view_elements.update(extract_action_buttons(scr))
        view_elements.update(extract_data_lists(scr))


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


def build_modules(gui_screens, main_pages, gui_model: GUIModel) -> set[Module]:
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
        )
        screens.update(single_screen_set)
    modules.add(Module(name=gui_model.name, screens=set(screens)))
    return modules


def mendix_to_gui(json_path: str, module_name: str,
                  _encoding: str = "utf-16") -> Optional[GUIModel]:
    """Load a Mendix GUI JSON and return the corresponding ``GUIModel``.

    The ``_encoding`` parameter is retained for compatibility but ignored; the
    implementation probes several common encodings.  Numerous early returns keep
    the control flow simple.
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
        modules={},
        description="",
    )
    modules_set = build_modules(
        gui_screens=gui_screens, gui_model=gui_model, main_pages=main_pages
    )
    modules_dict = {module.name: module for module in modules_set}
    gui_model.modules.update(modules_dict)

    return gui_model

