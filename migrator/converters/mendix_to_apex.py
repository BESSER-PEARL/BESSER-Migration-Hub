from anyio import Path
from pathlib import Path
from besser.BUML.metamodel.gui.graphical_ui import *
from migrator import GUIModelMigrator, ModelMigrator
from besser.utilities.buml_code_builder import domain_model_to_code

from besser.BUML.metamodel.structural import DomainModel
from migrator.converters.besser_to_apex import generate_pages_for_gui_model


# output can be folder or file depending on BESSER implementation
OUTPUT_PATH = Path("output").resolve()

# Parse json Mendix model to B-UML model
domain_model: DomainModel = ModelMigrator(lcp="mendix",
                                         openai_token = "",
                                         model_path=r"path/to/mendix/model.json",
                                         module_name="name_of_module")

gui_model_migrator: GUIModelMigrator  = GUIModelMigrator(lcp="mendix",
                                                        openai_token = "",
                                                         model_path=r"path/to/mendix/model.json",
                                                         module_name="name_of_module")


domain_model = domain_model.domain_model()

domain_model_to_code(model=domain_model, file_path="output")

print("\n✅ Code generation finished.")
print(f"📂 Output generated at:\n{OUTPUT_PATH}")

gui_model : GUIModel = gui_model_migrator.gui_model()


if gui_model and domain_model:

    apex_dir = r"path/to/apex/export/directory"
    workspace = "name_of_workspace"
    user = "user@example.com"

    # Pass your GUI model
    generate_pages_for_gui_model(apex_dir, gui_model, domain_model, workspace, user)
