prompt --application/pages/page_00004
begin
--   Manifest
--     PAGE: 00004
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
 p_id=>4
,p_name=>'Modify Collection Member'
,p_alias=>'MODIFY-COLLECTION-MEMBER'
,p_page_mode=>'MODAL'
,p_step_title=>'Modify Collection Member'
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
 p_id=>wwv_flow_imp.id(1723407525171506465)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>Use this page to modify a member of the collection.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1723407592968506466)
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
 p_id=>wwv_flow_imp.id(8877263432580523474)
,p_plug_name=>'Collection Member'
,p_static_id=>'collection-member'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noBorder'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877296036868545738)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1723407592968506466)
,p_button_name=>'Cancel'
,p_static_id=>'cancel'
,p_button_action=>'DEFINED_BY_DA'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'PREVIOUS'
,p_warn_on_unsaved_changes=>null
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877345618186691784)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1723407592968506466)
,p_button_name=>'Delete_Member'
,p_static_id=>'delete-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--simple:t-Button--danger'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete Member'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877300622108550962)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1723407592968506466)
,p_button_name=>'Update_Member'
,p_static_id=>'update-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Update Member'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8877296428728545740)
,p_branch_action=>'1'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877277341409534607)
,p_name=>'P4_ATTR1'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Character Attribute 1'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877281337743536246)
,p_name=>'P4_ATTR2'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Character Attribute 2'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877283634508537760)
,p_name=>'P4_ATTR3'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Character Attribute 3'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877287631489539167)
,p_name=>'P4_ATTR4'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Character Attribute 4'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877290427823540818)
,p_name=>'P4_ATTR5'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Character Attribute 5'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8406480453512174079)
,p_name=>'P4_DATE_ATTR1'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Date Attribute 1'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>4000
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
 p_id=>wwv_flow_imp.id(8406480733904177929)
,p_name=>'P4_DATE_ATTR2'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Date Attribute 2'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>4000
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
 p_id=>wwv_flow_imp.id(8406480944639180984)
,p_name=>'P4_DATE_ATTR3'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Date Attribute 3'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>4000
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
 p_id=>wwv_flow_imp.id(8877265724816527051)
,p_name=>'P4_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Name'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'N')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8440858766576004582)
,p_name=>'P4_NUM_ATTR1'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Numeric Attribute 1'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>4000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8440859047660008518)
,p_name=>'P4_NUM_ATTR2'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Numeric Attribute 2'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>4000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8440859253201010111)
,p_name=>'P4_NUM_ATTR3'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Numeric Attribute 3'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>4000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877271419209529663)
,p_name=>'P4_SEQ'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'Sequence'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'N')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8440860073202034841)
,p_name=>'P4_XMLTYPE'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_imp.id(8877263432580523474)
,p_prompt=>'XMLType'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>80
,p_cMaxlength=>4000
,p_cHeight=>5
,p_field_template=>3033038003750078790
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_help_text=>'Enter a well-formed XML fragment or document.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'Y',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(239269244410554875)
,p_name=>'Cancel Modal'
,p_static_id=>'cancel-modal'
,p_event_sequence=>10
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(8877296036868545738)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(239269341941554876)
,p_event_id=>wwv_flow_imp.id(239269244410554875)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-dialog-cancel'
,p_action=>'NATIVE_DIALOG_CANCEL'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877348515407698601)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Delete Member'
,p_static_id=>'delete-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.delete_member(',
'    p_collection_name => :P4_NAME,',
'    p_seq             => :P4_SEQ );',
'--',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error deleting member <b>&P4_SEQ.</b> in collection <b>&P4_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8877345618186691784)
,p_process_success_message=>'Successfully deleted member <b>&P4_SEQ.</b> in collection <b>&P4_NAME.</b>.'
,p_internal_uid=>8867105393702187191
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877340032709629760)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Populate form'
,p_static_id=>'populate-form'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'--',
'-- Given the values supplied for collection name and sequence,',
'-- fetch the values from the Collections database view',
'-- and populate the items on the page',
'--',
'for c1 in ( select c001, c002, c003, c004, c005, n001, n002, n003, d001, d002, d003, xmltype001',
'              from apex_collections',
'             where collection_name = :P4_NAME',
'               and seq_id = :P4_SEQ ) loop',
'    :P4_ATTR1 := c1.c001;',
'    :P4_ATTR2 := c1.c002;',
'    :P4_ATTR3 := c1.c003;',
'    :P4_ATTR4 := c1.c004;',
'    :P4_ATTR5 := c1.c005;',
'    :P4_NUM_ATTR1 := c1.n001;',
'    :P4_NUM_ATTR2 := c1.n002;',
'    :P4_NUM_ATTR3 := c1.n003;',
'    :P4_DATE_ATTR1 := c1.d001;',
'    :P4_DATE_ATTR2 := c1.d002;',
'    :P4_DATE_ATTR3 := c1.d003;',
'    if c1.xmltype001 is not null then',
'        :P4_XMLTYPE   := xmltype.extract(c1.xmltype001,''/'').getstringval();',
'    end if;',
'  ',
'    exit;',
'end loop;'))
,p_process_clob_language=>'PLSQL'
,p_internal_uid=>8867096911004118350
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877315532543569087)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Update Member'
,p_static_id=>'update-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_xmltype xmltype := null;',
'begin',
'    if :P4_XMLTYPE is not null then',
'        l_xmltype := xmltype( :P4_XMLTYPE );',
'    end if;',
'    --',
'    --',
'    -- This application uses the Application Level Date format to control the default date format for the application.',
'    -- Without this, then you would need to specify explict date format masks in the TO_DATE conversions.',
'    --',
'    apex_collection.update_member(',
'        p_collection_name => :P4_NAME,',
'        p_seq             => :P4_SEQ,',
'        p_c001            => :P4_ATTR1,',
'        p_c002            => :P4_ATTR2,',
'        p_c003            => :P4_ATTR3,',
'        p_c004            => :P4_ATTR4,',
'        p_c005            => :P4_ATTR5,',
'        p_n001            => :P4_NUM_ATTR1,',
'        p_n002            => :P4_NUM_ATTR2,',
'        p_n003            => :P4_NUM_ATTR3,',
'        p_d001            => to_date(:P4_DATE_ATTR1),',
'        p_d002            => to_date(:P4_DATE_ATTR2),',
'        p_d003            => to_date(:P4_DATE_ATTR3),',
'        p_xmltype001      => l_xmltype );',
'    commit;',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error updating member <b>&P4_SEQ.</b> in collection <b>&P4_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8877300622108550962)
,p_process_success_message=>'Successfully updated member <b>&P4_SEQ.</b> in collection <b>&P4_NAME.</b>.'
,p_internal_uid=>8867072410838057677
);
wwv_flow_imp.component_end;
end;
/
