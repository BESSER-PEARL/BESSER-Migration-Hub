import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    IntegerColumn,
    ReferenceColumn,
    DateColumn,
    DateTimeColumn,
    Record,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Eba Demo Dg Order Items
 */
export const u_eba_demo_dg_order_items = Table({
    name: 'u_eba_demo_dg_order_items',
    label: 'Eba Demo Dg Order Items',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        quantity: IntegerColumn({ mandatory: true,
            label: 'Quantity',
        }),

        unit_price: IntegerColumn({ mandatory: true,
            label: 'Unit Price',
        }),

        line_item_id: IntegerColumn({ mandatory: true,
            label: 'Line Item Id',
        }),
        ebademodgproducts: ReferenceColumn({
            referenceTable: 'u_eba_demo_dg_products',
            label: 'Ebademodgproducts',
        }),
        ebademodgorders: ReferenceColumn({
            referenceTable: 'u_eba_demo_dg_orders',
            label: 'Ebademodgorders',
        }),
    },
});

/**
 * Eba Demo Dg Dept
 */
export const u_eba_demo_dg_dept = Table({
    name: 'u_eba_demo_dg_dept',
    label: 'Eba Demo Dg Dept',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        dname: StringColumn({ mandatory: true,
            label: 'Dname',
        }),

        loc: StringColumn({ mandatory: true,
            label: 'Loc',
        }),
    },
});

/**
 * Eba Demo Dg Orders
 */
export const u_eba_demo_dg_orders = Table({
    name: 'u_eba_demo_dg_orders',
    label: 'Eba Demo Dg Orders',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        order_status: StringColumn({ mandatory: true,
            label: 'Order Status',
        }),

        order_datetime: DateTimeColumn({ mandatory: true,
            label: 'Order Datetime',
        }),
        ebademodgcustomers: ReferenceColumn({
            referenceTable: 'u_eba_demo_dg_customers',
            label: 'Ebademodgcustomers',
        }),
    },
});

/**
 * Eba Demo Dg Products
 */
export const u_eba_demo_dg_products = Table({
    name: 'u_eba_demo_dg_products',
    label: 'Eba Demo Dg Products',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        product_name: StringColumn({ mandatory: true,
            label: 'Product Name',
        }),

        unit_price: IntegerColumn({ mandatory: true,
            label: 'Unit Price',
        }),

        image_mime_type: StringColumn({ mandatory: true,
            label: 'Image Mime Type',
        }),

        image_last_updated: DateColumn({ mandatory: true,
            label: 'Image Last Updated',
        }),

        image_charset: StringColumn({ mandatory: true,
            label: 'Image Charset',
        }),

        image_filename: StringColumn({ mandatory: true,
            label: 'Image Filename',
        }),
    },
});

/**
 * Eba Demo Dg Customers
 */
export const u_eba_demo_dg_customers = Table({
    name: 'u_eba_demo_dg_customers',
    label: 'Eba Demo Dg Customers',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        full_name: StringColumn({ mandatory: true,
            label: 'Full Name',
        }),

        email_address: StringColumn({ mandatory: true,
            label: 'Email Address',
        }),
    },
});

/**
 * Eba Demo Dg Emp
 */
export const u_eba_demo_dg_emp = Table({
    name: 'u_eba_demo_dg_emp',
    label: 'Eba Demo Dg Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        comm: IntegerColumn({ mandatory: true,
            label: 'Comm',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),

        sal: IntegerColumn({ mandatory: true,
            label: 'Sal',
        }),
        ebademodgdept: ReferenceColumn({
            referenceTable: 'u_eba_demo_dg_dept',
            label: 'Ebademodgdept',
        }),
        ebademodgemp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_dg_emp',
            label: 'Ebademodgemp Mgr',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_dg_dept: u_eba_demo_dg_emp records (via u_eba_demo_dg_emp.ebademodgdept)
 */
const u_eba_demo_dg_dept_u_eba_demo_dg_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_dg_dept_u_eba_demo_dg_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_dg_dept',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_dg_dept_u_eba_demo_dg_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_dg_dept_u_eba_demo_dg_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_dg_emp.ebademodgdept',
    },
});

/**
 * Related List on u_eba_demo_dg_emp: u_eba_demo_dg_emp records (via u_eba_demo_dg_emp.ebademodgemp_mgr)
 */
const u_eba_demo_dg_emp_u_eba_demo_dg_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_dg_emp_u_eba_demo_dg_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_dg_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_dg_emp_u_eba_demo_dg_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_dg_emp_u_eba_demo_dg_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_dg_emp.ebademodgemp_mgr',
    },
});

/**
 * Related List on u_eba_demo_dg_products: u_eba_demo_dg_order_items records (via u_eba_demo_dg_order_items.ebademodgproducts)
 */
const u_eba_demo_dg_products_u_eba_demo_dg_order_items_related_list = Record({
    $id: Now.ID['u_eba_demo_dg_products_u_eba_demo_dg_order_items_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_dg_products',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_dg_products_u_eba_demo_dg_order_items_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_dg_products_u_eba_demo_dg_order_items_related_list,
        position: 0,
        related_list: 'u_eba_demo_dg_order_items.ebademodgproducts',
    },
});

/**
 * Related List on u_eba_demo_dg_customers: u_eba_demo_dg_orders records (via u_eba_demo_dg_orders.ebademodgcustomers)
 */
const u_eba_demo_dg_customers_u_eba_demo_dg_orders_related_list = Record({
    $id: Now.ID['u_eba_demo_dg_customers_u_eba_demo_dg_orders_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_dg_customers',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_dg_customers_u_eba_demo_dg_orders_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_dg_customers_u_eba_demo_dg_orders_related_list,
        position: 0,
        related_list: 'u_eba_demo_dg_orders.ebademodgcustomers',
    },
});

/**
 * Related List on u_eba_demo_dg_orders: u_eba_demo_dg_order_items records (via u_eba_demo_dg_order_items.ebademodgorders)
 */
const u_eba_demo_dg_orders_u_eba_demo_dg_order_items_related_list = Record({
    $id: Now.ID['u_eba_demo_dg_orders_u_eba_demo_dg_order_items_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_dg_orders',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_dg_orders_u_eba_demo_dg_order_items_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_dg_orders_u_eba_demo_dg_order_items_related_list,
        position: 0,
        related_list: 'u_eba_demo_dg_order_items.ebademodgorders',
    },
});