import "@servicenow/sdk/global";
import {
    Table,
    StringColumn,
    ReferenceColumn,
    DateColumn,
    DateTimeColumn,
    Record,
} from '@servicenow/sdk/core';





// --- TABLES ---

/**
 * Eba Demo Md Team Members
 */
export const u_eba_demo_md_team_members = Table({
    name: 'u_eba_demo_md_team_members',
    label: 'Eba Demo Md Team Members',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        email: StringColumn({ mandatory: true,
            label: 'Email',
        }),

        profile: StringColumn({ mandatory: true,
            label: 'Profile',
        }),

        username: StringColumn({ mandatory: true,
            label: 'Username',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        full_name: StringColumn({ mandatory: true,
            label: 'Full Name',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),
    },
});

/**
 * Eba Demo Md Tasks
 */
export const u_eba_demo_md_tasks = Table({
    name: 'u_eba_demo_md_tasks',
    label: 'Eba Demo Md Tasks',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        name: StringColumn({ mandatory: true,
            label: 'Name',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        end_date: DateColumn({ mandatory: true,
            label: 'End Date',
        }),

        is_complete_yn: StringColumn({ mandatory: true,
            label: 'Is Complete Yn',
        }),

        start_date: DateColumn({ mandatory: true,
            label: 'Start Date',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),
        ebademomdprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_projects',
            label: 'Ebademomdprojects',
        }),
        ebademomdmilestones: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_milestones',
            label: 'Ebademomdmilestones',
        }),
        ebademomdteammembers: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_team_members',
            label: 'Ebademomdteammembers',
        }),
    },
});

/**
 * Eba Demo Md Task Todos
 */
export const u_eba_demo_md_task_todos = Table({
    name: 'u_eba_demo_md_task_todos',
    label: 'Eba Demo Md Task Todos',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        is_complete_yn: StringColumn({ mandatory: true,
            label: 'Is Complete Yn',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        name: StringColumn({ mandatory: true,
            label: 'Name',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),
        ebademomdtasks: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_tasks',
            label: 'Ebademomdtasks',
        }),
        ebademomdteammembers: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_team_members',
            label: 'Ebademomdteammembers',
        }),
        ebademomdprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_projects',
            label: 'Ebademomdprojects',
        }),
    },
});

/**
 * Eba Demo Md Task Links
 */
export const u_eba_demo_md_task_links = Table({
    name: 'u_eba_demo_md_task_links',
    label: 'Eba Demo Md Task Links',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        application_id: StringColumn({ mandatory: true,
            label: 'Application Id',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        link_type: StringColumn({ mandatory: true,
            label: 'Link Type',
        }),

        url: StringColumn({ mandatory: true,
            label: 'Url',
        }),

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        application_page: StringColumn({ mandatory: true,
            label: 'Application Page',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),
        ebademomdtasks: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_tasks',
            label: 'Ebademomdtasks',
        }),
        ebademomdprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_projects',
            label: 'Ebademomdprojects',
        }),
    },
});

/**
 * Eba Demo Md Status
 */
export const u_eba_demo_md_status = Table({
    name: 'u_eba_demo_md_status',
    label: 'Eba Demo Md Status',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        display_order: StringColumn({ mandatory: true,
            label: 'Display Order',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        cd: StringColumn({ mandatory: true,
            label: 'Cd',
        }),
    },
});

/**
 * Eba Demo Md Projects
 */
export const u_eba_demo_md_projects = Table({
    name: 'u_eba_demo_md_projects',
    label: 'Eba Demo Md Projects',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        name: StringColumn({ mandatory: true,
            label: 'Name',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        completed_date: DateColumn({ mandatory: true,
            label: 'Completed Date',
        }),

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),
        ebademomdteammembers: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_team_members',
            label: 'Ebademomdteammembers',
        }),
        ebademomdstatus: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_status',
            label: 'Ebademomdstatus',
        }),
    },
});

/**
 * Eba Demo Md Milestones
 */
export const u_eba_demo_md_milestones = Table({
    name: 'u_eba_demo_md_milestones',
    label: 'Eba Demo Md Milestones',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        due_date: DateColumn({ mandatory: true,
            label: 'Due Date',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),

        name: StringColumn({ mandatory: true,
            label: 'Name',
        }),

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        description: StringColumn({ mandatory: true,
            label: 'Description',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),
        ebademomdprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_projects',
            label: 'Ebademomdprojects',
        }),
    },
});

/**
 * Eba Demo Md Comments
 */
export const u_eba_demo_md_comments = Table({
    name: 'u_eba_demo_md_comments',
    label: 'Eba Demo Md Comments',
    display: 'name',
    extensible: true,
    allowWebServiceAccess: true,
    schema: {

        id: StringColumn({ mandatory: true,
            label: 'Id',
        }),

        comment_text: StringColumn({ mandatory: true,
            label: 'Comment Text',
        }),

        created: DateTimeColumn({ mandatory: true,
            label: 'Created',
        }),

        updated_by: StringColumn({ mandatory: true,
            label: 'Updated By',
        }),

        updated: DateTimeColumn({ mandatory: true,
            label: 'Updated',
        }),

        created_by: StringColumn({ mandatory: true,
            label: 'Created By',
        }),
        ebademomdprojects: ReferenceColumn({
            referenceTable: 'u_eba_demo_md_projects',
            label: 'Ebademomdprojects',
        }),
    },
});



// --- RELATED LISTS ---

/**
 * Related List on u_eba_demo_md_projects: u_eba_demo_md_tasks records (via u_eba_demo_md_tasks.ebademomdprojects)
 */
const u_eba_demo_md_projects_u_eba_demo_md_tasks_related_list = Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_tasks_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_tasks_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_projects_u_eba_demo_md_tasks_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_tasks.ebademomdprojects',
    },
});

/**
 * Related List on u_eba_demo_md_tasks: u_eba_demo_md_task_todos records (via u_eba_demo_md_task_todos.ebademomdtasks)
 */
const u_eba_demo_md_tasks_u_eba_demo_md_task_todos_related_list = Record({
    $id: Now.ID['u_eba_demo_md_tasks_u_eba_demo_md_task_todos_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_tasks',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_tasks_u_eba_demo_md_task_todos_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_tasks_u_eba_demo_md_task_todos_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_task_todos.ebademomdtasks',
    },
});

/**
 * Related List on u_eba_demo_md_milestones: u_eba_demo_md_tasks records (via u_eba_demo_md_tasks.ebademomdmilestones)
 */
const u_eba_demo_md_milestones_u_eba_demo_md_tasks_related_list = Record({
    $id: Now.ID['u_eba_demo_md_milestones_u_eba_demo_md_tasks_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_milestones',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_milestones_u_eba_demo_md_tasks_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_milestones_u_eba_demo_md_tasks_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_tasks.ebademomdmilestones',
    },
});

/**
 * Related List on u_eba_demo_md_team_members: u_eba_demo_md_tasks records (via u_eba_demo_md_tasks.ebademomdteammembers)
 */
const u_eba_demo_md_team_members_u_eba_demo_md_tasks_related_list = Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_tasks_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_team_members',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_tasks_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_team_members_u_eba_demo_md_tasks_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_tasks.ebademomdteammembers',
    },
});

/**
 * Related List on u_eba_demo_md_projects: u_eba_demo_md_milestones records (via u_eba_demo_md_milestones.ebademomdprojects)
 */
const u_eba_demo_md_projects_u_eba_demo_md_milestones_related_list = Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_milestones_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_milestones_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_projects_u_eba_demo_md_milestones_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_milestones.ebademomdprojects',
    },
});

/**
 * Related List on u_eba_demo_md_team_members: u_eba_demo_md_projects records (via u_eba_demo_md_projects.ebademomdteammembers)
 */
const u_eba_demo_md_team_members_u_eba_demo_md_projects_related_list = Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_projects_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_team_members',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_projects_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_team_members_u_eba_demo_md_projects_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_projects.ebademomdteammembers',
    },
});

/**
 * Related List on u_eba_demo_md_tasks: u_eba_demo_md_task_links records (via u_eba_demo_md_task_links.ebademomdtasks)
 */
const u_eba_demo_md_tasks_u_eba_demo_md_task_links_related_list = Record({
    $id: Now.ID['u_eba_demo_md_tasks_u_eba_demo_md_task_links_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_tasks',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_tasks_u_eba_demo_md_task_links_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_tasks_u_eba_demo_md_task_links_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_task_links.ebademomdtasks',
    },
});

/**
 * Related List on u_eba_demo_md_team_members: u_eba_demo_md_task_todos records (via u_eba_demo_md_task_todos.ebademomdteammembers)
 */
const u_eba_demo_md_team_members_u_eba_demo_md_task_todos_related_list = Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_task_todos_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_team_members',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_team_members_u_eba_demo_md_task_todos_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_team_members_u_eba_demo_md_task_todos_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_task_todos.ebademomdteammembers',
    },
});

/**
 * Related List on u_eba_demo_md_status: u_eba_demo_md_projects records (via u_eba_demo_md_projects.ebademomdstatus)
 */
const u_eba_demo_md_status_u_eba_demo_md_projects_related_list = Record({
    $id: Now.ID['u_eba_demo_md_status_u_eba_demo_md_projects_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_status',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_status_u_eba_demo_md_projects_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_status_u_eba_demo_md_projects_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_projects.ebademomdstatus',
    },
});

/**
 * Related List on u_eba_demo_md_projects: u_eba_demo_md_task_todos records (via u_eba_demo_md_task_todos.ebademomdprojects)
 */
const u_eba_demo_md_projects_u_eba_demo_md_task_todos_related_list = Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_task_todos_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_task_todos_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_projects_u_eba_demo_md_task_todos_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_task_todos.ebademomdprojects',
    },
});

/**
 * Related List on u_eba_demo_md_projects: u_eba_demo_md_task_links records (via u_eba_demo_md_task_links.ebademomdprojects)
 */
const u_eba_demo_md_projects_u_eba_demo_md_task_links_related_list = Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_task_links_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_task_links_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_projects_u_eba_demo_md_task_links_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_task_links.ebademomdprojects',
    },
});

/**
 * Related List on u_eba_demo_md_projects: u_eba_demo_md_comments records (via u_eba_demo_md_comments.ebademomdprojects)
 */
const u_eba_demo_md_projects_u_eba_demo_md_comments_related_list = Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_comments_related_list'],
    table: 'sys_ui_related_list',
    data: {
        name: 'u_eba_demo_md_projects',
        view: 'Default view',
    },
});

Record({
    $id: Now.ID['u_eba_demo_md_projects_u_eba_demo_md_comments_related_list_entry'],
    table: 'sys_ui_related_list_entry',
    data: {
        list_id: u_eba_demo_md_projects_u_eba_demo_md_comments_related_list,
        position: 0,
        related_list: 'u_eba_demo_md_comments.ebademomdprojects',
    },
});