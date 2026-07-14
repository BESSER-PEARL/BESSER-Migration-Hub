import os
import re
import uuid
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import DomainModel
from besser.generators import GeneratorInterface
from besser.BUML.metamodel.gui.graphical_ui import (
    Button,
    DataList,
    DataSourceElement,
    GUIModel,
    Screen,
)
from besser.utilities.utils import sort_by_timestamp


def camel_to_snake(name):
    """Convert a camelCase or PascalCase name to snake_case."""
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# Oracle reserved words that must be renamed as column identifiers.
# Must stay in sync with ORACLE_RESERVED_COLUMN_MAP in oracle_apex_sql_generator.
_ORACLE_RESERVED_COLS = {
    'comment': 'comment_text',
    'level':   'level_num',
    'number':  'num_value',
    'file':    'file_name',
    'lock':    'lock_flag',
}


def oracle_col_name(name: str) -> str:
    """camelCase → snake_case, then apply Oracle reserved-word renaming.

    Mirrors _col_name() in OracleApexSQLGenerator so that page column
    references always match the actual DDL column names.
    """
    snake = camel_to_snake(name)
    return _ORACLE_RESERVED_COLS.get(snake, snake)


class UIPagesSQLGenerator(GeneratorInterface):
    """
    UIPagesSQLGenerator implements :class:`GeneratorInterface` and produces a set
    of SQL statements that define or modify the structure of user interface
    pages.

    Args:
        gui_model (GUIModel): An instance of the GUI Model representing the
            B-UML model.
        output_dir (str, optional): Directory where generated code is saved.
            Defaults to None.
        sql_dialect (str, optional): SQL dialect to use; None, "postgres", or
            "mysql" are supported.
    """

    TYPES = {

        "str": "STRING",
        "int" : "NUMBER",
        "date" : "DATE"

    }

    def _get_modules(self):
        if isinstance(self.gui_model.modules, dict):
            return self.gui_model.modules.values()
        return self.gui_model.modules

    @staticmethod
    def is_button(value):
        """Check if the given value is an instance of Button class."""
        return isinstance(value, Button)

    @staticmethod
    def is_list(value):
        """Check if the given value is an instance of DataList class."""
        return isinstance(value, DataList)

    @staticmethod
    def is_model_element(value):
        """Check if the given value is an instance of DataSourceElement class."""
        return isinstance(value, DataSourceElement)

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def __init__(
        self,
        model: DomainModel,
        gui_model: GUIModel,
        app_id: str,
        screen: Screen,
        screen_number: str,
        workspace_name: str,
        user_name: str,
        output_file_name: str,
        output_dir: str = None,
        sql_dialect: str = None,
        apex_version: str = '2024.11.30',
        apex_release: str = '24.2.6',
    ):
        super().__init__(model, output_dir)
        self.sql_dialect = sql_dialect
        self.gui_model = gui_model
        self.model = model
        self.app_id = app_id
        self.workspace_name = workspace_name
        self.user_name = user_name
        self.screen = screen
        self.screen_number = screen_number
        self.output_file_name = output_file_name
        self.apex_version = apex_version
        self.apex_release = apex_release

    def generate(self):
        """
        Generates SQL code based on the provided B-UML model (gui_model)
        and saves it to the specified output directory.
        If the output directory was not specified, the code generated
        will be stored in the <current directory>/output
        folder.
        """
        file_path = self.build_generation_path(file_name=self.output_file_name)

        templates_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(templates_path),
                          trim_blocks=True, lstrip_blocks=True)
        env.tests['is_Button'] = self.is_button
        env.tests['is_List'] = self.is_list
        env.tests['is_ModelElement'] = self.is_model_element
        env.globals['chr'] = chr
        env.filters['camel_to_snake'] = camel_to_snake
        env.filters['oracle_col_name'] = oracle_col_name
        template = env.get_template('ui_page_sql_template.sql.j2')

        # Use UUID-derived large integers so IDs are unique across all
        # generated pages and cannot clash with existing APEX metadata IDs.
        def _uid() -> int:
            return int(uuid.uuid4().hex[:14], 16)   # 56-bit unique int

        plug_id        = _uid()
        action_event_id = _uid()   # DA event
        action_da_id    = _uid()   # DA action (must differ from event ID)
        worksheet_uid   = _uid()   # worksheet internal_uid

        if not self.gui_model.modules:
            raise ValueError("GUI model has no modules")

        module = next(iter(self._get_modules()))
        screens = module.screens

        with open(file_path, mode="w", encoding="utf-8") as f:
            generated_code = template.render(
                model=self.model,
                gui_model=self.gui_model,
                sort_by_timestamp=sort_by_timestamp,
                screens=screens,
                screen=self.screen,
                app_id=self.app_id,
                screen_number=self.screen_number,
                workspace_name=self.workspace_name,
                user_name=self.user_name,
                types=self.TYPES,
                plug_id=plug_id,
                action_id=action_event_id,
                action_da_id=action_da_id,
                worksheet_uid=worksheet_uid,
                sql_dialect=self.sql_dialect,
                apex_version=self.apex_version,
                apex_release=self.apex_release,
            )
            f.write(generated_code)
            #print("Code generated in the location: " + file_path)

