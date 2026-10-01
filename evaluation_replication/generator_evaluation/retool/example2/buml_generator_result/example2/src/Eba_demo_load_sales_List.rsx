<Screen id="Eba_demo_load_sales_List" title="Eba_demo_load_sales_List" _order={6}>
<Frame id="$main" type="main" padding="8px 12px">
<Table id="Eba_demo_load_sales" showHeader={true} showFooter={true} data="{{ get_eba_demo_load_sales.data }}" primaryKeyColumnId="Eba_demo_load_sales_id">
<Column id="Eba_demo_load_sales_id" key="id" label="Id" format="decimal" />
<Column id="Eba_demo_load_sales_country" key="country" label="Country" format="string" />
<Column id="Eba_demo_load_sales_created" key="created" label="Created" format="date" />
<Column id="Eba_demo_load_sales_item_type" key="item_type" label="Item Type" format="string" />
<Column id="Eba_demo_load_sales_last_updated" key="last_updated" label="Last Updated" format="date" />
<Column id="Eba_demo_load_sales_order_date" key="order_date" label="Order Date" format="date" />
<Column id="Eba_demo_load_sales_order_id" key="order_id" label="Order Id" format="decimal" />
<Column id="Eba_demo_load_sales_order_priority" key="order_priority" label="Order Priority" format="string" />
<Column id="Eba_demo_load_sales_region" key="region" label="Region" format="string" />
<Column id="Eba_demo_load_sales_sales_channel" key="sales_channel" label="Sales Channel" format="string" />
<Column id="Eba_demo_load_sales_ship_date" key="ship_date" label="Ship Date" format="date" />
<Column id="Eba_demo_load_sales_total_cost" key="total_cost" label="Total Cost" format="decimal" />
<Column id="Eba_demo_load_sales_total_profit" key="total_profit" label="Total Profit" format="decimal" />
<Column id="Eba_demo_load_sales_total_revenue" key="total_revenue" label="Total Revenue" format="decimal" />
<Column id="Eba_demo_load_sales_unit_cost" key="unit_cost" label="Unit Cost" format="decimal" />
<Column id="Eba_demo_load_sales_unit_price" key="unit_price" label="Unit Price" format="decimal" />
<Column id="Eba_demo_load_sales_units_sold" key="units_sold" label="Units Sold" format="decimal" />
</Table>
</Frame>
</Screen>