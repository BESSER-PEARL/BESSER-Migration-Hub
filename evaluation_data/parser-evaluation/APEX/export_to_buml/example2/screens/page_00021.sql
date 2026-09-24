prompt --application/pages/page_00021
begin
--   Manifest
--     PAGE: 00021
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7850
,p_default_id_offset=>11008923455465249
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>21
,p_name=>'Data Load Source'
,p_alias=>'DATA-LOAD-SOURCE'
,p_step_title=>'Data Load Source'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>wwv_flow_string.join(wwv_flow_t_varchar2(
'function set_item()',
'{',
'$s("P21_IMPORT_FROM", "PASTE");',
'$x(''P21_COPY_PASTE'').value= $v(''P21_SAMPLE_DATA'');',
'$x(''P21_SEPARATOR'').value= '','';',
'$s(''P21_FIRST_ROW'', ''Y'');',
'}'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'17'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3386440438325086977)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--info'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>The Data Loading available starting from APEX 21.1 does not allow end users to speficy column mappings.  If it is important to allow your end users to do column mappings, please use the Legacy Data Loading Wizard.</a>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3338224527994735625)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>40
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(11521794561627835810)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4340448053770684068)
,p_plug_name=>'Data Load Source'
,p_static_id=>'data-load-source'
,p_parent_plug_id=>wwv_flow_imp.id(4340447823672684067)
,p_region_template_options=>'#DEFAULT#'
,p_region_attributes=>'style="width:100%;max-width:none;"'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'output_as', 'TEXT',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4340447823672684067)
,p_plug_name=>'Data Load Wizard Progress'
,p_static_id=>'data-load-wizard-progress'
,p_region_template_options=>'#DEFAULT#:t-Wizard--hideStepsSmall'
,p_component_template_options=>'#DEFAULT#:t-WizardSteps--displayLabels'
,p_plug_template=>2120525352897701877
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_list_id=>wwv_flow_imp.id(4340445102949684061)
,p_plug_source_type=>'NATIVE_LIST'
,p_list_template_id=>2011625478452504874
,p_translate_title=>'N'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(4302984181828657060)
,p_plug_name=>'Page Instructions'
,p_static_id=>'page-instructions'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Choose the <b>Import From</b> of "Copy and Paste", input <b>Separator</b> as "," and ensure the <b>First Row has Column Names</b> is checked.</br>',
' <b>',
'<a href="javascript:set_item();"> Click here </b></a> to copy and paste, or select the text below and paste it into the <b>Copy and Paste Delimited Data</b> section. <br> ',
'</p>',
'Empno,Ename,Job,Mgr,Hiredate,Sal,Comm,Deptno</br>',
'8011,Campbell,CLERK,King,1-Nov-11,1300,,ACCOUNTING</br>',
'8021,Chevy,ANALYST,Ford,20-Oct-11,3000,,RESEARCH</br>',
'7788,Scott,SALESMAN,BLAKE,9-Dec-82,3000,200,RESEARCH</br>',
'7698,BLAKE,MANAGER,CLARK,1-May-81,3500,,ACCOUNTING</br>',
'8118,BENZ,ANALYST,FORD,10-Oct-11,2800,,ACCOUNTING</br>',
'</br>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(4340448504407684068)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(4340447823672684067)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'PREVIOUS'
,p_button_redirect_url=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.'
,p_button_condition_type=>'NEVER'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(4340448931594684068)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(4340447823672684067)
,p_button_name=>'NEXT'
,p_static_id=>'next'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#:t-Button--iconRight'
,p_button_template_id=>2084305881903810008
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Next'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'javascript:apex.widget.textareaClob.uploadNonEmpty(''P21_COPY_PASTE'', ''NEXT'');'
,p_icon_css_classes=>'fa-chevron-right'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(4340465518078684084)
,p_branch_action=>'f?p=&APP_ID.:22:&SESSION.&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_when_button_id=>wwv_flow_imp.id(4340448931594684068)
,p_branch_sequence=>10
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340456870789684076)
,p_name=>'P21_APP_DATE_FORMAT'
,p_item_sequence=>150
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'Y'
,p_prompt=>'Date / Number Formats to use'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_RADIOGROUP'
,p_named_lov=>'DATE_FORMAT_OPT'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_help_text=>'Choose whether to provide custom or to use standard format masks'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_of_columns', '1',
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340457777991684079)
,p_name=>'P21_CHAR_SET'
,p_is_required=>true
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'UTF-8'
,p_prompt=>'File Character Set'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'DATA_LOAD_CHARSET'
,p_cHeight=>1
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_help_text=>'DATA_LOAD.CHAR_SET_ITEM_HELP'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340450963021684071)
,p_name=>'P21_COPY_PASTE'
,p_item_sequence=>15
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_prompt=>'Copy and Paste Delimited Data'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>80
,p_cHeight=>10
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'Y',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340458703803684079)
,p_name=>'P21_CURRENCY'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'$'
,p_prompt=>'Currency Symbol'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select value',
'  from nls_session_parameters',
' where parameter = ''NLS_CURRENCY'''))
,p_source_type=>'QUERY'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>2
,p_cMaxlength=>2
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>'If your data contains international currency symbol, enter it here. For example, if your data has "&euro;1,234.56" or "&yen;1,234.56", enter "&euro;" or "&yen;".  Otherwise the data will not load correctly.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340460352690684081)
,p_name=>'P21_DECIMAL_CHARACTER'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_prompt=>'Decimal Character'
,p_source=>'apex_application.get_nls_decimal_separator'
,p_source_type=>'EXPRESSION'
,p_source_language=>'PLSQL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>2
,p_cMaxlength=>2
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>The decimal character separates the integer and decimal parts of a number.</p>',
'<p> Any character can be the decimal character. The character specified must be single-byte, and the decimal character must be different from group separator. The character can be a space, but cannot be any numeric character or any of the following c'
||'haracters:</p>',
'<ul class="noIndent">',
'<li>plus (+)</li>',
'<li>hyphen (-)</li> ',
'<li>less than sign (<)</li>',
'<li>greater than sign (>)</li> ',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340452423348684072)
,p_name=>'P21_ENCLOSED_BY'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'"'
,p_prompt=>'Optionally Enclosed By'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>2
,p_cMaxlength=>2
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>'Enter a delimiter character. You can use this character to delineate the starting and ending boundary of a data value. If you specify a delimiter character, Data Workshop ignores whitespace occurring before the starting and ending boundary of a data '
||'value. You can also use this option to enclose a data value with the specified delimiter character.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340449683238684069)
,p_name=>'P21_FILE_NAME'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_prompt=>'File Name'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_FILE'
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>'Name of the file to upload'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'allow_copy_paste', 'N',
  'allow_multiple_files', 'N',
  'display_as', 'INLINE',
  'purge_file_at', 'REQUEST',
  'storage_type', 'APEX_APPLICATION_TEMP_FILES')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340453259126684073)
,p_name=>'P21_FIRST_ROW'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'Y'
,p_prompt=>'&nbsp;'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_CHECKBOX'
,p_lov=>'STATIC:First Row has Column Names;Y'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_of_columns', '1')).to_clob
,p_multi_value_type=>'SEPARATED'
,p_multi_value_separator=>':'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340459545689684080)
,p_name=>'P21_GROUP_SEPARATOR'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_prompt=>'Group Separator'
,p_source=>'apex_application.get_nls_group_separator'
,p_source_type=>'EXPRESSION'
,p_source_language=>'PLSQL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>2
,p_cMaxlength=>2
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>A group separator is a character that separates integer groups, for example to show thousands and millions.</p>',
'<p>Any character can be the group separator. The character specified must be single-byte, and the group separator must be different from any other decimal character. The character can be a space, but cannot be a numeric character or any of the follow'
||'ing:</p>',
'<ul class="noIndent">',
'<li>plus (+)</li>',
'<li>hyphen (-)</li> ',
'<li>less than sign (<)</li>',
'<li>greater than sign (>)</li> ',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340449429482684069)
,p_name=>'P21_IMPORT_FROM'
,p_is_required=>true
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'PASTE'
,p_prompt=>'Import From'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_RADIOGROUP'
,p_named_lov=>'DATA_LOAD_OPTION'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_of_columns', '1',
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4302984327419657061)
,p_name=>'P21_SAMPLE_DATA'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(4302984181828657060)
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'Empno,Ename,Job,Mgr,Hiredate,Sal,Comm,Deptno',
'8011,Campbell,CLERK,King,1-Nov-11,1300,,ACCOUNTING',
'8021,Chevy,ANALYST,Ford,20-Oct-11,3000,,RESEARCH',
'7788,Scott,SALESMAN,BLAKE,9-Dec-82,3000,200,RESEARCH',
'7698,BLAKE,MANAGER,CLARK,1-May-81,3500,,ACCOUNTING',
'8118,BENZ,ANALYST,FORD,10-Oct-11,2800,,ACCOUNTING'))
,p_source_type=>'STATIC'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340451496418684072)
,p_name=>'P21_SEPARATOR'
,p_is_required=>true
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_item_default=>'\t'
,p_prompt=>'Separator'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>2
,p_cMaxlength=>2
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>'Identify a column separator character. Use <code>\t</code> for tab separators.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(4340454186277684074)
,p_name=>'P21_SHOW_ADV_SETTINGS'
,p_item_sequence=>55
,p_item_plug_id=>wwv_flow_imp.id(4340448053770684068)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_CHECKBOX'
,p_lov=>'STATIC:Use Advanced Settings;Y'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'number_of_columns', '1')).to_clob
,p_multi_value_type=>'SEPARATED'
,p_multi_value_separator=>':'
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(4302985073849657069)
,p_computation_sequence=>10
,p_computation_item=>'P21_COPY_PASTE'
,p_static_id=>'p21-copy-paste'
,p_computation_point=>'BEFORE_HEADER'
,p_computation_type=>'STATIC_ASSIGNMENT'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(4340450711934684071)
,p_validation_name=>'Filename is not null'
,p_static_id=>'filename-is-not-null'
,p_validation_sequence=>10
,p_validation=>'P21_FILE_NAME'
,p_validation_type=>'ITEM_NOT_NULL'
,p_error_message=>'#LABEL# must have some value.'
,p_validation_condition=>'P21_IMPORT_FROM'
,p_validation_condition2=>'UPLOAD'
,p_validation_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_when_button_pressed=>wwv_flow_imp.id(4340448931594684068)
,p_associated_item=>wwv_flow_imp.id(4340449683238684069)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(4340455134125684074)
,p_validation_name=>'Uploaded data is not null'
,p_static_id=>'uploaded-data-is-not-null'
,p_validation_sequence=>20
,p_validation=>'P21_COPY_PASTE'
,p_validation_type=>'ITEM_NOT_NULL'
,p_error_message=>'#LABEL# must have some value.'
,p_validation_condition=>'P21_IMPORT_FROM'
,p_validation_condition2=>'PASTE'
,p_validation_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_when_button_pressed=>wwv_flow_imp.id(4340448931594684068)
,p_associated_item=>wwv_flow_imp.id(4340450963021684071)
,p_error_display_location=>'INLINE_WITH_FIELD_AND_NOTIFICATION'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(4340461159514684081)
,p_name=>'Import From Copy and Paste'
,p_static_id=>'import-from-copy-and-paste'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_IMPORT_FROM'
,p_condition_element=>'P21_IMPORT_FROM'
,p_triggering_condition_type=>'EQUALS'
,p_triggering_expression=>'PASTE'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340462687343684082)
,p_event_id=>wwv_flow_imp.id(4340461159514684081)
,p_event_result=>'FALSE'
,p_action_sequence=>20
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-hide'
,p_action=>'NATIVE_HIDE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_COPY_PASTE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'hide_page_items_on_same_line', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340462238972684082)
,p_event_id=>wwv_flow_imp.id(4340461159514684081)
,p_event_result=>'TRUE'
,p_action_sequence=>20
,p_execute_on_page_init=>'N'
,p_static_id=>'native-set-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_SEPARATOR'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'suppress_change_event', 'N',
  'type', 'STATIC_ASSIGNMENT',
  'value', '\t')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340461656918684081)
,p_event_id=>wwv_flow_imp.id(4340461159514684081)
,p_event_result=>'TRUE'
,p_action_sequence=>20
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-show'
,p_action=>'NATIVE_SHOW'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_COPY_PASTE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_on_same_line', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(4340463069408684083)
,p_name=>'Import from File'
,p_static_id=>'import-from-file'
,p_event_sequence=>20
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_IMPORT_FROM'
,p_condition_element=>'P21_IMPORT_FROM'
,p_triggering_condition_type=>'EQUALS'
,p_triggering_expression=>'UPLOAD'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340464609641684084)
,p_event_id=>wwv_flow_imp.id(4340463069408684083)
,p_event_result=>'FALSE'
,p_action_sequence=>20
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-hide'
,p_action=>'NATIVE_HIDE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_FILE_NAME'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'hide_page_items_on_same_line', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340464109192684083)
,p_event_id=>wwv_flow_imp.id(4340463069408684083)
,p_event_result=>'TRUE'
,p_action_sequence=>20
,p_execute_on_page_init=>'N'
,p_static_id=>'native-set-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_SEPARATOR'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'suppress_change_event', 'N',
  'type', 'STATIC_ASSIGNMENT',
  'value', ',')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340463623853684083)
,p_event_id=>wwv_flow_imp.id(4340463069408684083)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-show'
,p_action=>'NATIVE_SHOW'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_FILE_NAME'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'show_on_same_line', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(4340455438119684075)
,p_name=>'Show/Hide Advanced Settings'
,p_static_id=>'show-hide-advanced-settings'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_SHOW_ADV_SETTINGS'
,p_condition_element=>'P21_SHOW_ADV_SETTINGS'
,p_triggering_condition_type=>'EQUALS'
,p_triggering_expression=>'Y'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'change'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340456422009684076)
,p_event_id=>wwv_flow_imp.id(4340455438119684075)
,p_event_result=>'FALSE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-hide'
,p_action=>'NATIVE_HIDE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_CURRENCY,P21_GROUP_SEPARATOR,P21_DECIMAL_CHARACTER,P21_APP_DATE_FORMAT,P21_CHAR_SET'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(4340455854483684075)
,p_event_id=>wwv_flow_imp.id(4340455438119684075)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'Y'
,p_static_id=>'native-show'
,p_action=>'NATIVE_SHOW'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_CURRENCY,P21_GROUP_SEPARATOR,P21_DECIMAL_CHARACTER,P21_APP_DATE_FORMAT,P21_CHAR_SET'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(4340465073085684084)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PARSE_UPLOADED_DATA'
,p_process_name=>'Parse Uploaded Data'
,p_static_id=>'parse-uploaded-data'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'character_set_item', 'P21_CHAR_SET',
  'copy_and_paste_item', 'P21_COPY_PASTE',
  'currency_symbol_item', 'P21_CURRENCY',
  'data_load_definition_id', wwv_flow_imp.id(5971589154111614287),
  'date_format_item', 'P21_APP_DATE_FORMAT',
  'decimal_character_item', 'P21_DECIMAL_CHARACTER',
  'enclosed_by_item', 'P21_ENCLOSED_BY',
  'filename_item', 'P21_FILE_NAME',
  'first_row_item', 'P21_FIRST_ROW',
  'group_separator_item', 'P21_GROUP_SEPARATOR',
  'import_from_item', 'P21_IMPORT_FROM',
  'separator_item', 'P21_SEPARATOR')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(4340448931594684068)
,p_internal_uid=>2670875472146359754
);
wwv_flow_imp.component_end;
end;
/
