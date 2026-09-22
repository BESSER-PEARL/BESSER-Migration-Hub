prompt --application/pages/page_00017
begin
--   Manifest
--     PAGE: 00017
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7840
,p_default_id_offset=>1555159707774264
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>17
,p_name=>'Refresh'
,p_alias=>'REFRESH'
,p_step_title=>'Refresh'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'18'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2668748439060415980)
,p_plug_name=>'Employees'
,p_static_id=>'employees'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2102002977963900996
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT e.ROWID',
',      e.EMPNO',
',      e.ENAME',
',      e.JOB',
',      m.ename MGR',
',      e.HIREDATE',
',      e.SAL',
',      e.COMM',
',      d.dname DEPTNO',
'FROM EBA_DEMO_DA_EMP e',
',    EBA_DEMO_DA_EMP m',
',    EBA_DEMO_DA_DEPT d',
'WHERE e.mgr = m.empno (+)',
'AND   e.deptno = d.deptno (+)'))
,p_plug_source_type=>'NATIVE_IR'
,p_ai_enabled=>false
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(2668748655914415981)
,p_report_id_item=>'P17_REPORT_ID'
,p_max_row_count=>'100000'
,p_max_row_count_message=>'This query returns more than #MAX_ROW_COUNT# rows, please filter your data to ensure complete results.'
,p_no_data_found_message=>'No data found.'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_report_list_mode=>'TABS'
,p_fixed_header=>'NONE'
,p_lazy_loading=>false
,p_show_detail_link=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML'
,p_enable_mail_download=>'Y'
,p_internal_uid=>2020151519198772745
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749456982415987)
,p_db_column_name=>'COMM'
,p_display_order=>8
,p_column_identifier=>'H'
,p_column_label=>'Commission'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749557961415987)
,p_db_column_name=>'DEPTNO'
,p_display_order=>9
,p_column_identifier=>'I'
,p_column_label=>'Department'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668748847701415986)
,p_db_column_name=>'EMPNO'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'Employee #'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668748938689415987)
,p_db_column_name=>'ENAME'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'Name'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749249838415987)
,p_db_column_name=>'HIREDATE'
,p_display_order=>6
,p_column_identifier=>'F'
,p_column_label=>'Hire date'
,p_column_type=>'DATE'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749057444415987)
,p_db_column_name=>'JOB'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'Job'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749142658415987)
,p_db_column_name=>'MGR'
,p_display_order=>5
,p_column_identifier=>'E'
,p_column_label=>'Manager'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668748751967415986)
,p_db_column_name=>'ROWID'
,p_display_order=>1
,p_column_identifier=>'A'
,p_column_label=>'Rowid'
,p_column_type=>'OTHER'
,p_display_text_as=>'HIDDEN'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2668749348975415987)
,p_db_column_name=>'SAL'
,p_display_order=>7
,p_column_identifier=>'G'
,p_column_label=>'Salary'
,p_column_type=>'NUMBER'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(2669359741059480409)
,p_application_user=>'APXWS_ALTERNATIVE'
,p_name=>'High Paid Staff'
,p_report_seq=>10
,p_report_alias=>'HIGH_PAY'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ROWID:EMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO:CURRENT_TIMESTAMP'
,p_sort_column_1=>'SAL'
,p_sort_direction_1=>'DESC'
);
wwv_flow_imp_page.create_worksheet_condition(
 p_id=>wwv_flow_imp.id(2669359959512480409)
,p_report_id=>wwv_flow_imp.id(2669359741059480409)
,p_static_id=>'ir-condition'
,p_condition_type=>'FILTER'
,p_allow_delete=>'Y'
,p_column_name=>'SAL'
,p_operator=>'>='
,p_expr=>'5000'
,p_condition_sql=>'"SAL" >= to_number(#APXWS_EXPR#)'
,p_condition_display=>'#APXWS_COL_NAME# >= #APXWS_EXPR_NUMBER#  '
,p_enabled=>'Y'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(2668749737288415988)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'PRIMARY'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ROWID:EMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO:CURRENT_TIMESTAMP'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(2669128739281451526)
,p_application_user=>'APXWS_ALTERNATIVE'
,p_name=>'Salesmen Report'
,p_report_seq=>10
,p_report_alias=>'SALESMEN'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ROWID:EMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO:CURRENT_TIMESTAMP'
);
wwv_flow_imp_page.create_worksheet_condition(
 p_id=>wwv_flow_imp.id(2669128956302451528)
,p_report_id=>wwv_flow_imp.id(2669128739281451526)
,p_static_id=>'ir-condition'
,p_condition_type=>'FILTER'
,p_allow_delete=>'Y'
,p_column_name=>'JOB'
,p_operator=>'='
,p_expr=>'SALESMAN'
,p_condition_sql=>'"JOB" = #APXWS_EXPR#'
,p_condition_display=>'#APXWS_COL_NAME# = ''SALESMAN''  '
,p_enabled=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2668749962904415991)
,p_plug_name=>'Overview'
,p_static_id=>'overview'
,p_region_template_options=>'#DEFAULT#:t-ContentBlock--h2'
,p_plug_template=>2323592004483952560
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page demonstrates an alternative way to provision a list of ''Saved Reports'' to Interactive Report users, via a separate report on the page instead of the standard select list. Dynamic actions are required to refresh the list of ''Saved Reports'
||''', after the user has made changes to a report.</p>',
'<p>To achieve this, this page contains one dynamic action called ''REFRESH SAVED REPORTS''. This refreshes the ''Saved Interactive Reports'' report after the user makes changes to the report. Try saving a new report and see the new report appear in the r'
||'egion after saving the report. This makes use of the ''After Refresh'' event for the Interactive Report Region, see the item level help for the ''Event'' field for further information.</p>',
'<p>It uses one native action (''Refresh''), to refresh the ''Saved Reports'' report via Ajax.</p>',
'<p>The report includes the name of the saved report, its description if provided, and the visibility of the report-"Default" means created by an application developer, and is visible to all users; "Public" means created by an end user, but visible to'
||' all users; "Private" means created by an end user and only visible to that user.</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(2669550943052499935)
,p_name=>'Saved Interactive Reports'
,p_static_id=>'saved-interactive-reports'
,p_template=>4073835273271169698
,p_display_sequence=>20
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Cards--compact:t-Cards--5cols:u-colors:t-Cards--animColorFill'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ''visiblity: ''||case when report_type in (''PRIMARY_DEFAULT'', ''ALTERNATIVE_DEFAULT'') then',
'            ''Default''',
'        when report_type = ''PRIVATE'' then',
'            ''Private''',
'        else',
'            ''Public''',
'    end card_subtext,',
'    report_id,',
'    coalesce(report_name, ''Primary Report'') card_title,',
'    report_description card_text,',
'    apex_util.prepare_url(''f?p=''||:APP_ID||'':17:''||:APP_SESSION||'':::RP,17,RIR:P17_REPORT_ID:''||report_id) card_link',
'from apex_application_page_ir_rpt',
'where application_id = :APP_ID',
'    and page_id = :APP_PAGE_ID',
'    and (status = ''PUBLIC'' or',
'        (status = ''PRIVATE'' and application_user = :APP_USER))',
'    and report_type != ''SESSION''',
'order by 1 asc, 3, 4'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2976458789255810118
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_no_data_found=>'no data found'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_query_row_count_max=>500
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1854062596390816702)
,p_query_column_id=>5
,p_column_alias=>'CARD_LINK'
,p_column_display_sequence=>5
,p_column_heading=>'Card link'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1854062323843816699)
,p_query_column_id=>1
,p_column_alias=>'CARD_SUBTEXT'
,p_column_display_sequence=>2
,p_column_heading=>'Card subtext'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1854062502766816701)
,p_query_column_id=>4
,p_column_alias=>'CARD_TEXT'
,p_column_display_sequence=>4
,p_column_heading=>'Card text'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1854062402513816700)
,p_query_column_id=>3
,p_column_alias=>'CARD_TITLE'
,p_column_display_sequence=>3
,p_column_heading=>'Card title'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(2669551364608499940)
,p_query_column_id=>2
,p_column_alias=>'REPORT_ID'
,p_column_display_sequence=>1
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2668750552228415997)
,p_plug_name=>'Server Side - Refresh'
,p_static_id=>'server-side-refresh'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>40
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(8199705487948627945)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2177287928087191793)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(2668748439060415980)
,p_button_name=>'RESET'
,p_static_id=>'reset'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>2350584059425431644
,p_button_image_alt=>'Reset'
,p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'
,p_button_redirect_url=>'f?p=&APP_ID.:&APP_PAGE_ID.:&SESSION.::&DEBUG.:RP,RIR,&APP_PAGE_ID.::'
,p_icon_css_classes=>'fa-undo-alt'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2668750337860415995)
,p_name=>'P17_REPORT_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(2668748439060415980)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(2668751262561416011)
,p_name=>'REFRESH SAVED REPORT'
,p_static_id=>'refresh-saved-report'
,p_event_sequence=>10
,p_triggering_element_type=>'REGION'
,p_triggering_region_id=>wwv_flow_imp.id(2668748439060415980)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'apexafterrefresh'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2668751568615416011)
,p_event_id=>wwv_flow_imp.id(2668751262561416011)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-refresh'
,p_action=>'NATIVE_REFRESH'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(2669550943052499935)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'maintain_pagination', 'N')).to_clob
);
wwv_flow_imp.component_end;
end;
/
