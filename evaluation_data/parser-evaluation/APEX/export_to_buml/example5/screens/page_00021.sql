prompt --application/pages/page_00021
begin
--   Manifest
--     PAGE: 00021
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
 p_id=>21
,p_name=>'Debounce and Throttle'
,p_alias=>'DEBOUNCE-AND-THROTTLE'
,p_step_title=>'Debounce and Throttle'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'17'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(592363548607819030)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>10
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(8199705487948627945)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764562417627650)
,p_plug_name=>'Debounce Delay'
,p_static_id=>'debounce-delay'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>40
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573765106373627656)
,p_plug_name=>'Debounce Delay Help Text'
,p_static_id=>'debounce-delay-help-text'
,p_parent_plug_id=>wwv_flow_imp.id(573764562417627650)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p><strong>Debounce Delay:</strong> the Dynamic Action will execute 2000ms after the key release event was triggered. If the event is triggered multiple times before the delay is over, the timer resets each time and the action will execute after the '
||'last event.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764660933627651)
,p_plug_name=>'Debounce Immediate'
,p_static_id=>'debounce-immediate'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>50
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573765668502627661)
,p_plug_name=>'Debounce Immediate Help Text'
,p_static_id=>'debounce-immediate-help-text'
,p_parent_plug_id=>wwv_flow_imp.id(573764660933627651)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p><strong>Debounce Immediate:</strong> the Dynamic Action will execute immediately after the first key release event before starting the timer for 2000ms. If the event is triggered before the delay is over, the timer resets each time and all events '
||'are ignored until the delay is over.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(611961814479935449)
,p_plug_name=>'Enter Text Here'
,p_static_id=>'enter-text-here'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(611961741294935448)
,p_plug_name=>'Examples'
,p_static_id=>'examples'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_grid_column_span=>8
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764390508627649)
,p_plug_name=>'Immediate'
,p_static_id=>'immediate'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573765001153627655)
,p_plug_name=>'Immediate Help Text'
,p_static_id=>'immediate-help-text'
,p_parent_plug_id=>wwv_flow_imp.id(573764390508627649)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p><strong>Immediate:</strong> the Dynamic Action will execute immediately. Each time a key is released, the item will be updated to have the same value as the text area.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764095280627646)
,p_plug_name=>'Overview'
,p_static_id=>'overview'
,p_region_template_options=>'#DEFAULT#:t-ContentBlock--h2:js-headingLevel-2'
,p_plug_template=>2323592004483952560
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_grid_column_span=>8
,p_plug_grid_column_css_classes=>'col-sm-12'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This page demonstrates how the Execution properties of Dynamic Actions provide control over when a dynamic action executes. By default, actions are executed immediately. However, the Debounce and Throttle execution types can delay the execution of'
||' a dynamic action.</p>',
'<p>Debounce will execute an action a single time after a specified delay from the last time the dynamic action was triggered. Here are a couple examples:</p>',
'    <ul>',
'        <li>Use <strong>Debounce Delay</strong> to fire an AJAX request when a user has stopped typing for 2 seconds.</li>',
'        <li>Use <strong>Debounce Immediate</strong> to refresh a region once after a user clicks a button, then ignore all following button clicks until 2 seconds has passed from the last click.</li>',
'    </ul>',
'<p>Throttle will execute an action in intervals of a specified length, as long as the dynamic action continues getting triggered. Here are a couple examples:</p>',
'    <ul>',
'        <li>Use <strong>Throttle Immediate</strong> to refresh a region once every 2 seconds as a user continuously clicks a button.</li>',
'        <li>Use <strong>Throttle Delay</strong> to wait for page item values of a form to update before submitting the page when the Save button is clicked.</li>',
'    </ul>',
'<p>In the example on this page, typing in the text area will trigger dynamic actions to update each of the display only items. Each item will update a little differently based on the event Type used to execute the Set Value action.</p>',
''))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764806247627653)
,p_plug_name=>'Throttle Delay'
,p_static_id=>'throttle-delay'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>70
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573766130441627666)
,p_plug_name=>'Throttle Delay Help Text'
,p_static_id=>'throttle-delay-help-text'
,p_parent_plug_id=>wwv_flow_imp.id(573764806247627653)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p><strong>Throttle Delay:</strong> the Dynamic Action will execute 2000ms after the first key release event. If the event is triggered multiple times before the delay is over, the last triggered event will be executed at the end of the initial delay'
||'.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573764766215627652)
,p_plug_name=>'Throttle Immediate'
,p_static_id=>'throttle-immediate'
,p_parent_plug_id=>wwv_flow_imp.id(611961741294935448)
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--stacked:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>60
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(573765946790627664)
,p_plug_name=>'Throttle Immediate Help Text'
,p_static_id=>'throttle-immediate-help-text'
,p_parent_plug_id=>wwv_flow_imp.id(573764766215627652)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>3372714138756020509
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p><strong>Throttle Immediate:</strong> the Dynamic Action will execute immediately after the first key release and then the 2000ms delay begins. If the event is triggered during the delay, the last triggered event will be executed after the initial '
||'delay and another delay begins.</p>',
''))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573768569421627639)
,p_name=>'P21_DEBOUNCE_DELAY'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(573764562417627650)
,p_prompt=>'Debounce Delay'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Dynamic Action Settings:</p>',
'<ul>',
'    <li>Event: Key Release</li>',
'    <li>Execution Type: Debounce</li>',
'    <li>Execution Time: 2000</li>',
'    <li>Execution Immediate: off</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573770505065627641)
,p_name=>'P21_DEBOUNCE_IMMEDIATE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(573764660933627651)
,p_prompt=>'Debounce Immediate'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Dynamic Action Settings:</p>',
'<ul>',
'    <li>Event: Key Release</li>',
'    <li>Execution Type: Debounce</li>',
'    <li>Execution Time: 2000</li>',
'    <li>Execution Immediate: on</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573766682517627639)
,p_name=>'P21_IMMEDIATE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(573764390508627649)
,p_prompt=>'Immediate'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Dynamic Action Settings:</p>',
'<ul>',
'    <li>Event: Key Release</li>',
'    <li>Execution Type: Immediate</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573773993833627626)
,p_name=>'P21_TEXT_AREA'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(611961814479935449)
,p_prompt=>'Enter Text Here'
,p_placeholder=>'Start typing...'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>30
,p_cHeight=>5
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'N',
  'trim_spaces', 'BOTH')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573774207879627644)
,p_name=>'P21_THROTTLE_DELAY'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(573764806247627653)
,p_prompt=>'Throttle Delay'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Dynamic Action Settings:</p>',
'<ul>',
'    <li>Event: Key Release</li>',
'    <li>Execution Type: Throttle</li>',
'    <li>Execution Time: 2000</li>',
'    <li>Execution Immediate: off</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(573772216607627642)
,p_name=>'P21_THROTTLE_IMMEDIATE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(573764766215627652)
,p_prompt=>'Throttle Immediate'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_DISPLAY_ONLY'
,p_begin_on_new_line=>'N'
,p_colspan=>4
,p_field_template=>1610598304472262251
,p_item_template_options=>'#DEFAULT#'
,p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Dynamic Action Settings:</p>',
'<ul>',
'    <li>Event: Key Release</li>',
'    <li>Execution Type: Throttle</li>',
'    <li>Execution Time: 2000</li>',
'    <li>Execution Immediate: on</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'based_on', 'VALUE',
  'format', 'PLAIN',
  'send_on_page_submit', 'Y',
  'show_line_breaks', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(6611929550701453)
,p_name=>'Update P21_DEBOUNCE_DELAY'
,p_static_id=>'update-p21-debounce-delay'
,p_event_sequence=>20
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_TEXT_AREA'
,p_bind_type=>'bind'
,p_execution_type=>'DEBOUNCE'
,p_execution_time=>2000
,p_execution_immediate=>false
,p_bind_event_type=>'keyup'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(6612369190701453)
,p_event_id=>wwv_flow_imp.id(6611929550701453)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_name=>'Set item value'
,p_static_id=>'set-item-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_DEBOUNCE_DELAY'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.value',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(6612853550701452)
,p_name=>'Update P21_DEBOUNCE_IMMEDIATE'
,p_static_id=>'update-p21-debounce-immediate'
,p_event_sequence=>30
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_TEXT_AREA'
,p_bind_type=>'bind'
,p_execution_type=>'DEBOUNCE'
,p_execution_time=>2000
,p_execution_immediate=>true
,p_bind_event_type=>'keyup'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(6613349178701452)
,p_event_id=>wwv_flow_imp.id(6612853550701452)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_name=>'Set item value'
,p_static_id=>'set-item-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_DEBOUNCE_IMMEDIATE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.value',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(6610966278701454)
,p_name=>'Update P21_IMMEDIATE'
,p_static_id=>'update-p21-immediate'
,p_event_sequence=>10
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_TEXT_AREA'
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'keyup'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(6611517695701453)
,p_event_id=>wwv_flow_imp.id(6610966278701454)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_name=>'Set item value'
,p_static_id=>'set-item-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_IMMEDIATE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.value',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(6614656096701452)
,p_name=>'Update P21_THROTTLE_DELAY'
,p_static_id=>'update-p21-throttle-delay'
,p_event_sequence=>50
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_TEXT_AREA'
,p_bind_type=>'bind'
,p_execution_type=>'THROTTLE'
,p_execution_time=>2000
,p_execution_immediate=>false
,p_bind_event_type=>'keyup'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(6615077888701452)
,p_event_id=>wwv_flow_imp.id(6614656096701452)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_name=>'Set item value'
,p_static_id=>'set-item-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_THROTTLE_DELAY'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.value',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(6613745617701452)
,p_name=>'Update P21_THROTTLE_IMMEDIATE'
,p_static_id=>'update-p21-throttle-immediate'
,p_event_sequence=>40
,p_triggering_element_type=>'ITEM'
,p_triggering_element=>'P21_TEXT_AREA'
,p_bind_type=>'bind'
,p_execution_type=>'THROTTLE'
,p_execution_time=>2000
,p_execution_immediate=>true
,p_bind_event_type=>'keyup'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(6614254057701452)
,p_event_id=>wwv_flow_imp.id(6613745617701452)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_name=>'Set item value'
,p_static_id=>'set-item-value'
,p_action=>'NATIVE_SET_VALUE'
,p_affected_elements_type=>'ITEM'
,p_affected_elements=>'P21_THROTTLE_IMMEDIATE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'js_expression', 'this.triggeringElement.value',
  'suppress_change_event', 'N',
  'type', 'JAVASCRIPT_EXPRESSION')).to_clob
,p_wait_for_result=>'Y'
);
wwv_flow_imp.component_end;
end;
/
