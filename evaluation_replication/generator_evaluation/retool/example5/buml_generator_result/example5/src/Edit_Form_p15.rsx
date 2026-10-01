<Screen id="Edit_Form_p15" title="Edit_Form_p15" _order={8}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Cancel_5" text="Cancel" />
<Form id="Edit_fields_1_3" showBody={true} showFooter={true}>
<Text id="Edit_fields_1_3_title" value="Edit" />
<Body >
<NumberInput id="P15_COMM" formDataKey="P15_COMM" label="Commission" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P15_DEPTNO" formDataKey="P15_DEPTNO" label="Department" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P15_EMPNO" formDataKey="P15_EMPNO" label="Employee Number" placeholder="" required={true} disabled={false} readOnly={false} />
<TextInput id="P15_ENAME" formDataKey="P15_ENAME" label="Name" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P15_HIREDATE" formDataKey="P15_HIREDATE" label="Hire date" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P15_JOB" formDataKey="P15_JOB" label="Job" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P15_MGR" formDataKey="P15_MGR" label="Manager" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P15_ROWID" formDataKey="P15_ROWID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P15_SAL" formDataKey="P15_SAL" label="Salary" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Edit_fields_1_3_submit" text="Apply Changes" submit={true} submitTargetId="Edit_fields_1_3" />

</Footer>

</Form>
</Frame>
</Screen>