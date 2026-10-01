<Screen id="Delete_and_Refresh_List" title="Delete_and_Refresh_List" _order={4}>
<Frame id="$main" type="main" padding="8px 12px">
<Table id="Delete_and_Refresh" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Delete_and_Refresh_id">
<Column id="Delete_and_Refresh_id" key="id" label="Id" format="decimal" />
<Column id="Delete_and_Refresh_deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Delete_and_Refresh_dname" key="dname" label="Dname" format="string" />
<Column id="Delete_and_Refresh_loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Delete_and_Refresh_2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Delete_and_Refresh_2_id">
<Column id="Delete_and_Refresh_2_id" key="id" label="Id" format="decimal" />
<Column id="Delete_and_Refresh_2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Delete_and_Refresh_2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Delete_and_Refresh_2_ename" key="ename" label="Ename" format="string" />
<Column id="Delete_and_Refresh_2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Delete_and_Refresh_2_job" key="job" label="Job" format="string" />
<Column id="Delete_and_Refresh_2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Delete_and_Refresh_2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Delete_and_Refresh_2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
<Button id="Reset_3" text="Reset" />
</Frame>
</Screen>