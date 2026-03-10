import os
import random
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
        template = env.get_template('ui_page_sql_template.sql.j2')
        env.tests['is_Button'] = self.is_button
        env.tests['is_List'] = self.is_list
        env.tests['is_ModelElement'] = self.is_model_element
        env.globals['chr'] = chr

        random_id = random.randint(1000, 9999)
        action_random_id = random.randint(1000, 9999)

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
                plug_id=random_id,
                action_id=action_random_id,
                sql_dialect=self.sql_dialect,
            )
            f.write(generated_code)
            #print("Code generated in the location: " + file_path)

