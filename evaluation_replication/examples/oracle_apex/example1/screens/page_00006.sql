prompt --application/pages/page_00006
begin
--   Manifest
--     PAGE: 00006
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7940
,p_default_id_offset=>10243121705511410
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>6
,p_name=>'Data Synchronization'
,p_alias=>'EMP'
,p_step_title=>'Data Synchronization'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.t-Report-pagination, #report_table_emp_table {',
'	border-top: 1px solid var(--ut-report-cell-border-color, var(--ut-component-inner-border-color))',
'}'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8877804931117058777)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This use case populates an Oracle Application Express (APEX) collection from a sample Employees table, the user updates the collection, and then synchroniz',
'es the data in the collection with the base table.  To use this example, please follow the instructions below.</p>',
'<ol>',
'<li>Populate the collection from the EBA_DEMO_CS_EMP table',
'<li>Add, Delete, and Update members in the collection',
'<li>Synchronize the members of the collection with the EBA_DEMO_CS_EMP table by clicking the "Apply Collection" button',
'</ol>'))
,p_plug_column_width=>'valign=top'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328921079571903843)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>10
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(1328919002858891716)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2543164876176756362)
,p_plug_name=>'Container'
,p_static_id=>'container'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--removeHeader js-removeLandmark:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(8877554219151395759)
,p_name=>'EBA_DEMO_CS_EMP table'
,p_static_id=>'eba-demo-cs-emp-table'
,p_region_name=>'emp_table'
,p_parent_plug_id=>wwv_flow_imp.id(2543164876176756362)
,p_template=>4073835273271169698
,p_display_sequence=>10
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--noBorder:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--altRowsDefault:t-Report--rowHighlight:t-Report--inline'
,p_display_point=>'SUB_REGIONS'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select empno, ename, job, mgr, hiredate, sal, comm, deptno',
'  from eba_demo_cs_emp'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>50
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_num_rows_type=>'ROWS_X_TO_Y_OF_Z'
,p_query_row_count_max=>500
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'F'
,p_plug_query_strip_html=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159584969095510)
,p_query_column_id=>7
,p_column_alias=>'COMM'
,p_column_display_sequence=>7
,p_column_heading=>'Commission'
,p_column_format=>'FML999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159680562095511)
,p_query_column_id=>8
,p_column_alias=>'DEPTNO'
,p_column_display_sequence=>8
,p_column_heading=>'DeptNo'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159010088095510)
,p_query_column_id=>1
,p_column_alias=>'EMPNO'
,p_column_display_sequence=>1
,p_column_heading=>'EmpNo'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159098328095510)
,p_query_column_id=>2
,p_column_alias=>'ENAME'
,p_column_display_sequence=>2
,p_column_heading=>'Name'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159410959095510)
,p_query_column_id=>5
,p_column_alias=>'HIREDATE'
,p_column_display_sequence=>5
,p_column_heading=>'Hire&nbsp;Date'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159193250095510)
,p_query_column_id=>3
,p_column_alias=>'JOB'
,p_column_display_sequence=>3
,p_column_heading=>'Job'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159309793095510)
,p_query_column_id=>4
,p_column_alias=>'MGR'
,p_column_display_sequence=>4
,p_column_heading=>'Manager'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159499129095510)
,p_query_column_id=>6
,p_column_alias=>'SAL'
,p_column_display_sequence=>6
,p_column_heading=>'Salary'
,p_column_format=>'FML999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1330505478395918105)
,p_plug_name=>'EBA_DEMO_CS_EMP table SQL Source'
,p_static_id=>'eba-demo-cs-emp-table-sql-source'
,p_parent_plug_id=>wwv_flow_imp.id(2543164876176756362)
,p_region_template_options=>'#DEFAULT#:is-collapsed:t-Region--noBorder:t-Region--scrollBody'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>20
,p_plug_new_grid_row=>false
,p_plug_new_grid_column=>false
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.DISPLAY_SOURCE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', 'emp_table')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(8877566320864410117)
,p_name=>'EMP Collection'
,p_static_id=>'emp-collection'
,p_region_name=>'emp_collection'
,p_template=>4073835273271169698
,p_display_sequence=>20
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--altRowsDefault:t-Report--rowHighlight:t-Report--inline'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select seq_id editlink,',
'    seq_id, ',
'    n001, ',
'    n002, ',
'    n003, ',
'    n004, ',
'    d001, ',
'    c001, ',
'    c002, ',
'    c003, ',
'    c004 status',
'from apex_collections',
'where collection_name = ''EMPCOLLECTION''',
''))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>50
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_num_rows_type=>'ROWS_X_TO_Y_OF_Z'
,p_query_row_count_max=>500
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'F'
,p_plug_query_strip_html=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159985980095523)
,p_query_column_id=>8
,p_column_alias=>'C001'
,p_column_display_sequence=>4
,p_column_heading=>'Name'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800160101462095523)
,p_query_column_id=>9
,p_column_alias=>'C002'
,p_column_display_sequence=>5
,p_column_heading=>'Job'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800160195572095523)
,p_query_column_id=>10
,p_column_alias=>'C003'
,p_column_display_sequence=>6
,p_column_heading=>'Manager'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8406502639678021519)
,p_query_column_id=>7
,p_column_alias=>'D001'
,p_column_display_sequence=>7
,p_column_heading=>'Hire Date'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159784286095522)
,p_query_column_id=>1
,p_column_alias=>'EDITLINK'
,p_column_display_sequence=>1
,p_column_heading=>'Action'
,p_column_link=>'f?p=&APP_ID.:7:&SESSION.::&DEBUG.:7:P7_SEQ,P7_STATUS:#SEQ_ID#,#STATUS#'
,p_column_linktext=>'Edit'
,p_column_link_attr=>'class="t-Button t-Button--warning"'
,p_column_alignment=>'CENTER'
,p_display_as=>'WITHOUT_MODIFICATION'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8440854269701731097)
,p_query_column_id=>3
,p_column_alias=>'N001'
,p_column_display_sequence=>3
,p_column_heading=>'EmpNo'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8440854342996731098)
,p_query_column_id=>4
,p_column_alias=>'N002'
,p_column_display_sequence=>8
,p_column_heading=>'Salary'
,p_column_format=>'FML999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8440854456097731098)
,p_query_column_id=>5
,p_column_alias=>'N003'
,p_column_display_sequence=>9
,p_column_heading=>'Commission'
,p_column_format=>'FML999G999G999G999G990D00'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8440854541774731098)
,p_query_column_id=>6
,p_column_alias=>'N004'
,p_column_display_sequence=>10
,p_column_heading=>'DeptNo'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800159882181095523)
,p_query_column_id=>2
,p_column_alias=>'SEQ_ID'
,p_column_display_sequence=>2
,p_column_heading=>'Sequence'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(8800160806329095523)
,p_query_column_id=>11
,p_column_alias=>'STATUS'
,p_column_display_sequence=>11
,p_column_heading=>'Status'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_display_as=>'TEXT_FROM_LOV_ESC'
,p_named_lov=>wwv_flow_imp.id(1340963006341574589)
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1330505184218915491)
,p_plug_name=>'EMP Collection SQL Source'
,p_static_id=>'emp-collection-sql-source'
,p_parent_plug_id=>wwv_flow_imp.id(8877566320864410117)
,p_region_template_options=>'#DEFAULT#:is-collapsed:t-Region--noBorder:t-Region--scrollBody'
,p_region_attributes=>'style="margin-left: 8px;"'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>10
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.DISPLAY_SOURCE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', 'emp_collection')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877701324035791079)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(8877566320864410117)
,p_button_name=>'Add_Member'
,p_static_id=>'add-member'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Add Member'
,p_button_position=>'EDIT'
,p_button_redirect_url=>'f?p=&APP_ID.:7:&SESSION.::&DEBUG.:RP,7::'
,p_button_condition=>'apex_collection.collection_exists(''EMPCOLLECTION'')'
,p_button_condition2=>'PLSQL'
,p_button_condition_type=>'EXPRESSION'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877633134302510157)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(8877566320864410117)
,p_button_name=>'Apply_Collection'
,p_static_id=>'apply-collection'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Apply Collection'
,p_button_position=>'EDIT'
,p_button_condition=>'apex_collection.collection_exists(''EMPCOLLECTION'')'
,p_button_condition2=>'PLSQL'
,p_button_condition_type=>'EXPRESSION'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877582332215433837)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(8877566320864410117)
,p_button_name=>'Populate'
,p_static_id=>'populate'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Populate Collection from EBA_DEMO_CS_EMP '
,p_button_position=>'EDIT'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8877633516874510159)
,p_branch_name=>'Go To Page 6'
,p_branch_action=>'6'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877778534400996426)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Apply changes to EBA_DEMO_CS_EMP table'
,p_static_id=>'apply-changes-to-eba-demo-cs-emp-table'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'--',
'-- Loop through all the members of the collection.  For those that are still',
'-- marked as Original, they have not changed, so no changes need to be applied.',
'-- For those marked as updated, deleted, or new, issue the appropriate DML',
'-- against the SCOTT.EMP table.',
'--',
'for c1 in (select c001, c002, c003, c004, d001, n001, n002, n003, n004',
'             from apex_collections',
'            where collection_name = ''EMPCOLLECTION'') loop',
'    if c1.c004 = ''N'' then',
'        insert into eba_demo_cs_emp (empno, ename, job, mgr, hiredate, sal, comm, deptno)',
'        values (c1.n001, c1.c001, c1.c002, c1.c003, c1.d001, c1.n002, c1.n003, c1.n004 );',
'',
'    elsif c1.c004 = ''U'' then',
'        update eba_demo_cs_emp',
'           set ename    = c1.c001,',
'               job      = c1.c002,',
'               mgr      = c1.c003,',
'               hiredate = c1.d001,',
'               sal      = c1.n002,',
'               comm     = c1.n003,',
'               deptno   = c1.n004',
'         where empno = c1.n001;',
'',
'    elsif c1.c004 = ''D'' then',
'        delete from eba_demo_cs_emp',
'         where empno = c1.n001;',
'',
'    end if;',
'end loop;',
'--',
'-- Clear the contents of the collection',
'--',
'apex_collection.delete_collection( p_collection_name => ''EMPCOLLECTION'' );',
'--',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error applying changes to the database table.'
,p_process_when_button_id=>wwv_flow_imp.id(8877633134302510157)
,p_process_success_message=>'Successfully applied changes to the database table.'
,p_internal_uid=>8867535412695485016
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877586729022451973)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Populate'
,p_static_id=>'populate'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_rowxml varchar2(4000);',
'begin',
'if apex_collection.collection_exists( ''EMPCollection'') = TRUE then',
'    --',
'    apex_collection.delete_collection(',
'        p_collection_name => ''EMPCollection'' );',
'end if;',
'--',
'apex_collection.create_collection_from_query2(',
'    p_collection_name => ''EMPCollection'',',
'    p_query           => ''select empno, sal, comm, deptno, null, hiredate, null, null, null, null, ename, job, mgr, ''''O'''' original_flag from eba_demo_cs_emp order by ename'',',
'    p_generate_md5    => ''YES'');',
'--',
'for c1 in (select n001 empno, seq_id',
'             from apex_collections',
'            where collection_name = ''EMPCOLLECTION''',
'           order by seq_id) loop',
'    ',
'    l_rowxml := dbms_xmlgen.getxml( ''select * from eba_demo_cs_emp where empno = '' || c1.empno );',
'    apex_collection.update_member_attribute( ',
'        p_collection_name => ''EMPCollection'',',
'        p_seq             => c1.seq_id,',
'        p_xmltype_number  => 1,',
'        p_xmltype_value   => XMLType(l_rowxml));',
'end loop;',
'--',
'commit;',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_process_when_button_id=>wwv_flow_imp.id(8877582332215433837)
,p_internal_uid=>8867343607316940563
);
wwv_flow_imp.component_end;
end;
/
