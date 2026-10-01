<Container
  id="tabbedContainer1"
  currentViewKey="{{ self.viewKeys[0] }}"
  hoistFetching={true}
  showBody={true}
  showHeader={true}
>
  <Header>
    <Tabs
      id="tab1"
      itemMode="static"
      navigateContainer={true}
      targetContainerId="tabbedContainer1"
      value="{{ self.values[0] }}"
    >
      <Option id="2ced4" value="Tab 1" />
      <Option id="ae17b" value="Tab 2" />
      <Option id="5fa07" value="Tab 3" />
    </Tabs>
  </Header>
  <View
    id="a7fea"
    disabled={false}
    hidden={false}
    iconPosition="left"
    viewKey="Books"
  >
    <Include src="./tabbedContainer2.rsx" />
  </View>
  <View id="ec41b" viewKey="Discount Codes">
    <TableLegacy
      id="discountCodesTable"
      _columnVisibility={{
        ordered: [{ created_at: true }, { last_updated_at: true }],
      }}
      _compatibilityMode={false}
      actionButtons={[
        {
          ordered: [
            { actionButtonText: "Delete" },
            { actionButtonType: "runQuery" },
            { actionButtonQuery: "deleteDiscountCode" },
            { actionButtonInternalUrlPath: "" },
            { actionButtonInternalUrlQuery: "" },
            { actionButtonUrl: "" },
            { actionButtonNewWindow: false },
            { actionButtonDisabled: "" },
          ],
        },
      ]}
      columnEditable={{
        ordered: [
          { discount_code_id: false },
          { discount_code: true },
          { discount_percent: true },
          { expiration_date: true },
          { is_active: true },
          { created_at: false },
          { last_updated_at: false },
        ],
      }}
      data="{{getDiscountCodes.data}}"
      doubleClickToEdit={true}
      events={[
        {
          ordered: [
            { event: "saveChanges" },
            { type: "datasource" },
            { method: "trigger" },
            { pluginId: "updateDiscountCodes" },
            { targetId: null },
            { params: { ordered: [] } },
            { waitType: "debounce" },
            { waitMs: "0" },
          ],
        },
      ]}
      showAddRowButton={true}
      showBoxShadow={false}
    />
    <Form
      id="form3"
      hoistFetching={true}
      initialData=""
      requireValidation={true}
      resetAfterSubmit={true}
      scroll={true}
      showBody={true}
      showFooter={true}
      showHeader={true}
    >
      <Header>
        <Text
          id="formTitle4"
          _disclosedFields={{ array: [] }}
          value="#### Form title"
          verticalAlign="center"
        />
      </Header>
      <Body>
        <TextInput
          id="textInput16"
          _disclosedFields={{ array: [] }}
          formDataKey="discount_code"
          label="Discount code"
          placeholder="Enter value"
          required={true}
        />
        <NumberInput
          id="numberInput7"
          _disclosedFields={{ array: [] }}
          currency="USD"
          formDataKey="discount_percent"
          inputValue={0}
          label="Discount percent"
          placeholder="Enter value"
          required={true}
          showSeparators={true}
          showStepper={true}
          value={0}
        />
        <Date
          id="date1"
          _disclosedFields={{ array: [] }}
          dateFormat="MMM d, yyyy"
          datePlaceholder="{{ self.dateFormat.toUpperCase() }}"
          formDataKey="expiration_date"
          iconBefore="bold/interface-calendar"
          label="Expiration date"
          required={true}
          value="{{ new Date() }}"
        />
        <Checkbox
          id="checkbox1"
          _disclosedFields={{ array: [] }}
          formDataKey="is_active"
          label="Is active"
        />
      </Body>
      <Footer>
        <Button
          id="formButton4"
          _disclosedFields={{ array: [] }}
          submit={true}
          submitTargetId="form3"
          text="Submit"
        />
      </Footer>
      <Event
        event="submit"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="addDiscountCode"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Form>
  </View>
  <View
    id="1cf04"
    disabled={false}
    hidden={false}
    iconPosition="left"
    viewKey="Orders"
  >
    <TableLegacy
      id="ordersTable"
      _columns={[
        "order_id",
        "book_id",
        "isbn",
        "title",
        "price",
        "category",
        "author",
        "cover_image",
        "bookshelf",
        "quantity_in_stock",
        "created_at",
        "last_updated_at",
        "total_amount",
        "discount_code_id",
        "discount_code",
        "discount_percent",
        "order_date",
        "expiration_date",
        "is_active",
      ]}
      _columnSummaryTypes={{
        ordered: [
          { total_amount: "sum" },
          { price: "sum" },
          { created_at: "" },
        ],
      }}
      _columnSummaryValues={{
        ordered: [{ total_amount: "" }, { price: "" }, { created_at: "" }],
      }}
      _columnVisibility={{
        ordered: [
          { last_updated_at: false },
          { bookshelf: false },
          { created_at: true },
          { author: false },
          { discount_code_id: false },
          { quantity_in_stock: false },
          { cover_image: false },
          { is_active: false },
          { expiration_date: false },
          { order_date: false },
        ],
      }}
      _compatibilityMode={false}
      actionButtons={[
        {
          ordered: [
            { actionButtonText: "Delete" },
            { actionButtonType: "runQuery" },
            { actionButtonQuery: "deleteOrder" },
            { actionButtonInternalUrlPath: "" },
            { actionButtonInternalUrlQuery: "" },
            { actionButtonUrl: "" },
            { actionButtonNewWindow: false },
            { actionButtonDisabled: "" },
          ],
        },
      ]}
      columnAlignment={{
        ordered: [
          { total_amount: "right" },
          { price: "right" },
          { created_at: "left" },
        ],
      }}
      columnFormats={{
        ordered: [
          { total_amount: "CurrencyDataCell" },
          { price: "CurrencyDataCell" },
          { created_at: "DateTimeDataCell" },
        ],
      }}
      columnTypeProperties={{
        ordered: [
          {
            total_amount: {
              ordered: [
                { showSeparators: true },
                { currency: "USD" },
                { padDecimal: true },
              ],
            },
          },
          {
            price: {
              ordered: [
                { showSeparators: true },
                { currency: "USD" },
                { padDecimal: true },
              ],
            },
          },
          {
            created_at: {
              ordered: [
                { manageTimeZone: true },
                { dateFormat: "MMM d, yyyy" },
                { valueTimeZone: "00:00" },
                { displayTimeZone: "local" },
              ],
            },
          },
        ],
      }}
      columnWidths={[
        { object: { id: "isbn", value: 154.89236450195312 } },
        { object: { id: "created_at", value: 170.55382537841797 } },
        { object: { id: "title", value: 240.00000762939453 } },
        { object: { id: "discount_code", value: 141 } },
      ]}
      data="{{getOrdersJoin.data}}"
      defaultSortByColumn="order_id"
      defaultSortDescending={true}
      doubleClickToEdit={true}
      events={[
        {
          ordered: [
            { event: "saveChanges" },
            { type: "datasource" },
            { method: "trigger" },
            { pluginId: "createNewOrder" },
            { targetId: null },
            { params: { ordered: [] } },
            { waitType: "debounce" },
            { waitMs: "0" },
          ],
        },
      ]}
      showBoxShadow={false}
    />
  </View>
  <View
    id="5eac9"
    disabled={false}
    hidden={false}
    iconPosition="left"
    viewKey="Inventory Report"
  >
    <Icon
      id="icon1"
      _disclosedFields={{ array: [] }}
      horizontalAlign="center"
      icon="bold/interface-content-book-1"
      style={{ ordered: [{ color: "success" }] }}
    />
    <Text
      id="text7"
      _disclosedFields={{ array: [] }}
      value="## In Stock"
      verticalAlign="center"
    />
    <TableLegacy
      id="table2"
      _columnSummaryTypes={{
        ordered: [{ isbn: "" }, { quantity_in_stock: "sum" }],
      }}
      _columnSummaryValues={{
        ordered: [{ isbn: "" }, { quantity_in_stock: "" }],
      }}
      _compatibilityMode={false}
      columnAlignment={{
        ordered: [{ isbn: "left" }, { quantity_in_stock: "right" }],
      }}
      columnFormats={{
        ordered: [
          { isbn: "TextDataCell" },
          { quantity_in_stock: "NumberDataCell" },
        ],
      }}
      columnTypeProperties={{
        ordered: [
          { isbn: { ordered: [] } },
          {
            quantity_in_stock: {
              ordered: [{ showSeparators: true }, { padDecimal: true }],
            },
          },
        ],
      }}
      data="{{ getInStock.data }}"
      doubleClickToEdit={true}
      showBoxShadow={false}
    />
    <Divider
      id="divider3"
      _disclosedFields={{ array: [] }}
      textSize="default"
    />
    <Text
      id="text8"
      _disclosedFields={{ array: [] }}
      value="## Out Of Stock"
      verticalAlign="center"
    />
    <Icon
      id="icon2"
      _disclosedFields={{ array: [] }}
      horizontalAlign="center"
      icon="bold/interface-alert-warning-triangle-alternate"
      style={{ ordered: [{ color: "danger" }] }}
    />
    <TableLegacy
      id="table3"
      _columnSummaryTypes={{ ordered: [{ isbn: "" }] }}
      _columnSummaryValues={{ ordered: [{ isbn: "" }] }}
      _compatibilityMode={false}
      columnAlignment={{ ordered: [{ isbn: "left" }] }}
      columnFormats={{ ordered: [{ isbn: "TextDataCell" }] }}
      columnTypeProperties={{ ordered: [{ isbn: { ordered: [] } }] }}
      data="{{ getOutOfStock.data }}"
      doubleClickToEdit={true}
      showBoxShadow={false}
    />
  </View>
  <View
    id="bb625"
    disabled={false}
    hidden={false}
    iconPosition="left"
    viewKey="Sales Reports"
  >
    <Text
      id="text4"
      _disclosedFields={{ array: [] }}
      value="## Overview Sales Report"
      verticalAlign="center"
    />
    <Select
      id="reportDateRange"
      emptyMessage="No options"
      itemMode="static"
      label="Data Date Range"
      overlayMaxHeight={375}
      placeholder="Select an option"
      showSelectionIndicator={true}
      value="24 hours"
    >
      <Option id="2a1db" value="24 hours" />
      <Option id="d0f6d" value="7 days" />
      <Option id="fc276" value="30 days" />
    </Select>
    <KeyValueMap
      id="SalesReport"
      data="{{getSalesData.data}}"
      keyTitle="Stat"
      prevRowFormats={{
        ordered: [
          { discount_utilization_rate: "percent" },
          { average_sale_price: "usd_dollars" },
          { total_revenue: "usd_dollars" },
        ],
      }}
      prevRowMappers={{
        ordered: [
          { total_books_sold: "{{getSalesData.data.total_books_sold}}" },
          { total_revenue: "{{getSalesData.data.total_revenue}}" },
          { average_sale_price: "{{getSalesData.data.average_sale_price}}" },
          {
            discount_utilization_rate:
              "{{getSalesData.data.discount_utilization_rate}}",
          },
        ],
      }}
      rowFormats={{
        ordered: [
          { discount_utilization_rate: "percent" },
          { average_sale_price: "usd_dollars" },
          { total_revenue: "usd_dollars" },
        ],
      }}
      rowHeaderNames={{
        ordered: [
          { total_books_sold: "Total Books Sold" },
          { total_revenue: "Total Revenue" },
          { average_sale_price: "Average Sale Price" },
          { discount_utilization_rate: "Discount Utilization Rate" },
        ],
      }}
      rowMappers={{
        ordered: [
          { total_books_sold: "{{getSalesData.data.total_books_sold}}" },
          { total_revenue: "{{getSalesData.data.total_revenue}}" },
          { average_sale_price: "{{getSalesData.data.average_sale_price}}" },
          {
            discount_utilization_rate:
              "{{getSalesData.data.discount_utilization_rate}}",
          },
        ],
      }}
      rows={[
        "a",
        "b",
        "c",
        "total_books_sold",
        "total_revenue",
        "average_sale_price",
        "error",
        "message",
        "position",
        "queryExecutionMetadata",
        "source",
        "discount_utilization_rate",
        "average_order_value",
      ]}
      rowVisibility={{
        ordered: [
          { a: true },
          { total_revenue: true },
          { b: true },
          { c: true },
          { total_books_sold: true },
          { message: true },
          { error: true },
          { position: true },
          { average_sale_price: true },
          { discount_utilization_rate: true },
          { source: true },
          { average_order_value: true },
          { queryExecutionMetadata: true },
        ],
      }}
    />
    <PlotlyChart
      id="chart1"
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "total_orders" },
                { datasource: "{{getSalesOverTime.data['total_orders']}}" },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#033663" },
                { colors: { ordered: [] } },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
          {
            1: {
              ordered: [
                { label: "total_sales" },
                { datasource: "{{getSalesOverTime.data['total_sales']}}" },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#247BC7" },
                { colors: { ordered: [] } },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
        ],
      }}
      datasourceDataType="object"
      datasourceInputMode="javascript"
      datasourceJS="{{getSalesOverTime.data}}"
      isDataTemplateDirty={true}
      skipDatasourceUpdate={true}
      title="# of Orders & Sales (USD) in the last {{reportDateRange.value}}"
      xAxis="{{getSalesOverTime.data.order_day}}"
      xAxisDropdown="order_day"
      yAxisTitle="USD"
    />
    <Divider
      id="divider1"
      _disclosedFields={{ array: [] }}
      textSize="default"
    />
    <Text
      id="text5"
      _disclosedFields={{ array: [] }}
      value="## Top Selling Books"
      verticalAlign="center"
    />
    <PlotlyChart
      id="chart2"
      chartType="pie"
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "total_sales" },
                { datasource: "{{getMostPopularBook.data['total_sales']}}" },
                { chartType: "pie" },
                { aggregationType: "sum" },
                { color: null },
                {
                  colors: {
                    ordered: [
                      { 11: "#AED6BD" },
                      { 12: "#E3D7FF" },
                      { 13: "#BCAAE7" },
                      { 0: "#033663" },
                      { 1: "#247BC7" },
                      { 2: "#55A1E3" },
                      { 3: "#DAECFC" },
                      { 4: "#EECA86" },
                      { 5: "#E9AB11" },
                      { 6: "#D47E2F" },
                      { 7: "#C15627" },
                      { 8: "#224930" },
                      { 9: "#238146" },
                      { 10: "#55A874" },
                    ],
                  },
                },
                { visible: false },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
          {
            1: {
              ordered: [
                { label: "discount_percent" },
                {
                  datasource: "{{getMostPopularBook.data['discount_percent']}}",
                },
                { chartType: "pie" },
                { aggregationType: "sum" },
                { color: null },
                {
                  colors: {
                    ordered: [
                      { 11: "#AED6BD" },
                      { 12: "#E3D7FF" },
                      { 13: "#BCAAE7" },
                      { 0: "#033663" },
                      { 1: "#247BC7" },
                      { 2: "#55A1E3" },
                      { 3: "#DAECFC" },
                      { 4: "#EECA86" },
                      { 5: "#E9AB11" },
                      { 6: "#D47E2F" },
                      { 7: "#C15627" },
                      { 8: "#224930" },
                      { 9: "#238146" },
                      { 10: "#55A874" },
                    ],
                  },
                },
                { visible: false },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
          {
            2: {
              ordered: [
                { label: "total_books_sold" },
                {
                  datasource: "{{getMostPopularBook.data['total_books_sold']}}",
                },
                { chartType: "pie" },
                { aggregationType: "sum" },
                { color: null },
                {
                  colors: {
                    ordered: [
                      { 11: "#AED6BD" },
                      { 12: "#E3D7FF" },
                      { 13: "#BCAAE7" },
                      { 0: "#033663" },
                      { 1: "#247BC7" },
                      { 2: "#55A1E3" },
                      { 3: "#DAECFC" },
                      { 4: "#EECA86" },
                      { 5: "#E9AB11" },
                      { 6: "#D47E2F" },
                      { 7: "#C15627" },
                      { 8: "#224930" },
                      { 9: "#238146" },
                      { 10: "#55A874" },
                    ],
                  },
                },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
        ],
      }}
      datasourceDataType="object"
      datasourceInputMode="javascript"
      datasourceJS="{{getMostPopularBook.data}}"
      isDataTemplateDirty={true}
      legendAlignment="right"
      skipDatasourceUpdate={true}
      title="Top Selling Books by Quantity"
      xAxis="{{getMostPopularBook.data['title']}}"
      xAxisDropdown="title"
    />
    <PlotlyChart
      id="chart4"
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "total_books_sold" },
                {
                  datasource:
                    "{{getMostPopularCategory.data['total_books_sold']}}",
                },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#033663" },
                { colors: { ordered: [] } },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
        ],
      }}
      datasourceDataType="object"
      datasourceInputMode="javascript"
      datasourceJS="{{getMostPopularCategory.data}}"
      isDataTemplateDirty={true}
      legendAlignment="right"
      shouldShowLegend={false}
      skipDatasourceUpdate={true}
      title="Most Popular Book Sales by Category"
      xAxis="{{getMostPopularCategory.data.category}}"
      xAxisDropdown="category"
    />
    <TableLegacy
      id="PopularBooksTable"
      _columns={[
        "title",
        "author",
        "total_sales",
        "discount_code",
        "discount_percent",
        "total_books_sold",
      ]}
      _columnSummaryTypes={{
        ordered: [{ total_sales: "sum" }, { discount_percent: "average" }],
      }}
      _columnSummaryValues={{
        ordered: [{ total_sales: "" }, { discount_percent: "" }],
      }}
      _compatibilityMode={false}
      columnAlignment={{
        ordered: [{ total_sales: "right" }, { discount_percent: "right" }],
      }}
      columnFormats={{
        ordered: [
          { total_sales: "CurrencyDataCell" },
          { discount_percent: "PercentDataCell" },
        ],
      }}
      columnTypeProperties={{
        ordered: [
          {
            total_sales: {
              ordered: [
                { showSeparators: true },
                { currency: "USD" },
                { padDecimal: true },
              ],
            },
          },
          {
            discount_percent: {
              ordered: [{ showSeparators: true }, { padDecimal: true }],
            },
          },
        ],
      }}
      columnWidths={[{ object: { id: "title", value: 300 } }]}
      data="{{getMostPopularBook.data}}"
      defaultSortByColumn="total_books_sold"
      defaultSortDescending={true}
      doubleClickToEdit={true}
      showBoxShadow={false}
    />
    <Divider
      id="divider2"
      _disclosedFields={{ array: [] }}
      textSize="default"
    />
    <Text
      id="text6"
      _disclosedFields={{ array: [] }}
      value="## Discount Code Report"
      verticalAlign="center"
    />
    <TableLegacy
      id="table1"
      _compatibilityMode={false}
      data="{{ getDiscountReport.data }}"
      doubleClickToEdit={true}
      showBoxShadow={false}
    />
    <PlotlyChart
      id="chart3"
      dataseries={{
        ordered: [
          {
            0: {
              ordered: [
                { label: "times_used" },
                { datasource: "{{getDiscountReport.data['times_used']}}" },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#033663" },
                { colors: { ordered: [] } },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
          {
            1: {
              ordered: [
                { label: "total_revenue" },
                { datasource: "{{getDiscountReport.data['total_revenue']}}" },
                { chartType: "bar" },
                { aggregationType: "sum" },
                { color: "#247BC7" },
                { colors: { ordered: [] } },
                { visible: true },
                {
                  hovertemplate:
                    "<b>%{x}</b><br>%{fullData.name}: %{y}<extra></extra>",
                },
              ],
            },
          },
        ],
      }}
      datasourceDataType="object"
      datasourceInputMode="javascript"
      datasourceJS="{{getDiscountReport.data}}"
      isDataTemplateDirty={true}
      skipDatasourceUpdate={true}
      xAxis="{{getDiscountReport.data.discount_code}}"
      xAxisDropdown="discount_code"
    />
  </View>
</Container>
