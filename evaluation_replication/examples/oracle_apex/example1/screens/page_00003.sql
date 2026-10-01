prompt --application/pages/page_00003
begin
--   Manifest
--     PAGE: 00003
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
 p_id=>3
,p_name=>'Modify Collection'
,p_alias=>'MODIFY-COLLECTION'
,p_step_title=>'Modify Collection'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'16'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1723407474221506464)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>Use this page to add members (records) into your collection. Note that this application does not use all of the fields available in APEX collections.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328920195717899032)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>1
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(1328919002858891716)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8877019135766722663)
,p_plug_name=>'Collection'
,p_static_id=>'collection'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_column_width=>'valign=top'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8877020432532724174)
,p_plug_name=>'Member Attributes'
,p_static_id=>'member-attributes'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877057841456760137)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1328920195717899032)
,p_button_name=>'Add_Member'
,p_static_id=>'add-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Add Member'
,p_button_position=>'CREATE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877200918935446007)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1328920195717899032)
,p_button_name=>'Add_Member_Add_Another'
,p_static_id=>'add-member-add-another'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Add Member & Add Another'
,p_button_position=>'CREATE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877036341063731629)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1328920195717899032)
,p_button_name=>'Cancel'
,p_static_id=>'cancel'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'CLOSE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877224521537484556)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(8877019135766722663)
,p_button_name=>'Delete_Collection'
,p_static_id=>'delete-collection'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--simple:t-Button--danger'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete Collection'
,p_button_position=>'EDIT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877236235520498017)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(8877019135766722663)
,p_button_name=>'Resequence'
,p_static_id=>'resequence'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Resequence'
,p_button_position=>'EDIT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877217142877481267)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(8877019135766722663)
,p_button_name=>'Truncate_Collection'
,p_static_id=>'truncate-collection'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Truncate Collection'
,p_button_position=>'EDIT'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8877039543518734292)
,p_branch_action=>'1'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_sequence=>20
,p_branch_comment=>'Created 16-JUL-2002 15:56 by JOEL'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8877201335351446017)
,p_branch_action=>'3'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_when_button_id=>wwv_flow_imp.id(8877200918935446007)
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877043132304739457)
,p_name=>'P3_ATTR1'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8877045428206741410)
,p_name=>'P3_ATTR2'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8877047723461743567)
,p_name=>'P3_ATTR3'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8877050019148745537)
,p_name=>'P3_ATTR4'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8877052315051747413)
,p_name=>'P3_ATTR5'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8406477546015105740)
,p_name=>'P3_DATE_ATTR1'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8406477837142112641)
,p_name=>'P3_DATE_ATTR2'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8406478044415114685)
,p_name=>'P3_DATE_ATTR3'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8877029527787726401)
,p_name=>'P3_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(8877019135766722663)
,p_prompt=>'Collection Name'
,p_source=>'P2_NAME'
,p_source_type=>'ITEM'
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
 p_id=>wwv_flow_imp.id(8439857769247202679)
,p_name=>'P3_NUM_ATTR1'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8439857967683202680)
,p_name=>'P3_NUM_ATTR2'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
 p_id=>wwv_flow_imp.id(8439858156437202680)
,p_name=>'P3_NUM_ATTR3'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(8877020432532724174)
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
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(8877243735396506962)
,p_validation_name=>'Collection Name not null'
,p_static_id=>'collection-name-not-null'
,p_validation_sequence=>10
,p_validation=>'P3_NAME'
,p_validation_type=>'ITEM_NOT_NULL'
,p_error_message=>'Collection name cannot be null'
,p_validation_condition=>':REQUEST in (''Truncate_Collection'',''Delete_Collection'',''Resequence'',''Add_Member'',''Add_Member_Add_Another'')'
,p_validation_condition2=>'PLSQL'
,p_validation_condition_type=>'EXPRESSION'
,p_associated_item=>wwv_flow_imp.id(8877029527787726401)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877065121496774857)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Add Member'
,p_static_id=>'add-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'--',
'-- This application uses the Application Level Date format to control the default date format for the application.',
'-- Without this, then you would need to specify explict date format masks in the TO_DATE conversions.',
'apex_collection.add_member(',
'    p_collection_name => :P3_NAME,',
'    p_c001            => :P3_ATTR1,',
'    p_c002            => :P3_ATTR2,',
'    p_c003            => :P3_ATTR3,',
'    p_c004            => :P3_ATTR4,',
'    p_c005            => :P3_ATTR5,',
'    p_n001            => :P3_NUM_ATTR1,',
'    p_n002            => :P3_NUM_ATTR2,',
'    p_n003            => :P3_NUM_ATTR3,',
'    p_d001            => to_date(:P3_DATE_ATTR1),',
'    p_d002            => to_date(:P3_DATE_ATTR2),',
'    p_d003            => to_date(:P3_DATE_ATTR3),',
'    p_generate_md5    => ''YES'' );',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error adding member to collection <b>&P3_NAME.</b>.'
,p_process_when=>':REQUEST in (''Add_Member'',''Add_Member_Add_Another'')'
,p_process_when_type=>'EXPRESSION'
,p_process_when2=>'SQL'
,p_process_success_message=>'Successfully added member to collection <b>&P3_NAME.</b>.'
,p_internal_uid=>8866821999791263447
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(7970689830689204915)
,p_process_sequence=>50
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Cache'
,p_static_id=>'clear-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_internal_uid=>7960446708983693505
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877361623577725174)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Delete Collection'
,p_static_id=>'delete-collection'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.delete_collection(',
'    p_collection_name => :P3_NAME );',
'--',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error deleting collection <b>&P3_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8877224521537484556)
,p_process_success_message=>'Successfully deleted collection <b>&P3_NAME.</b>.'
,p_internal_uid=>8867118501872213764
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877357243202716012)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Resequence'
,p_static_id=>'resequence'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.resequence_collection(',
'    p_collection_name => :P3_NAME );',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error resequencing members in collection <b>&P3_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8877236235520498017)
,p_process_success_message=>'Successfully resequenced members in collection <b>&P3_NAME.</b>.'
,p_internal_uid=>8867114121497204602
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877424317396168659)
,p_process_sequence=>40
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Truncate Collection'
,p_static_id=>'truncate-collection'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'apex_collection.truncate_collection(',
'    p_collection_name => :P3_NAME );',
'--',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error truncating collection <b>&P3_NAME.</b>.'
,p_process_when_button_id=>wwv_flow_imp.id(8877217142877481267)
,p_process_success_message=>'Successfully truncated collection <b>&P3_NAME.</b>.'
,p_internal_uid=>8867181195690657249
);
wwv_flow_imp.component_end;
end;
/
