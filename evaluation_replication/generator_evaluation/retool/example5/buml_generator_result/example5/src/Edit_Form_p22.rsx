<Screen id="Edit_Form_p22" title="Edit_Form_p22" _order={9}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_6" text="Cancel" />
<Form id="Edit_fields_1_4" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_4_title" value="Edit" />
<Body >
<NumberInput id="P22_COMM" formDataKey="P22_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P22_DEPTNO" formDataKey="P22_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P22_EMPNO" formDataKey="P22_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P22_ENAME" formDataKey="P22_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P22_HIREDATE" formDataKey="P22_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P22_JOB" formDataKey="P22_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P22_MGR" formDataKey="P22_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P22_ROWID" formDataKey="P22_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P22_SAL" formDataKey="P22_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_4_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_4" />

</Footer>

</Form>
</Frame>
</Screen>