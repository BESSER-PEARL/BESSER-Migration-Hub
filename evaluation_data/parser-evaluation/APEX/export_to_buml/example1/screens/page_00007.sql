prompt --application/pages/page_00007
begin
--   Manifest
--     PAGE: 00007
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
 p_id=>7
,p_name=>'Add/Edit Collection Member'
,p_alias=>'EDITEMP'
,p_page_mode=>'MODAL'
,p_step_title=>'Add/Edit Collection Member'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>2123271369431536901
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_read_only_when_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_read_only_when=>'P7_STATUS'
,p_read_only_when2=>'D'
,p_page_component_map=>'16'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1723408030929506470)
,p_plug_name=>'Buttons'
,p_static_id=>'buttons'
,p_region_template_options=>'#DEFAULT#:t-ButtonRegion--noUI'
,p_plug_template=>2127905476394690047
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'REGION_POSITION_03'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8877651433988707945)
,p_plug_name=>'Collection Member'
,p_static_id=>'collection-member'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noBorder'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877676423641762565)
,p_button_sequence=>50
,p_button_plug_id=>wwv_flow_imp.id(1723408030929506470)
,p_button_name=>'Add_Member'
,p_static_id=>'add-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Add Member'
,p_button_position=>'NEXT'
,p_button_condition=>'P7_SEQ'
,p_button_condition_type=>'ITEM_IS_NULL'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877683314769769454)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1723408030929506470)
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
 p_id=>wwv_flow_imp.id(8877678731260764795)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1723408030929506470)
,p_button_name=>'Delete_Member'
,p_static_id=>'delete-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--simple:t-Button--danger'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete Member'
,p_button_position=>'NEXT'
,p_button_condition=>':P7_SEQ is not null and :P7_STATUS <> ''D'''
,p_button_condition2=>'PLSQL'
,p_button_condition_type=>'EXPRESSION'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877681040610767481)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1723408030929506470)
,p_button_name=>'Update_Member'
,p_static_id=>'update-member'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Update Member'
,p_button_position=>'NEXT'
,p_button_condition=>':P7_SEQ is not null and :P7_STATUS <> ''D'''
,p_button_condition2=>'PLSQL'
,p_button_condition_type=>'EXPRESSION'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(8877685730057770579)
,p_branch_action=>'6'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'BRANCH_TO_STEP'
,p_branch_sequence=>10
,p_branch_comment=>'Created 17-JUL-2002 14:16 by JOEL'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877669512613748288)
,p_name=>'P7_COMM'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Commission'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877671839774750827)
,p_name=>'P7_DEPTNO'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Dept&nbsp;No'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'DEPTNO LOV'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877654719107714821)
,p_name=>'P7_EMPNO'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Emp&nbsp;No'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_display_when=>'P7_EMPNO'
,p_display_when_type=>'ITEM_IS_NULL'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877657011991718182)
,p_name=>'P7_ENAME'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Employee&nbsp;Name'
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
 p_id=>wwv_flow_imp.id(8877664433113723599)
,p_name=>'P7_HIREDATE'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Hire&nbsp;Date'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>2000
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
 p_id=>wwv_flow_imp.id(8877659839798720423)
,p_name=>'P7_JOB'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Job'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'JOB LOV'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877662136779721871)
,p_name=>'P7_MGR'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Manager'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_lov=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select ename d, empno r',
'  from eba_demo_cs_emp',
' where (:P7_EMPNO is null or empno <> :P7_EMPNO)',
' order by 1 asc;'))
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877666724918727354)
,p_name=>'P7_SAL'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Salary'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_cSize=>64
,p_cMaxlength=>2000
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_alignment', 'right',
  'virtual_keyboard', 'text')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877688023371773696)
,p_name=>'P7_SEQ'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8877731340106872276)
,p_name=>'P7_STATUS'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'Status'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_named_lov=>'STATUS LOV'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'LOV',
  'format', 'PLAIN',
  'send_on_page_submit', 'N',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(8440862363954164589)
,p_name=>'P7_XMLTYPE'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(8877651433988707945)
,p_prompt=>'XMLType'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>80
,p_cMaxlength=>4000
,p_cHeight=>15
,p_display_when=>'P7_SEQ'
,p_display_when_type=>'ITEM_IS_NOT_NULL'
,p_field_template=>3033038003750078790
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_help_text=>'The XMLType field in this application is only used for demonstration purposes.  The value of this field is computed using the PL/SQL API DBMS_XMLGEN.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'Y',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(239269406121554877)
,p_name=>'Cancel Modal'
,p_static_id=>'cancel-modal'
,p_event_sequence=>10
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(8877683314769769454)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(239269524013554878)
,p_event_id=>wwv_flow_imp.id(239269406121554877)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-dialog-cancel'
,p_action=>'NATIVE_DIALOG_CANCEL'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877716736693828232)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Add Member'
,p_static_id=>'add-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_xmltype xmltype;',
'begin',
'if :P7_XMLTYPE is not null then',
'    l_xmltype := xmltype( :P7_XMLTYPE );',
'end if;',
'',
'apex_collection.add_member(',
'    p_collection_name => ''EMPCOLLECTION'',',
'    p_n001            => :P7_EMPNO,',
'    p_n002            => :P7_SAL,',
'    p_n003            => :P7_COMM,',
'    p_n004            => :P7_DEPTNO,',
'    p_c001            => :P7_ENAME,',
'    p_c002            => :P7_JOB,',
'    p_c003            => :P7_MGR,',
'    p_d001            => :P7_HIREDATE,',
'    p_c004            => ''N'',',
'    p_xmltype001      => l_xmltype,',
'    p_generate_md5    => ''YES'' );',
'--',
'commit;',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error adding new member to EMP collection.'
,p_process_when_button_id=>wwv_flow_imp.id(8877676423641762565)
,p_process_success_message=>'Successfully added new member to EMP collection.'
,p_internal_uid=>8867473614988316822
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877707133267799437)
,p_process_sequence=>50
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Cache'
,p_static_id=>'clear-cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_internal_uid=>8867464011562288027
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877746423704895017)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Delete Member'
,p_static_id=>'delete-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'--',
'-- If the member of the collection is ''New'', then we don''t',
'-- need to mark it for deletion, we can physically remove it',
'-- from the collection.  Otherwise, mark it for deletion so',
'-- it will be eventually physically removed from the EMP table',
'-- when applied',
'--',
'if :P7_STATUS = ''N'' then',
'    apex_collection.delete_member(',
'        p_collection_name => ''EMPCOLLECTION'',',
'        p_seq             => :P7_SEQ );',
'else',
'    apex_collection.update_member_attribute(',
'       p_collection_name => ''EMPCOLLECTION'',',
'       p_seq             => :P7_SEQ,',
'       p_attr_number     => 4,',
'       p_attr_value      => ''D'' );',
'end if;',
'--',
'commit;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>wwv_flow_string.join(wwv_flow_t_varchar2(
'Error deleting collection member.',
'',
''))
,p_process_when_button_id=>wwv_flow_imp.id(8877678731260764795)
,p_process_success_message=>'Succesfully deleted collection member.'
,p_internal_uid=>8867503301999383607
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877728512730869807)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Populate Form with Member Attributes'
,p_static_id=>'populate-form-with-member-attributes'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'for c1 in (select c001, c002, c003, c004, d001, n001, n002, n003, n004, xmltype001',
'             from apex_collections',
'            where collection_name = ''EMPCOLLECTION''',
'              and seq_id = :P7_SEQ) loop',
'    --',
'    :P7_EMPNO    := c1.n001;',
'    :P7_ENAME    := c1.c001;',
'    :P7_JOB      := c1.c002;',
'    :P7_MGR      := c1.c003;',
'    :P7_HIREDATE := c1.d001;',
'    :P7_SAL      := c1.n002;',
'    :P7_COMM     := c1.n003;',
'    :P7_DEPTNO   := c1.n004;',
'    :P7_STATUS   := c1.c004;',
'    if c1.xmltype001 is not null then',
'        :P7_XMLTYPE  := xmltype.extract(c1.xmltype001,''/*'').getstringval();',
'    end if;',
'    --',
'end loop;'))
,p_process_clob_language=>'PLSQL'
,p_process_when=>'P7_SEQ'
,p_process_when_type=>'ITEM_IS_NOT_NULL'
,p_internal_uid=>8867485391025358397
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(8877759435959934943)
,p_process_sequence=>40
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Update Member'
,p_static_id=>'update-member'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_status  varchar2(10);',
'    l_xmltype xmltype;',
'begin',
'    --',
'    -- If the member of the collection is marked as ''New'', then',
'    -- leave it marked as ''New'', otherwise mark as updated so',
'    -- it will eventually be updated to the EMP database table.',
'    --',
'    if :P7_STATUS = ''N'' then',
'        l_status := ''N'';',
'    else',
'        l_status := ''U'';',
'    end if;',
'    --',
'    if :P7_XMLTYPE is not null then',
'        l_xmltype := xmltype( :P7_XMLTYPE );',
'    end if;',
'    --',
'    apex_collection.update_member(',
'        p_collection_name => ''EMPCOLLECTION'',',
'        p_seq             => :P7_SEQ,',
'        p_n001 => :P7_EMPNO,',
'        p_n002 => :P7_SAL,',
'        p_n003 => :P7_COMM,',
'        p_n004 => :P7_DEPTNO,',
'        p_c001 => :P7_ENAME,',
'        p_c002 => :P7_JOB,',
'        p_c003 => :P7_MGR,',
'        p_d001 => :P7_HIREDATE,',
'        p_c004 => l_status,',
'        p_xmltype001 => l_xmltype );',
'    --',
'    commit;',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_process_error_message=>'Error updating collection member.'
,p_process_when_button_id=>wwv_flow_imp.id(8877681040610767481)
,p_process_success_message=>'Succesfully updated collection member.'
,p_internal_uid=>8867516314254423533
);
wwv_flow_imp.component_end;
end;
/
