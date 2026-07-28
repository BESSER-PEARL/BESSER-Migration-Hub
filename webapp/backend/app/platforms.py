"""Platform registry for the Migration Hub.

Single source of truth for source/target low-code platforms and their
capabilities. The frontend renders cards, badges, upload rules and tutorials
straight from this data, and the backend uses the same entries to guard
not-yet-implemented paths. Adding a platform is a one-file change here.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class SourcePlatform:
    id: str
    label: str
    # "deterministic" (dedicated parser) or "llm" (visual LLM extraction)
    transformation: str
    implemented: bool
    supports_data: bool
    supports_gui: bool
    # File upload rules for the UI dropzone.
    accepted_extensions: list[str]
    input_hint: str
    allow_multiple: bool = False
    needs_module: bool = False        # requires a module name (Mendix)
    needs_openai: bool = False        # requires an OpenAI token (LLM path)
    allow_csv: bool = False           # extra CSV files can complement the image
    # User-facing banner explaining what will happen once selected.
    banner: str = ""

    def public(self) -> dict:
        return asdict(self)


@dataclass
class TargetPlatform:
    id: str
    label: str
    implemented: bool
    supports_data: bool
    supports_gui: bool
    # Internal generator selector, consumed by services/generate.py.
    generator: Optional[str] = None
    sql_dialect: Optional[str] = None
    output_desc: str = ""
    tutorial: str = ""
    note: str = ""

    def public(self) -> dict:
        return asdict(self)


# --------------------------------------------------------------------------- #
# Source platforms
# --------------------------------------------------------------------------- #

SOURCES: dict[str, SourcePlatform] = {
    "mendix": SourcePlatform(
        id="mendix",
        label="Mendix",
        transformation="deterministic",
        implemented=True,
        supports_data=True,
        supports_gui=True,
        accepted_extensions=[".json"],
        input_hint="Upload the Mendix project export (JSON produced by the mx command-line tool).",
        allow_multiple=False,
        needs_module=True,
        needs_openai=False,
        banner=(
            "Mendix is supported through a **deterministic transformation**. "
            "Dedicated parsers read your exported model and build the pivot model "
            "exactly, with no AI involved."
        ),
    ),
    "powerapps": SourcePlatform(
        id="powerapps",
        label="Microsoft Power Apps",
        transformation="llm",
        implemented=True,
        supports_data=True,
        supports_gui=True,
        accepted_extensions=[".png", ".jpg", ".jpeg"],
        input_hint="Upload screenshots of the model or application screens. You may add exported CSV files to improve data-model accuracy.",
        allow_multiple=True,
        needs_module=False,
        needs_openai=True,
        allow_csv=True,
        banner=(
            "Power Apps has no full model export, so migration uses an "
            "**LLM-based transformation**: a visual model reads your screenshots "
            "(optionally helped by CSV exports) to reconstruct the data and GUI models. "
            "Results are best-effort and can be reviewed before generation."
        ),
    ),
    "outsystems": SourcePlatform(
        id="outsystems",
        label="OutSystems",
        transformation="llm",
        implemented=True,
        supports_data=False,
        supports_gui=True,
        accepted_extensions=[".png", ".jpg", ".jpeg"],
        input_hint="Upload screenshot(s) of your model.",
        allow_multiple=True,
        needs_openai=True,
        allow_csv=True,
        banner=(
            "OutSystems uses an **LLM-based transformation** from screenshots. "
            "The screenshot pipeline creates a GUI pivot model; data extraction is not available yet."
        ),
    ),
    "appian": SourcePlatform(
        id="appian",
        label="Appian",
        transformation="llm",
        implemented=True,
        supports_data=False,
        supports_gui=True,
        accepted_extensions=[".png", ".jpg", ".jpeg"],
        input_hint="Upload screenshot(s) of your model.",
        allow_multiple=True,
        needs_openai=True,
        allow_csv=True,
        banner=(
            "Appian uses an **LLM-based transformation** from screenshots. "
            "The screenshot pipeline creates a GUI pivot model; data extraction is not available yet."
        ),
    ),
    "salesforce": SourcePlatform(
        id="salesforce",
        label="Salesforce",
        transformation="llm",
        implemented=True,
        supports_data=False,
        supports_gui=True,
        accepted_extensions=[".png", ".jpg", ".jpeg"],
        input_hint="Upload screenshot(s) of your model.",
        allow_multiple=True,
        needs_openai=True,
        allow_csv=True,
        banner=(
            "Salesforce uses an **LLM-based transformation** from screenshots. "
            "The screenshot pipeline creates a GUI pivot model; data extraction is not available yet."
        ),
    ),
}


# --------------------------------------------------------------------------- #
# Target platforms
# --------------------------------------------------------------------------- #

_ORACLE_APEX_TUTORIAL = """\
### Importing into Oracle APEX

#### Stage 1: create the template APEX application

1. This hub has already performed the `mendix_to_structure.py` step for you:
   the downloaded pivot/domain model is the input used to create
   `tables_oracle_apex.sql`.
2. In your APEX workspace, open **SQL Workshop**, go to **SQL Scripts**, and
   import `tables_oracle_apex.sql`.
3. Select **Run Script**. When APEX asks whether it should create the
   application and its pages, select **Yes**.
4. Open the application that APEX created and export it using **Custom Export**
   with **Split into multiple files** enabled. Zip the exported folder.

#### Stage 2: generate and apply the GUI model

1. Return to this hub's artifacts step and upload the exported APEX ZIP. The
   hub accepts the `<export-name>/application/pages/...` layout and extracts
   the workspace/user metadata automatically.
2. Click **Generate GUI page SQL**. The hub runs the same page-generation logic
   as `migrator/converters/mendix_to_apex.py` using the stored domain and GUI
   pivot models.
3. Download the generated page SQL ZIP, return to **SQL Workshop > SQL
   Scripts**, import the generated SQL, and select **Run Script**.
4. When APEX prompts you to create the application and its pages, select
   **Yes**. This creates the final APEX application containing the migrated
   GUI. Verify the pages, regions, buttons, and navigation.

For screenshot-based sources, the interface first creates the GUI pivot model
with BESSER's `mockup_to_buml` pipeline. The same two-stage APEX workflow then
applies: create/export a template app, upload its split ZIP here, generate the
GUI page SQL, and run that SQL to create the final app.
"""

_POWERAPPS_TUTORIAL = """\
### Importing into Microsoft Power Apps

1. In Power Apps, create a new app **from Excel** (or add an Excel data source).
2. Upload the generated `model.xlsx`. Each sheet becomes a table; each column
   an attribute. Drop-down columns encode associations.
3. Because Power Apps *infers* the model from data, add at least one sample row
   (the file already includes example rows) so types and relations are detected.
4. Complete any many-to-many relations manually if Power Apps does not infer them.
"""

_SQL_DB_TUTORIAL = """\
### Importing into a SQL database

1. Open your database client (`psql`, `mysql`, DBeaver, …).
2. Run the generated `tables.sql` against a fresh schema.
3. Verify tables, foreign keys and constraints were created.
4. Point your low-code platform's "connect to existing database" wizard at the schema.
"""

TARGETS: dict[str, TargetPlatform] = {
    "oracle_apex": TargetPlatform(
        id="oracle_apex",
        label="Oracle APEX",
        implemented=True,
        supports_data=True,
        supports_gui=False,
        generator="oracle_apex",
        output_desc="Oracle-compatible DDL (tables, identity PKs, FKs, enum CHECKs).",
        tutorial=_ORACLE_APEX_TUTORIAL,
        note="GUI page SQL requires a split APEX export. Follow the GUI-model instructions in the import guide.",
    ),
    "powerapps": TargetPlatform(
        id="powerapps",
        label="Microsoft Power Apps (Excel import)",
        implemented=True,
        supports_data=True,
        supports_gui=False,
        generator="spreadsheet",
        output_desc="An Excel workbook (one sheet per class) that Power Apps can import as a data source.",
        tutorial=_POWERAPPS_TUTORIAL,
    ),
    "sql_postgres": TargetPlatform(
        id="sql_postgres",
        label="PostgreSQL database",
        implemented=True,
        supports_data=True,
        supports_gui=False,
        generator="sql",
        sql_dialect="postgresql",
        output_desc="A PostgreSQL DDL script (tables_postgresql.sql).",
        tutorial=_SQL_DB_TUTORIAL,
    ),
    "sql_mysql": TargetPlatform(
        id="sql_mysql",
        label="MySQL database",
        implemented=True,
        supports_data=True,
        supports_gui=False,
        generator="sql",
        sql_dialect="mysql",
        output_desc="A MySQL DDL script (tables_mysql.sql).",
        tutorial=_SQL_DB_TUTORIAL,
    ),
    "outsystems": TargetPlatform(
        id="outsystems",
        label="OutSystems",
        implemented=False,
        supports_data=True,
        supports_gui=False,
        output_desc="Coming soon.",
        note="No target generator wired yet.",
    ),
    "appian": TargetPlatform(
        id="appian",
        label="Appian",
        implemented=False,
        supports_data=True,
        supports_gui=False,
        output_desc="Coming soon.",
        note="No target generator wired yet.",
    ),
}


def get_source(platform_id: str) -> Optional[SourcePlatform]:
    return SOURCES.get(platform_id)


def get_target(platform_id: str) -> Optional[TargetPlatform]:
    return TARGETS.get(platform_id)


def sources_public() -> list[dict]:
    return [s.public() for s in SOURCES.values()]


def targets_public() -> list[dict]:
    return [t.public() for t in TARGETS.values()]
