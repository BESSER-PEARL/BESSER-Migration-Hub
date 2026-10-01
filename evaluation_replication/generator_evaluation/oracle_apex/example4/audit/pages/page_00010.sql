prompt --application/pages/page_00010
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8004
,p_default_id_offset=>12645642186646158
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>10
,p_name=>'Project_Tracking'
,p_step_title=>'Project_Tracking'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1103000)
,p_plug_name=>'Project_Tracking'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1104000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1103000)
,p_button_name=>'CONTRACT_ALL'
,p_button_image_alt=>'Collapse All'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1105000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1103000)
,p_button_name=>'EXPAND_ALL'
,p_button_image_alt=>'Expand All'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1106000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1103000)
,p_button_name=>'RESET_TREE'
,p_button_image_alt=>'Reset Tree'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
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
,p_default_application_id=>8004
,p_default_id_offset=>12645642186646158
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPROJFILES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREETASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREESUBTASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREESTOCKS CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPROJECTS CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPOPULATION CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1107000)
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
,p_default_application_id=>8004
,p_default_id_offset=>12645642186646158
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPROJFILES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREETASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREESUBTASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREESTOCKS CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPROJECTS CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEPOPULATION CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOTREEDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREEDEPT ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    DNAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LOC VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREEEMP ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMM NUMBER NOT NULL,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    EMPNO NUMBER NOT NULL,'||wwv_flow.LF||
'    ENAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIREDATE DATE NOT NULL,'||wwv_flow.LF||
'    JOB VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SAL NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademotreeemp_mgr_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (ebademotreeemp_mgr_id) REFERENCES EbaDemoTreeEmp(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREEPOPULATION ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    POPULATION NUMBER NOT NULL,'||wwv_flow.LF||
'    REGION NUMBER NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    STATE_CODE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    STATE_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREEPROJECTS ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMPLETION_DATE DATE NOT NULL,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    DESCRIPTION VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    ESTIMATED_COMPLETION DATE NOT NULL,'||wwv_flow.LF||
'    PROJ_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    PROJECT_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    START_DATE DATE NOT NULL,'||wwv_flow.LF||
'    STATUS NUMBER NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREESTOCKS ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CLOSING_VAL NUMBER NOT NULL,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIGH NUMBER NOT NULL,'||wwv_flow.LF||
'    LOW NUMBER NOT NULL,'||wwv_flow.LF||
'    OPENING_VAL NUMBER NOT NULL,'||wwv_flow.LF||
'    PRICING_DATE DATE NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    STOCK_CODE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    STOCK_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREESUBTASK ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    PROJ_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    SUB_ASSIGN VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SUB_COMP DATE NOT NULL,'||wwv_flow.LF||
'    SUB_DESC VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SUB_EST_COMP DATE NOT NULL,'||wwv_flow.LF||
'    SUB_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    SUB_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SUB_PRIORITY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SUB_START DATE NOT NULL,'||wwv_flow.LF||
'    SUB_STATUS VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    TASK_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREETASK ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    TASK_ASSIGN NUMBER NOT NULL,'||wwv_flow.LF||
'    TASK_COMP DATE NOT NULL,'||wwv_flow.LF||
'    TASK_DESC VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    TASK_EST_COMP DATE NOT NULL,'||wwv_flow.LF||
'    TASK_ID NUMBER NOT NULL,'||wwv_flow.LF||
'';
wwv_flow_imp.g_varchar2_table(2) := '    TASK_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    TASK_PRIORITY NUMBER NOT NULL,'||wwv_flow.LF||
'    TASK_START DATE NOT NULL,'||wwv_flow.LF||
'    TASK_STATUS NUMBER NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOTREEPROJFILES ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CREATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    CREATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    FILE_CHARSET VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    FILE_COMMENTS VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    FILE_LASTUPD DATE NOT NULL,'||wwv_flow.LF||
'    FILE_MIMETYPE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    FILE_NAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    ROW_VERSION_NUMBER NUMBER NOT NULL,'||wwv_flow.LF||
'    TAGS VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    UPDATED TIMESTAMP NOT NULL,'||wwv_flow.LF||
'    UPDATED_BY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    ebademotreeprojects_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (ebademotreeprojects_id) REFERENCES EbaDemoTreeProjects(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1108000)
,p_install_id=>wwv_flow_imp.id(1107000)
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
