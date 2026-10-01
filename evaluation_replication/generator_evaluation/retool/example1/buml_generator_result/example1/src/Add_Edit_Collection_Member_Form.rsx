<ModalFrame id="Add_Edit_Collection_Member_Form" hidden={true} showOverlay={true}>
<Body >
<Form id="Add_Edit_Collection_Member_fields_1" showBody={true} showFooter={true}>
<Text id="Add_Edit_Collection_Member_fields_1_title" value="Add/Edit Collection Member" />
<Body >
<NumberInput id="P7_COMM" formDataKey="P7_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_DEPTNO" formDataKey="P7_DEPTNO" label="Dept&amp;nbsp;No" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P7_EMPNO" formDataKey="P7_EMPNO" label="Emp&amp;nbsp;No" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_ENAME" formDataKey="P7_ENAME" label="Employee&amp;nbsp;Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P7_HIREDATE" formDataKey="P7_HIREDATE" label="Hire&amp;nbsp;Date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_JOB" formDataKey="P7_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_MGR" formDataKey="P7_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P7_SAL" formDataKey="P7_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_SEQ" formDataKey="P7_SEQ" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_STATUS" formDataKey="P7_STATUS" label="Status" placeholder="" required={false} disabled={false} readOnly={true} />
<TextArea id="P7_XMLTYPE" formDataKey="P7_XMLTYPE" label="XMLType" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Add_Edit_Collection_Member_fields_1_submit" text="Add Member" submit={true} submitTargetId="Add_Edit_Collection_Member_fields_1" />

</Footer>

</Form>
<Button id="Cancel_5" text="Cancel" />
<Button id="Delete_Member" text="Delete Member" />
<Button id="Update_Member" text="Update Member" />
</Body>
</ModalFrame>