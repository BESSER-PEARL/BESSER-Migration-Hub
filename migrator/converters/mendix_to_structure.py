from migrator import ModelMigrator
from besser.utilities.buml_code_builder import domain_model_to_code
from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator
from besser.BUML.metamodel.structural import *
from migrator.generators.sql import SQLGenerator
import os


# Parse json Mendix model to B-UML model
domain_model: DomainModel = ModelMigrator(lcp="mendix",
                                         openai_token = "",
                                         model_path=r"path/to/mendix/model.json",
                                         module_name="name_of_module")


#domain_model_to_code(model=gui_model, file_path="output")
domain_model = domain_model.domain_model()

if domain_model is None:
    raise RuntimeError("Domain model generation failed")

domain_model_to_code(model=domain_model, file_path="output")

# Generate SQL schema from domain model
sql_generator = SQLGenerator(
    model=domain_model,
    output_dir="output/sql",      # optional but recommended
    sql_dialect="oracle"              # or "postgres" / "mysql"
)

sql_generator.generate()

# ✅ Print absolute output path
abs_path = os.path.abspath("output/sql")
print(f"\n✅ Oracle APEX SQL generated successfully!")
print(f"📁 Output directory: {abs_path}")

