<Screen id="Edit_Form" title="Edit_Form" _order={6}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_3" text="Cancel" />
<Form id="Edit_fields_1" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_title" value="Edit" />
<Body >
<NumberInput id="P3_COMM" formDataKey="P3_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P3_DEPTNO" formDataKey="P3_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P3_EMPNO" formDataKey="P3_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P3_ENAME" formDataKey="P3_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P3_HIREDATE" formDataKey="P3_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P3_JOB" formDataKey="P3_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P3_MGR" formDataKey="P3_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_ROWID" formDataKey="P3_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P3_SAL" formDataKey="P3_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1" />

</Footer>

</Form>
</Frame>
</Screen>