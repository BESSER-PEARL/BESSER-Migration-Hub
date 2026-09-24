prompt --application/pages/page_00018
begin
--   Manifest
--     PAGE: 00018
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
 p_id=>18
,p_name=>'Delete and Refresh'
,p_alias=>'DELETE-AND-REFRESH'
,p_step_title=>'Delete and Refresh'
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
 p_id=>wwv_flow_imp.id(2673199968572361277)
,p_plug_name=>'Employees'
,p_static_id=>'employees'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2102002977963900996
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'SELECT e.ROWID',
',      e.EMPNO ID',
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
 p_id=>wwv_flow_imp.id(2673200161174361278)
,p_max_row_count=>'100000'
,p_max_row_count_message=>'This query returns more than #MAX_ROW_COUNT# rows, please filter your data to ensure complete results.'
,p_no_data_found_message=>'No data found.'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_report_list_mode=>'NONE'
,p_fixed_header=>'NONE'
,p_lazy_loading=>false
,p_show_detail_link=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML'
,p_enable_mail_download=>'Y'
,p_internal_uid=>2024603024458718042
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2673200960127361280)
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
 p_id=>wwv_flow_imp.id(2673201064406361280)
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
 p_id=>wwv_flow_imp.id(2673200363622361279)
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
 p_id=>wwv_flow_imp.id(2673200458058361279)
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
 p_id=>wwv_flow_imp.id(2673200765011361280)
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
 p_id=>wwv_flow_imp.id(2673528947139772039)
,p_db_column_name=>'ID'
,p_display_order=>10
,p_column_identifier=>'J'
,p_column_label=>'Delete'
,p_column_link=>'#'
,p_column_linktext=>'<span class="t-Icon fa fa-trash-o" aria-hidden="true"></span>'
,p_column_link_attr=>'id="#ID#" class="delete t-Button t-Button--danger t-Button--simple t-Button--small" title="Delete Employee: #ENAME#"'
,p_column_type=>'NUMBER'
,p_column_alignment=>'CENTER'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(2673200563678361280)
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
 p_id=>wwv_flow_imp.id(2673200664110361280)
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
 p_id=>wwv_flow_imp.id(2673200238860361279)
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
 p_id=>wwv_flow_imp.id(2673200856775361280)
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
 p_id=>wwv_flow_imp.id(2673201144199361281)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'20246041'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ID:EMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(2673201337598361281)
,p_application_user=>'APXWS_ALTERNATIVE'
,p_name=>'Salesmen Report'
,p_report_seq=>10
,p_report_alias=>'20246043'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ROWEMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO:CURRENT_TIMESTAMP:ID'
);
wwv_flow_imp_page.create_worksheet_condition(
 p_id=>wwv_flow_imp.id(2673201560236361282)
,p_report_id=>wwv_flow_imp.id(2673201337598361281)
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
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(2673201641482361282)
,p_application_user=>'APXWS_ALTERNATIVE'
,p_name=>'High Paid Staff'
,p_report_seq=>10
,p_report_alias=>'20246046'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>15
,p_report_columns=>'ROWEMPNO:ENAME:JOB:MGR:HIREDATE:SAL:COMM:DEPTNO:CURRENT_TIMESTAMP:ID'
,p_sort_column_1=>'SAL'
,p_sort_direction_1=>'DESC'
);
wwv_flow_imp_page.create_worksheet_condition(
 p_id=>wwv_flow_imp.id(2673201860457361282)
,p_report_id=>wwv_flow_imp.id(2673201641482361282)
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
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2673202151524361302)
,p_plug_name=>'Overview'
,p_static_id=>'overview'
,p_region_template_options=>'#DEFAULT#:t-ContentBlock--h2'
,p_plug_template=>2323592004483952560
,p_plug_display_sequence=>3
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page demonstrates how dynamic actions can be used to provide AJAX based delete row functionality. In the example, clicking on any of the ''Delete'' icons for any employee will result in that record being deleted from the database.</p>',
'<p>To achieve this, the page contains one dynamic action called ''DELETE EMP''. This fires when the user clicks on any of the ''Delete'' icons and has the following six ''True Actions'' that handle the delete:',
'<ul style="margin: 8px 24px;">',
'<li>''Confirm'' to confirm the user really wants to delete.</li>',
'<li>''Set Value'' of a hidden item to the ''empno'' value to delete.</li>',
'<li>''Execute PL/SQL Code'' to delete the record</li>',
'<li>''Refresh'' the report region.</li>',
'<li>''Notification'' to display a ''Employee deleted'' message.</li>',
'<li>''Cancel Event'' to stop the browser''s default handling of refreshing the entire page that would occur after a link is clicked.</li></ul></p>',
'<p>It uses five native actions (''Confirm'', ''Set Value'', ''Execute PL/SQL Code'', ''Refresh'' and ''Cancel Event'') and one plug-in action (''Notification'').</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2673203154943361305)
,p_plug_name=>'Server Side - Refresh 2'
,p_static_id=>'server-side-refresh'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>20
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(8199705487948627945)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2177290116743197798)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(2673199968572361277)
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
 p_id=>wwv_flow_imp.id(2673201946868361282)
,p_name=>'P18_EMPNO'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(2673199968572361277)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(2673453238614428974)
,p_name=>'DELETE EMP'
,p_static_id=>'delete-emp'
,p_event_sequence=>10
,p_triggering_element_type=>'JQUERY_SELECTOR'
,p_triggering_element=>'a.delete'
,p_bind_type=>'live'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2673453551676428974)
,p_event_id=>wwv_flow_imp.id(2673453238614428974)
,p_event_result=>'TRUE'
,p_action_sequence=>20
,p_execute_on_page_init=>'N'
,p_static_id=>'native-confirm'
,p_action=>'NATIVE_CONFIRM'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'message', 'Are you sure you want to delete this employee?')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2673480739783438745)
,p_event_id=>wwv_flow_imp.id(2673453238614428974)
,p_event_result=>'TRUE'
,p_action_sequence=>40
,p_execute_on_page_init=>'N'
,p_static_id=>'native-execute-plsql-code'
,p_action=>'NATIVE_EXECUTE_PLSQL_CODE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'items_to_submit', 'P18_EMPNO',
  'language', 'PLSQL',
  'plsql_code', wwv_flow_string.join(wwv_flow_t_varchar2(
    'begin',
    '    -- If the person to be deleted is a manager, move all of his/her employees',
    '    -- up a level.',
    '    update eba_demo_da_emp e1',
    '    set e1.mgr = ( select e2.mgr from eba_demo_da_emp e2 where e2.empno = :P18_EMPNO )',
    '    where e1.mgr = :P18_EMPNO;',
    '',
    '    delete from eba_demo_da_emp where empno = :P18_EMPNO;',
    '    commit;',
    'end;')),
  'show_processing', 'N')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(1854063855512816714)
,p_event_id=>wwv_flow_imp.id(2673453238614428974)
,p_event_result=>'TRUE'
,p_action_sequence=>60
,p_execute_on_page_init=>'N'
,p_static_id=>'native-javascript-code'
,p_action=>'NATIVE_JAVASCRIPT_CODE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_code', 'alert("Employee #"+$v("P18_EMPNO")+" removed.");')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2673488746017440520)
,p_event_id=>wwv_flow_imp.id(2673453238614428974)
,p_event_result=>'TRUE'
,p_action_sequence=>50
,p_execute_on_page_init=>'N'
,p_static_id=>'native-refresh'
,p_action=>'NATIVE_REFRESH'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(2673199968572361277)
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'maintain_pagination', 'N')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2673472752466432971)
,p_event_id=>wwv_flow_imp.id(2673453238614428974)
,p_event_result=>'TRUE'
,p_action_sequence=>30
,p_execute_on_page_init=>'N'
,p_static_id=>'native-set-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P18_EMPNO'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.id',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp.component_end;
end;
/
