import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    DateColumn,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Eba Demo Cal Sessions
 */
export const u_eba_demo_cal_sessions = Table({
    name: 'u_eba_demo_cal_sessions',
    label: 'Eba Demo Cal Sessions',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        session_type: StringColumn({ mandatory: true,
            label: 'Session Type',
        }),

        end_date: DateColumn({ mandatory: true,
            label: 'End Date',
        }),

        speaker: StringColumn({ mandatory: true,
            label: 'Speaker',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        status: StringColumn({ mandatory: true,
            label: 'Status',
        }),

        start_date: DateColumn({ mandatory: true,
            label: 'Start Date',
        }),

        title: StringColumn({ mandatory: true,
            label: 'Title',
        }),

        row_version_number: StringColumn({ mandatory: true,
            label: 'Row Version Number',
        }),
    },
});

/**
 * Eba Demo Cal Projects
 */
export const u_eba_demo_cal_projects = Table({
    name: 'u_eba_demo_cal_projects',
    label: 'Eba Demo Cal Projects',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        start_date: DateColumn({ mandatory: true,
            label: 'Start Date',
        }),

        cost: StringColumn({ mandatory: true,
            label: 'Cost',
        }),

        budget: StringColumn({ mandatory: true,
            label: 'Budget',
        }),

        status: StringColumn({ mandatory: true,
            label: 'Status',
        }),

        end_date: DateColumn({ mandatory: true,
            label: 'End Date',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        task_name: StringColumn({ mandatory: true,
            label: 'Task Name',
        }),

        row_version_number: StringColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        assigned_to: StringColumn({ mandatory: true,
            label: 'Assigned To',
        }),

        project: StringColumn({ mandatory: true,
            label: 'Project',
        }),
    },
});

/**
 * Eba Demo Cal Mysessions
 */
export const u_eba_demo_cal_mysessions = Table({
    name: 'u_eba_demo_cal_mysessions',
    label: 'Eba Demo Cal Mysessions',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        title: StringColumn({ mandatory: true,
            label: 'Title',
        }),

        start_date: DateColumn({ mandatory: true,
            label: 'Start Date',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        end_date: DateColumn({ mandatory: true,
            label: 'End Date',
        }),

        status: StringColumn({ mandatory: true,
            label: 'Status',
        }),

        row_version_number: StringColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        session_type: StringColumn({ mandatory: true,
            label: 'Session Type',
        }),

        speaker: StringColumn({ mandatory: true,
            label: 'Speaker',
        }),
    },
});

