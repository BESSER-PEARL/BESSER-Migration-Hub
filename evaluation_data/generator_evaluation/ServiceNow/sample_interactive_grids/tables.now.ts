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
 * Eba Demo Ig People
 */
export const u_eba_demo_ig_people = Table({
    name: 'u_eba_demo_ig_people',
    label: 'Eba Demo Ig People',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        flex1: StringColumn({ mandatory: true,
            label: 'Flex1',
        }),

        name: StringColumn({ mandatory: true,
            label: 'Name',
        }),

        country: StringColumn({ mandatory: true,
            label: 'Country',
        }),

        to_yr: StringColumn({ mandatory: true,
            label: 'To Yr',
        }),

        flex2: StringColumn({ mandatory: true,
            label: 'Flex2',
        }),

        link: StringColumn({ mandatory: true,
            label: 'Link',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        category: StringColumn({ mandatory: true,
            label: 'Category',
        }),

        from_yr: StringColumn({ mandatory: true,
            label: 'From Yr',
        }),

        gender: StringColumn({ mandatory: true,
            label: 'Gender',
        }),

        flex3: StringColumn({ mandatory: true,
            label: 'Flex3',
        }),

        rating: StringColumn({ mandatory: true,
            label: 'Rating',
        }),
    },
});

/**
 * Eba Demo Ig Emp
 */
export const u_eba_demo_ig_emp = Table({
    name: 'u_eba_demo_ig_emp',
    label: 'Eba Demo Ig Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        flex1: StringColumn({ mandatory: true,
            label: 'Flex1',
        }),

        comm: StringColumn({ mandatory: true,
            label: 'Comm',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),

        flex3: StringColumn({ mandatory: true,
            label: 'Flex3',
        }),

        flex4: StringColumn({ mandatory: true,
            label: 'Flex4',
        }),

        rating: StringColumn({ mandatory: true,
            label: 'Rating',
        }),

        sal: StringColumn({ mandatory: true,
            label: 'Sal',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        empno: StringColumn({ mandatory: true,
            label: 'Empno',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        onleave: StringColumn({ mandatory: true,
            label: 'Onleave',
        }),

        flex2: StringColumn({ mandatory: true,
            label: 'Flex2',
        }),

        notes: StringColumn({ mandatory: true,
            label: 'Notes',
        }),
        ebademoigdept: ReferenceColumn({
            referenceTable: 'u_eba_demo_ig_dept',
            label: 'Ebademoigdept',
        }),
        ebademoigemp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_ig_emp',
            label: 'Ebademoigemp Mgr',
        }),
    },
});

/**
 * Eba Demo Ig Dept
 */
export const u_eba_demo_ig_dept = Table({
    name: 'u_eba_demo_ig_dept',
    label: 'Eba Demo Ig Dept',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        deptno: StringColumn({ mandatory: true,
            label: 'Deptno',
        }),

        dname: StringColumn({ mandatory: true,
            label: 'Dname',
        }),

        notes: StringColumn({ mandatory: true,
            label: 'Notes',
        }),

        loc: StringColumn({ mandatory: true,
            label: 'Loc',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_ig_dept: u_eba_demo_ig_emp records (via u_eba_demo_ig_emp.ebademoigdept)
 */
const u_eba_demo_ig_dept_u_eba_demo_ig_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_ig_dept_u_eba_demo_ig_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_ig_dept',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_ig_dept_u_eba_demo_ig_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_ig_dept_u_eba_demo_ig_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_ig_emp.ebademoigdept',
    },
});

/**
 * Related List on u_eba_demo_ig_emp: u_eba_demo_ig_emp records (via u_eba_demo_ig_emp.ebademoigemp_mgr)
 */
const u_eba_demo_ig_emp_u_eba_demo_ig_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_ig_emp_u_eba_demo_ig_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_ig_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_ig_emp_u_eba_demo_ig_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_ig_emp_u_eba_demo_ig_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_ig_emp.ebademoigemp_mgr',
    },
});