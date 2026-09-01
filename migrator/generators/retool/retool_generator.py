"""
Retool Generator for BESSER B-UML domain models.

Generates:
  1. One CSV file per entity  → <output_dir>/csv/<table_name>.csv
  2. One Retool app JSON      → <output_dir>/json/<app_name>_retool_app.json

The JSON uses Retool's Transit-JSON app-state format (Cognitect Transit,
no cache optimisation — valid, importable, but larger than a cached export).
"""

import csv
import io
import json
import os
import re
import uuid as _uuid_mod
import random
from besser.BUML.metamodel.structural import DomainModel, Class, Enumeration
from besser.generators.structural_utils import get_foreign_keys


# ─── naming helpers ───────────────────────────────────────────────

def _camel_to_snake(name: str) -> str:
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def _short_id(seed: str) -> str:
    """5-char deterministic hex column ID."""
    rng = random.Random(seed)
    return ''.join(rng.choices('0123456789abcdef', k=5))


# ─── type mappings ────────────────────────────────────────────────

BUML_TO_RETOOL_FORMAT = {
    'int':       'decimal',
    'float':     'decimal',
    'bool':      'decimal',
    'str':       'string',
    'date':      'string',
    'datetime':  'string',
    'time':      'string',
    'timedelta': 'decimal',
    'any':       'string',
}

FIXED_TS = 1785912924434  # stable ms timestamp for generated artefacts


# ─── Minimal Transit-JSON encoder (no caching) ───────────────────
# Reference: https://github.com/cognitect/transit-format
# iR = immutable record, iOM = ordered map, iM = map, iL = list

def _tmap(kvs: list) -> list:
    """Transit standard map: ["^ ", k1, v1, k2, v2, ...]"""
    r = ["^ "]
    for k, v in kvs:
        r.append(k)
        r.append(v)
    return r


def _trec(name: str, val) -> list:
    """Transit iR record with fields n=<name>, v=<val>."""
    return ["~#iR", _tmap([("n", name), ("v", val)])]


def _tom(pairs: list) -> list:
    """Transit ordered map: ["~#iOM", [k1, v1, k2, v2, ...]]"""
    flat = []
    for k, v in pairs:
        flat.append(k)
        flat.append(v)
    return ["~#iOM", flat]


def _tim(kvs: list) -> list:
    """Transit iM map: ["~#iM", [k1, v1, ...]]"""
    flat = []
    for k, v in kvs:
        flat.append(k)
        flat.append(v)
    return ["~#iM", flat]


def _til(items: list) -> list:
    return ["~#iL", items]


def _ts(ms: int = FIXED_TS) -> str:
    return f"~m{ms}"


# ─── Plugin builders ──────────────────────────────────────────────

def _screen_plugin(screen_id: str, title: str, order: int, ts: int) -> tuple:
    template = _tim([
        ("title", title),
        ("browserTitle", ""),
        ("urlSlug", ""),
        ("_order", order),
        ("_searchParams", []),
        ("_hashParams", []),
        ("_customShortcuts", []),
    ])
    plugin = _tmap([
        ("id", screen_id),
        ("uuid", str(_uuid_mod.uuid4())),
        ("_comment", None),
        ("type", "screen"),
        ("subtype", "Screen"),
        ("namespace", None),
        ("resourceName", None),
        ("resourceDisplayName", None),
        ("template", template),
        ("style", None),
        ("position2", None),
        ("mobilePosition2", None),
        ("mobileAppPosition", None),
        ("tabIndex", None),
        ("container", ""),
        ("createdAt", _ts(ts)),
        ("updatedAt", _ts(ts)),
        ("folder", ""),
        ("presetName", None),
        ("screen", None),
        ("boxId", None),
        ("subBoxIds", None),
    ])
    return screen_id, _trec("pluginTemplate", plugin)


def _main_frame_plugin(frame_id: str, screen_id: str, ts: int) -> tuple:
    plugin = _tmap([
        ("id", frame_id),
        ("uuid", None),
        ("_comment", None),
        ("type", "frame"),
        ("subtype", "Frame"),
        ("namespace", None),
        ("resourceName", None),
        ("resourceDisplayName", None),
        ("template", _tim([
            ("type", "main"),
            ("padding", "8px 12px"),
            ("enableFullBleed", False),
            ("isHiddenOnDesktop", False),
            ("isHiddenOnMobile", False),
        ])),
        ("style", []),
        ("position2", None),
        ("mobilePosition2", None),
        ("mobileAppPosition", None),
        ("tabIndex", None),
        ("container", ""),
        ("createdAt", _ts(ts)),
        ("updatedAt", _ts(ts)),
        ("folder", ""),
        ("presetName", None),
        ("screen", screen_id),
        ("boxId", None),
        ("subBoxIds", None),
    ])
    return frame_id, _trec("pluginTemplate", plugin)


def _table_plugin(table_id: str, screen_id: str, query_id: str,
                  columns: list, ts: int) -> tuple:
    """columns: [(col_name, retool_format), ...]"""
    col_ids = [_short_id(f"{table_id}_{c}") for c, _ in columns]

    def cmap(val=""):
        return _tim([(cid, val) for cid in col_ids])

    def cmap_fmt():
        return _tim([(cid, fmt) for cid, (_, fmt) in zip(col_ids, columns)])

    def cmap_key():
        return _tim([(cid, name) for cid, (name, _) in zip(col_ids, columns)])

    def cmap_label():
        return _tim([(cid, name.replace('_', ' ').title())
                     for cid, (name, _) in zip(col_ids, columns)])

    def cmap_align():
        return _tim([(cid, "right" if fmt == "decimal" else "left")
                     for cid, (_, fmt) in zip(col_ids, columns)])

    def cmap_fmt_opts():
        items = []
        for cid, (_, fmt) in zip(col_ids, columns):
            if fmt == "decimal":
                items.append((cid, _tim([("showSeparators", True), ("notation", "standard")])))
            else:
                items.append((cid, _tim([])))
        return _tim(items)

    def cmap_agg():
        return _tim([(cid, "sum" if fmt == "decimal" else "none")
                     for cid, (_, fmt) in zip(col_ids, columns)])

    def cmap_edit():
        items = []
        for cid, (_, fmt) in zip(col_ids, columns):
            if fmt == "decimal":
                items.append((cid, _tim([("showStepper", True)])))
            else:
                items.append((cid, _tim([("spellCheck", False)])))
        return _tim(items)

    position = _trec("position2", _tmap([
        ("type", "grid"),
        ("container", ""),
        ("rowGroup", "body"),
        ("subcontainer", ""),
        ("row", 3.0),
        ("col", 0),
        ("height", 10),
        ("width", 12),
        ("tabNum", 0),
        ("stackPosition", None),
    ]))

    template = _tim([
        ("selectedRowKey", None),
        ("_nextAfterCursor", ""),
        ("_columnBackgroundColor", cmap("")),
        ("_defaultSort", None),
        ("_columnSearchMode", cmap("default")),
        ("_columnAlternateRowBackgroundColor", cmap("")),
        ("_clearChangesetOnSave", True),
        ("heightType", "fixed"),
        ("_columnTextColor", cmap("")),
        ("disableEdits", False),
        ("autoColumnWidth", False),
        ("_rowHeight", "medium"),
        ("_columnIds", col_ids),
        ("_isSaving", False),
        ("_headerTextWrap", False),
        ("_actionIds", []),
        ("_clearChangeset", False),
        ("caseSensitiveFiltering", False),
        ("_limitOffsetRowCount", None),
        ("selectedSourceRow", None),
        ("_dynamicColumnsEnabled", False),
        ("disableSave", False),
        ("_columnEditableOptions", cmap_edit()),
        ("_toolbarPosition", "bottom"),
        ("_groupByColumns", []),
        ("_toolbarButtonLabel", _tim([("1a", "Filter"), ("3c", "Download"), ("4d", "Refresh")])),
        ("_nextBeforeCursor", ""),
        ("_persistRowSelection", False),
        ("_toolbarButtonIcon", _tim([
            ("1a", "bold/interface-text-formatting-filter-2"),
            ("3c", "bold/interface-download-button-2"),
            ("4d", "bold/interface-arrows-round-left"),
        ])),
        ("changesetArray", []),
        ("groupByColumns", []),
        ("_toolbarButtonType", _tim([("1a", "filter"), ("3c", "custom"), ("4d", "custom")])),
        ("_columnOptionList", cmap(_tim([]))),
        ("_columnValueOverride", cmap("")),
        ("_showBorder", True),
        ("_templatePageSize", None),
        ("_dynamicColumnProperties", _tim([])),
        ("_showHeader", True),
        ("_currentPage", 0),
        ("overflowActionsOverlayMinWidth", None),
        ("_actionsOverflowPosition", 0),
        ("_columnKey", cmap_key()),
        ("hidden", False),
        ("_toolbarButtonIds", ["1a", "3c", "4d"]),
        ("columnOrdering", []),
        ("data", f"{{{{ {query_id}.data }}}}"),
        ("_cellSelection", "none"),
        ("_serverPaginated", False),
        ("_linkedFilterId", None),
        ("searchMode", "fuzzy"),
        ("_columnCellTooltip", cmap("")),
        ("_columnFormat", cmap_fmt()),
        ("_cursorCache", _tmap([])),
        ("_calculatedPageSize", None),
        ("_primaryKeyColumnId", col_ids[0] if col_ids else ""),
        ("selectedDataIndex", None),
        ("_columnAlignment", cmap_align()),
        ("_actionIcon", _tim([])),
        ("margin", "4px 8px"),
        ("_columnTooltip", cmap("")),
        ("_columnIcon", cmap("")),
        ("_alwaysShowRowSelectionCheckboxes", False),
        ("_columnCellTooltipMode", cmap("")),
        ("_pageSize", None),
        ("showInEditor", False),
        ("_isAddingNewRows", False),
        ("selectedSourceRows", []),
        ("_enableExpandableRows", False),
        ("_selectMultipleRowsOnActionClick", "no"),
        ("_columnSortDisabled", cmap(False)),
        ("_showSummaryRow", False),
        ("filterStack", None),
        ("_expandedRows", None),
        ("changesetObject", None),
        ("_actionDisabled", _tim([])),
        ("_columnReferenceId", cmap("")),
        ("_dynamicColumnSource", []),
        ("_rowSelection", "single"),
        ("_columnCaption", cmap("")),
        ("_dynamicColumnFormatOptions", _tim([])),
        ("_dynamicRowHeights", False),
        ("_columnFormatOptions", cmap_fmt_opts()),
        ("_changeset", None),
        ("_afterCursor", ""),
        ("_columnHeaderBackgroundColor", cmap("")),
        ("selectedRowKeys", []),
        ("_columnHeaderTextColor", cmap("")),
        ("_beforeCursor", ""),
        ("_columnSummaryAggregationMode", cmap("none")),
        ("searchTerm", ""),
        ("selectedRows", []),
        ("_disabledVirtualization", False),
        ("_expandedRowDataIndexes", []),
        ("_showColumnBorders", False),
        ("_columnStatusIndicatorOptions", cmap(_tim([]))),
        ("overflowActionsOverlayMaxHeight", None),
        ("_columnSize", cmap(100)),
        ("_serverPaginationType", "limitOffsetBased"),
        ("_columnSortMode", cmap("default")),
        ("_selectSingleRowsOnActionClick", "replace"),
        ("_showFooter", True),
        ("_groupedColumnConfig", _tim([])),
        ("_dynamicColumnSize", _tim([])),
        ("_virtualizeStartIndex", 0),
        ("_toolbarButtonHidden", _tim([("1a", ""), ("3c", ""), ("4d", "")])),
        ("_defaultFilters", _tim([])),
        ("events", []),
        ("_columnEditable", cmap("")),
        ("newRows", []),
        ("_rowBackgroundColor", []),
        ("emptyMessage", "No rows found"),
        ("pagination", None),
        ("selectedDataIndexes", []),
        ("_columnEditableInNewRows", cmap("")),
        ("_columnGroupAggregationMode", cmap_agg()),
        ("sortArray", []),
        ("_selectedCell", None),
        ("overflowType", "scroll"),
        ("selectedCell", None),
        ("_defaultSelectedRow", _tim([("mode", "index"), ("indexType", "display"), ("index", 0)])),
        ("_hasNextPage", False),
        ("_includeRowInChangesetArray", False),
        ("_columnPosition", cmap("center")),
        ("_enableSaveActions", True),
        ("_columnPlaceholder", cmap("Enter value")),
        ("_defaultFilterOperator", "and"),
        ("_actionLabel", _tim([])),
        ("_virtualizeEndIndex", 0),
        ("selectedRow", None),
        ("_actionHidden", _tim([])),
        ("maintainSpaceWhenHidden", False),
        ("_columnHidden", cmap("")),
        ("_columnLabel", cmap_label()),
        ("_showToolbar", True),
    ])

    plugin = _tmap([
        ("id", table_id),
        ("uuid", str(_uuid_mod.uuid4())),
        ("_comment", None),
        ("type", "widget"),
        ("subtype", "TableWidget2"),
        ("namespace", None),
        ("resourceName", None),
        ("resourceDisplayName", None),
        ("template", template),
        ("style", None),
        ("position2", position),
        ("mobilePosition2", None),
        ("mobileAppPosition", None),
        ("tabIndex", None),
        ("container", ""),
        ("createdAt", _ts(ts)),
        ("updatedAt", _ts(ts)),
        ("folder", ""),
        ("presetName", None),
        ("screen", screen_id),
        ("boxId", None),
        ("subBoxIds", None),
    ])
    return table_id, _trec("pluginTemplate", plugin)


def _query_plugin(query_id: str, screen_id: str, sql: str, ts: int) -> tuple:
    template = _tim([
        ("queryRefreshTime", ""),
        ("allowedGroupIds", []),
        ("streamResponse", False),
        ("records", ""),
        ("lastReceivedFromResourceAt", None),
        ("isFunction", False),
        ("databasePasswordOverride", ""),
        ("queryDisabledMessage", ""),
        ("servedFromCache", False),
        ("successMessage", ""),
        ("queryDisabled", ""),
        ("playgroundQuerySaveId", "latest"),
        ("resourceNameOverride", ""),
        ("runWhenModelUpdates", True),
        ("workflowRunExecutionType", "sync"),
        ("showFailureToaster", True),
        ("query", sql),
        ("error", None),
        ("privateParams", []),
        ("queryRunOnSelectorUpdate", False),
        ("runWhenPageLoadsDelay", ""),
        ("warningCodes", []),
        ("data", None),
        ("recordId", ""),
        ("importedQueryInputs", _tim([])),
        ("_additionalScope", []),
        ("isImported", False),
        ("showSuccessToaster", True),
        ("dataArray", []),
        ("cacheKeyTtl", ""),
        ("filterBy", ""),
        ("requestSentTimestamp", None),
        ("databaseHostOverride", ""),
        ("metadata", None),
        ("editorMode", "sql"),
        ("queryRunTime", None),
        ("actionType", ""),
        ("changesetObject", ""),
        ("shouldUseLegacySql", False),
        ("errorTransformer", "return data.error"),
        ("databaseNameOverride", ""),
        ("confirmationMessage", None),
        ("isFetching", False),
        ("changeset", ""),
        ("rawData", None),
        ("queryTriggerDelay", "0"),
        ("watchedParams", []),
        ("enableErrorTransformer", False),
        ("enableBulkUpdates", False),
        ("showLatestVersionUpdatedWarning", False),
        ("timestamp", 0),
        ("importedQueryDefaults", _tim([])),
        ("enableTransformer", False),
        ("overrideOrgCacheForUserCache", False),
        ("bulkUpdatePrimaryKey", ""),
        ("runWhenPageLoads", False),
        ("transformer", "return data"),
        ("tableName", ""),
        ("queryTimeout", "10000"),
        ("requireConfirmation", False),
        ("queryFailureConditions", ""),
        ("changesetIsObject", False),
        ("enableCaching", False),
        ("allowedGroups", []),
        ("databaseUsernameOverride", ""),
        ("shouldEnableBatchQuerying", False),
        ("doNotThrowOnNoOp", False),
        ("offlineQueryType", "None"),
        ("queryThrottleTime", "750"),
        ("updateSetValueDynamically", False),
        ("notificationDuration", ""),
    ])

    plugin = _tmap([
        ("id", query_id),
        ("uuid", None),
        ("_comment", None),
        ("type", "datasource"),
        ("subtype", "SqlQueryUnified"),
        ("namespace", None),
        ("resourceId", None),        # null so Retool prompts resource selection on import
        ("resourceName", "retool_db"),
        ("resourceDisplayName", None),
        ("template", template),
        ("style", None),
        ("position2", None),
        ("mobilePosition2", None),
        ("mobileAppPosition", None),
        ("tabIndex", None),
        ("container", ""),
        ("createdAt", _ts(ts)),
        ("updatedAt", _ts(ts)),
        ("folder", ""),
        ("presetName", None),
        ("screen", screen_id),
        ("boxId", None),
        ("subBoxIds", None),
    ])
    return query_id, _trec("pluginTemplate", plugin)


def _button_plugin(btn_id: str, screen_id: str, label: str, ts: int) -> tuple:
    position = _trec("position2", _tmap([
        ("type", "grid"),
        ("container", ""),
        ("rowGroup", "body"),
        ("subcontainer", ""),
        ("row", 1.5),
        ("col", 0),
        ("height", 1),
        ("width", 3),
        ("tabNum", 0),
        ("stackPosition", None),
    ]))

    template = _tim([
        ("heightType", "fixed"),
        ("horizontalAlign", "stretch"),
        ("clickable", False),
        ("iconAfter", ""),
        ("submitTargetId", None),
        ("hidden", False),
        ("ariaLabel", ""),
        ("text", label),
        ("margin", "4px 8px"),
        ("showInEditor", False),
        ("tooltipText", ""),
        ("allowWrap", True),
        ("styleVariant", "solid"),
        ("submit", False),
        ("iconBefore", ""),
        ("events", []),
        ("loading", False),
        ("loaderPosition", "auto"),
        ("disabled", False),
        ("maintainSpaceWhenHidden", False),
    ])

    plugin = _tmap([
        ("id", btn_id),
        ("uuid", str(_uuid_mod.uuid4())),
        ("_comment", None),
        ("type", "widget"),
        ("subtype", "ButtonWidget2"),
        ("namespace", None),
        ("resourceName", None),
        ("resourceDisplayName", None),
        ("template", template),
        ("style", None),
        ("position2", position),
        ("mobilePosition2", None),
        ("mobileAppPosition", None),
        ("tabIndex", None),
        ("container", ""),
        ("createdAt", _ts(ts)),
        ("updatedAt", _ts(ts)),
        ("folder", ""),
        ("presetName", None),
        ("screen", screen_id),
        ("boxId", None),
        ("subBoxIds", None),
    ])
    return btn_id, _trec("pluginTemplate", plugin)


# ─── App-state builder ────────────────────────────────────────────

def _build_app_state(entities_info: list, ts: int) -> str:
    """
    entities_info: [(entity_name, table_name, columns), ...]
      columns: [(col_name, retool_format), ...]
    Returns the Transit-encoded appState JSON string.
    """
    plugin_pairs = []
    first_screen_id = None

    for i, (entity_name, table_name, columns) in enumerate(entities_info):
        snake = _camel_to_snake(entity_name)
        screen_id = f"{snake}_page"
        frame_id  = f"{snake}_main"
        table_id  = f"{snake}_table"
        query_id  = f"{snake}_query"
        btn_id    = f"{snake}_add_button"

        if i == 0:
            first_screen_id = screen_id

        plugin_pairs.append(_screen_plugin(screen_id, entity_name, i, ts))
        plugin_pairs.append(_main_frame_plugin(frame_id, screen_id, ts))
        plugin_pairs.append(_table_plugin(table_id, screen_id, query_id, columns, ts))
        plugin_pairs.append(_query_plugin(
            query_id, screen_id,
            f"SELECT * FROM {table_name};",
            ts,
        ))
        plugin_pairs.append(_button_plugin(btn_id, screen_id, f"Add new {entity_name}", ts))

    app_template = _tmap([
        ("appMaxWidth", "1200px"),
        ("appStyles", ""),
        ("appTesting", None),
        ("appThemeId", None),
        ("appThemeModeId", None),
        ("appThemeName", None),
        ("createdAt", None),
        ("customComponentCollections", []),
        ("customDocumentTitle", ""),
        ("customDocumentTitleEnabled", False),
        ("customShortcuts", []),
        ("experimentalFeatures", _tmap([
            ("disableMultiplayerEditing", False),
            ("multiplayerEditingEnabled", False),
            ("sourceControlTemplateDehydration", False),
        ])),
        ("folders", _til([])),
        ("formAppSettings", _tmap([("customRedirectUrl", "")])),
        ("inAppRetoolPillAppearance", "NO_OVERRIDE"),
        ("instrumentationEnabled", False),
        ("internationalizationSettings", _tmap([
            ("internationalizationEnabled", False),
            ("internationalizationFiles", []),
        ])),
        ("isFetching", False),
        ("isFormApp", False),
        ("isGlobalWidget", False),
        ("isMobileApp", False),
        ("loadingIndicatorsDisabled", False),
        ("markdownLinkBehavior", "auto"),
        ("mobileAppSettings", _tmap([
            ("displaySetting", _tmap([("landscapeMode", False), ("tabletMode", False)])),
            ("mobileOfflineModeBannerMode", "default"),
            ("mobileOfflineModeDelaySync", False),
            ("mobileOfflineModeEnabled", False),
        ])),
        ("mobileOfflineAssets", []),
        ("multiScreenMobileApp", False),
        ("notificationsSettings", _tmap([
            ("globalQueryShowFailureToast", True),
            ("globalQueryShowSuccessToast", False),
            ("globalQueryToastDuration", 4.5),
            ("globalToastPosition", "bottomRight"),
        ])),
        ("pageCodeFolders", _tmap([])),
        ("pageLoadValueOverrides", []),
        ("persistUrlParams", False),
        ("plugins", _tom(plugin_pairs)),
        ("preloadedAppJavaScript", None),
        ("preloadedAppJSLinks", []),
        ("pubAppDecoupledQueriesDisabled", True),
        ("queryStatusVisibility", False),
        ("responsiveLayoutDisabled", False),
        ("rootScreen", first_screen_id or "page1"),
        ("savePlatform", "web"),
        ("shortlink", None),
        ("testEntities", []),
        ("tests", []),
        ("urlFragmentDefinitions", []),
        ("version", "4.36.0"),
        ("serializedLayout", None),
        ("agentEvals", _tmap([])),
    ])

    root = _trec("appTemplate", app_template)
    return json.dumps(root, ensure_ascii=False, separators=(',', ':'))


# ─── Domain-model introspection ───────────────────────────────────

def _collect_entities_info(model: DomainModel) -> list:
    """
    Returns [(entity_name, table_name, columns), ...]
    columns: [(col_name, retool_format), ...]  — includes id + attrs + FK cols
    """
    fkeys = get_foreign_keys(model)   # {assoc_name: [class_with_fk, ref_prop_name]}

    # Build FK column map per class
    fk_map: dict = {}
    for assoc in model.associations:
        ends = list(assoc.ends)
        if len(ends) != 2:
            continue
        e0, e1 = ends[0], ends[1]
        max0, max1 = e0.multiplicity.max, e1.multiplicity.max
        if max0 > 1 and max1 > 1:
            continue   # N:M handled via junction tables (omitted from single-entity CSV)
        if assoc.name not in fkeys:
            continue
        class_with_fk, ref_prop_name = fkeys[assoc.name]
        fk_col = _camel_to_snake(ref_prop_name) + '_id'
        fk_map.setdefault(class_with_fk, []).append(fk_col)

    result = []
    try:
        classes = list(model.classes_sorted_by_inheritance())
    except Exception:
        classes = list(model.classes)

    for cls in classes:
        table_name = _camel_to_snake(cls.name)
        columns: list = [("id", "decimal")]

        for attr in sorted(cls.attributes, key=lambda a: a.name):
            col_name = _camel_to_snake(attr.name)
            type_name = getattr(attr.type, 'name', 'str')
            if isinstance(attr.type, Enumeration):
                fmt = 'string'
            else:
                fmt = BUML_TO_RETOOL_FORMAT.get(type_name, 'string')
            columns.append((col_name, fmt))

        for fk_col in fk_map.get(cls.name, []):
            columns.append((fk_col, 'decimal'))

        result.append((cls.name, table_name, columns))

    return result


# ─── Public generator class ───────────────────────────────────────

class RetoolGenerator:
    """
    Generates ReTool-importable artefacts from a BESSER B-UML DomainModel.

    Args:
        model (DomainModel): The B-UML domain model.
        app_name (str): Name used for the JSON filename.
        output_dir (str): Root output directory.
            CSV files → <output_dir>/csv/<table>.csv
            App JSON  → <output_dir>/json/<app_name>_retool_app.json
        resource_id (str): UUID of the 'retool_db' resource in ReTool.
            Defaults to a stable placeholder UUID.
    """

    _DEFAULT_RESOURCE_ID = "2a86a318-80a0-4803-95d8-409396e41af2"

    def __init__(self, model: DomainModel,
                 app_name: str = "app",
                 output_dir: str = None,
                 resource_id: str = None):
        self.model = model
        self.app_name = app_name
        self.output_dir = output_dir or os.path.join(os.getcwd(), "retool_output")
        self.resource_id = resource_id or self._DEFAULT_RESOURCE_ID

    # ── CSV generation ────────────────────────────────────────────

    def generate_csv(self) -> list:
        """Write one CSV per entity; return list of written file paths."""
        csv_dir = os.path.join(self.output_dir, "csv")
        os.makedirs(csv_dir, exist_ok=True)

        entities_info = _collect_entities_info(self.model)
        written = []

        for entity_name, table_name, columns in entities_info:
            file_path = os.path.join(csv_dir, f"{table_name}.csv")
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Header row
                writer.writerow([col for col, _ in columns])
                # One sample row with type-appropriate placeholder values
                sample = []
                for col, fmt in columns:
                    if col == "id":
                        sample.append("1")
                    elif fmt == "decimal":
                        sample.append("0")
                    elif "date" in col or "time" in col:
                        sample.append("2024-01-01")
                    else:
                        sample.append(f"sample_{col}")
                writer.writerow(sample)
            written.append(file_path)
            print(f"  CSV: {file_path}")

        return written

    # ── JSON generation ───────────────────────────────────────────

    def generate_json(self) -> str:
        """Write the ReTool app JSON; return file path."""
        json_dir = os.path.join(self.output_dir, "json")
        os.makedirs(json_dir, exist_ok=True)

        entities_info = _collect_entities_info(self.model)
        app_state_str = _build_app_state(entities_info, FIXED_TS)

        app_json = {
            "uuid": str(_uuid_mod.uuid4()),
            "page": {
                "id": random.randint(100_000_000, 999_999_999),
                "data": {
                    "appState": app_state_str
                },
                "changesRecord": [],
                "changesRecordV2": [],
                "checksum": None,
                "multiplayerSessionId": str(_uuid_mod.uuid4()),
                "appTestingSaveId": None,
                "subflows": None,
                "isCopilotGenerated": False,
                "createdAt": "2026-08-05T00:00:00.000Z",
                "updatedAt": "2026-08-05T00:00:00.000Z",
                "pageId": random.randint(1_000_000, 9_999_999),
                "userId": 0
            },
            "modules": {}
        }

        file_name = f"{self.app_name}_retool_app.json"
        file_path = os.path.join(json_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(app_json, f, ensure_ascii=False, indent=2)
        print(f"  JSON: {file_path}")
        return file_path

    # ── Combined ──────────────────────────────────────────────────

    def generate(self):
        """Generate both CSV files and the ReTool app JSON."""
        print(f"\n[RetoolGenerator] Generating for '{self.app_name}'")
        csv_files = self.generate_csv()
        json_file = self.generate_json()
        print(f"[RetoolGenerator] Done — {len(csv_files)} CSV(s), 1 JSON")
        return csv_files, json_file
