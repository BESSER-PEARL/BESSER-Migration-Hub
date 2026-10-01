prompt --application/pages/page_00018
begin
--   Manifest
--     PAGE: 00018
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
 p_id=>18
,p_name=>'Load Status'
,p_alias=>'LOAD-STATUS'
,p_step_title=>'Load Status'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'18'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(6666991100068217250)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>50
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(11521794561627835810)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(4165072647771625983)
,p_name=>'Load Status'
,p_static_id=>'load-status'
,p_region_name=>'loadStatus'
,p_template=>4073835273271169698
,p_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noBorder:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-BadgeList--xlarge:t-BadgeList--dash:t-BadgeList--fixed:t-Report--hideNoPagination'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select initcap(status_code)                                               as status,',
'       sofar                                                              as rows_processed,',
'       json_value( status_message, ''$.rows_processed''  returning number ) as rows_successful,',
'       json_value( status_message, ''$.rows_with_error'' returning number ) as rows_with_error',
'  from apex_appl_page_bg_proc_status',
' where execution_id = :P18_LOAD_EXEC_ID'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2106120299521025145
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3336261236895214356)
,p_query_column_id=>2
,p_column_alias=>'ROWS_PROCESSED'
,p_column_display_sequence=>20
,p_column_heading=>'Rows Processed'
,p_column_format=>'999G999G999G999G999G999G990'
,p_disable_sort_column=>'N'
,p_display_when_cond_type=>'VALUE_OF_ITEM_IN_CONDITION_NOT_IN_COLON_DELIMITED_LIST'
,p_display_when_condition=>'P18_LOADING_STATUS'
,p_display_when_condition2=>'SUCCESS:ABORTED:FAILED'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1825746975714157257)
,p_query_column_id=>3
,p_column_alias=>'ROWS_SUCCESSFUL'
,p_column_display_sequence=>30
,p_column_heading=>'Rows Successful'
,p_column_format=>'999G999G999G999G999G999G990'
,p_disable_sort_column=>'N'
,p_display_when_cond_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_display_when_condition=>'P18_LOADING_STATUS'
,p_display_when_condition2=>'SUCCESS:ABORTED:FAILED'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3335432348702540649)
,p_query_column_id=>4
,p_column_alias=>'ROWS_WITH_ERROR'
,p_column_display_sequence=>40
,p_column_heading=>'Rows With Error'
,p_column_format=>'999G999G999G999G999G999G990'
,p_disable_sort_column=>'N'
,p_display_when_cond_type=>'VALUE_OF_ITEM_IN_CONDITION_IN_COLON_DELIMITED_LIST'
,p_display_when_condition=>'P18_LOADING_STATUS'
,p_display_when_condition2=>'SUCCESS:ABORTED:FAILED'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3336260846108214358)
,p_query_column_id=>1
,p_column_alias=>'STATUS'
,p_column_display_sequence=>10
,p_column_heading=>'Status'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3338224120111735621)
,p_name=>'Rows with Errors'
,p_static_id=>'rows-with-errors'
,p_region_name=>'loadError'
,p_template=>4073835273271169698
,p_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--staticRowColors:t-Report--rowHighlight:t-Report--horizontalBorders:t-Report--hideNoPagination'
,p_region_attributes=>'style="display:none;"'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select n001 row_number, c001 error_message',
'   from apex_collections',
' where collection_name = ''SALES_DATA_LOAD_ERR'';'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_no_data_found=>'No error rows logged.'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3338224326927735623)
,p_query_column_id=>2
,p_column_alias=>'ERROR_MESSAGE'
,p_column_display_sequence=>20
,p_column_heading=>'Error Message'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3338224172187735622)
,p_query_column_id=>1
,p_column_alias=>'ROW_NUMBER'
,p_column_display_sequence=>10
,p_column_heading=>'Row Number'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4213526711292472565)
,p_plug_name=>'Sales Table Contents'
,p_static_id=>'sales-table-contents'
,p_region_name=>'sales'
,p_region_template_options=>'#DEFAULT#:is-collapsed:t-Region--noBorder:t-Region--scrollBody'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>40
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'TABLE'
,p_query_table=>'EBA_DEMO_LOAD_SALES'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_IR'
,p_prn_content_disposition=>'ATTACHMENT'
,p_prn_units=>'INCHES'
,p_prn_paper_size=>'LETTER'
,p_prn_width=>11
,p_prn_height=>8.5
,p_prn_orientation=>'HORIZONTAL'
,p_prn_page_header=>'Sales Table Contents'
,p_prn_page_header_font_color=>'#000000'
,p_prn_page_header_font_family=>'Helvetica'
,p_prn_page_header_font_weight=>'normal'
,p_prn_page_header_font_size=>'12'
,p_prn_page_footer_font_color=>'#000000'
,p_prn_page_footer_font_family=>'Helvetica'
,p_prn_page_footer_font_weight=>'normal'
,p_prn_page_footer_font_size=>'12'
,p_prn_header_bg_color=>'#EEEEEE'
,p_prn_header_font_color=>'#000000'
,p_prn_header_font_family=>'Helvetica'
,p_prn_header_font_weight=>'bold'
,p_prn_header_font_size=>'10'
,p_prn_body_bg_color=>'#FFFFFF'
,p_prn_body_font_color=>'#000000'
,p_prn_body_font_family=>'Helvetica'
,p_prn_body_font_weight=>'normal'
,p_prn_body_font_size=>'10'
,p_prn_border_width=>.5
,p_prn_page_header_alignment=>'CENTER'
,p_prn_page_footer_alignment=>'CENTER'
,p_prn_border_color=>'#666666'
,p_ai_enabled=>false
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(3336826755441600028)
,p_no_data_found_message=>'No sales data found.'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_report_list_mode=>'TABS'
,p_lazy_loading=>false
,p_show_detail_link=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:XLSX:PDF'
,p_enable_mail_download=>'Y'
,p_internal_uid=>830208900339471008
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827117449600031)
,p_db_column_name=>'COUNTRY'
,p_display_order=>30
,p_column_identifier=>'C'
,p_column_label=>'Country'
,p_column_type=>'STRING'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336828420651600044)
,p_db_column_name=>'CREATED'
,p_display_order=>160
,p_column_identifier=>'P'
,p_column_label=>'Created'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'SINCE'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336826915811600029)
,p_db_column_name=>'ID'
,p_display_order=>10
,p_column_identifier=>'A'
,p_column_label=>'Id'
,p_column_type=>'NUMBER'
,p_display_text_as=>'HIDDEN'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827223427600032)
,p_db_column_name=>'ITEM_TYPE'
,p_display_order=>40
,p_column_identifier=>'D'
,p_column_label=>'Item Type'
,p_column_type=>'STRING'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336828502795600045)
,p_db_column_name=>'LAST_UPDATED'
,p_display_order=>170
,p_column_identifier=>'Q'
,p_column_label=>'Last Updated'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_format_mask=>'SINCE'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827471160600035)
,p_db_column_name=>'ORDER_DATE'
,p_display_order=>70
,p_column_identifier=>'G'
,p_column_label=>'Order Date'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827594593600036)
,p_db_column_name=>'ORDER_ID'
,p_display_order=>80
,p_column_identifier=>'H'
,p_column_label=>'Order Id'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827413105600034)
,p_db_column_name=>'ORDER_PRIORITY'
,p_display_order=>60
,p_column_identifier=>'F'
,p_column_label=>'Order Priority'
,p_column_type=>'STRING'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827028188600030)
,p_db_column_name=>'REGION'
,p_display_order=>20
,p_column_identifier=>'B'
,p_column_label=>'Region'
,p_column_type=>'STRING'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827292838600033)
,p_db_column_name=>'SALES_CHANNEL'
,p_display_order=>50
,p_column_identifier=>'E'
,p_column_label=>'Sales Channel'
,p_column_type=>'STRING'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827701757600037)
,p_db_column_name=>'SHIP_DATE'
,p_display_order=>90
,p_column_identifier=>'I'
,p_column_label=>'Ship Date'
,p_column_type=>'DATE'
,p_column_alignment=>'CENTER'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336828221030600042)
,p_db_column_name=>'TOTAL_COST'
,p_display_order=>140
,p_column_identifier=>'N'
,p_column_label=>'Total Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336828327636600043)
,p_db_column_name=>'TOTAL_PROFIT'
,p_display_order=>150
,p_column_identifier=>'O'
,p_column_label=>'Total Profit'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336828088015600041)
,p_db_column_name=>'TOTAL_REVENUE'
,p_display_order=>130
,p_column_identifier=>'M'
,p_column_label=>'Total Revenue'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827768719600038)
,p_db_column_name=>'UNITS_SOLD'
,p_display_order=>100
,p_column_identifier=>'J'
,p_column_label=>'Units Sold'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827967129600040)
,p_db_column_name=>'UNIT_COST'
,p_display_order=>120
,p_column_identifier=>'L'
,p_column_label=>'Unit Cost'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(3336827874142600039)
,p_db_column_name=>'UNIT_PRICE'
,p_display_order=>110
,p_column_identifier=>'K'
,p_column_label=>'Unit Price'
,p_column_type=>'NUMBER'
,p_column_alignment=>'RIGHT'
,p_format_mask=>'FML999G999G999G999G990D00'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(3336854733676371578)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'8302369'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'REGION:COUNTRY:ITEM_TYPE:SALES_CHANNEL:ORDER_PRIORITY:UNITS_SOLD:UNIT_PRICE:UNIT_COST:TOTAL_PROFIT:LAST_UPDATED'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3335432403443540650)
,p_plug_name=>'Timer Container'
,p_static_id=>'timer-container'
,p_region_name=>'timer-container'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3336261578568214350)
,p_name=>'P18_LOADING_STATUS'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(4165072647771625983)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1825747128140157259)
,p_name=>'P18_LOAD_EXEC_ID'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(4165072647771625983)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3335432530421540651)
,p_name=>'Refresh Load Status on Timer'
,p_static_id=>'refresh-load-status-on-timer'
,p_event_sequence=>20
,p_triggering_element_type=>'JQUERY_SELECTOR'
,p_triggering_element=>'#timer-container'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'custom'
,p_bind_event_type_custom=>'job_timer'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3336270251271206630)
,p_event_id=>wwv_flow_imp.id(3335432530421540651)
,p_event_result=>'TRUE'
,p_action_sequence=>30
,p_execute_on_page_init=>'N'
,p_name=>'Get Loading Job Status'
,p_static_id=>'get-loading-job-status'
,p_action=>'NATIVE_EXECUTE_PLSQL_CODE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'items_to_return', 'P18_LOADING_STATUS',
  'language', 'PLSQL',
  'plsql_code', wwv_flow_string.join(wwv_flow_t_varchar2(
    'begin',
    '    select status_code',
    '      into :P18_LOADING_STATUS',
    '      from apex_appl_page_bg_proc_status',
    '     where execution_id = :P18_LOAD_EXEC_ID;',
    'exception when others then',
    '    :P18_LOADING_STATUS := ''SUCCESS'';',
    'end;')),
  'show_processing', 'Y',
  'suppress_change_event', 'N')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(3335432809379540654)
,p_name=>'Refresh Load Status Timer'
,p_static_id=>'refresh-load-status-timer'
,p_event_sequence=>30
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'ready'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(3335432916526540655)
,p_event_id=>wwv_flow_imp.id(3335432809379540654)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_name=>'Initialize Timer for Load Status Refresh'
,p_static_id=>'initialize-timer-for-load-status-refresh'
,p_action=>'NATIVE_JAVASCRIPT_CODE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_code', wwv_flow_string.join(wwv_flow_t_varchar2(
    'var lSpinner$ = apex.util.showSpinner( $( "#loadStatus" ) );',
    '',
    'var triggerRefresh = function(){ ',
    '    var lstatus = apex.item("P18_LOADING_STATUS").getValue() ?? "ENQUEUED";',
    '',
    '    apex.event.trigger( apex.jQuery("#timer-container"), "job_timer" );',
    '',
    '    console.log( "current satus " + lstatus );',
    '',
    '    if (  lstatus === ''SUCCESS''  || ',
    '          lstatus === ''ABORTED''  || ',
    '          lstatus === ''FAILED'' ) {',
    '      apex.region( "loadStatus" ).refresh();',
    '      apex.region( "sales" ).refresh();',
    '      ',
    '      if ( lstatus === ''FAILED'' ||  ',
    '           lstatus === ''ABORTED'' ) {',
    '          apex.region( "loadError" ).element.show();',
    '          apex.region( "loadError" ).refresh();',
    '      }',
    '',
    '      clearInterval( refreshInterval );',
    '      lSpinner$.remove();',
    '    } else {',
    '      apex.region( "loadStatus" ).refresh();',
    '      apex.region( "sales" ).refresh(); ',
    '    }',
    '};',
    '',
    'var refreshInterval = setInterval( triggerRefresh, 1000);')))).to_clob
);
wwv_flow_imp.component_end;
end;
/
