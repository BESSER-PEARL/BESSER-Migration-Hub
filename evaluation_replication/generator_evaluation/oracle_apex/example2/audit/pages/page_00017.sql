prompt --application/pages/page_00017
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>17
,p_name=>'Transform_and_Lookup_Form'
,p_step_title=>'Transform_and_Lookup_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1127000)
,p_plug_name=>'Transform_and_Lookup_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1128000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1127000)
,p_button_name=>'CLEAR'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1129000)
,p_plug_name=>'Transform and Lookup'
,p_plug_display_sequence=>30
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ERROR_ROW_COUNT, cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as FILE_NAME_2 from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1130000)
,p_name=>'P17_ERROR_ROW_COUNT'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ERROR_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1131000)
,p_name=>'P17_FILE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1132000)
,p_name=>'P17_FILE_NAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>'Loaded File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'FILE_NAME_2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1133000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1129000)
,p_button_name=>'FORM_2_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1134000)
,p_process_sequence=>30
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Transform_and_Lookup_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1129000)
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADSALES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1135000)
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADSALES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADDEPT ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    DNAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LOC VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADSALES ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COUNTRY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    CREATED DATE NOT NULL,'||wwv_flow.LF||
'    ITEM_TYPE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LAST_UPDATED DATE NOT NULL,'||wwv_flow.LF||
'    ORDER_DATE DATE NOT NULL,'||wwv_flow.LF||
'    ORDER_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    ORDER_PRIORITY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    REGION VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SALES_CHANNEL VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SHIP_DATE DATE NOT NULL,'||wwv_flow.LF||
'    TOTAL_COST NUMBER NOT NULL,'||wwv_flow.LF||
'    TOTAL_PROFIT NUMBER NOT NULL,'||wwv_flow.LF||
'    TOTAL_REVENUE NUMBER NOT NULL,'||wwv_flow.LF||
'    UNIT_COST NUMBER NOT NULL,'||wwv_flow.LF||
'    UNIT_PRICE NUMBER NOT NULL,'||wwv_flow.LF||
'    UNITS_SOLD NUMBER NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADEMP ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMM NUMBER NOT NULL,'||wwv_flow.LF||
'    CREATED DATE NOT NULL,'||wwv_flow.LF||
'    EMPNO NUMBER NOT NULL,'||wwv_flow.LF||
'    ENAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIREDATE DATE NOT NULL,'||wwv_flow.LF||
'    JOB VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LAST_UPDATED DATE NOT NULL,'||wwv_flow.LF||
'    SAL NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademoloaddept_id NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademoloademp_mgr_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (ebademoloaddept_id) REFERENCES EbaDemoLoadDept(id),'||wwv_flow.LF||
'    FOREIGN KEY (ebademoloademp_mgr_id) REFERENCES EbaDemoLoadEmp(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1136000)
,p_install_id=>wwv_flow_imp.id(1135000)
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
