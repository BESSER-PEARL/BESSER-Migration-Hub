prompt --application/pages/page_00002
begin
--   Manifest
--     PAGE: 00002
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7940
,p_default_id_offset=>10243121705511410
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>2
,p_name=>'Create Collection'
,p_alias=>'CREATE-COLLECTION'
,p_page_mode=>'MODAL'
,p_step_title=>'Create Collection'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>2123271369431536901
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'16'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1723407323445506463)
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
 p_id=>wwv_flow_imp.id(8876959211176475802)
,p_plug_name=>'Collection'
,p_static_id=>'collection'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_column_width=>'valign=top'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8876966136617484318)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1723407323445506463)
,p_button_name=>'Cancel'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'PREVIOUS'
,p_button_redirect_url=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.:::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8876971524974490418)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1723407323445506463)
,p_button_name=>'Create'
,p_static_id=>'create'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Create Collection'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8876974132246492524)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1723407323445506463)
,p_button_name=>'Create_Replace'
,p_static_id=>'create-replace'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create/Replace Collection'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8876966522277484320)
,p_branch_action=>'3'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8876961539415477907)
,p_name=>'P2_NAME'
,p_is_required=>true
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(8876959211176475802)
,p_prompt=>'Collection Name'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'Y',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8876988835077510306)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Create'
,p_static_id=>'create'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.create_collection( p_collection_name => :P2_NAME );',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error creating collection <b>&P2_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8876971524974490418)
,p_process_success_message=>'Successfully created collection <b>&P2_NAME.</b>.'
,p_internal_uid=>8866745713371998896
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1166558267312899931)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Create on Return Key Submit'
,p_static_id=>'create-on-return-key-submit'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.create_collection( p_collection_name => :P2_NAME );',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error creating collection <b>&P2_NAME.</b>.'
,p_process_when=>'P2_NAME'
,p_process_when_type=>'REQUEST_EQUALS_CONDITION'
,p_process_success_message=>'Successfully created collection <b>&P2_NAME.</b>.'
,p_internal_uid=>1156315145607388521
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8876993541750522320)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Create/Replace'
,p_static_id=>'create-replace'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.create_or_truncate_collection( p_collection_name => :P2_NAME );',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error creating/replacing collection <b>&P2_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8876974132246492524)
,p_process_success_message=>'Successfully created/replaced collection <b>&P2_NAME.</b>.'
,p_internal_uid=>8866750420045010910
);
wwv_flow_imp.component_end;
end;
/
