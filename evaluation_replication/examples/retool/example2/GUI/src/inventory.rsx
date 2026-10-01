<Screen
  id="inventory"
  _customShortcuts={[]}
  _hashParams={[]}
  _order={0}
  _searchParams={[]}
  browserTitle=""
  title="Page 1"
  urlSlug=""
  uuid="3296af8d-2f96-4098-b0ba-ea22d11a3231"
>
  <SqlQueryUnified
    id="getInventory"
    query={include("../lib/getInventory.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    warningCodes={[]}
  />
  <SqlQueryUnified
    id="getInventoryPaginated"
    notificationDuration={4.5}
    query={include("../lib/getInventoryPaginated.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    showSuccessToaster={false}
    showUpdateSetValueDynamicallyToggle={false}
    updateSetValueDynamically={true}
    warningCodes={[]}
  />
  <SqlQueryUnified
    id="getTableSize"
    query={include("../lib/getTableSize.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    warningCodes={[]}
  />
  <SqlQueryUnified
    id="getVendorInventory"
    query={include("../lib/getVendorInventory.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    warningCodes={[]}
  />
  <Frame
    id="$main"
    enableFullBleed={false}
    isHiddenOnDesktop={false}
    isHiddenOnMobile={false}
    padding="8px 12px"
    type="main"
  >
    <Container
      id="tabbedContainer1"
      currentViewKey="{{ self.viewKeys[0] }}"
      footerPadding="4px 12px"
      headerPadding="4px 12px"
      padding="12px"
      showBody={true}
      showHeader={true}
    >
      <Header>
        <Tabs
          id="tabs1"
          itemMode="static"
          navigateContainer={true}
          targetContainerId="tabbedContainer1"
          value="{{ self.values[0] }}"
        >
          <Option id="dc484" value="Tab 1" />
          <Option id="de548" value="Tab 2" />
          <Option id="6cac9" value="Tab 3" />
        </Tabs>
      </Header>
      <View id="d3404" label="Local" viewKey="local">
        <Table
          id="inventoryTable"
          cellSelection="none"
          clearChangesetOnSave={true}
          data="{{ getInventoryPaginated.data }}"
          defaultSelectedRow={{ mode: "index", indexType: "display", index: 0 }}
          emptyMessage="No rows found"
          enableSaveActions={true}
          groupByColumns={{}}
          limitOffsetRowCount="{{ getTableSize.data.count[0] }}"
          overflowType="pagination"
          primaryKeyColumnId="d4a8f"
          rowHeight="small"
          serverPaginated={true}
          showBorder={true}
          showFooter={true}
          showHeader={true}
          templatePageSize="5"
          toolbarPosition="bottom"
        >
          <Column
            id="d4a8f"
            alignment="right"
            editableOptions={{ showStepper: true }}
            format="decimal"
            formatOptions={{ showSeparators: true, notation: "standard" }}
            groupAggregationMode="sum"
            key="id"
            label="ID"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="81df0"
            alignment="left"
            format="string"
            groupAggregationMode="none"
            key="sku"
            label="SKU"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="c90d7"
            alignment="left"
            format="string"
            groupAggregationMode="none"
            key="description"
            label="Description"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="d4cd3"
            alignment="right"
            editableOptions={{ showStepper: true }}
            format="decimal"
            formatOptions={{ showSeparators: true, notation: "standard" }}
            groupAggregationMode="sum"
            key="quantity"
            label="Quantity"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="910c9"
            alignment="right"
            editableOptions={{ showStepper: true }}
            format="decimal"
            formatOptions={{ showSeparators: true, notation: "standard" }}
            groupAggregationMode="sum"
            key="replenish"
            label="Replenish"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="8989e"
            alignment="left"
            format="tag"
            formatOptions={{ automaticColors: true }}
            groupAggregationMode="none"
            key="location"
            label="Location"
            placeholder="Select option"
            position="center"
            size={100}
            summaryAggregationMode="none"
            valueOverride="{{ _.startCase(item) }}"
          />
          <Column
            id="e3223"
            alignment="right"
            editableOptions={{ showStepper: true }}
            format="decimal"
            formatOptions={{ showSeparators: true, notation: "standard" }}
            groupAggregationMode="sum"
            key="latitude"
            label="Latitude"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="8a1bb"
            alignment="right"
            editableOptions={{ showStepper: true }}
            format="decimal"
            formatOptions={{ showSeparators: true, notation: "standard" }}
            groupAggregationMode="sum"
            key="longitude"
            label="Longitude"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <Column
            id="e9839"
            alignment="left"
            format="string"
            groupAggregationMode="none"
            key="image_url"
            label="Image URL"
            placeholder="Enter value"
            position="center"
            size={100}
            summaryAggregationMode="none"
          />
          <ToolbarButton
            id="1a"
            icon="bold/interface-text-formatting-filter-2"
            label="Filter"
            type="filter"
          />
          <ToolbarButton
            id="3c"
            icon="bold/interface-download-button-2"
            label="Download"
            type="custom"
          >
            <Event
              event="clickToolbar"
              method="exportData"
              pluginId="inventoryTable"
              type="widget"
              waitMs="0"
              waitType="debounce"
            />
          </ToolbarButton>
          <ToolbarButton
            id="4d"
            icon="bold/interface-arrows-round-left"
            label="Refresh"
            type="custom"
          >
            <Event
              event="clickToolbar"
              method="refresh"
              pluginId="inventoryTable"
              type="widget"
              waitMs="0"
              waitType="debounce"
            />
          </ToolbarButton>
        </Table>
      </View>
      <View id="1cb58" label="Vendor" viewKey="vendor">
        <Chart
          id="localInventoryChart"
          barGap={0.4}
          barMode="group"
          legendPosition="none"
          selectedPoints="[]"
          stackedBarTotalsDataLabelPosition="none"
          title={null}
          xAxisRangeMax=""
          xAxisRangeMin=""
          xAxisShowTickLabels={true}
          xAxisTickFormatMode="gui"
          xAxisTitle="Part name"
          xAxisTitleStandoff={20}
          yAxis2LineWidth={1}
          yAxis2RangeMax=""
          yAxis2RangeMin=""
          yAxis2ShowTickLabels={true}
          yAxis2TickFormatMode="gui"
          yAxis2TitleStandoff={20}
          yAxisGrid={true}
          yAxisRangeMax=""
          yAxisRangeMin=""
          yAxisShowLine={true}
          yAxisShowTickLabels={true}
          yAxisTickFormatMode="gui"
          yAxisTitle="Quantity"
          yAxisTitleStandoff={20}
          yAxisZeroLine={true}
        >
          <Series
            id="0"
            aggregationType="none"
            colorArray={{ array: [] }}
            colorArrayDropDown={{ array: [] }}
            colorInputMode="gradientColorArray"
            connectorLineColor="#000000"
            dataLabelPosition="none"
            datasource="{{ getInventory.data }}"
            datasourceMode="manual"
            decreasingBorderColor="#000000"
            decreasingColor="#000000"
            filteredGroups={null}
            filteredGroupsMode="source"
            gradientColorArray={{ array: [] }}
            groupBy={{ array: [] }}
            groupByDropdownType="manual"
            groupByStyles={{}}
            hidden={false}
            hiddenMode="manual"
            hoverTemplateArray={{ array: [] }}
            hoverTemplateMode="manual"
            increasingBorderColor="#000000"
            increasingColor="#000000"
            lineColor="#000000"
            lineDash="solid"
            lineShape="linear"
            lineUnderFillMode="none"
            lineWidth={2}
            markerBorderColor="#ffffff"
            markerBorderWidth={1}
            markerColor="{{ theme.primary }}"
            markerSize={6}
            markerSymbol="circle"
            name="Local Inventory Data"
            showMarkers={false}
            textTemplateMode="manual"
            type="bar"
            waterfallBase={0}
            waterfallMeasures={{ array: [] }}
            waterfallMeasuresMode="source"
            xData="{{ getInventory.data.sku }}"
            xDataMode="source"
            yAxis="y"
            yData="{{ getInventory.data.quantity }}"
            yDataMode="source"
            zData="[1, 2, 3, 4, 5]"
            zDataMode="manual"
          />
        </Chart>
        <Chart
          id="vendorInventoryChart"
          barGap={0.4}
          legendPosition="none"
          selectedPoints="[]"
          stackedBarTotalsDataLabelPosition="none"
          title={null}
          xAxisGrid={true}
          xAxisRangeMax=""
          xAxisRangeMin=""
          xAxisShowLine={true}
          xAxisShowTickLabels={true}
          xAxisTickFormatMode="gui"
          xAxisTitle="Part name"
          xAxisTitleStandoff={20}
          xAxisZeroLine={true}
          yAxis2LineWidth={1}
          yAxis2RangeMax=""
          yAxis2RangeMin=""
          yAxis2ShowTickLabels={true}
          yAxis2TickFormatMode="gui"
          yAxis2TitleStandoff={20}
          yAxisGrid={true}
          yAxisRangeMax=""
          yAxisRangeMin=""
          yAxisShowLine={true}
          yAxisShowTickLabels={true}
          yAxisTickFormatMode="gui"
          yAxisTitle="Quantity"
          yAxisTitleStandoff={20}
          yAxisZeroLine={true}
        >
          <Series
            id="0"
            aggregationType="none"
            colorArray={{ array: [] }}
            colorArrayDropDown={{ array: [] }}
            colorInputMode="gradientColorArray"
            connectorLineColor="#000000"
            dataLabelPosition="none"
            datasource="{{ getVendorInventory.data }}"
            datasourceMode="manual"
            decreasingBorderColor="#000000"
            decreasingColor="#000000"
            filteredGroups={null}
            filteredGroupsMode="source"
            gradientColorArray={{ array: [] }}
            groupBy={{ array: ["vendor_name"] }}
            groupByDropdownType="source"
            groupByStyles={{}}
            hidden={false}
            hiddenMode="manual"
            hoverTemplateArray={{ array: [] }}
            hoverTemplateMode="manual"
            increasingBorderColor="#000000"
            increasingColor="#000000"
            lineColor="#000000"
            lineDash="solid"
            lineShape="linear"
            lineUnderFillMode="none"
            lineWidth={2}
            markerBorderColor="#ffffff"
            markerBorderWidth={1}
            markerColor="#000000"
            markerSize={6}
            markerSymbol="circle"
            name="Vendor Inventory Data"
            showMarkers={false}
            textTemplateMode="manual"
            type="bar"
            waterfallBase={0}
            waterfallMeasures={{ array: [] }}
            waterfallMeasuresMode="source"
            xData="{{ getVendorInventory.data.sku }}"
            xDataMode="source"
            yAxis="y"
            yData="{{ getVendorInventory.data.available_quantity }}"
            yDataMode="source"
            zData="[1, 2, 3, 4, 5]"
            zDataMode="manual"
          />
        </Chart>
      </View>
    </Container>
  </Frame>
</Screen>
