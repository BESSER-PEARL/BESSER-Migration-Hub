<Screen id="Edit_Form_p9" title="Edit_Form_p9" _order={12}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_9" text="Cancel" />
<Form id="Edit_fields_1_7" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_7_title" value="Edit" />
<Body >
<NumberInput id="P9_COMM" formDataKey="P9_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P9_DEPTNO" formDataKey="P9_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_EMPNO" formDataKey="P9_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P9_ENAME" formDataKey="P9_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P9_HIREDATE" formDataKey="P9_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P9_JOB" formDataKey="P9_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P9_MGR" formDataKey="P9_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P9_ROWID" formDataKey="P9_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P9_SAL" formDataKey="P9_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_7_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_7" />

</Footer>

</Form>
</Frame>
</Screen>