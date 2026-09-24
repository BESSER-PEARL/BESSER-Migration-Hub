prompt --application/pages/page_00007
begin
--   Manifest
--     PAGE: 00007
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
 p_id=>7
,p_name=>'Edit'
,p_alias=>'EDIT3'
,p_step_title=>'Edit'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.validation_error {',
'  border-color: #ff0000 !important;',
'}',
''))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2656892340987124345)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_header=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page contains one dynamic action called ''NAME IS NULL''. This fires whenever the user leaves the ''Name'' page item and checks if it is empty. If the ''Name'' page item is empty a red border is applied to indicate there is a problem. The border is'
||' subsequently removed if and when the user leaves the ''Name'' page item having entered some text.</p>',
'<p>It uses two native actions (''Add Class'' and ''Remove Class'').</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2656803763861119577)
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
 p_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2656796955367119477)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(2656803763861119577)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'f?p=&APP_ID.:6:&SESSION.::&DEBUG.:::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2656796656201119469)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(2656803763861119577)
,p_button_name=>'SAVE'
,p_static_id=>'save'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'NEXT'
,p_button_condition=>'P7_ROWID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(2656797550309119487)
,p_branch_action=>'f?p=&APP_ID.:6:&SESSION.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2656799540310119519)
,p_name=>'P7_COMM'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2656799754867119519)
,p_name=>'P7_DEPTNO'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Department'
,p_source=>'DEPTNO'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'P7_EBA_DEMO_DA_EMP_DEPTNO'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2656797941703119503)
,p_name=>'P7_EMPNO'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Employee Number'
,p_source=>'EMPNO'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>4
,p_cMaxlength=>4
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2656798160949119509)
,p_name=>'P7_ENAME'
,p_is_required=>true
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2656799143180119518)
,p_name=>'P7_HIREDATE'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2656798369434119515)
,p_name=>'P7_JOB'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Job'
,p_source=>'JOB'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'P7_EBA_DEMO_DA_EMP_JOB'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2656798751822119518)
,p_name=>'P7_MGR'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Manager'
,p_source=>'MGR'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_POPUP_LOV'
,p_named_lov=>'P7_EBA_DEMO_DA_EMP_MGR'
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
 p_id=>wwv_flow_imp.id(2656797738222119492)
,p_name=>'P7_ROWID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2656799366411119519)
,p_name=>'P7_SAL'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(2656796355485119467)
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
 p_id=>wwv_flow_imp.id(2658048158676356531)
,p_name=>'NAME IS NULL'
,p_static_id=>'name-is-null'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P7_ENAME'
,p_condition_element=>'P7_ENAME'
,p_triggering_condition_type=>'NULL'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'focusout'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2658048452400356532)
,p_event_id=>wwv_flow_imp.id(2658048158676356531)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-add-class'
,p_action=>'NATIVE_ADD_CLASS'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P7_ENAME'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'css_class', 'validation_error')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2658048652820356533)
,p_event_id=>wwv_flow_imp.id(2658048158676356531)
,p_event_result=>'FALSE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-remove-class'
,p_action=>'NATIVE_REMOVE_CLASS'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P7_ENAME'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'css_class', 'validation_error')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2656801154890119526)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from EBA_DEMO_DA_EMP'
,p_static_id=>'fetch-row-from-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P7_ROWID',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_internal_uid=>2650644750062138401
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2656801343411119528)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of EBA_DEMO_DA_EMP'
,p_static_id=>'process-row-of-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P7_ROWID',
  'supported_operations', 'I:U:D',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_success_message=>'Action Processed.'
,p_internal_uid=>2650644938583138403
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2656801537303119530)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'reset page'
,p_static_id=>'reset-page'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_internal_uid=>2650645132475138405
);
wwv_flow_imp.component_end;
end;
/
