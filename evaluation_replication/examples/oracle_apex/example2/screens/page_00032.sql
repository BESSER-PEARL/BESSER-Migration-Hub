prompt --application/pages/page_00032
begin
--   Manifest
--     PAGE: 00032
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7850
,p_default_id_offset=>11008923455465249
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>32
,p_name=>'Load Data using PL/SQL API'
,p_alias=>'LOAD-DATA-USING-PL-SQL-API'
,p_step_title=>'Load Data using PL/SQL API'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>wwv_flow_string.join(wwv_flow_t_varchar2(
'function set_item() {',
'    $x(''P32_DATA'').value= $v(''P32_SAMPLE_DATA'');',
'}'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3534430211386335892)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>1
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(11521794561627835810)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3534433982656357231)
,p_plug_name=>'Data Loading SQL Statement'
,p_static_id=>'data-loading-sql-statement'
,p_region_template_options=>'#DEFAULT#:js-useLocalStorage:is-collapsed:t-Region--scrollBody'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>',
'Clicking the <strong>Load Data</strong> will execute the following SQL Statement:',
'</p>',
'<pre>',
'insert into EBA_DEMO_LOAD_EMP (empno, ename, job, mgr, hiredate, sal, comm, deptno ) (',
'<span style="color: blue">    select to_number( col001 ),',
'           upper( col002 ),',
'           upper( col003 ),        ',
'           (select empno from eba_demo_load_emp where ename = upper( col004 ) ),',
'           to_date( col005 ), ',
'           to_number( col006 ), ',
'           to_number( col007 ), ',
'           (select deptno from eba_demo_load_dept where dname = upper( col008 ) )',
'      from table( apex_data_parser.parse(',
'               p_content   => to_blob( <em>{- the data -}</em> ),',
'               p_skip_rows => 1,',
'               p_file_type => apex_data_parser.c_file_type_csv ) )</span> ',
')',
'log errors into EBA_DEMO_LOAD_EMP_ERR$ ',
'reject limit unlimited;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3711322322597458552)
,p_name=>'Employees'
,p_static_id=>'employees'
,p_template=>2665811232373458102
,p_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_region_template_options=>'#DEFAULT#:is-collapsed:t-Region--noBorder:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlightOff:t-Report--horizontalBorders'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'TABLE'
,p_query_table=>'EBA_DEMO_LOAD_EMP'
,p_include_rowid_column=>false
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_no_data_found=>'The EBA_DEMO_LOAD_EMP table is empty.'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711323018909458559)
,p_query_column_id=>7
,p_column_alias=>'COMM'
,p_column_display_sequence=>7
,p_column_heading=>'Comm'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711323237728458561)
,p_query_column_id=>9
,p_column_alias=>'CREATED'
,p_column_display_sequence=>9
,p_column_heading=>'Created'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711323137845458560)
,p_query_column_id=>8
,p_column_alias=>'DEPTNO'
,p_column_display_sequence=>8
,p_column_heading=>'Deptno'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322470246458553)
,p_query_column_id=>1
,p_column_alias=>'EMPNO'
,p_column_display_sequence=>1
,p_column_heading=>'Empno'
,p_heading_alignment=>'LEFT'
,p_default_sort_column_sequence=>1
,p_default_sort_dir=>'desc'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322559430458554)
,p_query_column_id=>2
,p_column_alias=>'ENAME'
,p_column_display_sequence=>2
,p_column_heading=>'Ename'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322849059458557)
,p_query_column_id=>5
,p_column_alias=>'HIREDATE'
,p_column_display_sequence=>5
,p_column_heading=>'Hiredate'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322665576458555)
,p_query_column_id=>3
,p_column_alias=>'JOB'
,p_column_display_sequence=>3
,p_column_heading=>'Job'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3534432099746357212)
,p_query_column_id=>10
,p_column_alias=>'LAST_UPDATED'
,p_column_display_sequence=>10
,p_column_heading=>'Last Updated'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322735481458556)
,p_query_column_id=>4
,p_column_alias=>'MGR'
,p_column_display_sequence=>4
,p_column_heading=>'Mgr'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711322950889458558)
,p_query_column_id=>6
,p_column_alias=>'SAL'
,p_column_display_sequence=>6
,p_column_heading=>'Sal'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3534432366553357214)
,p_name=>'Failed Rows'
,p_static_id=>'failed-rows'
,p_region_name=>'failed_rows'
,p_template=>4073835273271169698
,p_display_sequence=>50
,p_include_in_reg_disp_sel_yn=>'Y'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlightOff:t-Report--horizontalBorders'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ',
'       ORA_ERR_NUMBER$  F_ORA_ERR_NUMBER$,',
'       ORA_ERR_MESG$    F_ORA_ERR_MESG$,',
'       ORA_ERR_ROWID$   F_ORA_ERR_ROWID$,',
'       ORA_ERR_OPTYP$   F_ORA_ERR_OPTYP$,',
'       ORA_ERR_TAG$     F_ORA_ERR_TAG$,',
'       EMPNO            F_EMPNO,',
'       ENAME            F_ENAME,',
'       JOB              F_JOB,',
'       MGR              F_MGR,',
'       HIREDATE         F_HIREDATE,',
'       SAL              F_SAL,',
'       COMM             F_COMM,',
'       DEPTNO           F_DEPTNO,',
'       CREATED          F_CREATED,',
'       LAST_UPDATED     F_LAST_UPDATED',
'  from EBA_DEMO_LOAD_EMP_ERR$',
''))
,p_display_when_condition=>'select * from eba_demo_load_emp_err$'
,p_display_condition_type=>'EXISTS'
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_no_data_found=>'The EBA_DEMO_LOAD_EMP table is empty.'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609648126267918)
,p_query_column_id=>12
,p_column_alias=>'F_COMM'
,p_column_display_sequence=>12
,p_column_heading=>'Comm'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609856484267920)
,p_query_column_id=>14
,p_column_alias=>'F_CREATED'
,p_column_display_sequence=>14
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609747777267919)
,p_query_column_id=>13
,p_column_alias=>'F_DEPTNO'
,p_column_display_sequence=>13
,p_column_heading=>'Deptno'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609007503267912)
,p_query_column_id=>6
,p_column_alias=>'F_EMPNO'
,p_column_display_sequence=>6
,p_column_heading=>'Empno'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609116085267913)
,p_query_column_id=>7
,p_column_alias=>'F_ENAME'
,p_column_display_sequence=>7
,p_column_heading=>'Ename'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609407529267916)
,p_query_column_id=>10
,p_column_alias=>'F_HIREDATE'
,p_column_display_sequence=>10
,p_column_heading=>'Hiredate'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609235584267914)
,p_query_column_id=>8
,p_column_alias=>'F_JOB'
,p_column_display_sequence=>8
,p_column_heading=>'Job'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609962157267921)
,p_query_column_id=>15
,p_column_alias=>'F_LAST_UPDATED'
,p_column_display_sequence=>15
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609345757267915)
,p_query_column_id=>9
,p_column_alias=>'F_MGR'
,p_column_display_sequence=>9
,p_column_heading=>'Mgr'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3722972218812428758)
,p_query_column_id=>2
,p_column_alias=>'F_ORA_ERR_MESG$'
,p_column_display_sequence=>2
,p_column_heading=>'Message'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3722972175090428757)
,p_query_column_id=>1
,p_column_alias=>'F_ORA_ERR_NUMBER$'
,p_column_display_sequence=>16
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3722972475154428760)
,p_query_column_id=>4
,p_column_alias=>'F_ORA_ERR_OPTYP$'
,p_column_display_sequence=>18
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3722972307466428759)
,p_query_column_id=>3
,p_column_alias=>'F_ORA_ERR_ROWID$'
,p_column_display_sequence=>17
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3722972479027428761)
,p_query_column_id=>5
,p_column_alias=>'F_ORA_ERR_TAG$'
,p_column_display_sequence=>19
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3760609498855267917)
,p_query_column_id=>11
,p_column_alias=>'F_SAL'
,p_column_display_sequence=>11
,p_column_heading=>'Sal'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3711321628283458545)
,p_plug_name=>'Load Data'
,p_static_id=>'load-data'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4509241822355783071)
,p_plug_name=>'Page Instructions'
,p_static_id=>'page-instructions'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>',
'This page uploads data into an existing table (<strong>EBA_DEMO_LOAD_EMP</strong>) using a SQL INSERT statement and the <strong>APEX_DATA_PARSER.PARSE</strong> PL/SQL function. Unlike using the APEX Data Loading wizard, this approach allows to implem'
||'ent "single-step" data loading, without any further end user interaction. On the other hand, uploaded data has to match the target table structure.',
'After load, table contents can be reviewed below. Failed rows will be placed into the <strong>EBA_DEMO_LOAD_EMP_ERR$</strong> table, which can be reviewed in report at the bottom of the page.</p>',
'<p><a href="javascript:set_item();">Click here</b></a> to copy and paste, or select the text below and paste it into the <b>Copy and Paste Delimited Data</b> section. One row (<code>9000,DOE,MARKERING_ANALYST...</code>) is supposed to be rejected; it'
||' will show up as <strong>Failed Row</strong> after loading.',
'</p>',
'<pre>',
'&P32_SAMPLE_DATA.',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3711321962100458548)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3534430211386335892)
,p_button_name=>'LOAD_DATA'
,p_static_id=>'load-data'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Load Data'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3711321723857458546)
,p_name=>'P32_DATA'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(3711321628283458545)
,p_prompt=>'Copy and Paste Delimited Data'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>30
,p_cHeight=>5
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'Y',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3534434154694357232)
,p_name=>'P32_ROWS_FAILED'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3711321628283458545)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3534433910104357230)
,p_name=>'P32_ROWS_LOADED'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3711321628283458545)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3534428222160309440)
,p_name=>'P32_SAMPLE_DATA'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(4509241822355783071)
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'Empno,Ename,Job,Mgr,Hiredate,Sal,Comm,Deptno',
'8011,Campbell,CLERK,King,1-Nov-11,1300,,ACCOUNTING',
'8021,Chevy,ANALYST,Ford,20-Oct-11,3000,,RESEARCH',
'8118,BENZ,ANALYST,FORD,10-Oct-11,2800,,ACCOUNTING',
'9000,DOE,MARKERING_ANALYST,KING,10-jan-12,0,0,ACCOUNTING'))
,p_source_type=>'STATIC'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3534432242135357213)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Load Data'
,p_static_id=>'load-data'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_error_log_exists boolean := false;',
'    l_data             raw(32767);',
'begin',
'    l_data := sys.utl_raw.cast_to_raw( :P32_DATA );',
'',
'    delete from EBA_DEMO_LOAD_EMP_ERR$;',
'    ',
'    insert into EBA_DEMO_LOAD_EMP (empno, ename, job, mgr, hiredate, sal, comm, deptno ) (',
'        select to_number( col001 ),',
'               upper( col002 ),',
'               upper( col003 ),        ',
'               (select empno from eba_demo_load_emp where ename = upper( col004 ) ),',
'               to_date( col005 ), ',
'               to_number( col006 ), ',
'               to_number( col007 ), ',
'               (select deptno from eba_demo_load_dept where dname = upper( col008 ) )',
'          from table( apex_data_parser.parse(',
'                   p_content   => to_blob( l_data ),',
'                   p_skip_rows => 1,',
'                   p_file_type => apex_data_parser.c_file_type_csv ) ) )',
'   log errors into EBA_DEMO_LOAD_EMP_ERR$ ',
'   reject limit unlimited;',
'   ',
'   :P32_ROWS_LOADED := sql%rowcount;',
'   ',
'   select count(*) ',
'     into :P32_ROWS_FAILED',
'     from EBA_DEMO_LOAD_EMP_ERR$;',
'',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3711321962100458548)
,p_process_success_message=>'&P32_ROWS_LOADED. row(s) loaded successfully into EBA_DEMO_LOAD_EMP; &P32_ROWS_FAILED. row(s) failed.'
,p_internal_uid=>1864842641196032883
);
wwv_flow_imp.component_end;
end;
/
