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
 * Eba Demo Tree Emp
 */
export const u_eba_demo_tree_emp = Table({
    name: 'u_eba_demo_tree_emp',
    label: 'Eba Demo Tree Emp',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        deptno: IntegerColumn({ mandatory: true,
            label: 'Deptno',
        }),

        ename: StringColumn({ mandatory: true,
            label: 'Ename',
        }),

        empno: IntegerColumn({ mandatory: true,
            label: 'Empno',
        }),

        sal: IntegerColumn({ mandatory: true,
            label: 'Sal',
        }),

        hiredate: DateColumn({ mandatory: true,
            label: 'Hiredate',
        }),

        job: StringColumn({ mandatory: true,
            label: 'Job',
        }),

        comm: IntegerColumn({ mandatory: true,
            label: 'Comm',
        }),
        ebademotreeemp_mgr: ReferenceColumn({
            referenceTable: 'u_eba_demo_tree_emp',
            label: 'Ebademotreeemp Mgr',
        }),
    },
});

/**
 * Eba Demo Tree Dept
 */
export const u_eba_demo_tree_dept = Table({
    name: 'u_eba_demo_tree_dept',
    label: 'Eba Demo Tree Dept',
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

/**
 * Eba Demo Tree Population
 */
export const u_eba_demo_tree_population = Table({
    name: 'u_eba_demo_tree_population',
    label: 'Eba Demo Tree Population',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        region: IntegerColumn({ mandatory: true,
            label: 'Region',
        }),

        state_name: StringColumn({ mandatory: true,
            label: 'State Name',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        state_code: StringColumn({ mandatory: true,
            label: 'State Code',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        id: IntegerColumn({ mandatory: true,
            label: 'Id',
        }),

        population: IntegerColumn({ mandatory: true,
            label: 'Population',
        }),
    },
});

/**
 * Eba Demo Tree Stocks
 */
export const u_eba_demo_tree_stocks = Table({
    name: 'u_eba_demo_tree_stocks',
    label: 'Eba Demo Tree Stocks',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        low: IntegerColumn({ mandatory: true,
            label: 'Low',
        }),

        closing_val: IntegerColumn({ mandatory: true,
            label: 'Closing Val',
        }),

        stock_code: StringColumn({ mandatory: true,
            label: 'Stock Code',
        }),

        high: IntegerColumn({ mandatory: true,
            label: 'High',
        }),

        opening_val: IntegerColumn({ mandatory: true,
            label: 'Opening Val',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        stock_name: StringColumn({ mandatory: true,
            label: 'Stock Name',
        }),

        pricing_date: DateColumn({ mandatory: true,
            label: 'Pricing Date',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        id: IntegerColumn({ mandatory: true,
            label: 'Id',
        }),
    },
});

/**
 * Eba Demo Tree Proj Files
 */
export const u_eba_demo_tree_proj_files = Table({
    name: 'u_eba_demo_tree_proj_files',
    label: 'Eba Demo Tree Proj Files',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        file_charset: StringColumn({ mandatory: true,
            label: 'File Charset',
        }),

        file_name: StringColumn({ mandatory: true,
            label: 'File Name',
        }),

        file_mimetype: StringColumn({ mandatory: true,
            label: 'File Mimetype',
        }),

        file_lastupd: DateColumn({ mandatory: true,
            label: 'File Lastupd',
        }),

        tags: StringColumn({ mandatory: true,
            label: 'Tags',
        }),

        id: IntegerColumn({ mandatory: true,
            label: 'Id',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        file_comments: StringColumn({ mandatory: true,
            label: 'File Comments',
        }),
        ebademotreeprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_tree_projects',
            label: 'Ebademotreeprojects',
        }),
    },
});

/**
 * Eba Demo Tree Projects
 */
export const u_eba_demo_tree_projects = Table({
    name: 'u_eba_demo_tree_projects',
    label: 'Eba Demo Tree Projects',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        status: IntegerColumn({ mandatory: true,
            label: 'Status',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        start_date: DateColumn({ mandatory: true,
            label: 'Start Date',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        estimated_completion: DateColumn({ mandatory: true,
            label: 'Estimated Completion',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        proj_id: IntegerColumn({ mandatory: true,
            label: 'Proj Id',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        completion_date: DateColumn({ mandatory: true,
            label: 'Completion Date',
        }),

        project_name: StringColumn({ mandatory: true,
            label: 'Project Name',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),
    },
});

/**
 * Eba Demo Tree Subtask
 */
export const u_eba_demo_tree_subtask = Table({
    name: 'u_eba_demo_tree_subtask',
    label: 'Eba Demo Tree Subtask',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        sub_assign: StringColumn({ mandatory: true,
            label: 'Sub Assign',
        }),

        sub_id: IntegerColumn({ mandatory: true,
            label: 'Sub Id',
        }),

        sub_priority: StringColumn({ mandatory: true,
            label: 'Sub Priority',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        sub_desc: StringColumn({ mandatory: true,
            label: 'Sub Desc',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        task_id: IntegerColumn({ mandatory: true,
            label: 'Task Id',
        }),

        sub_est_comp: DateColumn({ mandatory: true,
            label: 'Sub Est Comp',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        proj_id: IntegerColumn({ mandatory: true,
            label: 'Proj Id',
        }),

        sub_name: StringColumn({ mandatory: true,
            label: 'Sub Name',
        }),

        sub_status: StringColumn({ mandatory: true,
            label: 'Sub Status',
        }),

        sub_start: DateColumn({ mandatory: true,
            label: 'Sub Start',
        }),

        sub_comp: DateColumn({ mandatory: true,
            label: 'Sub Comp',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),
    },
});

/**
 * Eba Demo Tree Task
 */
export const u_eba_demo_tree_task = Table({
    name: 'u_eba_demo_tree_task',
    label: 'Eba Demo Tree Task',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        task_desc: StringColumn({ mandatory: true,
            label: 'Task Desc',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        task_assign: IntegerColumn({ mandatory: true,
            label: 'Task Assign',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        task_name: StringColumn({ mandatory: true,
            label: 'Task Name',
        }),

        task_est_comp: DateColumn({ mandatory: true,
            label: 'Task Est Comp',
        }),

        task_start: DateColumn({ mandatory: true,
            label: 'Task Start',
        }),

        task_comp: DateColumn({ mandatory: true,
            label: 'Task Comp',
        }),

        row_version_number: IntegerColumn({ mandatory: true,
            label: 'Row Version Number',
        }),

        task_status: IntegerColumn({ mandatory: true,
            label: 'Task Status',
        }),

        task_priority: IntegerColumn({ mandatory: true,
            label: 'Task Priority',
        }),

        task_id: IntegerColumn({ mandatory: true,
            label: 'Task Id',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_tree_emp: u_eba_demo_tree_emp records (via u_eba_demo_tree_emp.ebademotreeemp_mgr)
 */
const u_eba_demo_tree_emp_u_eba_demo_tree_emp_related_list = Record({
    $id: Now.ID['u_eba_demo_tree_emp_u_eba_demo_tree_emp_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_tree_emp',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_tree_emp_u_eba_demo_tree_emp_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_tree_emp_u_eba_demo_tree_emp_related_list,
        position: 0,
        related_list: 'u_eba_demo_tree_emp.ebademotreeemp_mgr',
    },
});

/**
 * Related List on u_eba_demo_tree_projects: u_eba_demo_tree_proj_files records (via u_eba_demo_tree_proj_files.ebademotreeprojects)
 */
const u_eba_demo_tree_projects_u_eba_demo_tree_proj_files_related_list = Record({
    $id: Now.ID['u_eba_demo_tree_projects_u_eba_demo_tree_proj_files_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_tree_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_tree_projects_u_eba_demo_tree_proj_files_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_tree_projects_u_eba_demo_tree_proj_files_related_list,
        position: 0,
        related_list: 'u_eba_demo_tree_proj_files.ebademotreeprojects',
    },
});