<Screen id="Stripe_Report_List" title="Stripe_Report_List" _order={20}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Reset_11" text="Reset" />
<Table id="Stripe_Report" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Stripe_Report_id">
<Column id="Stripe_Report_id" key="id" label="Id" format="decimal" />
<Column id="Stripe_Report_deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Stripe_Report_dname" key="dname" label="Dname" format="string" />
<Column id="Stripe_Report_loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Stripe_Report_2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Stripe_Report_2_id">
<Column id="Stripe_Report_2_id" key="id" label="Id" format="decimal" />
<Column id="Stripe_Report_2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Stripe_Report_2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Stripe_Report_2_ename" key="ename" label="Ename" format="string" />
<Column id="Stripe_Report_2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Stripe_Report_2_job" key="job" label="Job" format="string" />
<Column id="Stripe_Report_2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Stripe_Report_2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Stripe_Report_2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
</Frame>
</Screen>