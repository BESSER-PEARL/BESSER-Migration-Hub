<Screen id="Add_Remove_Class__Error__List" title="Add_Remove_Class__Error__List" _order={0}>
<Frame id="$main" type="main" padding="8px 12px">
<Table id="Add_Remove_Class__Error_" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Add_Remove_Class__Error__id">
<Column id="Add_Remove_Class__Error__id" key="id" label="Id" format="decimal" />
<Column id="Add_Remove_Class__Error__deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Add_Remove_Class__Error__dname" key="dname" label="Dname" format="string" />
<Column id="Add_Remove_Class__Error__loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Add_Remove_Class__Error__2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Add_Remove_Class__Error__2_id">
<Column id="Add_Remove_Class__Error__2_id" key="id" label="Id" format="decimal" />
<Column id="Add_Remove_Class__Error__2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Add_Remove_Class__Error__2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Add_Remove_Class__Error__2_ename" key="ename" label="Ename" format="string" />
<Column id="Add_Remove_Class__Error__2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Add_Remove_Class__Error__2_job" key="job" label="Job" format="string" />
<Column id="Add_Remove_Class__Error__2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Add_Remove_Class__Error__2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Add_Remove_Class__Error__2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
<Button id="Reset" text="Reset" />
</Frame>
</Screen>