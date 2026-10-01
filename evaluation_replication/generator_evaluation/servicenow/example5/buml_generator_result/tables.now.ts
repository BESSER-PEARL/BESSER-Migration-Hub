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
 * Eba Demo Da Emp
 */
export const u_eba_demo_da_emp = Table({
    name: 'u_eba_demo_da_emp',
    label: 'Eba Demo Da Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        comm: IntegerColumn({ mandatory: true,
            label: 'Comm',
        }),

        empno: IntegerColumn({ mandatory: true,
            label: 'Empno',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        sal: IntegerColumn({ mandatory: true,
            label: 'Sal',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),
        ebademodadept: ReferenceColumn({
            referenceTable: 'u_eba_demo_da_dept',
            label: 'Ebademodadept',
        }),
        ebademodaemp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_da_emp',
            label: 'Ebademodaemp Mgr',
        }),
    },
});

/**
 * Eba Demo Da Dept
 */
export const u_eba_demo_da_dept = Table({
    name: 'u_eba_demo_da_dept',
    label: 'Eba Demo Da Dept',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        loc: StringColumn({ mandatory: true,
            label: 'Loc',
        }),

        dname: StringColumn({ mandatory: true,
            label: 'Dname',
        }),

        deptno: IntegerColumn({ mandatory: true,
            label: 'Deptno',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_da_dept: u_eba_demo_da_emp records (via u_eba_demo_da_emp.ebademodadept)
 */
const u_eba_demo_da_dept_u_eba_demo_da_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_da_dept_u_eba_demo_da_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_da_dept',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_da_dept_u_eba_demo_da_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_da_dept_u_eba_demo_da_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_da_emp.ebademodadept',
    },
});

/**
 * Related List on u_eba_demo_da_emp: u_eba_demo_da_emp records (via u_eba_demo_da_emp.ebademodaemp_mgr)
 */
const u_eba_demo_da_emp_u_eba_demo_da_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_da_emp_u_eba_demo_da_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_da_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_da_emp_u_eba_demo_da_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_da_emp_u_eba_demo_da_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_da_emp.ebademodaemp_mgr',
    },
});