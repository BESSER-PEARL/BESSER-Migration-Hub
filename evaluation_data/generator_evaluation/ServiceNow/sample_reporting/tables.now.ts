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
 * Eba Demo Ir Emp
 */
export const u_eba_demo_ir_emp = Table({
    name: 'u_eba_demo_ir_emp',
    label: 'Eba Demo Ir Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        sal: StringColumn({ mandatory: true,
            label: 'Sal',
        }),

        deptno: StringColumn({ mandatory: true,
            label: 'Deptno',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        empno: StringColumn({ mandatory: true,
            label: 'Empno',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        comm: StringColumn({ mandatory: true,
            label: 'Comm',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),
        ebademoiremp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_ir_emp',
            label: 'Ebademoiremp Mgr',
        }),
    },
});

/**
 * Eba Demo Ir Dept
 */
export const u_eba_demo_ir_dept = Table({
    name: 'u_eba_demo_ir_dept',
    label: 'Eba Demo Ir Dept',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        dname: StringColumn({ mandatory: true,
            label: 'Dname',
        }),

        deptno: StringColumn({ mandatory: true,
            label: 'Deptno',
        }),

        loc: StringColumn({ mandatory: true,
            label: 'Loc',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_ir_emp: u_eba_demo_ir_emp records (via u_eba_demo_ir_emp.ebademoiremp_mgr)
 */
const u_eba_demo_ir_emp_u_eba_demo_ir_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_ir_emp_u_eba_demo_ir_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_ir_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_ir_emp_u_eba_demo_ir_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_ir_emp_u_eba_demo_ir_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_ir_emp.ebademoiremp_mgr',
    },
});