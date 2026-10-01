import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    IntegerColumn,
    ReferenceColumn,
    DateColumn,
    Record,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Eba Demo Load Sales
 */
export const u_eba_demo_load_sales = Table({
    name: 'u_eba_demo_load_sales',
    label: 'Eba Demo Load Sales',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        created: DateColumn({ mandatory: true,
            label: 'Created',
        }),

        total_profit: IntegerColumn({ mandatory: true,
            label: 'Total Profit',
        }),

        units_sold: IntegerColumn({ mandatory: true,
            label: 'Units Sold',
        }),

        unit_price: IntegerColumn({ mandatory: true,
            label: 'Unit Price',
        }),

        ship_date: DateColumn({ mandatory: true,
            label: 'Ship Date',
        }),

        order_id: IntegerColumn({ mandatory: true,
            label: 'Order Id',
        }),

        order_date: DateColumn({ mandatory: true,
            label: 'Order Date',
        }),

        country: StringColumn({ mandatory: true,
            label: 'Country',
        }),

        unit_cost: IntegerColumn({ mandatory: true,
            label: 'Unit Cost',
        }),

        order_priority: StringColumn({ mandatory: true,
            label: 'Order Priority',
        }),

        sales_channel: StringColumn({ mandatory: true,
            label: 'Sales Channel',
        }),

        last_updated: DateColumn({ mandatory: true,
            label: 'Last Updated',
        }),

        item_type: StringColumn({ mandatory: true,
            label: 'Item Type',
        }),

        total_cost: IntegerColumn({ mandatory: true,
            label: 'Total Cost',
        }),

        region: StringColumn({ mandatory: true,
            label: 'Region',
        }),

        total_revenue: IntegerColumn({ mandatory: true,
            label: 'Total Revenue',
        }),
    },
});

/**
 * Eba Demo Load Emp
 */
export const u_eba_demo_load_emp = Table({
    name: 'u_eba_demo_load_emp',
    label: 'Eba Demo Load Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        comm: IntegerColumn({ mandatory: true,
            label: 'Comm',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        sal: IntegerColumn({ mandatory: true,
            label: 'Sal',
        }),

        created: DateColumn({ mandatory: true,
            label: 'Created',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        last_updated: DateColumn({ mandatory: true,
            label: 'Last Updated',
        }),

        empno: IntegerColumn({ mandatory: true,
            label: 'Empno',
        }),
        ebademoloademp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_load_emp',
            label: 'Ebademoloademp Mgr',
        }),
        ebademoloaddept: ReferenceColumn({
            referenceTable: 'u_eba_demo_load_dept',
            label: 'Ebademoloaddept',
        }),
    },
});

/**
 * Eba Demo Load Dept
 */
export const u_eba_demo_load_dept = Table({
    name: 'u_eba_demo_load_dept',
    label: 'Eba Demo Load Dept',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        loc: StringColumn({ mandatory: true,
            label: 'Loc',
        }),

        deptno: IntegerColumn({ mandatory: true,
            label: 'Deptno',
        }),

        dname: StringColumn({ mandatory: true,
            label: 'Dname',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_load_emp: u_eba_demo_load_emp records (via u_eba_demo_load_emp.ebademoloademp_mgr)
 */
const u_eba_demo_load_emp_u_eba_demo_load_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_load_emp_u_eba_demo_load_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_load_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_load_emp_u_eba_demo_load_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_load_emp_u_eba_demo_load_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_load_emp.ebademoloademp_mgr',
    },
});

/**
 * Related List on u_eba_demo_load_dept: u_eba_demo_load_emp records (via u_eba_demo_load_emp.ebademoloaddept)
 */
const u_eba_demo_load_dept_u_eba_demo_load_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_load_dept_u_eba_demo_load_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_load_dept',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_load_dept_u_eba_demo_load_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_load_dept_u_eba_demo_load_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_load_emp.ebademoloaddept',
    },
});