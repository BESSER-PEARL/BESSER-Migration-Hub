from besser.BUML.metamodel.structural import DomainModel
from besser.utilities import buml_code_builder
from migrator.generators.spreadsheet import SpreadSheetGenerator
from migrator import ModelMigrator

# Parse json Mendix model to B-UML model
model_migrator: ModelMigrator  = ModelMigrator(lcp="mendix", 
                                            model_path="library.json", 
                                            module_name="MyFirstModule")
domain_model: DomainModel = model_migrator.domain_model()

# Generate Python base code for the B-UML model
buml_code_builder.domain_model_to_code(model=domain_model, file_path="output/buml_model.py")

# Generate Spreadsheet
generator = SpreadSheetGenerator(model=domain_model, output_dir="output/output_model.xlsx")
generator.generate()