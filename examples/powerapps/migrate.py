import configparser

from besser.BUML.metamodel.structural import DomainModel
from besser.utilities import buml_code_builder
from besser.generators.sql.sql_generator import SQLGenerator
from migrator import ModelMigrator

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Access the token
openai_token = config['DEFAULT']['OPENAI_TOKEN']


# Parse json Mendix model to B-UML model
model_migrator: ModelMigrator  = ModelMigrator(lcp="powerapps",
                                            model_path="base_examples/library/library.png",
                                            module_name=["base_examples/library/author.csv",
                                                         "base_examples/library/book.csv",
                                                         "base_examples/library/library.csv"],
                                            openai_token = openai_token
                                            )
buml_model: DomainModel = model_migrator.domain_model()

# Generate Python base code for the B-UML model
buml_code_builder.domain_model_to_code(model=buml_model, file_path="buml_parser_result/library/buml_model.py")

# Generate the Oracle SQL code
generator = SQLGenerator(model=buml_model, sql_dialect="oracle", output_dir="buml_generator_result/oracle_apex/library")
generator.generate()
