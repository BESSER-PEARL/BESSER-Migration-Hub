<Screen id="Execute_PL_SQL_Code_List" title="Execute_PL_SQL_Code_List" _order={13}>
<Frame id="$main" type="main" padding="8px 12px">
<Table id="Execute_PL_SQL_Code" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Execute_PL_SQL_Code_id">
<Column id="Execute_PL_SQL_Code_id" key="id" label="Id" format="decimal" />
<Column id="Execute_PL_SQL_Code_deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Execute_PL_SQL_Code_dname" key="dname" label="Dname" format="string" />
<Column id="Execute_PL_SQL_Code_loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Execute_PL_SQL_Code_2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Execute_PL_SQL_Code_2_id">
<Column id="Execute_PL_SQL_Code_2_id" key="id" label="Id" format="decimal" />
<Column id="Execute_PL_SQL_Code_2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Execute_PL_SQL_Code_2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Execute_PL_SQL_Code_2_ename" key="ename" label="Ename" format="string" />
<Column id="Execute_PL_SQL_Code_2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Execute_PL_SQL_Code_2_job" key="job" label="Job" format="string" />
<Column id="Execute_PL_SQL_Code_2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Execute_PL_SQL_Code_2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Execute_PL_SQL_Code_2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
<Button id="Reset_5" text="Reset" />
<Button id="Update_Salary" text="Update Salary by 10%" />
</Frame>
</Screen>