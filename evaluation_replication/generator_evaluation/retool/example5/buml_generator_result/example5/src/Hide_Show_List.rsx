<Screen id="Hide_Show_List" title="Hide_Show_List" _order={15}>
<Frame id="$main" type="main" padding="8px 12px">
<Table id="Hide_Show" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_dept.data }}" primaryKeyColumnId="Hide_Show_id">
<Column id="Hide_Show_id" key="id" label="Id" format="decimal" />
<Column id="Hide_Show_deptno" key="deptno" label="Deptno" format="decimal" />
<Column id="Hide_Show_dname" key="dname" label="Dname" format="string" />
<Column id="Hide_Show_loc" key="loc" label="Loc" format="string" />
</Table>
<Table id="Hide_Show_2" showHeader={true} showFooter={true} data="{{ get_eba_demo_da_emp.data }}" primaryKeyColumnId="Hide_Show_2_id">
<Column id="Hide_Show_2_id" key="id" label="Id" format="decimal" />
<Column id="Hide_Show_2_comm" key="comm" label="Comm" format="decimal" />
<Column id="Hide_Show_2_empno" key="empno" label="Empno" format="decimal" />
<Column id="Hide_Show_2_ename" key="ename" label="Ename" format="string" />
<Column id="Hide_Show_2_hiredate" key="hiredate" label="Hiredate" format="date" />
<Column id="Hide_Show_2_job" key="job" label="Job" format="string" />
<Column id="Hide_Show_2_sal" key="sal" label="Sal" format="decimal" />
<Column id="Hide_Show_2_ebademodadept_id" key="ebademodadept_id" label="Ebademodadept Id" format="decimal" />
<Column id="Hide_Show_2_ebademodaemp_mgr_id" key="ebademodaemp_mgr_id" label="Ebademodaemp Mgr Id" format="decimal" />
</Table>
<Button id="Reset_6" text="Reset" />
</Frame>
</Screen>