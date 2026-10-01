<Screen id="Edit_Form_p5" title="Edit_Form_p5" _order={10}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_7" text="Cancel" />
<Form id="Edit_fields_1_5" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_5_title" value="Edit" />
<Body >
<NumberInput id="P5_COMM" formDataKey="P5_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P5_DEPTNO" formDataKey="P5_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P5_EMPNO" formDataKey="P5_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P5_ENAME" formDataKey="P5_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P5_HIREDATE" formDataKey="P5_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P5_JOB" formDataKey="P5_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P5_MGR" formDataKey="P5_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P5_ROWID" formDataKey="P5_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P5_SAL" formDataKey="P5_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_5_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_5" />

</Footer>

</Form>
</Frame>
</Screen>