import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    ReferenceColumn,
    DateColumn,
    Record,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Oow Demo Stores
 */
export const u_oow_demo_stores = Table({
    name: 'u_oow_demo_stores',
    label: 'Oow Demo Stores',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        store_state: StringColumn({ mandatory: true,
            label: 'Store State',
        }),

        store_address: StringColumn({ mandatory: true,
            label: 'Store Address',
        }),

        store_lng: StringColumn({ mandatory: true,
            label: 'Store Lng',
        }),

        store_type: StringColumn({ mandatory: true,
            label: 'Store Type',
        }),

        store_city: StringColumn({ mandatory: true,
            label: 'Store City',
        }),

        store_name: StringColumn({ mandatory: true,
            label: 'Store Name',
        }),

        store_zip: StringColumn({ mandatory: true,
            label: 'Store Zip',
        }),

        store_lat: StringColumn({ mandatory: true,
            label: 'Store Lat',
        }),
        oowdemoregions: ReferenceColumn({
            referenceTable: 'u_oow_demo_regions',
            label: 'Oowdemoregions',
        }),
    },
});

/**
 * Oow Demo Store Products
 */
export const u_oow_demo_store_products = Table({
    name: 'u_oow_demo_store_products',
    label: 'Oow Demo Store Products',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        sale_start_date: DateColumn({ mandatory: true,
            label: 'Sale Start Date',
        }),

        item_price: StringColumn({ mandatory: true,
            label: 'Item Price',
        }),

        sale_end_date: DateColumn({ mandatory: true,
            label: 'Sale End Date',
        }),

        discount_pct: StringColumn({ mandatory: true,
            label: 'Discount Pct',
        }),
        oowdemostores: ReferenceColumn({
            referenceTable: 'u_oow_demo_stores',
            label: 'Oowdemostores',
        }),
        oowdemoitems: ReferenceColumn({
            referenceTable: 'u_oow_demo_items',
            label: 'Oowdemoitems',
        }),
    },
});

/**
 * Oow Demo Sales History
 */
export const u_oow_demo_sales_history = Table({
    name: 'u_oow_demo_sales_history',
    label: 'Oow Demo Sales History',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        transaction_id: StringColumn({ mandatory: true,
            label: 'Transaction Id',
        }),

        date_of_sale: DateColumn({ mandatory: true,
            label: 'Date Of Sale',
        }),

        item_price: StringColumn({ mandatory: true,
            label: 'Item Price',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        quantity: StringColumn({ mandatory: true,
            label: 'Quantity',
        }),
        oowdemostores: ReferenceColumn({
            referenceTable: 'u_oow_demo_stores',
            label: 'Oowdemostores',
        }),
        oowdemostoreproducts: ReferenceColumn({
            referenceTable: 'u_oow_demo_store_products',
            label: 'Oowdemostoreproducts',
        }),
    },
});

/**
 * Oow Demo Regions
 */
export const u_oow_demo_regions = Table({
    name: 'u_oow_demo_regions',
    label: 'Oow Demo Regions',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        region_zoom: StringColumn({ mandatory: true,
            label: 'Region Zoom',
        }),

        is_default_yn: StringColumn({ mandatory: true,
            label: 'Is Default Yn',
        }),

        region_name: StringColumn({ mandatory: true,
            label: 'Region Name',
        }),

        region_lng: StringColumn({ mandatory: true,
            label: 'Region Lng',
        }),

        region_lat: StringColumn({ mandatory: true,
            label: 'Region Lat',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        region_color: StringColumn({ mandatory: true,
            label: 'Region Color',
        }),
    },
});

/**
 * Oow Demo Items
 */
export const u_oow_demo_items = Table({
    name: 'u_oow_demo_items',
    label: 'Oow Demo Items',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        item_desc: StringColumn({ mandatory: true,
            label: 'Item Desc',
        }),

        item_name: StringColumn({ mandatory: true,
            label: 'Item Name',
        }),

        msrp: StringColumn({ mandatory: true,
            label: 'Msrp',
        }),

        item_type: StringColumn({ mandatory: true,
            label: 'Item Type',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_oow_demo_regions: u_oow_demo_stores records (via u_oow_demo_stores.oowdemoregions)
 */
const u_oow_demo_regions_u_oow_demo_stores_related_list = Record({
    $id: Now.ID['u_oow_demo_regions_u_oow_demo_stores_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_oow_demo_regions',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_oow_demo_regions_u_oow_demo_stores_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_oow_demo_regions_u_oow_demo_stores_related_list,
        position: 0,
        related_list: 'u_oow_demo_stores.oowdemoregions',
    },
});

/**
 * Related List on u_oow_demo_stores: u_oow_demo_store_products records (via u_oow_demo_store_products.oowdemostores)
 */
const u_oow_demo_stores_u_oow_demo_store_products_related_list = Record({
    $id: Now.ID['u_oow_demo_stores_u_oow_demo_store_products_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_oow_demo_stores',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_oow_demo_stores_u_oow_demo_store_products_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_oow_demo_stores_u_oow_demo_store_products_related_list,
        position: 0,
        related_list: 'u_oow_demo_store_products.oowdemostores',
    },
});

/**
 * Related List on u_oow_demo_items: u_oow_demo_store_products records (via u_oow_demo_store_products.oowdemoitems)
 */
const u_oow_demo_items_u_oow_demo_store_products_related_list = Record({
    $id: Now.ID['u_oow_demo_items_u_oow_demo_store_products_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_oow_demo_items',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_oow_demo_items_u_oow_demo_store_products_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_oow_demo_items_u_oow_demo_store_products_related_list,
        position: 0,
        related_list: 'u_oow_demo_store_products.oowdemoitems',
    },
});

/**
 * Related List on u_oow_demo_stores: u_oow_demo_sales_history records (via u_oow_demo_sales_history.oowdemostores)
 */
const u_oow_demo_stores_u_oow_demo_sales_history_related_list = Record({
    $id: Now.ID['u_oow_demo_stores_u_oow_demo_sales_history_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_oow_demo_stores',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_oow_demo_stores_u_oow_demo_sales_history_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_oow_demo_stores_u_oow_demo_sales_history_related_list,
        position: 0,
        related_list: 'u_oow_demo_sales_history.oowdemostores',
    },
});

/**
 * Related List on u_oow_demo_store_products: u_oow_demo_sales_history records (via u_oow_demo_sales_history.oowdemostoreproducts)
 */
const u_oow_demo_store_products_u_oow_demo_sales_history_related_list = Record({
    $id: Now.ID['u_oow_demo_store_products_u_oow_demo_sales_history_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_oow_demo_store_products',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_oow_demo_store_products_u_oow_demo_sales_history_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_oow_demo_store_products_u_oow_demo_sales_history_related_list,
        position: 0,
        related_list: 'u_oow_demo_sales_history.oowdemostoreproducts',
    },
});