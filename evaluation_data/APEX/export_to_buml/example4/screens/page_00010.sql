prompt --application/pages/page_00010
begin
--   Manifest
--     PAGE: 00010
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7910
,p_default_id_offset=>12904184294728383
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>10
,p_name=>'Modify Subtask Information'
,p_alias=>'MODIFY-SUBTASK-INFORMATION'
,p_page_mode=>'MODAL'
,p_step_title=>'Modify Subtask Information'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';'
,p_step_template=>2123271369431536901
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1588112244198423450)
,p_plug_name=>'Buttons'
,p_static_id=>'buttons'
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'REGION_POSITION_03'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3183750086682386800)
,p_plug_name=>'Subtask Information'
,p_static_id=>'subtask-information'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody:t-Region--noBorder:t-Region--hideHeader js-addHiddenHeadingRoleDesc'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183750688211386800)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1588112244198423450)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'DEFINED_BY_DA'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'PREVIOUS'
,p_warn_on_unsaved_changes=>null
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183750269560386800)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1588112244198423450)
,p_button_name=>'CREATE'
,p_static_id=>'create'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create Subtask'
,p_button_position=>'NEXT'
,p_button_condition=>'P10_ROWID'
,p_button_condition_type=>'ITEM_IS_NULL'
,p_database_action=>'INSERT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183750476861386800)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1588112244198423450)
,p_button_name=>'DELETE'
,p_static_id=>'delete'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#:t-Button--simple:t-Button--danger'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'javascript:apex.confirm(htmldb_delete_message,''DELETE'');'
,p_button_execute_validations=>'N'
,p_button_condition=>'P10_ROWID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183750368855386800)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1588112244198423450)
,p_button_name=>'SAVE'
,p_static_id=>'save'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'NEXT'
,p_button_condition=>'P10_ROWID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(3183751277939386802)
,p_branch_action=>'f?p=&APP_ID.:&LAST_VIEW.:&SESSION.::&DEBUG.:::&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>1
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183753495948386812)
,p_name=>'P10_CREATED'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_source=>'CREATED'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183751682845386806)
,p_name=>'P10_PROJ_ID'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Project:'
,p_source=>'PROJ_ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'PROJECTS'
,p_cHeight=>1
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183751484327386806)
,p_name=>'P10_ROWID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_source=>'ROWID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183753875639386812)
,p_name=>'P10_SUB_ASSIGN'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Assignee'
,p_source=>'SUB_ASSIGN'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>400
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183752880458386812)
,p_name=>'P10_SUB_COMP'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Completed'
,p_source=>'SUB_COMP'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183754091736386813)
,p_name=>'P10_SUB_DESC'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Description'
,p_source=>'SUB_DESC'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>64
,p_cMaxlength=>32000
,p_cHeight=>4
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'N',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183752692351386811)
,p_name=>'P10_SUB_EST_COMP'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Estimated Completion'
,p_source=>'SUB_EST_COMP'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183752086544386807)
,p_name=>'P10_SUB_ID'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_source=>'SUB_ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183752277249386810)
,p_name=>'P10_SUB_NAME'
,p_is_required=>true
,p_item_sequence=>5
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Name'
,p_source=>'SUB_NAME'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>4000
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183753074944386812)
,p_name=>'P10_SUB_PRIORITY'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Priority'
,p_source=>'SUB_PRIORITY'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'PRIORITY'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'- None -'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183752477534386811)
,p_name=>'P10_SUB_START'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Start Date'
,p_source=>'SUB_START'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183753279293386812)
,p_name=>'P10_SUB_STATUS'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_item_default=>'0'
,p_prompt=>'Status'
,p_source=>'SUB_STATUS'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'STATUS'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183751891463386806)
,p_name=>'P10_TASK_ID'
,p_is_required=>true
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Task'
,p_source=>'TASK_ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'TASKS'
,p_cHeight=>1
,p_cattributes_element=>'class="fielddatabold"'
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183753677874386812)
,p_name=>'P10_UPDATED'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(3183750086682386800)
,p_use_cache_before_default=>'NO'
,p_source=>'UPDATED'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(241929949724771844)
,p_name=>'Cancel Modal'
,p_static_id=>'cancel-modal'
,p_event_sequence=>10
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(3183750688211386800)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(241929969974771845)
,p_event_id=>wwv_flow_imp.id(241929949724771844)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-dialog-cancel'
,p_action=>'NATIVE_DIALOG_CANCEL'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183755782303386815)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from EBA_DEMO_TREE_SUBTASK'
,p_static_id=>'fetch-row-from-eba-demo-tree-subtask'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P10_ROWID',
  'table_name', 'EBA_DEMO_TREE_SUBTASK')).to_clob
,p_internal_uid=>3170851598008658432
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183755973689386816)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of EBA_DEMO_TREE_SUBTASK'
,p_static_id=>'process-row-of-eba-demo-tree-subtask'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P10_ROWID',
  'supported_operations', 'I:U:D',
  'table_name', 'EBA_DEMO_TREE_SUBTASK')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_success_message=>'Action Processed.'
,p_internal_uid=>3170851789394658433
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183756167571386816)
,p_process_sequence=>40
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'reset page'
,p_static_id=>'reset-page'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3183750476861386800)
,p_internal_uid=>3170851983276658433
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3187515067730800983)
,p_process_sequence=>50
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Set Page Navigation'
,p_static_id=>'set-page-navigation'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if :REQUEST = ''T'' then ',
'    :LAST_VIEW := 3;',
'else',
'    :LAST_VIEW := 9;',
'end if;'))
,p_process_clob_language=>'PLSQL'
,p_internal_uid=>3174610883436072600
);
wwv_flow_imp.component_end;
end;
/
