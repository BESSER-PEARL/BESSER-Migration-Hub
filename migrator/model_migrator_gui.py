from besser.BUML.metamodel.gui.graphical_ui import GUIModel
from migrator.parsers.mendix_gui import mendix_to_gui


class GUIModelMigrator:
    """Represents the migration process for a model from a low-code platform (LCP) to BESSER.

    Args:
        lcp (str): The name of the low-code platform from which the model will be migrated.
        model_path (str): The path to the model file that will be migrated.
        module_name (str): The name of the module within the LCP from which the model will
            be extracted.

    Attributes:
        lcp (str): The name of the low-code platform.
        model_path (str): The path to the model file.
        module_name (str): The name of the module.
    """

    def __init__(self, lcp: str, model_path: str, module_name: str, openai_token: str):
        self.lcp: str = lcp
        self.model_path: str = model_path
        self.module_name: str = module_name
        self.openai_token: str = openai_token

    # Getter and Setter for lcp
    @property
    def lcp(self) -> str:
        """str: Get the name of the low-code platform."""
        return self.__lcp

    @lcp.setter
    def lcp(self, lcp: str):
        """str: Set the name of the low-code platform."""
        self.__lcp = lcp

    # Getter and Setter for model_path
    @property
    def model_path(self) -> str:
        """str: Get the path to the model file."""
        return self.__model_path

    @model_path.setter
    def model_path(self, model_path: str):
        """str: Set the path to the model file."""
        self.__model_path = model_path

    # Getter and Setter for module_name
    @property
    def module_name(self) -> str:
        """str: Get the name of the module within BESSER."""
        return self.__module_name

    @module_name.setter
    def module_name(self, module_name: str):
        """str: Set the name of the module within BESSER."""
        self.__module_name = module_name

    def gui_model(self) -> GUIModel:
        """Return a :class:`~metamodel.graphical_ui.GUIModel` for the configured
        low-code platform and module.
        """
        gui_model: GUIModel | None = None
        if self.lcp == "mendix":
            gui_model = mendix_to_gui(
                json_path=self.model_path,
                module_name=self.module_name,
            )
        elif self.lcp == "powerapps":
            # the powerapps parser isn't written yet, keep structure for future
            # gui_model = powerapps_to_buml(
            #     image_path=self.model_path,
            #     csv_paths=self.module_name,
            #     openai_token=self.openai_token,
            # )
            print("PowerApps GUI model migration is not implemented yet.")
        else:
            raise ValueError("Low code platform not supported")

        return gui_model
