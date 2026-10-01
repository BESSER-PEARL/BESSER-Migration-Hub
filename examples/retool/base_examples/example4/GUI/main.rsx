<App>
  <Include src="./functions.rsx" />
  <Include src="./src/setupGuideModal.rsx" />
  <Frame
    id="$main"
    isHiddenOnDesktop={false}
    isHiddenOnMobile={false}
    padding="8px 12px"
    paddingType="normal"
    sticky={false}
    type="main"
  >
    <Text
      id="pageTitle"
      marginType="normal"
      value="### Sales Dashboard"
      verticalAlign="center"
    />
    <Button id="setupGuideBtn" marginType="normal" text="Setup Guide">
      <Event
        id="fa1b2c3d"
        event="click"
        method="show"
        params={{}}
        pluginId="setupGuideModal"
        type="widget"
        waitMs="0"
        waitType="debounce"
      />
    </Button>
    <Statistic
      id="statRevenue"
      label="Total Revenue"
      marginType="normal"
      prefix="$"
      value="{{ Array.isArray(fetchSalesData.data) ? fetchSalesData.data.reduce((sum, r) => sum + r.revenue, 0).toLocaleString() : '124,500' }}"
    />
    <Statistic
      id="statOrders"
      label="Total Orders"
      marginType="normal"
      value="{{ Array.isArray(fetchSalesData.data) ? fetchSalesData.data.reduce((sum, r) => sum + r.orders, 0).toLocaleString() : '1,847' }}"
    />
    <Statistic
      id="statConversion"
      label="Avg Conversion"
      marginType="normal"
      suffix="%"
      value="{{ Array.isArray(fetchSalesData.data) ? (fetchSalesData.data.reduce((sum, r) => sum + r.conversion, 0) / fetchSalesData.data.length).toFixed(1) : '3.2' }}"
    />
    <Text
      id="revenueChartTitle"
      marginType="normal"
      value="#### Monthly Revenue"
      verticalAlign="center"
    />
    <PlotlyChart
      id="revenueChart"
      chartType="line"
      data={include("./lib/revenueChart.data.json", "string")}
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "month" },
                {
                  datasource:
                    "{{formatDataAsObject(fetchSalesData.data)['month']}}",
                },
                { chartType: "line" },
                { aggregationType: "sum" },
                { color: "#033663" },
                { colors: { ordered: [] } },
                { visible: false },
                { hovertemplate: "%{x} — %{fullData.name}: %{y}" },
              ],
            },
          },
          {
            1: {
              ordered: [
                { label: "revenue" },
                {
                  datasource:
                    "{{formatDataAsObject(fetchSalesData.data)['revenue']}}",
                },
                { chartType: "line" },
                { aggregationType: "sum" },
                { color: "#247BC7" },
                { colors: { ordered: [] } },
                { visible: true },
                { hovertemplate: "%{x} — Revenue: $%{y:,.0f}" },
              ],
            },
          },
        ],
      }}
      datasourceDataType="array"
      datasourceInputMode="javascript"
      datasourceJS="{{fetchSalesData.data}}"
      isJsonTemplateDirty={true}
      isLayoutJsonDirty={true}
      layout={include("./lib/revenueChart.layout.json", "string")}
      xAxis="{{formatDataAsObject(fetchSalesData.data)['month']}}"
      xAxisDropdown="month"
    />
    <Text
      id="categoryChartTitle"
      marginType="normal"
      value="#### Revenue by Category"
      verticalAlign="center"
    />
    <PlotlyChart
      id="categoryChart"
      data={include("./lib/categoryChart.data.json", "string")}
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "category" },
                {
                  datasource:
                    "{{formatDataAsObject(fetchCategoryData.data)['category']}}",
                },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#033663" },
                { colors: { ordered: [] } },
                { visible: false },
                { hovertemplate: "%{x} — %{fullData.name}: %{y}" },
              ],
            },
          },
          {
            1: {
              ordered: [
                { label: "revenue" },
                {
                  datasource:
                    "{{formatDataAsObject(fetchCategoryData.data)['revenue']}}",
                },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#247BC7" },
                { colors: { ordered: [] } },
                { visible: true },
                { hovertemplate: "%{x} — Revenue: $%{y:,.0f}" },
              ],
            },
          },
          {
            2: {
              ordered: [
                { label: "orders" },
                {
                  datasource:
                    "{{formatDataAsObject(fetchCategoryData.data)['orders']}}",
                },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#55A1E3" },
                { colors: { ordered: [] } },
                { visible: true },
                { hovertemplate: "%{x} — Orders: %{y}" },
              ],
            },
          },
        ],
      }}
      datasourceDataType="array"
      datasourceInputMode="javascript"
      datasourceJS="{{fetchCategoryData.data}}"
      isJsonTemplateDirty={true}
      isLayoutJsonDirty={true}
      layout={include("./lib/categoryChart.layout.json", "string")}
      xAxis="{{formatDataAsObject(fetchCategoryData.data)['category']}}"
      xAxisDropdown="category"
    />
    <Text
      id="dataTableTitle"
      marginType="normal"
      value="#### Raw Data"
      verticalAlign="center"
    />
    <Table
      id="salesTable"
      cellSelection="none"
      data="{{ Array.isArray(fetchSalesData.data) ? fetchSalesData.data : [{ month: 'Jan', revenue: 8500, orders: 120, conversion: 2.8 }, { month: 'Feb', revenue: 9200, orders: 135, conversion: 3.1 }, { month: 'Mar', revenue: 11800, orders: 167, conversion: 3.5 }] }}"
      defaultSelectedRow={{ mode: "index", indexType: "display", index: 0 }}
      primaryKeyColumnId="c1a1a"
      showBorder={true}
      showFooter={true}
      showHeader={true}
      templatePageSize={12}
    >
      <Column
        id="c1a1a"
        alignment="left"
        format="string"
        key="month"
        label="Month"
        position="center"
        size={100}
      />
      <Column
        id="c2b2b"
        alignment="right"
        format="currency"
        formatOptions={{
          currency: "USD",
          currencySign: "standard",
          notation: "standard",
          showSeparators: true,
          currencyDisplay: "symbol",
        }}
        key="revenue"
        label="Revenue"
        position="center"
        size={140}
        summaryAggregationMode="sum"
      />
      <Column
        id="c3c3c"
        alignment="right"
        format="decimal"
        formatOptions={{ showSeparators: true, notation: "standard" }}
        key="orders"
        label="Orders"
        position="center"
        size={100}
        summaryAggregationMode="sum"
      />
      <Column
        id="c4d4d"
        alignment="right"
        format="decimal"
        formatOptions={{ showSeparators: true, notation: "standard" }}
        key="conversion"
        label="Conversion %"
        position="center"
        size={120}
        summaryAggregationMode="avg"
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
          id="a1b2c3d4"
          event="clickToolbar"
          method="exportData"
          pluginId="salesTable"
          type="widget"
          waitMs="0"
          waitType="debounce"
        />
      </ToolbarButton>
    </Table>
  </Frame>
</App>
