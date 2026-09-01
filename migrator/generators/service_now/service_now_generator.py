import os
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import DomainModel, AssociationClass
from besser.generators import GeneratorInterface
from besser.utilities.utils import sort_by_timestamp


class ServiceNowGenerator(GeneratorInterface):
    """
    ServiceNowGenerator is a class that implements the GeneratorInterface and is responsible for generating
    ServiceNow SDK TypeScript code based on B-UML models.

    Args:
        model (DomainModel): An instance of the DomainModel class representing the B-UML model.
        output_dir (str, optional): The output directory where the generated code will be saved. Defaults to None.
    """

    TYPES = {
        "int": "IntegerColumn",
        "str": "StringColumn",
        "float": "DecimalColumn",
        "bool": "BooleanColumn",
        "time": "StringColumn",
        "date": "DateColumn",
        "datetime": "DateTimeColumn",
        "timedelta": "StringColumn",
        "any": "StringColumn",
    }

    RESERVED_NAMES = {
        "Table",
        "StringColumn",
        "IntegerColumn",
        "ChoiceColumn",
        "ReferenceColumn",
        "DateColumn",
        "DateTimeColumn",
        "EmailColumn",
        "BooleanColumn",
        "DecimalColumn",
        "UrlColumn",
        "HtmlColumn",
        "Record",
        "Now",
    }

    def __init__(self, model: DomainModel, output_dir: str = None, table_prefix: str = ""):
        super().__init__(model, output_dir)
        self.table_prefix = table_prefix
        # Work on an instance-level copy so per-model enum entries never leak
        self.TYPES = dict(type(self).TYPES)
        # Add enums to TYPES dictionary
        for enum in model.get_enumerations():
            self.TYPES[enum.name] = "ChoiceColumn"

    def get_table_name(self, class_name: str) -> str:
        """
        Convert a class name to a ServiceNow table name.

        Format: u_ + optional_prefix + _ + snake_case_name
        - No prefix: u_book, u_author
        - With prefix: u_app_book, u_app_author
        """
        # Convert CamelCase to snake_case
        snake_name = ""
        for i, char in enumerate(class_name):
            if char.isupper() and i > 0:
                snake_name += "_" + char.lower()
            else:
                snake_name += char.lower()

        # Always start with u_, then add optional prefix
        if self.table_prefix:
            return f"u_{self.table_prefix}_{snake_name}"
        return f"u_{snake_name}"

    def get_display_name(self, class_name: str) -> str:
        """Convert a class name to a display name."""
        # Convert CamelCase to Title Case
        result = ""
        for i, char in enumerate(class_name):
            if char.isupper() and i > 0:
                result += " " + char
            else:
                result += char
        return result

    def separate_classes(self):
        """
        Separates regular classes from association classes in the model.

        Returns:
            tuple: A tuple containing two lists (regular_classes, association_classes)
        """
        classes_list = self.model.classes_sorted_by_inheritance()
        classes = []
        asso_classes = []

        for class_item in classes_list:
            if isinstance(class_item, AssociationClass):
                asso_classes.append(class_item)
            else:
                classes.append(class_item)

        return classes, asso_classes

    def get_reference_columns(self):
        """
        Returns a dictionary mapping class names to their reference associations.

        Returns:
            dict: Dictionary where keys are class names and values are lists of reference properties
        """
        references = {}
        for association in self.model.associations:
            if len(association.ends) == 2:
                for end in association.ends:
                    class_name = end.type.name
                    if class_name not in references:
                        references[class_name] = []
                    other_end = [e for e in association.ends if e != end][0]
                    references[class_name].append({
                        "property_name": end.name,
                        "reference_table": self.get_table_name(other_end.type.name),
                        "multiplicity_max": end.multiplicity.max,
                        "other_end_name": other_end.name,
                        "other_multiplicity_max": other_end.multiplicity.max
                    })
        return references

    def validate_model(self):
        """
        Validates that the model doesn't use reserved names for classes, enumerations, or attributes.

        Raises:
            ValueError: If any reserved names are found in the model.
        """
        conflicts = []

        for cls in self.model.get_classes():
            if cls.name in self.RESERVED_NAMES:
                conflicts.append(f"Class name '{cls.name}' is reserved and cannot be used.")

            for attr in cls.attributes:
                if attr.name in self.RESERVED_NAMES:
                    conflicts.append(
                        f"Attribute name '{attr.name}' in class '{cls.name}' is reserved and cannot be used."
                    )

        for enum in self.model.get_enumerations():
            if enum.name in self.RESERVED_NAMES:
                conflicts.append(f"Enumeration name '{enum.name}' is reserved and cannot be used.")

        for association in self.model.associations:
            if association.name in self.RESERVED_NAMES:
                conflicts.append(f"Association name '{association.name}' is reserved and cannot be used.")

        if conflicts:
            error_message = "ServiceNow code generation failed due to reserved name conflicts:\n" + "\n".join(
                f"  - {conflict}" for conflict in conflicts
            )
            error_message += (
                f"\n\nReserved names that cannot be used: {', '.join(sorted(self.RESERVED_NAMES))}."
            )
            raise ValueError(error_message)

    def validate_attribute_types(self):
        """
        Validates that every attribute type in the model maps to a known ServiceNow column type.

        Raises:
            ValueError: If any attribute uses a type not present in TYPES.
        """
        unsupported = []
        for cls in self.model.get_classes():
            for attr in cls.attributes:
                if attr.type.name not in self.TYPES:
                    unsupported.append(
                        f"  - Attribute '{cls.name}.{attr.name}' has unsupported type '{attr.type.name}'."
                    )
        if unsupported:
            raise ValueError(
                "ServiceNow code generation failed: unsupported attribute types found:\n"
                + "\n".join(sorted(unsupported))
                + f"\n\nSupported types: {', '.join(sorted(self.TYPES))}."
            )

    def get_used_column_types(self, classes, enumerations):
        """
        Determine which ServiceNow column types are actually used in the model.

        Returns:
            list: List of column type names (e.g., ['StringColumn', 'IntegerColumn'])
        """
        used_types = set()

        # Check all class attributes
        for cls in classes:
            for attr in cls.attributes:
                if attr.type.__class__.__name__ == 'Enumeration':
                    used_types.add('ChoiceColumn')
                else:
                    column_type = self.TYPES.get(attr.type.name, 'StringColumn')
                    used_types.add(column_type)

        # Check for ReferenceColumns (from associations)
        if self.model.associations:
            used_types.add('ReferenceColumn')

        # Add Table if we have any classes
        if classes:
            used_types.add('Table')

        # Add Record if we have associations with many-to-one
        for association in self.model.associations:
            if len(association.ends) == 2:
                for end in association.ends:
                    if end.multiplicity.max > 1:
                        used_types.add('Record')
                        break

        return sorted(list(used_types))

    def generate(self):
        """
        Generates ServiceNow SDK TypeScript code based on the provided B-UML model and saves it to the specified
        output directory.

        Returns:
            None, but stores the generated code as a file named tables.now.ts
        """
        # Validate the model
        self.validate_model()
        self.validate_attribute_types()

        classes, asso_classes = self.separate_classes()
        references = self.get_reference_columns()
        used_column_types = self.get_used_column_types(classes, self.model.get_enumerations())

        file_path = self.build_generation_path(file_name="tables.now.ts")
        templates_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(templates_path))
        template = env.get_template('service_now_template.ts.j2')

        with open(file_path, mode="w", encoding="utf-8") as f:
            generated_code = template.render(
                classes=classes,
                asso_classes=asso_classes,
                types=self.TYPES,
                associations=self.model.associations,
                enumerations=self.model.get_enumerations(),
                model_name=self.model.name,
                references=references,
                sort=sort_by_timestamp,
                get_table_name=self.get_table_name,
                get_display_name=self.get_display_name,
                used_column_types=used_column_types,
            )
            f.write(generated_code)
            print("ServiceNow code generated successfully!")
