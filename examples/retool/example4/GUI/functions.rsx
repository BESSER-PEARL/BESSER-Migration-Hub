<GlobalFunctions>
  <SqlQueryUnified
    id="fetchSalesData"
    isMultiplayerEdited={false}
    query={include("./lib/fetchSalesData.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    resourceTypeOverride=""
    warningCodes={[]}
  />
  <SqlQueryUnified
    id="fetchCategoryData"
    query={include("./lib/fetchCategoryData.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    resourceTypeOverride=""
    warningCodes={[]}
  />
  <SqlQueryUnified
    id="query1"
    notificationDuration={4.5}
    query={include("./lib/query1.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    showUpdateSetValueDynamicallyToggle={false}
    updateSetValueDynamically={true}
    warningCodes={[]}
  />
</GlobalFunctions>
