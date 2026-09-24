prompt --application/pages/page_00031
begin
--   Manifest
--     PAGE: 00031
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
 p_id=>31
,p_name=>'PL/SQL Parser'
,p_alias=>'PL-SQL-PARSER'
,p_step_title=>'APEX_DATA_PARSER PL/SQL API'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code_onload=>'$("#parsed-data table.t-Report-report tr:first td").css( "font-weight","bold" );'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3534410411164088421)
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
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3534434482847357236)
,p_name=>'Discovered Columns'
,p_static_id=>'discovered-columns'
,p_parent_plug_id=>wwv_flow_imp.id(3534434419908357235)
,p_template=>4073835273271169698
,p_display_sequence=>50
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noBorder:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders'
,p_display_point=>'SUB_REGIONS'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select column_position, column_name, data_type, format_mask',
'  from apex_collections c, ',
'       table( apex_data_parser.get_columns( p_profile => c.clob001 ) )',
' where c.collection_name = ''FILE_PARSER_COLLECTION'' ',
'   and c.seq_id = 1'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3534434682922357238)
,p_query_column_id=>2
,p_column_alias=>'COLUMN_NAME'
,p_column_display_sequence=>2
,p_column_heading=>'Column Name'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3534435204007357243)
,p_query_column_id=>1
,p_column_alias=>'COLUMN_POSITION'
,p_column_display_sequence=>1
,p_column_heading=>'#'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3534434878077357239)
,p_query_column_id=>3
,p_column_alias=>'DATA_TYPE'
,p_column_display_sequence=>3
,p_column_heading=>'Data Type'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3534434950806357240)
,p_query_column_id=>4
,p_column_alias=>'FORMAT_MASK'
,p_column_display_sequence=>4
,p_column_heading=>'Format Mask'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3711321077817458539)
,p_plug_name=>'Information'
,p_static_id=>'information'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>',
'The <strong>APEX_DATA_PARSER.PARSE</strong> table function allows to parse XML, JSON, XLSX or CSV files. File contents are returned as columns <strong>COL001</strong> to <strong>COL300</strong>. Since the parser is implemented as a table function, pa'
||'rsing is invoked using a SELECT statement, like selecting data from a table (see report source below). Developers can thus perform arbitrary processing logic on the parser results.</p>',
'<p>Typical CSV column separators like comma, colon or tab are detected automatically. For more information on APEX_DATA_PARSER.PARSE review the Application Express API Reference.</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3534434419908357235)
,p_plug_name=>'Parsed Data'
,p_static_id=>'parsed-data'
,p_region_template_options=>'#DEFAULT#:t-TabsRegion-mod--simple'
,p_plug_template=>3224648155363603145
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P31_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3711319586218458525)
,p_name=>'Parsed Data'
,p_static_id=>'parsed-data-2'
,p_region_name=>'parsed-data'
,p_parent_plug_id=>wwv_flow_imp.id(3534434419908357235)
,p_template=>4073835273271169698
,p_display_sequence=>40
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noBorder:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders'
,p_display_point=>'SUB_REGIONS'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'-- The APEX_DATA_PARSER.PARSE function allows to "select" up to 300 columns (COL001 to COL300) from the',
'-- parsed file. This example uses the following parameters.',
'--',
'--     P_CONTENT             the file content to be parsed as a BLOB',
'--     P_FILE_NAME           the name of the file; only used to derive the file type. ',
'--     P_ADD_HEADERS_ROW     add the detected attribute names for XML or JSON files as the first row',
'--     P_XLSX_SHEET_NAME     For XLSX workbooks. The name of the worksheet to parse. If omitted or NULL, the function will',
'--                           use the first worksheet found.',
'--      ',
'select line_number, col001, col002, col003, col004, col005, col006, col007, col008, col009, col010',
'       -- more columns (col011 to col300) can be selected here.',
'  from apex_application_temp_files f, ',
'       table( apex_data_parser.parse(',
'                  p_content                     => f.blob_content,',
'                  p_add_headers_row             => ''Y'',',
'                  p_xlsx_sheet_name             => :P31_XLSX_WORKSHEET,',
'                  p_max_rows                    => 500,',
'                  p_store_profile_to_collection => ''FILE_PARSER_COLLECTION'',',
'                  p_file_name                   => f.filename ) ) p',
' where f.name = :P31_FILE',
' and line_number > 1'))
,p_header=>'Showing the first 10 columns only. Adjust the report SQL Query to show more columns.'
,p_ajax_enabled=>'Y'
,p_ajax_items_to_submit=>'P31_XLSX_WORKSHEET,P31_FILE'
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
'                  p_content                     => f.blob_content,',
'                  p_add_headers_row             => ''Y'',',
'                  p_xlsx_sheet_name             => :P31_XLSX_WORKSHEET,',
'                  p_max_rows                    => 500,',
'                  p_store_profile_to_collection => ''FILE_PARSER_COLLECTION'',',
'                  p_file_name                   => f.filename ) ) p',
'     where f.name = :P31_FILE',
'     and p.line_number = 1;',
'',
'    return l_col_headers;',
'end;'))
,p_query_headings_type=>'FUNCTION_BODY_RETURNING_COLON_DELIMITED_LIST'
,p_query_num_rows=>50
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_no_data_found=>'No data parsed. Please upload a file.'
,p_csv_output=>'Y'
,p_csv_output_link_text=>'Download'
,p_prn_output=>'N'
,p_sort_null=>'F'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711319703989458526)
,p_query_column_id=>2
,p_column_alias=>'COL001'
,p_column_display_sequence=>2
,p_column_heading=>'Col001'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711319778434458527)
,p_query_column_id=>3
,p_column_alias=>'COL002'
,p_column_display_sequence=>3
,p_column_heading=>'Col002'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711319961349458528)
,p_query_column_id=>4
,p_column_alias=>'COL003'
,p_column_display_sequence=>4
,p_column_heading=>'Col003'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320075994458529)
,p_query_column_id=>5
,p_column_alias=>'COL004'
,p_column_display_sequence=>5
,p_column_heading=>'Col004'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320117622458530)
,p_query_column_id=>6
,p_column_alias=>'COL005'
,p_column_display_sequence=>6
,p_column_heading=>'Col005'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320264379458531)
,p_query_column_id=>7
,p_column_alias=>'COL006'
,p_column_display_sequence=>7
,p_column_heading=>'Col006'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320368575458532)
,p_query_column_id=>8
,p_column_alias=>'COL007'
,p_column_display_sequence=>8
,p_column_heading=>'Col007'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320456517458533)
,p_query_column_id=>9
,p_column_alias=>'COL008'
,p_column_display_sequence=>9
,p_column_heading=>'Col008'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320617955458535)
,p_query_column_id=>10
,p_column_alias=>'COL009'
,p_column_display_sequence=>10
,p_column_heading=>'Col009'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320681659458536)
,p_query_column_id=>11
,p_column_alias=>'COL010'
,p_column_display_sequence=>11
,p_column_heading=>'Col010'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3711320853880458537)
,p_query_column_id=>1
,p_column_alias=>'LINE_NUMBER'
,p_column_display_sequence=>1
,p_column_heading=>'Line Number'
,p_column_alignment=>'RIGHT'
,p_heading_alignment=>'RIGHT'
,p_default_sort_column_sequence=>1
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3711320940921458538)
,p_plug_name=>'Report Source'
,p_static_id=>'report-source'
,p_region_template_options=>'#DEFAULT#:t-Region--noBorder:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>50
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_new_grid_row=>false
,p_plug_new_grid_column=>false
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.DISPLAY_SOURCE'
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P31_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', 'parsed-data')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3711318396372458513)
,p_plug_name=>'Upload a file'
,p_static_id=>'upload-a-file'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody:t-Form--large'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'BELOW'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3711320577132458534)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3534410411164088421)
,p_button_name=>'UPLOAD'
,p_static_id=>'upload'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Upload File'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3711319535516458524)
,p_name=>'P31_FILE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3711318396372458513)
,p_prompt=>'Upload a File'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_FILE'
,p_cSize=>100
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>'Upload a file to be parsed by the APEX_DATA_PARSER PL/SQL API. After upload, file contents can be reviewed in an APEX report. No data will be stored.'
,p_inline_help_text=>'Valid extensions: .xlsx, .txt, .csv, .js, .json, .xml'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'allow_copy_paste', 'N',
  'allow_multiple_files', 'N',
  'display_as', 'INLINE',
  'purge_file_at', 'SESSION',
  'storage_type', 'APEX_APPLICATION_TEMP_FILES')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3711321134729458540)
,p_name=>'P31_XLSX_WORKSHEET'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3711318396372458513)
,p_prompt=>'XLSX Worksheet'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select sheet_display_name, sheet_file_name',
'  from apex_application_temp_files f,',
'       table( apex_data_parser.get_xlsx_worksheets( p_content => blob_content ) ) p',
' where f.name = :P31_FILE'))
,p_cHeight=>1
,p_display_when=>'lower(:P31_FILE) like ''%xlsx'''
,p_display_when2=>'PLSQL'
,p_display_when_type=>'EXPRESSION'
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3711321507539458544)
,p_computation_sequence=>10
,p_computation_item=>'P31_XLSX_WORKSHEET'
,p_static_id=>'p31-xlsx-worksheet'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_compute_when=>'UPLOAD'
,p_compute_when_type=>'REQUEST_EQUALS_CONDITION'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(3534434337213357234)
,p_validation_name=>'Must be a valid file type'
,p_static_id=>'must-be-a-valid-file-type'
,p_validation_sequence=>10
,p_validation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'lower( :P31_FILE ) like ''%.xlsx'' or',
'lower( :P31_FILE ) like ''%.xml'' or',
'lower( :P31_FILE ) like ''%.csv'' or',
'lower( :P31_FILE ) like ''%.txt'' or',
'lower( :P31_FILE ) like ''%.js'' or',
'lower( :P31_FILE ) like ''%.json'' or',
'lower( :P31_FILE ) like ''%.geojson'''))
,p_validation2=>'PLSQL'
,p_validation_type=>'EXPRESSION'
,p_error_message=>'Only XML, JSON, XLSX or delimited (CSV) files are supported.'
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3534435024073357241)
,p_name=>'Refresh Columns'
,p_static_id=>'refresh-columns'
,p_event_sequence=>20
,p_triggering_element_type=>'REGION'
,p_triggering_region_id=>wwv_flow_imp.id(3711319586218458525)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'apexafterrefresh'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3534435102476357242)
,p_event_id=>wwv_flow_imp.id(3534435024073357241)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-refresh'
,p_action=>'NATIVE_REFRESH'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(3534434482847357236)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'maintain_pagination', 'N')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3711321211340458541)
,p_name=>'Worksheet chosen'
,p_static_id=>'worksheet-chosen'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P31_XLSX_WORKSHEET'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3711321321819458542)
,p_event_id=>wwv_flow_imp.id(3711321211340458541)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-refresh'
,p_action=>'NATIVE_REFRESH'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(3711319586218458525)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'maintain_pagination', 'N')).to_clob
);
wwv_flow_imp.component_end;
end;
/
