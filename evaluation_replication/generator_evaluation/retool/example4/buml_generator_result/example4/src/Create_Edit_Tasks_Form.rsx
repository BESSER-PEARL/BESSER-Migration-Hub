<Screen id="Create_Edit_Tasks_Form" title="Create_Edit_Tasks_Form" _order={1}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_2" text="Cancel" />
<Form id="Create_Edit_Tasks_fields_1" showBody={true} showFooter={true}>
<Text id="Create_Edit_Tasks_fields_1_title" value="Create/Edit Tasks" />
<Body >
<Select id="P9_PROJ_ID" formDataKey="P9_PROJ_ID" label="Project:" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_ASSIGN" formDataKey="P9_TASK_ASSIGN" label="Task Assign" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P9_TASK_COMP" formDataKey="P9_TASK_COMP" label="Completed" placeholder="" required={false} disabled={false} readOnly={false} />
<TextArea id="P9_TASK_DESC" formDataKey="P9_TASK_DESC" label="Details" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P9_TASK_EST_COMP" formDataKey="P9_TASK_EST_COMP" label="Estimated Completion" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_ID" formDataKey="P9_TASK_ID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_ID_COUNT" formDataKey="P9_TASK_ID_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_ID_NEXT" formDataKey="P9_TASK_ID_NEXT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_ID_PREV" formDataKey="P9_TASK_ID_PREV" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_TASK_NAME" formDataKey="P9_TASK_NAME" label="Task Name" placeholder="" required={true} disabled={false} readOnly={false} />
<Select id="P9_TASK_PRIORITY" formDataKey="P9_TASK_PRIORITY" label="Priority" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P9_TASK_START" formDataKey="P9_TASK_START" label="Start Date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P9_TASK_STATUS" formDataKey="P9_TASK_STATUS" label="Status" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Create_Edit_Tasks_fields_1_submit" text="Create" submit={true} submitTargetId="Create_Edit_Tasks_fields_1" />

</Footer>

</Form>
<Button id="Create_Subtask" text="Create Subtask" />
<Button id="Delete" text="Delete" />
<Button id="Get_Next_Task_Id" text="&amp;gt;" />
<Button id="Get_Previous_Task_Id" text="&amp;lt;" />
<Button id="Save" text="Apply Changes" />
</Frame>
</Screen>