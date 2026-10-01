import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    IntegerColumn,
    DateColumn,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Eba Demo Cs Emp
 */
export const u_eba_demo_cs_emp = Table({
    name: 'u_eba_demo_cs_emp',
    label: 'Eba Demo Cs Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        empno: IntegerColumn({ mandatory: true,
            label: 'Empno',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        deptno: IntegerColumn({ mandatory: true,
            label: 'Deptno',
        }),

        mgr: IntegerColumn({ mandatory: true,
            label: 'Mgr',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),

        sal: IntegerColumn({ mandatory: true,
            label: 'Sal',
        }),

        comm: IntegerColumn({ mandatory: true,
            label: 'Comm',
        }),
    },
});

