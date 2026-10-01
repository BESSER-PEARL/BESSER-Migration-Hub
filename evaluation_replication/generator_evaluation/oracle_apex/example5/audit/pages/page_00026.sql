prompt --application/pages/page_00026
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8005
,p_default_id_offset=>49461010066525635
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>26
,p_name=>'Timer_List'
,p_step_title=>'Timer_List'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1421000)
,p_plug_name=>'Timer_List'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1422000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1421000)
,p_button_name=>'RESET'
,p_button_image_alt=>'Reset'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1423000)
,p_plug_name=>'Timer_List_EbaDemoDaDept'
,p_plug_display_sequence=>30
,p_query_type=>'TABLE'
,p_query_table=>'EBADEMODADEPT'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_IR'
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(1424000)
,p_name=>'Timer_List'
,p_internal_uid=>1425000
,p_base_pk1=>'ID'
,p_show_detail_link=>'N'
,p_owner=>USER
,p_pagination_type=>'ROWS_X_TO_Y'
,p_report_list_mode=>'TABS'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1426000)
,p_db_column_name=>'ID'
,p_display_order=>1
,p_column_identifier=>'A'
,p_column_label=>'ID'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1427000)
,p_db_column_name=>'DEPTNO'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'DEPTNO'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1428000)
,p_db_column_name=>'DNAME'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'DNAME'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1429000)
,p_db_column_name=>'LOC'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'LOC'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(1430000)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'1423000'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'ID:DEPTNO:DNAME:LOC'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1431000)
,p_plug_name=>'Timer_List_EbaDemoDaEmp'
,p_plug_display_sequence=>30
,p_query_type=>'TABLE'
,p_query_table=>'EBADEMODAEMP'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_IR'
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(1432000)
,p_name=>'Timer_List'
,p_internal_uid=>1433000
,p_base_pk1=>'ID'
,p_show_detail_link=>'N'
,p_owner=>USER
,p_pagination_type=>'ROWS_X_TO_Y'
,p_report_list_mode=>'TABS'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1434000)
,p_db_column_name=>'ID'
,p_display_order=>1
,p_column_identifier=>'A'
,p_column_label=>'ID'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1435000)
,p_db_column_name=>'COMM'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'COMM'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1436000)
,p_db_column_name=>'EMPNO'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'EMPNO'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1437000)
,p_db_column_name=>'ENAME'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'ENAME'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1438000)
,p_db_column_name=>'HIREDATE'
,p_display_order=>5
,p_column_identifier=>'E'
,p_column_label=>'HIREDATE'
,p_column_type=>'DATE'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1439000)
,p_db_column_name=>'JOB'
,p_display_order=>6
,p_column_identifier=>'F'
,p_column_label=>'JOB'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1440000)
,p_db_column_name=>'SAL'
,p_display_order=>7
,p_column_identifier=>'G'
,p_column_label=>'SAL'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(1441000)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'1431000'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'ID:COMM:EMPNO:ENAME:HIREDATE:JOB:SAL'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/deployment/definition
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8005
,p_default_id_offset=>49461010066525635
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMODAEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMODADEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1442000)
,p_deinstall_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)
,p_required_free_kb=>100
);
wwv_flow_imp.component_end;
end;
/


prompt --application/deployment/installscripts/create_tables
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8005
,p_default_id_offset=>49461010066525635
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMODAEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMODADEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMODADEPT ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    DNAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LOC VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMODAEMP ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMM NUMBER NOT NULL,'||wwv_flow.LF||
'    EMPNO NUMBER NOT NULL,'||wwv_flow.LF||
'    ENAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIREDATE DATE NOT NULL,'||wwv_flow.LF||
'    JOB VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SAL NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademodadept_id NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademodaemp_mgr_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (ebademodadept_id) REFERENCES EbaDemoDaDept(id),'||wwv_flow.LF||
'    FOREIGN KEY (ebademodaemp_mgr_id) REFERENCES EbaDemoDaEmp(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1443000)
,p_install_id=>wwv_flow_imp.id(1442000)
,p_name=>'create_tables'
,p_sequence=>10
,p_script_type=>'INSTALL'
,p_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/end_environment
begin
wwv_flow_imp.import_end(
  p_auto_install_sup_obj => nvl(
    wwv_flow_application_install.get_auto_install_sup_obj, false));
commit;
end;
/
set verify on feedback on define on
prompt  ...done
