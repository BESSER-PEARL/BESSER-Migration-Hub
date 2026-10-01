<ModalFrame id="Create_Edit_Project_Form" hidden={true} showOverlay={true}>
<Body >
<Button id="Cancel_4" text="Cancel" />
<Form id="Create_Edit_Project_fields_1" showBody={true} showFooter={true}>
<Text id="Create_Edit_Project_fields_1_title" value="Create/Edit Project" />
<Body >
<Date id="P7_COMPLETION_DATE" formDataKey="P7_COMPLETION_DATE" label="Completion Date" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P7_ESTIMATED_COMPLETION" formDataKey="P7_ESTIMATED_COMPLETION" label="Estimated Completion" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_PROJECT_NAME" formDataKey="P7_PROJECT_NAME" label="Project Name" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P7_PROJ_ID" formDataKey="P7_PROJ_ID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P7_START_DATE" formDataKey="P7_START_DATE" label="Start Date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_STATUS" formDataKey="P7_STATUS" label="Status" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_UPDATED" formDataKey="P7_UPDATED" label="" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Create_Edit_Project_fields_1_submit" text="Create" submit={true} submitTargetId="Create_Edit_Project_fields_1" />

</Footer>

</Form>
<Button id="Delete_2" text="Delete" />
<Button id="Save_2" text="Apply Changes" />
</Body>
</ModalFrame>