<Screen id="Edit_Form_p7" title="Edit_Form_p7" _order={11}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_8" text="Cancel" />
<Form id="Edit_fields_1_6" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_6_title" value="Edit" />
<Body >
<NumberInput id="P7_COMM" formDataKey="P7_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_DEPTNO" formDataKey="P7_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_EMPNO" formDataKey="P7_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P7_ENAME" formDataKey="P7_ENAME" label="Name" placeholder="" required={true} disabled={false} readOnly={false} />
<Date id="P7_HIREDATE" formDataKey="P7_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_JOB" formDataKey="P7_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P7_MGR" formDataKey="P7_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P7_ROWID" formDataKey="P7_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P7_SAL" formDataKey="P7_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_6_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_6" />

</Footer>

</Form>
</Frame>
</Screen>