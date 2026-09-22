prompt --application/pages/page_00011
begin
--   Manifest
--     PAGE: 00011
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
 p_id=>11
,p_name=>'CSV Load'
,p_alias=>'CSV-LOAD'
,p_step_title=>'CSV Load'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2554269025885801742)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--info'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>Use this page to load employees data in <strong>CSV</strong> file format.  Download sample <a href="#APP_IMAGES#Employees.csv">Employees.csv</a> file to try the load.</a>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3338224692163735627)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>80
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(11521794561627835810)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3328235364540059721)
,p_plug_name=>'Button Bar'
,p_static_id=>'button-bar'
,p_parent_plug_id=>wwv_flow_imp.id(3328237402727059731)
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>20
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P11_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4150879311661266395)
,p_plug_name=>'Button Bar'
,p_static_id=>'button-bar-2'
,p_parent_plug_id=>wwv_flow_imp.id(4150872153511197917)
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>10
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4150872153511197917)
,p_plug_name=>'Copy and Paste  Delimited Data'
,p_static_id=>'copy-and-paste-delimited-data'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>50
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4150872561277197918)
,p_plug_name=>'Copy and Paste Delimited Data'
,p_static_id=>'copy-and-paste-delimited-data-2'
,p_parent_plug_id=>wwv_flow_imp.id(4150872153511197917)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>20
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NULL'
,p_plug_display_when_condition=>'P11_DATA'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(2554269108227801743)
,p_name=>'Employees'
,p_static_id=>'employees'
,p_template=>2665811232373458102
,p_display_sequence=>70
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
 p_id=>wwv_flow_imp.id(2554270892259801761)
,p_query_column_id=>7
,p_column_alias=>'COMM'
,p_column_display_sequence=>70
,p_column_heading=>'Comm'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554271142008801763)
,p_query_column_id=>9
,p_column_alias=>'CREATED'
,p_column_display_sequence=>90
,p_column_heading=>'Created'
,p_column_format=>'SINCE'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554271020765801762)
,p_query_column_id=>8
,p_column_alias=>'DEPTNO'
,p_column_display_sequence=>80
,p_column_heading=>'Deptno'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270264057801755)
,p_query_column_id=>1
,p_column_alias=>'EMPNO'
,p_column_display_sequence=>10
,p_column_heading=>'Empno'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270423581801756)
,p_query_column_id=>2
,p_column_alias=>'ENAME'
,p_column_display_sequence=>20
,p_column_heading=>'Ename'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270749221801759)
,p_query_column_id=>5
,p_column_alias=>'HIREDATE'
,p_column_display_sequence=>50
,p_column_heading=>'Hiredate'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270549811801757)
,p_query_column_id=>3
,p_column_alias=>'JOB'
,p_column_display_sequence=>30
,p_column_heading=>'Job'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554271231317801764)
,p_query_column_id=>10
,p_column_alias=>'LAST_UPDATED'
,p_column_display_sequence=>100
,p_column_heading=>'Last Updated'
,p_column_format=>'SINCE'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270575419801758)
,p_query_column_id=>4
,p_column_alias=>'MGR'
,p_column_display_sequence=>40
,p_column_heading=>'Mgr'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2554270819458801760)
,p_query_column_id=>6
,p_column_alias=>'SAL'
,p_column_display_sequence=>60
,p_column_heading=>'Sal'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3328239882276059741)
,p_plug_name=>'Loaded File'
,p_static_id=>'loaded-file'
,p_parent_plug_id=>wwv_flow_imp.id(3328237402727059731)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>40
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P11_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4150873829909197950)
,p_plug_name=>'Pasted Data'
,p_static_id=>'pasted-data'
,p_parent_plug_id=>wwv_flow_imp.id(4150872153511197917)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P11_DATA'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3328241376826059745)
,p_name=>'Preview'
,p_static_id=>'preview'
,p_parent_plug_id=>wwv_flow_imp.id(3328237402727059731)
,p_template=>4073835273271169698
,p_display_sequence=>60
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders:t-Report--hideNoPagination'
,p_display_point=>'SUB_REGIONS'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select p.line_number,',
'       p.col001, p.col002, p.col003, p.col004, p.col005, p.col006, p.col007, p.col008, p.col009, p.col010',
'       -- add more columns (col011 to col300) here.',
'  from apex_application_temp_files f, ',
'       table( apex_data_parser.parse(',
'                  p_content          => f.blob_content,',
'                  p_file_name        => f.filename,',
'                  p_add_headers_row   => ''Y'',',
'                  p_csv_enclosed      => ''"'',',
'                  p_file_charset      => ''WE8ISO8859P1'',',
'                  p_max_rows         => 10 ) ) p',
' where f.name = :P11_FILE',
' and p.line_number > 1'))
,p_display_when_condition=>'P11_FILE'
,p_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_headings=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_col_headers varchar2(32767);',
'begin',
'    select p.line_number || '':'' ||',
'           p.col001 || '':'' || p.col002 || '':'' || p.col003 || '':'' || p.col004 || '':'' || p.col005 || '':'' || ',
'           p.col006 || '':'' ||  p.col007 || '':'' || p.col008 || '':'' || p.col009 || '':'' || p.col010',
'      into l_col_headers',
'           -- add more columns (col011 to col300) here.',
'      from apex_application_temp_files f, ',
'           table( apex_data_parser.parse(',
'                      p_content          => f.blob_content,',
'                      p_file_name        => f.filename,',
'                      p_add_headers_row   => ''Y'',',
'                      p_csv_enclosed      => ''"'',',
'                      p_file_charset      => ''WE8ISO8859P1'',',
'                      p_max_rows         => 10 ) ) p',
'     where f.name = :P11_FILE',
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
 p_id=>wwv_flow_imp.id(3328242213611059768)
,p_query_column_id=>2
,p_column_alias=>'COL001'
,p_column_display_sequence=>2
,p_column_heading=>'Col001'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328242572447059768)
,p_query_column_id=>3
,p_column_alias=>'COL002'
,p_column_display_sequence=>3
,p_column_heading=>'Col002'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328242983183059768)
,p_query_column_id=>4
,p_column_alias=>'COL003'
,p_column_display_sequence=>4
,p_column_heading=>'Col003'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328243423136059769)
,p_query_column_id=>5
,p_column_alias=>'COL004'
,p_column_display_sequence=>5
,p_column_heading=>'Col004'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328243758621059769)
,p_query_column_id=>6
,p_column_alias=>'COL005'
,p_column_display_sequence=>6
,p_column_heading=>'Col005'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328244172346059769)
,p_query_column_id=>7
,p_column_alias=>'COL006'
,p_column_display_sequence=>7
,p_column_heading=>'Col006'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328244577145059769)
,p_query_column_id=>8
,p_column_alias=>'COL007'
,p_column_display_sequence=>8
,p_column_heading=>'Col007'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328244964733059770)
,p_query_column_id=>9
,p_column_alias=>'COL008'
,p_column_display_sequence=>9
,p_column_heading=>'Col008'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328245401569059770)
,p_query_column_id=>10
,p_column_alias=>'COL009'
,p_column_display_sequence=>10
,p_column_heading=>'Col009'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328245815137059770)
,p_query_column_id=>11
,p_column_alias=>'COL010'
,p_column_display_sequence=>11
,p_column_heading=>'Col010'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328241837095059764)
,p_query_column_id=>1
,p_column_alias=>'LINE_NUMBER'
,p_column_display_sequence=>1
,p_column_heading=>'Line Number'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(4150891143200388007)
,p_name=>'Preview'
,p_static_id=>'preview-2'
,p_parent_plug_id=>wwv_flow_imp.id(4150872153511197917)
,p_template=>4073835273271169698
,p_display_sequence=>80
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders:t-Report--hideNoPagination'
,p_display_point=>'SUB_REGIONS'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select p.line_number,',
'       p.col001, p.col002, p.col003, p.col004, p.col005, p.col006, p.col007, p.col008, p.col009, p.col010',
'       -- add more columns (col011 to col300) here.',
'  from table( apex_data_parser.parse(',
'                  p_content          => to_blob(sys.utl_raw.cast_to_raw( :P11_DATA )),',
'                  p_file_name        => ''pasted_data.csv'', ',
'                  p_add_headers_row   => ''Y'',',
'                  p_csv_enclosed      => ''"'',',
'                  p_file_charset      => ''WE8ISO8859P1'',',
'                  p_max_rows         => 10 ) ) p',
'  where p.line_number > 1'))
,p_display_when_condition=>'P11_DATA'
,p_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_ajax_enabled=>'Y'
,p_ajax_items_to_submit=>'P11_DATA'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_headings=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_col_headers varchar2(32767);',
'begin',
'    select p.line_number || '':'' || ',
'         p.col001 || '':'' || p.col002 || '':'' || p.col003 || '':'' || p.col004 || '':'' ||  p.col005 || '':'' ||',
'         p.col006 || '':'' || p.col007 || '':'' || p.col008 || '':'' || p.col009 || '':'' || p.col010',
'    into l_col_headers',
'         -- add more columns (col011 to col300) here.',
'    from table( apex_data_parser.parse(',
'                    p_content          => to_blob(sys.utl_raw.cast_to_raw( :P11_DATA )),',
'                    p_file_name        => ''pasted_data.csv'', ',
'                    p_add_headers_row   => ''Y'',',
'                    p_csv_enclosed      => ''"'',',
'                    p_file_charset      => ''WE8ISO8859P1'',',
'                    p_max_rows         => 10 ) ) p',
'    where p.line_number = 1;',
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
 p_id=>wwv_flow_imp.id(3328767756490356752)
,p_query_column_id=>2
,p_column_alias=>'COL001'
,p_column_display_sequence=>2
,p_column_heading=>'Col001'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328768223923356753)
,p_query_column_id=>3
,p_column_alias=>'COL002'
,p_column_display_sequence=>3
,p_column_heading=>'Col002'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328768640212356753)
,p_query_column_id=>4
,p_column_alias=>'COL003'
,p_column_display_sequence=>4
,p_column_heading=>'Col003'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328768977945356753)
,p_query_column_id=>5
,p_column_alias=>'COL004'
,p_column_display_sequence=>5
,p_column_heading=>'Col004'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328769410485356754)
,p_query_column_id=>6
,p_column_alias=>'COL005'
,p_column_display_sequence=>6
,p_column_heading=>'Col005'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328769767681356754)
,p_query_column_id=>7
,p_column_alias=>'COL006'
,p_column_display_sequence=>7
,p_column_heading=>'Col006'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328770193719356754)
,p_query_column_id=>8
,p_column_alias=>'COL007'
,p_column_display_sequence=>8
,p_column_heading=>'Col007'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328770637084356755)
,p_query_column_id=>9
,p_column_alias=>'COL008'
,p_column_display_sequence=>9
,p_column_heading=>'Col008'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328771045460356755)
,p_query_column_id=>10
,p_column_alias=>'COL009'
,p_column_display_sequence=>10
,p_column_heading=>'Col009'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328771449964356755)
,p_query_column_id=>11
,p_column_alias=>'COL010'
,p_column_display_sequence=>11
,p_column_heading=>'Col010'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3328767451865356748)
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
 p_id=>wwv_flow_imp.id(2554271292052801765)
,p_plug_name=>'RDS'
,p_static_id=>'rds'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'NATIVE_DISPLAY_SELECTOR'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_region_icons', 'N',
  'include_show_all', 'N',
  'rds_mode', 'STANDARD',
  'remember_selection', 'NO')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3328237783778059732)
,p_plug_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_parent_plug_id=>wwv_flow_imp.id(3328237402727059731)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NULL'
,p_plug_display_when_condition=>'P11_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3328237402727059731)
,p_plug_name=>'Upload File'
,p_static_id=>'upload-file'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3328760267315235208)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(4150879311661266395)
,p_button_name=>'CLEAR_DATA'
,p_static_id=>'clear-data'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Clear'
,p_button_position=>'NEXT'
,p_button_condition=>'P11_DATA'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3328235918455059722)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3328235364540059721)
,p_button_name=>'CLEAR_FILE'
,p_static_id=>'clear-file'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Clear'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3328760727804235209)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(4150879311661266395)
,p_button_name=>'LOAD_DATA'
,p_static_id=>'load-data'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Load Data'
,p_button_position=>'NEXT'
,p_button_condition=>'P11_DATA'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3328236180915059729)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3328235364540059721)
,p_button_name=>'LOAD_FILE'
,p_static_id=>'load-file'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Load Data'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3328761074919235210)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(4150879311661266395)
,p_button_name=>'NEXT'
,p_static_id=>'next'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--iconRight'
,p_button_template_id=>2084305881903810008
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Next'
,p_button_position=>'NEXT'
,p_button_condition=>'P11_DATA'
,p_button_condition_type=>'ITEM_IS_NULL'
,p_icon_css_classes=>'fa-angle-right'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3328751553596166706)
,p_name=>'P11_COPY_PASTE_ERROR_ROW_COUNT'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(4150872561277197918)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3328751101809166703)
,p_name=>'P11_DATA'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(4150872561277197918)
,p_prompt=>'Copy and Paste Delimited Data'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>60
,p_cHeight=>10
,p_field_template=>2042262243893469891
,p_item_template_options=>'#DEFAULT#:t-Form-fieldContainer--stretchInputs'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'Y',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3328238204222059733)
,p_name=>'P11_FILE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3328237783778059732)
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
  'dropzone_description', 'Supported formats CSV, TXT',
  'max_file_size', '5000',
  'purge_file_at', 'SESSION',
  'storage_type', 'APEX_APPLICATION_TEMP_FILES')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3328238576473059736)
,p_name=>'P11_FILE_ERROR_ROW_COUNT'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3328237783778059732)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3328240250591059742)
,p_name=>'P11_FILE_NAME'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3328239882276059741)
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
 p_id=>wwv_flow_imp.id(3328752163443166707)
,p_name=>'P11_PASTED_DATA'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(4150873829909197950)
,p_item_default=>'Pasted Data'
,p_prompt=>'Pasted Data'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>2042262243893469891
,p_item_icon_css_classes=>'fa-clipboard-arrow-up fa-2x'
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3328240747939059742)
,p_computation_sequence=>10
,p_computation_item=>'P11_FILE_NAME'
,p_static_id=>'p11-file-name'
,p_computation_type=>'QUERY'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select filename',
'  from apex_application_temp_files ',
' where name = :P11_FILE'))
,p_compute_when=>':P11_FILE is not null and :REQUEST = ''LOAD_FILE'''
,p_compute_when_text=>'PLSQL'
,p_compute_when_type=>'EXPRESSION'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(3328241055766059745)
,p_validation_name=>'Is valid file type'
,p_static_id=>'is-valid-file-type'
,p_validation_sequence=>10
,p_validation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if apex_data_parser.assert_file_type(',
'       p_file_name => :P11_FILE_NAME,',
'       p_file_type => apex_data_parser.c_file_type_csv )',
'then',
'    return true;',
'else',
'    :P11_FILE := null;',
'    return false;',
'end if;'))
,p_validation2=>'PLSQL'
,p_validation_type=>'FUNC_BODY_RETURNING_BOOLEAN'
,p_error_message=>'Invalid file type. Supported file types CSV, TXT.'
,p_when_button_pressed=>wwv_flow_imp.id(3328236180915059729)
,p_associated_item=>wwv_flow_imp.id(3328238204222059733)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3328238987777059736)
,p_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P11_FILE'
,p_condition_element=>'P11_FILE'
,p_triggering_condition_type=>'NOT_NULL'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3328239539757059737)
,p_event_id=>wwv_flow_imp.id(3328238987777059736)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-submit-page'
,p_action=>'NATIVE_SUBMIT_PAGE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_processing', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3328237064610059730)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear File Cache'
,p_static_id=>'clear-file-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when=>':REQUEST = ''CLEAR_FILE'' or :P11_FILE_ERROR_ROW_COUNT = 0'
,p_process_when_type=>'EXPRESSION'
,p_process_when2=>'PLSQL'
,p_internal_uid=>1658647463670735400
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2554271441329801766)
,p_process_sequence=>50
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Pasted Data Cache'
,p_static_id=>'clear-pasted-data-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when=>':REQUEST = ''CLEAR_DATA'' or :P11_COPY_PASTE_ERROR_ROW_COUNT = 0'
,p_process_when_type=>'EXPRESSION'
,p_process_when2=>'PLSQL'
,p_internal_uid=>884681840390477436
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3328236660448059729)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_DATA_LOADING'
,p_process_name=>'Load File Data'
,p_static_id=>'load-file-data'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'data_load_definition_id', wwv_flow_imp.id(3336238955261657208),
  'error_row_count_item', 'P11_FILE_ERROR_ROW_COUNT',
  'source_data_type', 'FILE',
  'source_file_browse_item', 'P11_FILE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3328236180915059729)
,p_process_when=>'P11_FILE'
,p_process_when_type=>'ITEM_IS_NOT_NULL'
,p_internal_uid=>1658647059508735399
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3328757244597196337)
,p_process_sequence=>40
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_DATA_LOADING'
,p_process_name=>'Load Pasted Data'
,p_static_id=>'load-pasted-data'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'data_load_definition_id', wwv_flow_imp.id(3336238955261657208),
  'error_row_count_item', 'P11_COPY_PASTE_ERROR_ROW_COUNT',
  'source_data_type', 'TEXT',
  'source_textarea_item', 'P11_DATA')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3328760727804235209)
,p_process_when=>'P11_DATA'
,p_process_when_type=>'ITEM_IS_NOT_NULL'
,p_internal_uid=>1659167643657872007
);
wwv_flow_imp.component_end;
end;
/
