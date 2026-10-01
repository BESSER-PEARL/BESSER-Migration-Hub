<Screen id="Set_Values__SQL__List" title="Set_Values__SQL__List" _order={18}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Reset_9" text="Reset" />
<Table id="Set_Values__SQL_" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Set_Values__SQL__id">
<Column id="Set_Values__SQL__id" key="id" label="Id" format="decimal" />
<Column id="Set_Values__SQL__deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Set_Values__SQL__dname" key="dname" label="Dname" format="string" />
<Column id="Set_Values__SQL__loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Set_Values__SQL__2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Set_Values__SQL__2_id">
<Column id="Set_Values__SQL__2_id" key="id" label="Id" format="decimal" />
<Column id="Set_Values__SQL__2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Set_Values__SQL__2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Set_Values__SQL__2_ename" key="ename" label="Ename" format="string" />
<Column id="Set_Values__SQL__2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Set_Values__SQL__2_job" key="job" label="Job" format="string" />
<Column id="Set_Values__SQL__2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Set_Values__SQL__2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Set_Values__SQL__2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
</Frame>
</Screen>