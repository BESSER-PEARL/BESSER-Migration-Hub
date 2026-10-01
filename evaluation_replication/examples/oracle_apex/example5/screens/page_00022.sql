prompt --application/pages/page_00022
begin
--   Manifest
--     PAGE: 00022
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
 p_id=>22
,p_name=>'Edit'
,p_alias=>'EDIT7'
,p_step_title=>'Edit'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'.ui-slider {',
'    width: 180px;',
'    margin: 8px;',
'}'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2674970952418104760)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page contains two dynamic actions called ''SALARY HIGH'' and ''CALC COMMISSION''.</p><p>''SALARY HIGH'' fires whenever the value of the ''Salary'' slider has changed and checks if the salary is greater than 5000. If the salary is greater than 5000 th'
||'e salary display field is set to red. If the salary is less than or equal to 5000 the salary display field is set to green.</p><p>''CALC COMMISSION'' does a similar job as in the ''Set Value (PL/SQL)'' example (firing an AJAX call to retrieve the commiss'
||'ion and highlighting the ''Commission'' page item), only this time, it is being fired when the value of the ''Salary'' slider changes.</p>',
'<p>''SALARY HIGH'' uses one native action (''Add Class'') in combination with an event raised by one plug-in item type (''Slider'').</p>',
'<p>''CALC COMMISSION'' uses one native action (''Set Value'' with a ''Set Type'' of ''PL/SQL Function Body'') and one plug-in action (''Highlight'').</p>',
''))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2674874748140092580)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>30
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(8199705487948627945)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674867958823092517)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(2674874748140092580)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'f?p=&APP_ID.:21:&SESSION.::&DEBUG.:::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2674867663546092515)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(2674874748140092580)
,p_button_name=>'SAVE'
,p_static_id=>'save'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'NEXT'
,p_button_condition=>'P22_ROWID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(2674868559078092524)
,p_branch_action=>'f?p=&APP_ID.:21:&SESSION.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2674870538608092550)
,p_name=>'P22_COMM'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674870740750092550)
,p_name=>'P22_DEPTNO'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Department'
,p_source=>'DEPTNO'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'P22_EBA_DEMO_DA_EMP_DEPTNO'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2674868955731092543)
,p_name=>'P22_EMPNO'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674869146197092544)
,p_name=>'P22_ENAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674870149542092550)
,p_name=>'P22_HIREDATE'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674869360555092545)
,p_name=>'P22_JOB'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Job'
,p_source=>'JOB'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'P22_EBA_DEMO_DA_EMP_JOB'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(2674869765361092549)
,p_name=>'P22_MGR'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Manager'
,p_source=>'MGR'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_POPUP_LOV'
,p_named_lov=>'P22_EBA_DEMO_DA_EMP_MGR'
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
 p_id=>wwv_flow_imp.id(2674868765964092531)
,p_name=>'P22_ROWID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
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
 p_id=>wwv_flow_imp.id(2674870345359092550)
,p_name=>'P22_SAL'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(2674867341731092513)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Salary'
,p_source=>'SAL'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'PLUGIN_COM.ORACLE.APEX.SLIDER'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_encrypt_session_state_yn=>'N'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', 'horizontal',
  'attribute_02', '0',
  'attribute_03', '10000',
  'attribute_04', '100',
  'attribute_05', 'N',
  'attribute_06', ' ')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(2675214059662229834)
,p_name=>'CALC COMMISSION'
,p_static_id=>'calc-commission'
,p_event_sequence=>20
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P22_SAL'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'PLUGIN_COM.ORACLE.APEX.SLIDER|ITEM TYPE|slidechange'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2675214361157229834)
,p_event_id=>wwv_flow_imp.id(2675214059662229834)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-set-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P22_COMM'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'escape_special_characters', 'Y',
  'items_to_submit', 'P22_JOB,P22_SAL',
  'plsql_function_body', wwv_flow_string.join(wwv_flow_t_varchar2(
    'declare',
    '    l_multiplier number := 0;',
    'begin',
    '    -- determine multiplier based on job',
    '    case :P22_JOB',
    '        when ''ANALYST''      then l_multiplier := .1;',
    '        when ''CLERK''        then l_multiplier := .2;',
    '        when ''MANAGER''      then l_multiplier := .3;',
    '        when ''PRESIDENT''    then l_multiplier := .4;',
    '        when ''SALESMAN''     then l_multiplier := .3;',
    '        else                     l_multiplier := .1;',
    '    end case;',
    '    -- return commission, which is calculated by multiplying salary my multiplier',
    '    return :P22_SAL * l_multiplier;',
    'end;')),
  'suppress_change_event', 'N',
  'type', 'FUNCTION_BODY')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2675237455984238233)
,p_event_id=>wwv_flow_imp.id(2675214059662229834)
,p_event_result=>'TRUE'
,p_action_sequence=>20
,p_execute_on_page_init=>'N'
,p_static_id=>'plugin-com-oracle-apex-highlight'
,p_action=>'PLUGIN_COM.ORACLE.APEX.HIGHLIGHT'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P22_COMM'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', '#E5FFCC',
  'attribute_02', 'slow')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(2675107249788189176)
,p_name=>'SALARY HIGH'
,p_static_id=>'salary-high'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P22_SAL'
,p_condition_element=>'P22_SAL'
,p_triggering_condition_type=>'GREATER_THAN'
,p_triggering_expression=>'5000'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'PLUGIN_COM.ORACLE.APEX.SLIDER|ITEM TYPE|slidechange'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2675107550626189176)
,p_event_id=>wwv_flow_imp.id(2675107249788189176)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-set-css'
,p_action=>'NATIVE_SET_CSS'
,p_affected_elements_type=>'DOM_OBJECT'
,p_affected_elements=>'P22_SAL_display'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'style_name', 'color',
  'value', 'red')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(2675107761375189176)
,p_event_id=>wwv_flow_imp.id(2675107249788189176)
,p_event_result=>'FALSE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-set-css-2'
,p_action=>'NATIVE_SET_CSS'
,p_affected_elements_type=>'DOM_OBJECT'
,p_affected_elements=>'P22_SAL_display'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'style_name', 'color',
  'value', 'green')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2674872149813092552)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from EBA_DEMO_DA_EMP'
,p_static_id=>'fetch-row-from-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P22_ROWID',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_internal_uid=>2668715744985111427
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2674872358015092556)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of EBA_DEMO_DA_EMP'
,p_static_id=>'process-row-of-eba-demo-da-emp'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'ROWID',
  'primary_key_item', 'P22_ROWID',
  'supported_operations', 'I:U:D',
  'table_name', 'EBA_DEMO_DA_EMP')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_success_message=>'Action Processed.'
,p_internal_uid=>2668715953187111431
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(2674872547177092556)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'reset page'
,p_static_id=>'reset-page'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_internal_uid=>2668716142349111431
);
wwv_flow_imp.component_end;
end;
/
