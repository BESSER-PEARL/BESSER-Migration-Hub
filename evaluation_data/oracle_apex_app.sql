--
-- APEX APPLICATION
-- Import via App Builder → Import → Application.
-- Tables are created by the Supporting Objects install script
-- embedded at the end of this file.
--

prompt --application/set_environment
set define off verify off feedback off
whenever sqlerror exit sql.sqlcode rollback
begin
wwv_flow_imp.import_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>nvl(wwv_flow_application_install.get_application_id,6785)
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);
wwv_flow.g_import_in_progress := true;
wwv_flow.g_flow_id := nvl(wwv_flow_application_install.get_application_id,6785);
end;
/


prompt --application/create_application
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_imp_workspace.create_flow(
 p_id=>wwv_flow.g_flow_id
,p_owner=>USER
,p_name=>nvl(wwv_flow_application_install.get_application_name,'TaskTracker')
,p_alias=>'TASKTRACKER'
,p_application_tab_set=>0
,p_logo_type=>'T'
,p_logo_text=>'TaskTracker'
,p_public_user=>'APEX_PUBLIC_USER'
,p_authentication_id=>wwv_flow_imp.id(1001000)
,p_flow_status=>'AVAILABLE_W_EDIT_LINK'
,p_compatibility_mode=>'19.2'
,p_theme_id=>42
,p_home_url=>'f?p=&APP_ID.:1:&SESSION.'
,p_theme_style_by_user_pref=>false
,p_navigation_list_id=>wwv_flow_imp.id(1002000)
,p_navigation_list_position=>'SIDE'
,p_nav_bar_type=>'LIST'
,p_nav_bar_list_id=>wwv_flow_imp.id(1003000)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/shared_components/user_interface/theme_style
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_theme_style(
 p_id=>wwv_flow_imp.id(1004000)
,p_theme_id=>42
,p_name=>'Vita'
,p_static_id=>'VITA'
,p_css_file_urls=>'#THEME_FILES#css/Vita#MIN#.css?v=#APEX_VERSION#'
,p_is_current=>true
,p_is_public=>true
,p_is_accessible=>false
);
wwv_flow_imp.component_end;
end;
/


prompt --application/shared_components/user_interface/theme
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_theme(
 p_id=>wwv_flow_imp.id(1005000)
,p_theme_id=>42
,p_static_id=>'universal-theme'
,p_theme_name=>'Universal Theme'
,p_theme_internal_name=>'UNIVERSAL_THEME'
,p_version_identifier=>'26.1'
,p_navigation_type=>'L'
,p_nav_bar_type=>'LIST'
,p_is_locked=>false
,p_current_theme_style_id=>wwv_flow_imp.id(1004000)
,p_default_page_template=>4073832297226169690
,p_default_dialog_template=>2101883943284197310
,p_error_template=>2102634289808461002
,p_printer_friendly_template=>4073832297226169690
,p_login_template=>2102634289808461002
,p_default_button_template=>4073839297780169708
,p_default_region_template=>4073835273271169698
,p_default_chart_template=>4073835273271169698
,p_default_form_template=>4073835273271169698
,p_default_reportr_template=>4073835273271169698
,p_default_wizard_template=>4073835273271169698
,p_default_menur_template=>2532939663579242476
,p_default_listr_template=>4073835273271169698
,p_default_irr_template=>2102002977963900996
,p_default_report_template=>2540130677583398057
,p_default_label_template=>1610598304472262251
,p_default_menu_template=>4073839682315169711
,p_default_list_template=>4073837480889169704
,p_default_top_nav_list_temp=>2528231041045349458
,p_default_side_nav_list_temp=>2469215554099805162
,p_default_nav_list_position=>'SIDE'
,p_default_dialogbtnr_template=>2127905476394690047
,p_default_dialogr_template=>4502917002193490937
,p_default_option_label=>1610598304472262251
,p_default_required_label=>1610598484065263269
,p_default_navbar_list_template=>2849019392706229583
,p_file_prefix=>nvl(wwv_flow_application_install.get_static_theme_file_prefix(42),'#APEX_FILES#themes/theme_42/26.1/')
,p_files_version=>64
,p_icon_library=>'FONTAPEX'
,p_javascript_file_urls=>wwv_flow_string.join(wwv_flow_t_varchar2(
'#APEX_FILES#libraries/apex/#MIN_DIRECTORY#widget.stickyWidget#MIN#.js?v=#APEX_VERSION#',
'#THEME_FILES#js/theme42#MIN#.js?v=#APEX_VERSION#'))
,p_css_file_urls=>'#THEME_FILES#css/Core#MIN#.css?v=#APEX_VERSION#'
,p_reference_id=>wwv_imp_util.get_subscription_id(4073840274158169736,2000,'universal-theme',8842.261)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/shared_components/security/authentications/apex_accounts
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_authentication(
 p_id=>wwv_flow_imp.id(1001000)
,p_name=>'Application Express Accounts'
,p_static_id=>'apex-accounts'
,p_scheme_type=>'NATIVE_APEX_ACCOUNTS'
,p_invalid_session_type=>'LOGIN'
,p_logout_url=>'f?p=&APP_ID.:1:&SESSION.'
,p_use_secure_cookie_yn=>'N'
,p_ras_mode=>0
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00101
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>101
,p_name=>'Login'
,p_alias=>'LOGIN'
,p_step_title=>'Sign In'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>2102634289808461002
,p_page_template_options=>'#DEFAULT#'
,p_page_is_public_y_n=>'Y'
,p_protection_level=>'C'
,p_page_component_map=>'16'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1006000)
,p_plug_name=>'TaskTracker'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2675634334296186762
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1007000)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1006000)
,p_button_name=>'LOGIN'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Sign In'
,p_button_position=>'NEXT'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1008000)
,p_name=>'P101_USERNAME'
,p_is_required=>true
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1006000)
,p_prompt=>'Username'
,p_placeholder=>'username'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>100
,p_field_template=>2042262243893469891
,p_item_template_options=>'#DEFAULT#'
,p_restricted_characters=>'WEB_SAFE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1009000)
,p_name=>'P101_PASSWORD'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1006000)
,p_prompt=>'Password'
,p_placeholder=>'password'
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_PASSWORD'
,p_cSize=>64
,p_cMaxlength=>100
,p_field_template=>2042262243893469891
,p_item_template_options=>'#DEFAULT#'
,p_is_persistent=>'N'
,p_restricted_characters=>'WEB_SAFE'
,p_encrypt_session_state_yn=>'N'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'submit_when_enter_pressed', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1010000)
,p_process_sequence=>10
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Get Username Cookie'
,p_process_sql_clob=>':P101_USERNAME := apex_authentication.get_login_username_cookie;'
,p_process_clob_language=>'PLSQL'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1011000)
,p_process_sequence=>10
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Set Username Cookie'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
  'apex_authentication.send_login_username_cookie (',
  '    p_username => lower(:P101_USERNAME) );'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1012000)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Login'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
  'apex_authentication.login(',
  '    p_username => :P101_USERNAME,',
  '    p_password => :P101_PASSWORD );'))
,p_process_clob_language=>'PLSQL'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1013000)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'Clear Page(s) Cache'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/shared_components/navigation/lists/navigation_menu
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_list(
 p_id=>wwv_flow_imp.id(1002000)
,p_name=>'Navigation Menu'
,p_static_id=>'navigation-menu'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1014000)
,p_list_item_display_sequence=>10
,p_list_item_link_text=>'Home'
,p_list_item_link_target=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-home'
,p_list_item_current_type=>'TARGET_PAGE'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1015000)
,p_list_item_display_sequence=>30
,p_list_item_link_text=>'Task'
,p_list_item_link_target=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'4,5'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1016000)
,p_list_item_display_sequence=>40
,p_list_item_link_text=>'Team'
,p_list_item_link_target=>'f?p=&APP_ID.:6:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'6'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/shared_components/navigation/lists/navigation_bar
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_list(
 p_id=>wwv_flow_imp.id(1003000)
,p_name=>'Navigation Bar'
,p_static_id=>'navigation-bar'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1017000)
,p_list_item_display_sequence=>10
,p_list_item_link_text=>'Log Out'
,p_list_item_link_target=>'f?p=&APP_ID.:9999:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-sign-out'
,p_list_item_current_type=>'NEVER'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00000
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>0
,p_name=>'Global Page'
,p_step_title=>'Global Page'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'D'
,p_page_component_map=>'08'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00001
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>1
,p_name=>'TaskTracker'
,p_step_title=>'TaskTracker'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'08'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1018000)
,p_plug_name=>'Entities'
,p_region_template_options=>'#DEFAULT#'
,p_plug_display_sequence=>10
,p_location=>null
,p_plug_source=>'<ul>
<li><a href="f?p=&APP_ID.:4:&SESSION.">Task</a></li>
<li><a href="f?p=&APP_ID.:6:&SESSION.">Team</a></li>
</ul>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00004
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>4
,p_name=>'Tasks'
,p_step_title=>'Tasks'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'18'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1019000)
,p_plug_name=>'Tasks'
,p_region_template_options=>'#DEFAULT#'
,p_plug_display_sequence=>10
,p_query_type=>'TABLE'
,p_query_table=>'TASK'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_IR'
,p_prn_page_header=>'Tasks'
);
wwv_flow_imp_page.create_worksheet(
 p_name=>'Tasks'
,p_max_row_count_message=>'The maximum row count for this report is #MAX_ROW_COUNT# rows.'
,p_no_data_found_message=>'No data found.'
,p_base_pk1=>'ID'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_report_list_mode=>'TABS'
,p_lazy_loading=>false
,p_show_detail_link=>'C'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:XLSX:PDF'
,p_enable_mail_download=>'Y'
,p_detail_link=>'f?p=&APP_ID.:5:&APP_SESSION.::&DEBUG.:RP:P5_ID:#ID#'
,p_detail_link_text=>'<span aria-label="Edit"><span class="fa fa-edit" aria-hidden="true"></span></span>'
,p_owner=>USER
,p_internal_uid=>1020000
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'ID'
,p_display_order=>1
,p_is_primary_key=>'Y'
,p_column_identifier=>'A'
,p_column_label=>'Id'
,p_column_type=>'NUMBER'
,p_display_text_as=>'HIDDEN_ESCAPE_SC'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'DESCRIPTION'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'Description'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'DUE_DATE'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'Duedate'
,p_column_type=>'DATE'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'PRIORITY'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'Priority'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'STATUS'
,p_display_order=>5
,p_column_identifier=>'E'
,p_column_label=>'Status'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_db_column_name=>'TITLE'
,p_display_order=>6
,p_column_identifier=>'F'
,p_column_label=>'Title'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'DEFAULT'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'DESCRIPTION:DUE_DATE:PRIORITY:STATUS:TITLE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1021000)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1019000)
,p_button_name=>'CREATE'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create'
,p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'
,p_button_redirect_url=>'f?p=&APP_ID.:5:&APP_SESSION.::&DEBUG.:5::'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(1022000)
,p_name=>'Refresh Report After Dialog'
,p_event_sequence=>10
,p_triggering_element_type=>'REGION'
,p_triggering_region_id=>wwv_flow_imp.id(1019000)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'apexafterclosedialog'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(1023000)
,p_event_id=>wwv_flow_imp.id(1022000)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_action=>'NATIVE_REFRESH'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(1019000)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00005
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>5
,p_name=>'Manage Task'
,p_step_title=>'Manage Task'
,p_page_mode=>'MODAL'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>'var htmldb_delete_message = ''"DELETE_CONFIRM_MSG"'';'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1024000)
,p_plug_name=>'Task'
,p_region_template_options=>'#DEFAULT#'
,p_plug_display_sequence=>10
,p_query_type=>'TABLE'
,p_query_table=>'TASK'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_FORM'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1025000)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1024000)
,p_button_name=>'CANCEL'
,p_button_action=>'DEFINED_BY_DA'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'CLOSE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1026000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1024000)
,p_button_name=>'DELETE'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete'
,p_button_position=>'DELETE'
,p_button_condition=>'P5_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1027000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1024000)
,p_button_name=>'SAVE'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--hot'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'CHANGE'
,p_button_condition=>'P5_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1028000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1024000)
,p_button_name=>'CREATE'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#:t-Button--hot'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Create'
,p_button_position=>'CREATE'
,p_button_condition=>'P5_ID'
,p_button_condition_type=>'ITEM_IS_NULL'
,p_database_action=>'INSERT'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1029000)
,p_name=>'P5_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_source=>'ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2('value_protected','Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1034000)
,p_name=>'P5_DESCRIPTION'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Description'
,p_source=>'DESCRIPTION'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled','N',
  'submit_when_enter_pressed','N',
  'subtype','TEXT',
  'trim_spaces','NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1035000)
,p_name=>'P5_DUE_DATE'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Duedate'
,p_source=>'DUE_DATE'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled','N',
  'submit_when_enter_pressed','N',
  'subtype','TEXT',
  'trim_spaces','NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1036000)
,p_name=>'P5_PRIORITY'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Priority'
,p_source=>'PRIORITY'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled','N',
  'submit_when_enter_pressed','N',
  'subtype','TEXT',
  'trim_spaces','NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1037000)
,p_name=>'P5_STATUS'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Status'
,p_source=>'STATUS'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled','N',
  'submit_when_enter_pressed','N',
  'subtype','TEXT',
  'trim_spaces','NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1038000)
,p_name=>'P5_TITLE'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1024000)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Title'
,p_source=>'TITLE'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled','N',
  'submit_when_enter_pressed','N',
  'subtype','TEXT',
  'trim_spaces','NONE')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1030000)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from Task'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'ID',
  'primary_key_item', 'P5_ID',
  'table_name', 'TASK')).to_clob
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1031000)
,p_process_sequence=>20
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of Task'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'ID',
  'primary_key_item', 'P5_ID',
  'return_key_into_item', 'P5_ID',
  'supported_operations', 'I:U:D',
  'table_name', 'TASK')).to_clob
,p_process_error_message=>'#SQLERRM#'
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when=>'CREATE,SAVE,DELETE'
,p_process_when_type=>'REQUEST_IN_CONDITION'
,p_process_success_message=>'Action Processed.'
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(1032000)
,p_name=>'Cancel Dialog'
,p_event_sequence=>10
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(1025000)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(1033000)
,p_event_id=>wwv_flow_imp.id(1032000)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_action=>'NATIVE_DIALOG_CANCEL'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/deployment/definition
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE FILEUPLOAD CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE APP_COMMENT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE TASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE PAGEHELPER CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE COMMENTHELPER CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1039000)
,p_deinstall_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)
,p_required_free_kb=>100
);
wwv_flow_imp.component_end;
end;
/


prompt --application/deployment/installscripts/create_tables
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>6785
,p_default_id_offset=>35853793830688242
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE FILEUPLOAD CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE APP_COMMENT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE TASK CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE PAGEHELPER CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE COMMENTHELPER CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE COMMENTHELPER ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CONTENT VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE PAGEHELPER ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    ASSIGNED_TASKS NUMBER NOT NULL,'||wwv_flow.LF||
'    TEAM_PROGRESS NUMBER NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE TASK ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    DESCRIPTION VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    DUE_DATE DATE NOT NULL,'||wwv_flow.LF||
'    PRIORITY VARCHAR2(20) NOT NULL,'||wwv_flow.LF||
'    STATUS VARCHAR2(20) NOT NULL,'||wwv_flow.LF||
'    TITLE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    CONSTRAINT chk_task_PRIORITY CHECK (PRIORITY IN (''High'', ''Low'', ''Medium'')),'||wwv_flow.LF||
'    CONSTRAINT chk_task_STATUS CHECK (STATUS IN (''Done'', ''Review'', ''Running'', ''To_Do''))'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE APP_COMMENT ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    CONTENT VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    task_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (task_id) REFERENCES Task(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE FILEUPLOAD ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    task_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (task_id) REFERENCES Task(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1040000)
,p_install_id=>wwv_flow_imp.id(1039000)
,p_name=>'create_tables'
,p_sequence=>10
,p_script_type=>'INSTALL'
,p_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/end_environment
begin
wwv_flow_imp.import_end(
  p_auto_install_sup_obj => nvl(
    wwv_flow_application_install.get_auto_install_sup_obj, false));
commit;
end;
/
set verify on feedback on define on
prompt  ...done
