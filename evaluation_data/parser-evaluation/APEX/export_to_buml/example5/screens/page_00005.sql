prompt --application/pages/page_00005
begin
--   Manifest
--     PAGE: 00005
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
 p_id=>5
,p_name=>'Edit'
,p_alias=>'EDIT2'
,p_step_title=>'Edit'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2655438167961829336)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page shows how dynamic actions can control hiding and showing page elements, including controlling the item''s label if it exists.</p>',
'<p>To achieve this, the page contains 1 dynamic action called ''JOB EQUALS SALESMAN''. This fires when the ''Job'' page item changes and checks if the value is equal to ''SALESMAN''. If it is equal to ''SALESMAN'', both the ''Hire date'' and ''Commission'' page '
||'items and their associated labels are shown, otherwise they are hidden.</p>',
'<p>It uses 2 native actions (''Show'' and ''Hide'').</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2654118847110049476)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
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
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2654111465019049452)
,p_plug_name=>'Maintain Employee'
,p_static_id=>'maintain-employee'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2654112048761049452)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(2654118847110049476)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.:::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2654111756903049452)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(2654118847110049476)
,p_button_name=>'SAVE'
,p_static_id=>'save'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'NEXT'
,p_button_condition=>'P5_ROWID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(2654112646939049454)
,p_branch_action=>'f?p=&APP_ID.:4:&SESSION.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654114654296049465)
,p_name=>'P5_COMM'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Commission'
,p_source=>'COMM'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>7
,p_cMaxlength=>7
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654114845208049465)
,p_name=>'P5_DEPTNO'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Department'
,p_source=>'DEPTNO'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'DEPARTMENT'
,p_cHeight=>1
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654113048711049461)
,p_name=>'P5_EMPNO'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Employee Number'
,p_source=>'EMPNO'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>4
,p_cMaxlength=>4
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654113246772049461)
,p_name=>'P5_ENAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Name'
,p_source=>'ENAME'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>10
,p_cMaxlength=>10
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654114249050049464)
,p_name=>'P5_HIREDATE'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Hire date'
,p_format_mask=>'DD-MON-YYYY'
,p_source=>'HIREDATE'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>30
,p_cMaxlength=>255
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654113459707049462)
,p_name=>'P5_JOB'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Job'
,p_source=>'JOB'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'JOB'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654113843165049464)
,p_name=>'P5_MGR'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Manager'
,p_source=>'MGR'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_POPUP_LOV'
,p_named_lov=>'MANAGER'
,p_cSize=>30
,p_cMaxlength=>4
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'case_sensitive', 'N',
  'display_as', 'DIALOG',
  'fetch_on_search', 'N',
  'initial_fetch', 'FIRST_ROWSET',
  'manual_entry', 'N',
  'match_type', 'CONTAINS',
  'min_chars', '0')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654112843737049455)
,p_name=>'P5_ROWID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_source=>'ROWID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2654114455039049464)
,p_name=>'P5_SAL'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(2654111465019049452)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Salary'
,p_source=>'SAL'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>7
,p_cMaxlength=>7
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(2655572162813856234)
,p_name=>'JOB EQUALS SALESMAN'
,p_static_id=>'job-equals-salesman'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P5_JOB'
,p_condition_element=>'P5_JOB'
,p_triggering_condition_type=>'EQUALS'
,p_triggering_expression=>'SALESMAN'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2655572657474856249)
,p_event_id=>wwv_flow_imp.id(2655572162813856234)
,p_event_result=>'FALSE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-hide'
,p_action=>'NATIVE_HIDE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P5_HIREDATE,P5_COMM'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2655572450004856246)
,p_event_id=>wwv_flow_imp.id(2655572162813856234)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-show'
,p_action=>'NATIVE_SHOW'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P5_HIREDATE,P5_COMM'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2654116241103049467)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from EBA_DEMO_DA_EMP'
,p_static_id=>'fetch-row-from-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P5_ROWID',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_internal_uid=>2647959836275068342
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2654116468269049467)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of EBA_DEMO_DA_EMP'
,p_static_id=>'process-row-of-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P5_ROWID',
  'supported_operations', 'I:U:D',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_success_message=>'Action Processed.'
,p_internal_uid=>2647960063441068342
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2654116642300049468)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'reset page'
,p_static_id=>'reset-page'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_internal_uid=>2647960237472068343
);
wwv_flow_imp.component_end;
end;
/
