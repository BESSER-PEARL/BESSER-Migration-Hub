prompt --application/pages/page_00017
begin
--   Manifest
--     PAGE: 00017
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
 p_id=>17
,p_name=>'Background Load'
,p_alias=>'BACKGROUND-LOAD'
,p_step_title=>'Background Load'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4206236394783497011)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--info'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>If you are loading large datasets, the loading can run into a long running page process.  ',
'   If the instance is set up with a resource limit, you will see the maximum limit has been reached for this type of load. To load large data efficiently, ',
'   you can run the loading process in the background.</p>',
'<p>This page illustrates how to use a process of the <strong>Execution Chain</strong> type to send the',
'   Data Loading execution to the background. The status of the background loading operation can be ',
'   monitored in the <strong>APEX_APPL_PAGE_BG_PROC_STATUS</strong> APEX view. You can also review',
'   currently running background executions by clicking <strong>Session</strong> in the ',
'   <strong>Developer Toolbar</strong> and then viewing <strong>Background Executions</strong>.',
'   </p>',
'',
'<p>Download sample <a href="#APP_IMAGES#SalesData.zip">SalesData.zip</a> file.</a> This page uses <em>APEX_ZIP</em> package to unzip the zip file.  You can upload either the ZIP or CSV file.</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(5834798628003106348)
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
 p_id=>wwv_flow_imp.id(3331540110890254608)
,p_plug_name=>'Button Bar'
,p_static_id=>'button-bar'
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P17_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3338224360911735624)
,p_plug_name=>'Create Job Privilege is Missing'
,p_static_id=>'create-job-privilege-is-missing'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--warning'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>To use this page, your application parsing schema must have <em>CREATE JOB</em> privilege. Contact your database administrator to get the <strong>CREATE JOB</strong> privilege granted using the following SQL statement.</p>',
'<pre>grant CREATE JOB to #OWNER#;</pre>',
'<p>Then log out and back into the application and revisit this page. </p>'))
,p_plug_required_role=>'!'||wwv_flow_imp.id(3338778276393463645)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3331542145245254627)
,p_plug_name=>'Data Source'
,p_static_id=>'data-source'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>40
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_required_role=>wwv_flow_imp.id(3338778276393463645)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3331544624055254640)
,p_plug_name=>'Loaded File'
,p_static_id=>'loaded-file'
,p_parent_plug_id=>wwv_flow_imp.id(3331542145245254627)
,p_region_template_options=>'#DEFAULT#:t-Form--large:t-Form--stretchInputs'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>40
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_plug_display_when_condition=>'P17_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3331546087936254658)
,p_name=>'Preview'
,p_static_id=>'preview'
,p_template=>4073835273271169698
,p_display_sequence=>50
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
'                  p_content          => eba_demo_data_load.zip_to_csv(',
'                                            p_blob_content => f.blob_content,',
'                                            p_mime_type    => f.mime_type ),',
'                  p_file_name        => f.filename,',
'                  p_file_type        => 2,  -- csv file type',
'                  p_add_headers_row  => ''Y'',',
'                  p_csv_enclosed     => ''"'',',
'                  p_file_charset     => ''WE8ISO8859P1'',',
'                  p_max_rows         => 10 ) ) p',
' where f.name = :P17_FILE',
' and p.line_number > 1;'))
,p_display_when_condition=>'P17_FILE'
,p_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_headings=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_col_headers varchar2(32767);',
'begin',
'    select p.line_number || '':'' || ',
'       p.col001 || '':'' || p.col002 || '':'' || p.col003 || '':'' || p.col004 || '':'' || p.col005 || '':'' || ',
'       p.col006 || '':'' || p.col007 || '':'' || p.col008 || '':'' || p.col009 || '':'' || p.col010',
'    into l_col_headers',
'       -- add more columns (col011 to col300) here.',
'     from apex_application_temp_files f, ',
'          table( apex_data_parser.parse(',
'                     p_content          => eba_demo_data_load.zip_to_csv(',
'                                               p_blob_content => f.blob_content,',
'                                               p_mime_type    => f.mime_type ),',
'                     p_file_name        => f.filename,',
'                     p_file_type        => 2,  -- csv file type',
'                     p_add_headers_row  => ''Y'',',
'                     p_csv_enclosed     => ''"'',',
'                     p_file_charset     => ''WE8ISO8859P1'',',
'                     p_max_rows         => 10 ) ) p',
'    where f.name = :P17_FILE',
'    and p.line_number = 1;',
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
 p_id=>wwv_flow_imp.id(3331546943398254719)
,p_query_column_id=>2
,p_column_alias=>'COL001'
,p_column_display_sequence=>2
,p_column_heading=>'Col001'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331547340261254719)
,p_query_column_id=>3
,p_column_alias=>'COL002'
,p_column_display_sequence=>3
,p_column_heading=>'Col002'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331547700320254720)
,p_query_column_id=>4
,p_column_alias=>'COL003'
,p_column_display_sequence=>4
,p_column_heading=>'Col003'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331548056754254722)
,p_query_column_id=>5
,p_column_alias=>'COL004'
,p_column_display_sequence=>5
,p_column_heading=>'Col004'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331548480785254722)
,p_query_column_id=>6
,p_column_alias=>'COL005'
,p_column_display_sequence=>6
,p_column_heading=>'Col005'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331548860618254722)
,p_query_column_id=>7
,p_column_alias=>'COL006'
,p_column_display_sequence=>7
,p_column_heading=>'Col006'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331549311308254722)
,p_query_column_id=>8
,p_column_alias=>'COL007'
,p_column_display_sequence=>8
,p_column_heading=>'Col007'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331549655966254723)
,p_query_column_id=>9
,p_column_alias=>'COL008'
,p_column_display_sequence=>9
,p_column_heading=>'Col008'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331550116123254723)
,p_query_column_id=>10
,p_column_alias=>'COL009'
,p_column_display_sequence=>10
,p_column_heading=>'Col009'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331550473270254723)
,p_query_column_id=>11
,p_column_alias=>'COL010'
,p_column_display_sequence=>11
,p_column_heading=>'Col010'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3331546552680254715)
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
 p_id=>wwv_flow_imp.id(3331542542976254628)
,p_plug_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_parent_plug_id=>wwv_flow_imp.id(3331542145245254627)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'ITEM_IS_NULL'
,p_plug_display_when_condition=>'P17_FILE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3331540559372254618)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3331540110890254608)
,p_button_name=>'CLEAR'
,p_static_id=>'clear'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Clear'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3331540858622254620)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3331540110890254608)
,p_button_name=>'LOAD'
,p_static_id=>'load'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Load Data'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(3335432175938540648)
,p_branch_name=>'View Load Status'
,p_branch_action=>'f?p=&APP_ID.:18:&SESSION.::&DEBUG.:17,18,SALES_DATA_LOAD_ERR:P18_LOAD_EXEC_ID:&P17_LOAD_EXEC_ID.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_when_button_id=>wwv_flow_imp.id(3331540858622254620)
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1825746450442157252)
,p_name=>'P17_ERROR_ROWS'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(4206236394783497011)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3331542930503254629)
,p_name=>'P17_FILE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3331542542976254628)
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
  'dropzone_description', 'Supported formats CSV, TXT, ZIP',
  'dropzone_title', 'Drag and Drop Sales Data',
  'max_file_size', '10000',
  'purge_file_at', 'SESSION',
  'storage_type', 'APEX_APPLICATION_TEMP_FILES')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3331545020374254642)
,p_name=>'P17_FILE_NAME'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3331544624055254640)
,p_item_default=>'Pasted Data'
,p_prompt=>'Loaded File'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>3033038003750078790
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1825746144989157249)
,p_name=>'P17_LOAD_EXEC_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(4206236394783497011)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1825746218313157250)
,p_name=>'P17_PROCESSED_ROWS'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(4206236394783497011)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3331545398387254643)
,p_computation_sequence=>10
,p_computation_item=>'P17_FILE_NAME'
,p_static_id=>'p17-file-name'
,p_computation_type=>'QUERY'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select filename',
'  from apex_application_temp_files ',
' where name = :P17_FILE'))
,p_compute_when=>'P17_FILE'
,p_compute_when_type=>'ITEM_IS_NOT_NULL'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(3331545764532254652)
,p_validation_name=>'Is valid file type'
,p_static_id=>'is-valid-file-type'
,p_validation_sequence=>10
,p_validation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if apex_data_parser.assert_file_type(',
'       p_file_name => :P17_FILE_NAME,',
'       p_file_type => apex_data_parser.c_file_type_csv ) or',
'   lower( :P17_FILE_NAME ) like ''%.zip''',
'then',
'    return true;',
'else',
'    :P17_FILE := null;',
'    return false;',
'end if;'))
,p_validation2=>'PLSQL'
,p_validation_type=>'FUNC_BODY_RETURNING_BOOLEAN'
,p_error_message=>'Invalid file type. Supported file types CSV, TXT, ZIP.'
,p_associated_item=>wwv_flow_imp.id(3331542930503254629)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3331543693428254638)
,p_name=>'Upload a File'
,p_static_id=>'upload-a-file'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P17_FILE'
,p_condition_element=>'P17_FILE'
,p_triggering_condition_type=>'NOT_NULL'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3331544194616254639)
,p_event_id=>wwv_flow_imp.id(3331543693428254638)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-submit-page'
,p_action=>'NATIVE_SUBMIT_PAGE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_processing', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3331541811095254624)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Cache'
,p_static_id=>'clear-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3331540559372254618)
,p_internal_uid=>1661952210155930294
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1825746746233157255)
,p_process_sequence=>20
,p_parent_process_id=>wwv_flow_imp.id(1825746548884157253)
,p_process_type=>'NATIVE_DATA_LOADING'
,p_process_name=>'Load Data'
,p_static_id=>'load-data'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'data_load_definition_id', wwv_flow_imp.id(3336824988029646376),
  'error_row_count_item', 'P17_ERROR_ROWS',
  'processed_row_count_item', 'P17_PROCESSED_ROWS',
  'source_data_type', 'SQL_QUERY',
  'source_sql_query', 'select eba_demo_data_load.get_file_blob from sys.dual')).to_clob
,p_process_success_message=>'{"rows_processed": &P17_PROCESSED_ROWS., "rows_with_error": &P17_ERROR_ROWS. }  '
,p_internal_uid=>156157145293832925
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1825746548884157253)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_EXECUTION_CHAIN'
,p_process_name=>'Load Data Background'
,p_static_id=>'load-data-background'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'executions_limit', '1',
  'return_id_into_item', 'P17_LOAD_EXEC_ID',
  'run_in_background', 'Y',
  'serialize', 'Y',
  'submit_immediately', 'Y',
  'temporary_file_handling', 'MOVE',
  'temporary_file_items', 'P17_FILE',
  'when_already_running', 'WAIT')).to_clob
,p_process_error_message=>'Only one file can be loaded at a time.'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3331540858622254620)
,p_process_when=>'P17_FILE'
,p_process_when_type=>'ITEM_IS_NOT_NULL'
,p_process_success_message=>'Data Loading task kicked off for execution.'
,p_internal_uid=>156156947944832923
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1825746825740157256)
,p_process_sequence=>30
,p_parent_process_id=>wwv_flow_imp.id(1825746548884157253)
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Report Loading Results'
,p_static_id=>'report-loading-results'
,p_process_sql_clob=>'apex_background_process.set_status( ''{"rows_processed":'' || :P17_PROCESSED_ROWS || '',"rows_with_error":'' || :P17_ERROR_ROWS || ''}'' );'
,p_process_clob_language=>'PLSQL'
,p_internal_uid=>156157224800832926
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1825746616619157254)
,p_process_sequence=>10
,p_parent_process_id=>wwv_flow_imp.id(1825746548884157253)
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Unpack ZIP Archive'
,p_static_id=>'unpack-zip-archive'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_file      blob;',
'    l_mime_type apex_application_temp_files.mime_type%type;',
'begin',
'    select mime_type,',
'           blob_content',
'      into l_mime_type,',
'           l_file',
'      from apex_application_temp_files',
'     where name = :P17_FILE;',
'',
'    if l_mime_type = ''application/zip'' then',
'        l_file := eba_demo_data_load.zip_to_csv( p_blob_content => l_file, p_mime_type => l_mime_type );',
'    end if;',
'',
'    eba_demo_data_load.set_file_blob( l_file );',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_internal_uid=>156157015679832924
);
wwv_flow_imp.component_end;
end;
/
