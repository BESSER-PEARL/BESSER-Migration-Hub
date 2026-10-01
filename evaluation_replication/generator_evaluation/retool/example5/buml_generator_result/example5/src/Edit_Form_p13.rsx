<Screen id="Edit_Form_p13" title="Edit_Form_p13" _order={7}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_4" text="Cancel" />
<Form id="Edit_fields_1_2" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_2_title" value="Edit" />
<Body >
<NumberInput id="P13_COMM" formDataKey="P13_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P13_DEPTNO" formDataKey="P13_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P13_EMPNO" formDataKey="P13_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P13_ENAME" formDataKey="P13_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P13_HIREDATE" formDataKey="P13_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P13_JOB" formDataKey="P13_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P13_LOCATION" formDataKey="P13_LOCATION" label="Location" placeholder="" required={false} disabled={false} readOnly={true} />
<Select id="P13_MGR" formDataKey="P13_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P13_NO_OF_EMPLOYEES" formDataKey="P13_NO_OF_EMPLOYEES" label="Number of Employees" placeholder="" required={false} disabled={false} readOnly={true} />
<TextInput id="P13_ROWID" formDataKey="P13_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P13_SAL" formDataKey="P13_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_2_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_2" />

</Footer>

</Form>
</Frame>
</Screen>