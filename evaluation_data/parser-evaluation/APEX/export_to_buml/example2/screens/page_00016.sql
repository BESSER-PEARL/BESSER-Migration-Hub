prompt --application/pages/page_00016
begin
--   Manifest
--     PAGE: 00016
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
 p_id=>16
,p_name=>'Multiple File Types Load'
,p_alias=>'MULTI-FILETYPES-LOAD'
,p_step_title=>'Multiple File Types Load'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4198714094990407410)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--info'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page allows uploading employees data in CSV, XLSX, XML or JSON file types.  It uses <a href="https://docs.oracle.com/en/database/oracle/application-express/21.1/aeapi/APEX_DATA_LOADING.html" target="_new">APEX_DATA_LOADING</a> package to call'
||' different application data loading definition based on file types. Download sample files to try the load.</p>',
'',
'<ul>',
'<li><a href="#APP_IMAGES#Employees.csv">Employees.csv</a></li>',
'<li><a href="#APP_IMAGES#Employees.xlsx">Employees.xlsx</a></li>',
'<li><a href="#APP_IMAGES#Employees.xml">Employees.xml</a></li>',
'<li><a href="#APP_IMAGES#Employees.json">Employees.json</a></li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(5002606662674990993)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>60
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(11521794561627835810)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3329318113014052430)
,p_plug_name=>'Button Bar'
,p_static_id=>'button-bar'
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P16_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3329320126972052437)
,p_plug_name=>'Data Source'
,p_static_id=>'data-source'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--hiddenOverflow'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(4198738743648511978)
,p_name=>'Employees'
,p_static_id=>'employees'
,p_template=>2665811232373458102
,p_display_sequence=>50
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
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329372856690355187)
,p_query_column_id=>7
,p_column_alias=>'COMM'
,p_column_display_sequence=>70
,p_column_heading=>'Comm'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329373691082355188)
,p_query_column_id=>9
,p_column_alias=>'CREATED'
,p_column_display_sequence=>90
,p_column_heading=>'Created'
,p_column_format=>'SINCE'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329373304066355188)
,p_query_column_id=>8
,p_column_alias=>'DEPTNO'
,p_column_display_sequence=>80
,p_column_heading=>'Deptno'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329370536782355185)
,p_query_column_id=>1
,p_column_alias=>'EMPNO'
,p_column_display_sequence=>10
,p_column_heading=>'Empno'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329370905147355186)
,p_query_column_id=>2
,p_column_alias=>'ENAME'
,p_column_display_sequence=>20
,p_column_heading=>'Ename'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329372146992355187)
,p_query_column_id=>5
,p_column_alias=>'HIREDATE'
,p_column_display_sequence=>50
,p_column_heading=>'Hiredate'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329371299370355186)
,p_query_column_id=>3
,p_column_alias=>'JOB'
,p_column_display_sequence=>30
,p_column_heading=>'Job'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329374109922355188)
,p_query_column_id=>10
,p_column_alias=>'LAST_UPDATED'
,p_column_display_sequence=>100
,p_column_heading=>'Last Updated'
,p_column_format=>'SINCE'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329371680065355187)
,p_query_column_id=>4
,p_column_alias=>'MGR'
,p_column_display_sequence=>40
,p_column_heading=>'Mgr'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329372457497355187)
,p_query_column_id=>6
,p_column_alias=>'SAL'
,p_column_display_sequence=>60
,p_column_heading=>'Sal'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3329322491791052442)
,p_plug_name=>'Loaded File'
,p_static_id=>'loaded-file'
,p_parent_plug_id=>wwv_flow_imp.id(3329320126972052437)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>40
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P16_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3329325431997052445)
,p_name=>'Preview'
,p_static_id=>'preview'
,p_template=>4073835273271169698
,p_display_sequence=>40
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders:t-Report--hideNoPagination'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select p.line_number,',
'       p.col001, p.col002, p.col003, p.col004, p.col005, p.col006, p.col007, p.col008, p.col009, p.col010',
'       -- add more columns (col011 to col300) here.',
'  from apex_application_temp_files f, ',
'       table( apex_data_parser.parse(',
'                  p_content           => f.blob_content,',
'                  p_file_name         => f.filename,',
'                  p_xlsx_sheet_name   => case when :P16_FILE_TYPE = 1 and :P16_XLSX_WORKSHEET is not null then :P16_XLSX_WORKSHEET end,',
'                  p_add_headers_row   => ''Y'',',
'                  p_csv_enclosed      => case when :P16_FILE_TYPE = 2 then ''"'' end,',
'                  p_file_charset      => case when :P16_FILE_TYPE = 2 then',
'                                             ''WE8ISO8859P1''',
'                                         else',
'                                             ''AL32UTF8''',
'                                         end,',
'                  p_max_rows          => 10 ) ) p',
' where f.name = :P16_FILE',
' and p.line_number > 1'))
,p_display_when_condition=>'P16_FILE'
,p_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_ajax_enabled=>'Y'
,p_ajax_items_to_submit=>'P16_FILE'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_headings=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_col_headers varchar2(32000);',
'begin',
'    select p.line_number || '':'' || p.col001 || '':'' || p.col002 || '':'' || p.col003 || '':'' || p.col004 || '':'' || p.col005 || '':'' || ',
'           p.col006 || '':'' || p.col007 || '':'' || p.col008 || '':'' || p.col009 || '':'' || p.col010',
'      into l_col_headers',
'      from apex_application_temp_files f, ',
'           table( apex_data_parser.parse(',
'                      p_content           => f.blob_content,',
'                      p_file_name         => f.filename,',
'                      p_xlsx_sheet_name   => case when :P16_FILE_TYPE = 1 and :P16_XLSX_WORKSHEET is not null then :P16_XLSX_WORKSHEET end,',
'                      p_add_headers_row   => ''Y'',',
'                      p_csv_enclosed      => case when :P16_FILE_TYPE = 2 then ''"'' end,',
'                      p_file_charset      => case when :P16_FILE_TYPE = 2 then',
'                                                 ''WE8ISO8859P1''',
'                                             else',
'                                                 ''AL32UTF8''',
'                                             end,',
'                      p_max_rows          => 10 ) ) p',
'     where f.name = :P16_FILE',
'     and p.line_number = 1;',
'',
'    return l_col_headers;',
'end;'))
,p_query_headings_type=>'FUNCTION_BODY_RETURNING_COLON_DELIMITED_LIST'
,p_query_num_rows=>50
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_no_data_found=>'no data found'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_query_row_count_max=>500
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329326199240052451)
,p_query_column_id=>2
,p_column_alias=>'COL001'
,p_column_display_sequence=>2
,p_column_heading=>'Col001'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329326614709052451)
,p_query_column_id=>3
,p_column_alias=>'COL002'
,p_column_display_sequence=>3
,p_column_heading=>'Col002'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329326988874052451)
,p_query_column_id=>4
,p_column_alias=>'COL003'
,p_column_display_sequence=>4
,p_column_heading=>'Col003'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329327422069052452)
,p_query_column_id=>5
,p_column_alias=>'COL004'
,p_column_display_sequence=>5
,p_column_heading=>'Col004'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329327801939052452)
,p_query_column_id=>6
,p_column_alias=>'COL005'
,p_column_display_sequence=>6
,p_column_heading=>'Col005'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329328242950052452)
,p_query_column_id=>7
,p_column_alias=>'COL006'
,p_column_display_sequence=>7
,p_column_heading=>'Col006'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329328646533052452)
,p_query_column_id=>8
,p_column_alias=>'COL007'
,p_column_display_sequence=>8
,p_column_heading=>'Col007'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329329053500052453)
,p_query_column_id=>9
,p_column_alias=>'COL008'
,p_column_display_sequence=>9
,p_column_heading=>'Col008'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329329373646052453)
,p_query_column_id=>10
,p_column_alias=>'COL009'
,p_column_display_sequence=>10
,p_column_heading=>'Col009'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329329800124052453)
,p_query_column_id=>11
,p_column_alias=>'COL010'
,p_column_display_sequence=>11
,p_column_heading=>'Col010'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3329325827061052450)
,p_query_column_id=>1
,p_column_alias=>'LINE_NUMBER'
,p_column_display_sequence=>1
,p_column_heading=>'Line Number'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3329320485061052437)
,p_plug_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_parent_plug_id=>wwv_flow_imp.id(3329320126972052437)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NULL'
,p_plug_display_when_condition=>'P16_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3329318586506052431)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3329318113014052430)
,p_button_name=>'CLEAR'
,p_static_id=>'clear'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Clear'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3329318947259052431)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3329318113014052430)
,p_button_name=>'LOAD'
,p_static_id=>'load'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Load Data'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329321275125052441)
,p_name=>'P16_ERROR_ROW_COUNT'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3329320485061052437)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329320886030052438)
,p_name=>'P16_FILE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3329320485061052437)
,p_prompt=>'Upload a File'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_FILE'
,p_grid_label_column_span=>0
,p_field_template=>2042262243893469891
,p_item_template_options=>'#DEFAULT#:t-Form-fieldContainer--stretchInputs'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'allow_copy_paste', 'N',
  'allow_multiple_files', 'N',
  'display_as', 'DROPZONE_BLOCK',
  'dropzone_description', 'Supported formats CSV, TXT, XLSX, XML, JSON',
  'max_file_size', '5000',
  'purge_file_at', 'SESSION',
  'storage_type', 'APEX_APPLICATION_TEMP_FILES')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329322859597052442)
,p_name=>'P16_FILE_NAME'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3329322491791052442)
,p_item_default=>'Pasted Data'
,p_prompt=>'Loaded File'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329334190665093321)
,p_name=>'P16_FILE_TYPE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3329322491791052442)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329334545422093324)
,p_name=>'P16_PROCESSED_ROW_COUNT'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(3329320485061052437)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3329324153813052443)
,p_name=>'P16_XLSX_WORKSHEET'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(3329322491791052442)
,p_prompt=>'XLSX Worksheet'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select p.sheet_display_name,',
'       p.sheet_file_name',
'  from apex_application_temp_files f,',
'       table( apex_data_parser.get_xlsx_worksheets( p_content => f.blob_content ) ) p',
' where f.name = :P16_FILE'))
,p_cHeight=>1
,p_display_when=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_sheet_count number;',
'begin',
'    if :P16_FILE_TYPE != apex_data_parser.c_file_type_xlsx then',
'        return false;',
'    end if;',
'',
'    select count(*)',
'      into l_sheet_count',
'      from apex_application_temp_files f,',
'           table( apex_data_parser.get_xlsx_worksheets( p_content => f.blob_content ) ) p',
'     where f.name = :P16_FILE;',
'    ',
'     -- display if the XSLX file contains multiple worksheets',
'    return ( l_sheet_count > 1 );',
'exception',
'    when others then ',
'        return false;',
'end;'))
,p_display_when2=>'PLSQL'
,p_display_when_type=>'FUNCTION_BODY'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3329323400695052442)
,p_computation_sequence=>10
,p_computation_item=>'P16_FILE_NAME'
,p_static_id=>'p16-file-name'
,p_computation_type=>'QUERY'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select filename',
'  from apex_application_temp_files ',
' where name = :P16_FILE'))
,p_compute_when=>'P16_FILE'
,p_compute_when_type=>'ITEM_IS_NOT_NULL'
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3329334278436093322)
,p_computation_sequence=>10
,p_computation_item=>'P16_FILE_TYPE'
,p_static_id=>'p16-file-type'
,p_computation_type=>'EXPRESSION'
,p_computation_language=>'PLSQL'
,p_computation=>'apex_data_parser.get_file_type( p_file_name => :P16_FILE )'
,p_compute_when=>'P16_FILE'
,p_compute_when_type=>'ITEM_IS_NOT_NULL'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(3329323775344052443)
,p_validation_name=>'Is valid file type'
,p_static_id=>'is-valid-file-type'
,p_validation_sequence=>10
,p_validation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if :P16_FILE_TYPE in (',
'    apex_data_parser.c_file_type_csv,',
'    apex_data_parser.c_file_type_xlsx,',
'    apex_data_parser.c_file_type_xml,',
'    apex_data_parser.c_file_type_json )',
'then',
'    return true;',
'else',
'    :P16_FILE := null;',
'    return false;',
'end if;'))
,p_validation2=>'PLSQL'
,p_validation_type=>'FUNC_BODY_RETURNING_BOOLEAN'
,p_error_message=>'Invalid file type. Supported file types are CSV, TXT, XLSX, XML, JSON.'
,p_associated_item=>wwv_flow_imp.id(3329320886030052438)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3329324530465052445)
,p_name=>'Submit worksheet on change'
,p_static_id=>'submit-worksheet-on-change'
,p_event_sequence=>20
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P16_XLSX_WORKSHEET'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3329325024208052445)
,p_event_id=>wwv_flow_imp.id(3329324530465052445)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-submit-page'
,p_action=>'NATIVE_SUBMIT_PAGE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_processing', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3329321724451052441)
,p_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P16_FILE'
,p_condition_element=>'P16_FILE'
,p_triggering_condition_type=>'NOT_NULL'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3329322250369052441)
,p_event_id=>wwv_flow_imp.id(3329321724451052441)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-submit-page'
,p_action=>'NATIVE_SUBMIT_PAGE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_processing', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3329319770086052437)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Cache'
,p_static_id=>'clear-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when=>':REQUEST = ''CLEAR'' or :P16_ERROR_ROW_COUNT = 0'
,p_process_when_type=>'EXPRESSION'
,p_process_when2=>'PLSQL'
,p_internal_uid=>1659730169146728107
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3329334366998093323)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Load Data'
,p_static_id=>'load-data'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'DECLARE',
'    l_file blob;',
'    l_load_result apex_data_loading.t_data_load_result;',
'BEGIN',
'    SELECT blob_content',
'      INTO l_file',
'      FROM apex_application_temp_files',
'     WHERE name = :P16_FILE;',
'    ',
'    if :P16_FILE_TYPE = apex_data_parser.c_file_type_csv then',
'        l_load_result := apex_data_loading.load_data (',
'                             p_static_id    => ''CSV_Load'',',
'                             p_data_to_load => l_file );',
'    elsif :P16_FILE_TYPE = apex_data_parser.c_file_type_xlsx then',
'        l_load_result := apex_data_loading.load_data (',
'                             p_static_id       => ''XLSX_Load'',',
'                             p_data_to_load    => l_file,',
'                             p_xlsx_sheet_name => :P16_XLSX_WORKSHEET );',
'    elsif :P16_FILE_TYPE = apex_data_parser.c_file_type_xml then',
'        l_load_result := apex_data_loading.load_data (',
'                             p_static_id    => ''XML_Load'',',
'                             p_data_to_load => l_file );',
'    elsif :P16_FILE_TYPE = apex_data_parser.c_file_type_json then',
'        l_load_result := apex_data_loading.load_data (',
'                             p_static_id    => ''JSON_Load'',',
'                             p_data_to_load => l_file );',
'    end if;',
'',
'    :P16_ERROR_ROW_COUNT := l_load_result.error_rows;',
'    :P16_PROCESSED_ROW_COUNT := l_load_result.processed_rows;',
'END;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Failed to load &P16_ERROR_ROW_COUNT!HTML. rows.'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3329318947259052431)
,p_process_success_message=>'Loaded &P16_PROCESSED_ROW_COUNT!HTML. rows.'
,p_internal_uid=>1659744766058768993
);
wwv_flow_imp.component_end;
end;
/
