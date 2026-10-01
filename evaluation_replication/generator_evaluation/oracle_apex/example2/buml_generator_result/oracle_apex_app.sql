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
,p_default_application_id=>nvl(wwv_flow_application_install.get_application_id,8002)
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);
wwv_flow.g_import_in_progress := true;
wwv_flow.g_flow_id := nvl(wwv_flow_application_install.get_application_id,8002);
end;
/


prompt --application/create_application
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_imp_workspace.create_flow(
 p_id=>wwv_flow.g_flow_id
,p_owner=>USER
,p_name=>nvl(wwv_flow_application_install.get_application_name,'example2')
,p_alias=>'EXAMPLE2'
,p_application_tab_set=>0
,p_logo_type=>'T'
,p_logo_text=>'example2'
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_plug_name=>'example2'
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_list_item_display_sequence=>20
,p_list_item_link_text=>'Administration'
,p_list_item_link_target=>'f?p=&APP_ID.:2:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'2'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1016000)
,p_list_item_display_sequence=>30
,p_list_item_link_text=>'Application Theme Style Form'
,p_list_item_link_target=>'f?p=&APP_ID.:3:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'3'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1017000)
,p_list_item_display_sequence=>40
,p_list_item_link_text=>'Background Load Form'
,p_list_item_link_target=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'4'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1018000)
,p_list_item_display_sequence=>50
,p_list_item_link_text=>'CSV Load Form'
,p_list_item_link_target=>'f?p=&APP_ID.:5:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'5'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1019000)
,p_list_item_display_sequence=>60
,p_list_item_link_text=>'Data Load Results'
,p_list_item_link_target=>'f?p=&APP_ID.:6:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'6'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1020000)
,p_list_item_display_sequence=>70
,p_list_item_link_text=>'Data Load Source'
,p_list_item_link_target=>'f?p=&APP_ID.:7:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'7'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1021000)
,p_list_item_display_sequence=>80
,p_list_item_link_text=>'Data Loading'
,p_list_item_link_target=>'f?p=&APP_ID.:8:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'8'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1022000)
,p_list_item_display_sequence=>90
,p_list_item_link_text=>'Data Validation'
,p_list_item_link_target=>'f?p=&APP_ID.:9:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'9'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1023000)
,p_list_item_display_sequence=>100
,p_list_item_link_text=>'Eba demo load sales List'
,p_list_item_link_target=>'f?p=&APP_ID.:10:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'10'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1024000)
,p_list_item_display_sequence=>110
,p_list_item_link_text=>'Help'
,p_list_item_link_target=>'f?p=&APP_ID.:11:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'11'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1025000)
,p_list_item_display_sequence=>120
,p_list_item_link_text=>'Load Data using PL SQL API Form'
,p_list_item_link_target=>'f?p=&APP_ID.:12:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'12'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1026000)
,p_list_item_display_sequence=>130
,p_list_item_link_text=>'Manual Data Loading'
,p_list_item_link_target=>'f?p=&APP_ID.:13:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'13'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1027000)
,p_list_item_display_sequence=>140
,p_list_item_link_text=>'Multiple File Types Load Form'
,p_list_item_link_target=>'f?p=&APP_ID.:14:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'14'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1028000)
,p_list_item_display_sequence=>150
,p_list_item_link_text=>'PL SQL Parser Form'
,p_list_item_link_target=>'f?p=&APP_ID.:15:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'15'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1029000)
,p_list_item_display_sequence=>160
,p_list_item_link_text=>'Reset Data'
,p_list_item_link_target=>'f?p=&APP_ID.:16:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'16'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1030000)
,p_list_item_display_sequence=>170
,p_list_item_link_text=>'Transform and Lookup Form'
,p_list_item_link_target=>'f?p=&APP_ID.:17:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'17'
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_list(
 p_id=>wwv_flow_imp.id(1003000)
,p_name=>'Navigation Bar'
,p_static_id=>'navigation-bar'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1031000)
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>1
,p_name=>'example2'
,p_step_title=>'example2'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'08'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1032000)
,p_plug_name=>'Entities'
,p_region_template_options=>'#DEFAULT#'
,p_plug_display_sequence=>10
,p_location=>null
,p_plug_source=>'<ul>
<li><a href="f?p=&APP_ID.:2:&SESSION.">Administration</a></li>
<li><a href="f?p=&APP_ID.:3:&SESSION.">Application Theme Style Form</a></li>
<li><a href="f?p=&APP_ID.:4:&SESSION.">Background Load Form</a></li>
<li><a href="f?p=&APP_ID.:5:&SESSION.">CSV Load Form</a></li>
<li><a href="f?p=&APP_ID.:6:&SESSION.">Data Load Results</a></li>
<li><a href="f?p=&APP_ID.:7:&SESSION.">Data Load Source</a></li>
<li><a href="f?p=&APP_ID.:8:&SESSION.">Data Loading</a></li>
<li><a href="f?p=&APP_ID.:9:&SESSION.">Data Validation</a></li>
<li><a href="f?p=&APP_ID.:10:&SESSION.">Eba demo load sales List</a></li>
<li><a href="f?p=&APP_ID.:11:&SESSION.">Help</a></li>
<li><a href="f?p=&APP_ID.:12:&SESSION.">Load Data using PL SQL API Form</a></li>
<li><a href="f?p=&APP_ID.:13:&SESSION.">Manual Data Loading</a></li>
<li><a href="f?p=&APP_ID.:14:&SESSION.">Multiple File Types Load Form</a></li>
<li><a href="f?p=&APP_ID.:15:&SESSION.">PL SQL Parser Form</a></li>
<li><a href="f?p=&APP_ID.:16:&SESSION.">Reset Data</a></li>
<li><a href="f?p=&APP_ID.:17:&SESSION.">Transform and Lookup Form</a></li>
</ul>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00002
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>2
,p_name=>'Administration'
,p_step_title=>'Administration'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1033000)
,p_plug_name=>'Administration'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00003
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>3
,p_name=>'Application_Theme_Style_Form'
,p_step_title=>'Application_Theme_Style_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1034000)
,p_plug_name=>'Application_Theme_Style_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1035000)
,p_plug_name=>'Application Theme Style'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as DESKTOP_THEME_STYLE_ID from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1036000)
,p_name=>'P3_DESKTOP_THEME_STYLE_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1035000)
,p_prompt=>'Desktop Theme Style'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>true
,p_source=>'DESKTOP_THEME_STYLE_ID'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1037000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1035000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Apply Changes'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1038000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Application_Theme_Style_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1035000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1039000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1034000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>4
,p_name=>'Background_Load_Form'
,p_step_title=>'Background_Load_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1040000)
,p_plug_name=>'Background_Load_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1041000)
,p_plug_name=>'Background Load'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ERROR_ROWS, cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as FILE_NAME_2, cast(null as varchar2(4000)) as LOAD_EXEC_ID, cast(null as varchar2(4000)) as PROCESSED_ROWS from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1042000)
,p_name=>'P4_ERROR_ROWS'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1041000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ERROR_ROWS'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1043000)
,p_name=>'P4_FILE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1041000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1044000)
,p_name=>'P4_FILE_NAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1041000)
,p_prompt=>'Loaded File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'FILE_NAME_2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1045000)
,p_name=>'P4_LOAD_EXEC_ID'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1041000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'LOAD_EXEC_ID'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1046000)
,p_name=>'P4_PROCESSED_ROWS'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1041000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'PROCESSED_ROWS'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1047000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1041000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1048000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Background_Load_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1041000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1049000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1040000)
,p_button_name=>'CLEAR'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>5
,p_name=>'CSV_Load_Form'
,p_step_title=>'CSV_Load_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1050000)
,p_plug_name=>'CSV_Load_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1051000)
,p_plug_name=>'CSV Load'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as COPY_PASTE_ERROR_ROW_COUNT, cast(null as varchar2(4000)) as DATA, cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as FILE_ERROR_ROW_COUNT, cast(null as varchar2(4000)) as FILE_NAME_2, cast(null as varchar2(4000)) as PASTED_DATA from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1052000)
,p_name=>'P5_COPY_PASTE_ERROR_ROW_COUNT'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'COPY_PASTE_ERROR_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1053000)
,p_name=>'P5_DATA'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>'Copy and Paste Delimited Data'
,p_display_as=>'NATIVE_TEXTAREA'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATA'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1054000)
,p_name=>'P5_FILE'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1055000)
,p_name=>'P5_FILE_ERROR_ROW_COUNT'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_ERROR_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1056000)
,p_name=>'P5_FILE_NAME'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>'Loaded File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'FILE_NAME_2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1057000)
,p_name=>'P5_PASTED_DATA'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1051000)
,p_prompt=>'Pasted Data'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'PASTED_DATA'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1058000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1051000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1059000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize CSV_Load_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1051000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1060000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1050000)
,p_button_name=>'CLEAR_DATA'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1061000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1050000)
,p_button_name=>'CLEAR_FILE'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1062000)
,p_button_sequence=>50
,p_button_plug_id=>wwv_flow_imp.id(1050000)
,p_button_name=>'LOAD_FILE'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1063000)
,p_button_sequence=>60
,p_button_plug_id=>wwv_flow_imp.id(1050000)
,p_button_name=>'NEXT'
,p_button_image_alt=>'Next'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00006
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>6
,p_name=>'Data_Load_Results'
,p_step_title=>'Data_Load_Results'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1064000)
,p_plug_name=>'Data_Load_Results'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1065000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1064000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1066000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1064000)
,p_button_name=>'FINISH'
,p_button_image_alt=>'Finish'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00007
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>7
,p_name=>'Data_Load_Source'
,p_step_title=>'Data_Load_Source'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1067000)
,p_plug_name=>'Data_Load_Source'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1068000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1067000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1069000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1067000)
,p_button_name=>'NEXT'
,p_button_image_alt=>'Next'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00008
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>8
,p_name=>'Data_Loading'
,p_step_title=>'Data_Loading'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1070000)
,p_plug_name=>'Data_Loading'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00009
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>9
,p_name=>'Data_Validation'
,p_step_title=>'Data_Validation'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1071000)
,p_plug_name=>'Data_Validation'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1072000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1071000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1073000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1071000)
,p_button_name=>'NEXT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1074000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1071000)
,p_button_name=>'PREVIOUS'
,p_button_image_alt=>'Previous'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00010
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>10
,p_name=>'Eba_demo_load_sales_List'
,p_step_title=>'Eba_demo_load_sales_List'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1075000)
,p_plug_name=>'Eba_demo_load_sales_List'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1076000)
,p_plug_name=>'Eba_demo_load_sales_List_EbaDemoLoadSales'
,p_plug_display_sequence=>20
,p_query_type=>'TABLE'
,p_query_table=>'EBADEMOLOADSALES'
,p_include_rowid_column=>false
,p_plug_source_type=>'NATIVE_IR'
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(1077000)
,p_name=>'Eba_demo_load_sales_List'
,p_internal_uid=>1078000
,p_base_pk1=>'ID'
,p_show_detail_link=>'N'
,p_owner=>USER
,p_pagination_type=>'ROWS_X_TO_Y'
,p_report_list_mode=>'TABS'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1079000)
,p_db_column_name=>'ID'
,p_display_order=>1
,p_column_identifier=>'A'
,p_column_label=>'ID'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1080000)
,p_db_column_name=>'COUNTRY'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'COUNTRY'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1081000)
,p_db_column_name=>'CREATED'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'CREATED'
,p_column_type=>'DATE'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1082000)
,p_db_column_name=>'ITEM_TYPE'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'ITEM_TYPE'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1083000)
,p_db_column_name=>'LAST_UPDATED'
,p_display_order=>5
,p_column_identifier=>'E'
,p_column_label=>'LAST_UPDATED'
,p_column_type=>'DATE'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1084000)
,p_db_column_name=>'ORDER_DATE'
,p_display_order=>6
,p_column_identifier=>'F'
,p_column_label=>'ORDER_DATE'
,p_column_type=>'DATE'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1085000)
,p_db_column_name=>'ORDER_ID'
,p_display_order=>7
,p_column_identifier=>'G'
,p_column_label=>'ORDER_ID'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1086000)
,p_db_column_name=>'ORDER_PRIORITY'
,p_display_order=>8
,p_column_identifier=>'H'
,p_column_label=>'ORDER_PRIORITY'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1087000)
,p_db_column_name=>'REGION'
,p_display_order=>9
,p_column_identifier=>'I'
,p_column_label=>'REGION'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1088000)
,p_db_column_name=>'SALES_CHANNEL'
,p_display_order=>10
,p_column_identifier=>'J'
,p_column_label=>'SALES_CHANNEL'
,p_column_type=>'STRING'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1089000)
,p_db_column_name=>'SHIP_DATE'
,p_display_order=>11
,p_column_identifier=>'K'
,p_column_label=>'SHIP_DATE'
,p_column_type=>'DATE'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1090000)
,p_db_column_name=>'TOTAL_COST'
,p_display_order=>12
,p_column_identifier=>'L'
,p_column_label=>'TOTAL_COST'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1091000)
,p_db_column_name=>'TOTAL_PROFIT'
,p_display_order=>13
,p_column_identifier=>'M'
,p_column_label=>'TOTAL_PROFIT'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1092000)
,p_db_column_name=>'TOTAL_REVENUE'
,p_display_order=>14
,p_column_identifier=>'N'
,p_column_label=>'TOTAL_REVENUE'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1093000)
,p_db_column_name=>'UNITS_SOLD'
,p_display_order=>15
,p_column_identifier=>'O'
,p_column_label=>'UNITS_SOLD'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1094000)
,p_db_column_name=>'UNIT_COST'
,p_display_order=>16
,p_column_identifier=>'P'
,p_column_label=>'UNIT_COST'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1095000)
,p_db_column_name=>'UNIT_PRICE'
,p_display_order=>17
,p_column_identifier=>'Q'
,p_column_label=>'UNIT_PRICE'
,p_column_type=>'NUMBER'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(1096000)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'1076000'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'ID:COUNTRY:CREATED:ITEM_TYPE:LAST_UPDATED:ORDER_DATE:ORDER_ID:ORDER_PRIORITY:REGION:SALES_CHANNEL:SHIP_DATE:TOTAL_COST:TOTAL_PROFIT:TOTAL_REVENUE:UNITS_SOLD:UNIT_COST:UNIT_PRICE'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00011
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>11
,p_name=>'Help'
,p_step_title=>'Help'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1097000)
,p_plug_name=>'Help'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00012
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>12
,p_name=>'Load_Data_using_PL_SQL_API_Form'
,p_step_title=>'Load_Data_using_PL_SQL_API_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1098000)
,p_plug_name=>'Load_Data_using_PL_SQL_API_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1099000)
,p_plug_name=>'Load Data using PL/SQL API'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as DATA, cast(null as varchar2(4000)) as ROWS_FAILED, cast(null as varchar2(4000)) as ROWS_LOADED, cast(null as varchar2(4000)) as SAMPLE_DATA from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1100000)
,p_name=>'P12_DATA'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1099000)
,p_prompt=>'Copy and Paste Delimited Data'
,p_display_as=>'NATIVE_TEXTAREA'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATA'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1101000)
,p_name=>'P12_ROWS_FAILED'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1099000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ROWS_FAILED'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1102000)
,p_name=>'P12_ROWS_LOADED'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1099000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ROWS_LOADED'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1103000)
,p_name=>'P12_SAMPLE_DATA'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1099000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'SAMPLE_DATA'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1104000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1099000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1105000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Load_Data_using_PL_SQL_API_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1099000)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00013
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>13
,p_name=>'Manual_Data_Loading'
,p_step_title=>'Manual_Data_Loading'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1106000)
,p_plug_name=>'Manual_Data_Loading'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00014
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>14
,p_name=>'Multiple_File_Types_Load_Form'
,p_step_title=>'Multiple_File_Types_Load_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1107000)
,p_plug_name=>'Multiple_File_Types_Load_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1108000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1107000)
,p_button_name=>'CLEAR'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1109000)
,p_plug_name=>'Multiple File Types Load'
,p_plug_display_sequence=>30
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ERROR_ROW_COUNT, cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as FILE_NAME_2, cast(null as varchar2(4000)) as FILE_TYPE, cast(null as varchar2(4000)) as PROCESSED_ROW_COUNT, cast(null as varchar2(4000)) as XLSX_WORKSHEET from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1110000)
,p_name=>'P14_ERROR_ROW_COUNT'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ERROR_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1111000)
,p_name=>'P14_FILE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1112000)
,p_name=>'P14_FILE_NAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>'Loaded File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'FILE_NAME_2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1113000)
,p_name=>'P14_FILE_TYPE'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_TYPE'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1114000)
,p_name=>'P14_PROCESSED_ROW_COUNT'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'PROCESSED_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1115000)
,p_name=>'P14_XLSX_WORKSHEET'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1109000)
,p_prompt=>'XLSX Worksheet'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'XLSX_WORKSHEET'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1116000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1109000)
,p_button_name=>'FORM_2_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1117000)
,p_process_sequence=>30
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Multiple_File_Types_Load_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1109000)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00015
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>15
,p_name=>'PL_SQL_Parser_Form'
,p_step_title=>'PL_SQL_Parser_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1118000)
,p_plug_name=>'PL_SQL_Parser_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1119000)
,p_plug_name=>'PL/SQL Parser'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as XLSX_WORKSHEET from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1120000)
,p_name=>'P15_FILE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1119000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1121000)
,p_name=>'P15_XLSX_WORKSHEET'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1119000)
,p_prompt=>'XLSX Worksheet'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'XLSX_WORKSHEET'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1122000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1119000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Upload File'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1123000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize PL_SQL_Parser_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1119000)
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00016
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>16
,p_name=>'Reset_Data'
,p_step_title=>'Reset_Data'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1124000)
,p_plug_name=>'Reset_Data'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1125000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1124000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1126000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1124000)
,p_button_name=>'RESET_DATA'
,p_button_image_alt=>'Reset Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
);
wwv_flow_imp.component_end;
end;
/


prompt --application/pages/page_00017
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>17
,p_name=>'Transform_and_Lookup_Form'
,p_step_title=>'Transform_and_Lookup_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1127000)
,p_plug_name=>'Transform_and_Lookup_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1128000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1127000)
,p_button_name=>'CLEAR'
,p_button_image_alt=>'Clear'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1129000)
,p_plug_name=>'Transform and Lookup'
,p_plug_display_sequence=>30
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ERROR_ROW_COUNT, cast(null as varchar2(4000)) as FILE_NAME, cast(null as varchar2(4000)) as FILE_NAME_2 from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1130000)
,p_name=>'P17_ERROR_ROW_COUNT'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ERROR_ROW_COUNT'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1131000)
,p_name=>'P17_FILE'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>'Upload a File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'FILE_NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1132000)
,p_name=>'P17_FILE_NAME'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1129000)
,p_prompt=>'Loaded File'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'FILE_NAME_2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1133000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1129000)
,p_button_name=>'FORM_2_SUBMIT'
,p_button_image_alt=>'Load Data'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1134000)
,p_process_sequence=>30
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Transform_and_Lookup_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1129000)
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADSALES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1135000)
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
,p_default_application_id=>8002
,p_default_id_offset=>80671573584977288
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADSALES CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOLOADDEPT CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADDEPT ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    DNAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LOC VARCHAR2(100) NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADSALES ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COUNTRY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    CREATED DATE NOT NULL,'||wwv_flow.LF||
'    ITEM_TYPE VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LAST_UPDATED DATE NOT NULL,'||wwv_flow.LF||
'    ORDER_DATE DATE NOT NULL,'||wwv_flow.LF||
'    ORDER_ID NUMBER NOT NULL,'||wwv_flow.LF||
'    ORDER_PRIORITY VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    REGION VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SALES_CHANNEL VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    SHIP_DATE DATE NOT NULL,'||wwv_flow.LF||
'    TOTAL_COST NUMBER NOT NULL,'||wwv_flow.LF||
'    TOTAL_PROFIT NUMBER NOT NULL,'||wwv_flow.LF||
'    TOTAL_REVENUE NUMBER NOT NULL,'||wwv_flow.LF||
'    UNIT_COST NUMBER NOT NULL,'||wwv_flow.LF||
'    UNIT_PRICE NUMBER NOT NULL,'||wwv_flow.LF||
'    UNITS_SOLD NUMBER NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOLOADEMP ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMM NUMBER NOT NULL,'||wwv_flow.LF||
'    CREATED DATE NOT NULL,'||wwv_flow.LF||
'    EMPNO NUMBER NOT NULL,'||wwv_flow.LF||
'    ENAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIREDATE DATE NOT NULL,'||wwv_flow.LF||
'    JOB VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    LAST_UPDATED DATE NOT NULL,'||wwv_flow.LF||
'    SAL NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademoloaddept_id NUMBER NOT NULL,'||wwv_flow.LF||
'    ebademoloademp_mgr_id NUMBER NOT NULL,'||wwv_flow.LF||
'    FOREIGN KEY (ebademoloaddept_id) REFERENCES EbaDemoLoadDept(id),'||wwv_flow.LF||
'    FOREIGN KEY (ebademoloademp_mgr_id) REFERENCES EbaDemoLoadEmp(id)'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1136000)
,p_install_id=>wwv_flow_imp.id(1135000)
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
