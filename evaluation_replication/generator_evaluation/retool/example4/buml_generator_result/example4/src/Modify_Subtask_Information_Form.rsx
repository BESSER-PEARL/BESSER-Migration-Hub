<ModalFrame id="Modify_Subtask_Information_Form" hidden={true} showOverlay={true}>
<Body >
<Button id="Cancel_5" text="Cancel" />
<Button id="Delete_3" text="Delete" />
<Form id="Modify_Subtask_Information_fields_1" showBody={true} showFooter={true}>
<Text id="Modify_Subtask_Information_fields_1_title" value="Modify Subtask Information" />
<Body >
<TextInput id="P10_CREATED" formDataKey="P10_CREATED" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P10_PROJ_ID" formDataKey="P10_PROJ_ID" label="Project:" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P10_ROWID" formDataKey="P10_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P10_SUB_ASSIGN" formDataKey="P10_SUB_ASSIGN" label="Assignee" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P10_SUB_COMP" formDataKey="P10_SUB_COMP" label="Completed" placeholder="" required={false} disabled={false} readOnly={false} />
<TextArea id="P10_SUB_DESC" formDataKey="P10_SUB_DESC" label="Description" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P10_SUB_EST_COMP" formDataKey="P10_SUB_EST_COMP" label="Estimated Completion" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P10_SUB_ID" formDataKey="P10_SUB_ID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P10_SUB_NAME" formDataKey="P10_SUB_NAME" label="Name" placeholder="" required={true} disabled={false} readOnly={false} />
<Select id="P10_SUB_PRIORITY" formDataKey="P10_SUB_PRIORITY" label="Priority" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P10_SUB_START" formDataKey="P10_SUB_START" label="Start Date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P10_SUB_STATUS" formDataKey="P10_SUB_STATUS" label="Status" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P10_TASK_ID" formDataKey="P10_TASK_ID" label="Task" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P10_UPDATED" formDataKey="P10_UPDATED" label="" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Modify_Subtask_Information_fields_1_submit" text="Create Subtask" submit={true} submitTargetId="Modify_Subtask_Information_fields_1" />

</Footer>

</Form>
<Button id="Save_3" text="Apply Changes" />
</Body>
</ModalFrame>