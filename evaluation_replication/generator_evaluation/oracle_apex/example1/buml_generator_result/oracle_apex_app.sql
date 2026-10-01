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
,p_default_application_id=>nvl(wwv_flow_application_install.get_application_id,8001)
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);
wwv_flow.g_import_in_progress := true;
wwv_flow.g_flow_id := nvl(wwv_flow_application_install.get_application_id,8001);
end;
/


prompt --application/create_application
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_imp_workspace.create_flow(
 p_id=>wwv_flow.g_flow_id
,p_owner=>USER
,p_name=>nvl(wwv_flow_application_install.get_application_name,'example1')
,p_alias=>'EXAMPLE1'
,p_application_tab_set=>0
,p_logo_type=>'T'
,p_logo_text=>'example1'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_plug_name=>'example1'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_list_item_link_text=>'Add Edit Collection Member Form'
,p_list_item_link_target=>'f?p=&APP_ID.:2:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'2'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1016000)
,p_list_item_display_sequence=>30
,p_list_item_link_text=>'Administration'
,p_list_item_link_target=>'f?p=&APP_ID.:3:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'3'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1017000)
,p_list_item_display_sequence=>40
,p_list_item_link_text=>'Application Theme Style Form'
,p_list_item_link_target=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'4'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1018000)
,p_list_item_display_sequence=>50
,p_list_item_link_text=>'Create Collection Form'
,p_list_item_link_target=>'f?p=&APP_ID.:5:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'5'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1019000)
,p_list_item_display_sequence=>60
,p_list_item_link_text=>'Data Synchronization'
,p_list_item_link_target=>'f?p=&APP_ID.:6:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'6'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1020000)
,p_list_item_display_sequence=>70
,p_list_item_link_text=>'Help'
,p_list_item_link_target=>'f?p=&APP_ID.:7:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'7'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1021000)
,p_list_item_display_sequence=>80
,p_list_item_link_text=>'Login Page Form'
,p_list_item_link_target=>'f?p=&APP_ID.:8:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'8'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1022000)
,p_list_item_display_sequence=>90
,p_list_item_link_text=>'Modify Collection Form'
,p_list_item_link_target=>'f?p=&APP_ID.:9:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'9'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1023000)
,p_list_item_display_sequence=>100
,p_list_item_link_text=>'Modify Collection Member Form'
,p_list_item_link_target=>'f?p=&APP_ID.:10:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'10'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1024000)
,p_list_item_display_sequence=>110
,p_list_item_link_text=>'Remove Collections'
,p_list_item_link_target=>'f?p=&APP_ID.:11:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'11'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1025000)
,p_list_item_display_sequence=>120
,p_list_item_link_text=>'Reset Data'
,p_list_item_link_target=>'f?p=&APP_ID.:12:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'12'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1026000)
,p_list_item_display_sequence=>130
,p_list_item_link_text=>'Sample Collections   API Examples'
,p_list_item_link_target=>'f?p=&APP_ID.:13:&SESSION.::&DEBUG.::::'
,p_list_item_icon=>'fa-table'
,p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'
,p_list_item_current_for_pages=>'13'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_shared.create_list(
 p_id=>wwv_flow_imp.id(1003000)
,p_name=>'Navigation Bar'
,p_static_id=>'navigation-bar'
);
wwv_flow_imp_shared.create_list_item(
 p_id=>wwv_flow_imp.id(1027000)
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>1
,p_name=>'example1'
,p_step_title=>'example1'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_page_component_map=>'08'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1028000)
,p_plug_name=>'Entities'
,p_region_template_options=>'#DEFAULT#'
,p_plug_display_sequence=>10
,p_location=>null
,p_plug_source=>'<ul>
<li><a href="f?p=&APP_ID.:2:&SESSION.">Add Edit Collection Member Form</a></li>
<li><a href="f?p=&APP_ID.:3:&SESSION.">Administration</a></li>
<li><a href="f?p=&APP_ID.:4:&SESSION.">Application Theme Style Form</a></li>
<li><a href="f?p=&APP_ID.:5:&SESSION.">Create Collection Form</a></li>
<li><a href="f?p=&APP_ID.:6:&SESSION.">Data Synchronization</a></li>
<li><a href="f?p=&APP_ID.:7:&SESSION.">Help</a></li>
<li><a href="f?p=&APP_ID.:8:&SESSION.">Login Page Form</a></li>
<li><a href="f?p=&APP_ID.:9:&SESSION.">Modify Collection Form</a></li>
<li><a href="f?p=&APP_ID.:10:&SESSION.">Modify Collection Member Form</a></li>
<li><a href="f?p=&APP_ID.:11:&SESSION.">Remove Collections</a></li>
<li><a href="f?p=&APP_ID.:12:&SESSION.">Reset Data</a></li>
<li><a href="f?p=&APP_ID.:13:&SESSION.">Sample Collections   API Examples</a></li>
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>2
,p_name=>'Add_Edit_Collection_Member_Form'
,p_step_title=>'Add_Edit_Collection_Member_Form'
,p_page_mode=>'MODAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1029000)
,p_plug_name=>'Add_Edit_Collection_Member_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1030000)
,p_plug_name=>'Add/Edit Collection Member'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as number) as COMM, cast(null as varchar2(4000)) as DEPTNO, cast(null as number) as EMPNO, cast(null as varchar2(4000)) as ENAME, cast(null as date) as HIREDATE, cast(null as varchar2(4000)) as JOB, cast(null as varchar2(4000)) as MGR, cast(null as number) as SAL, cast(null as varchar2(4000)) as SEQ, cast(null as varchar2(4000)) as STATUS, cast(null as varchar2(4000)) as XMLTYPE from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1031000)
,p_name=>'P2_COMM'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Commission'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'COMM'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1032000)
,p_name=>'P2_DEPTNO'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Dept&nbsp;No'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DEPTNO'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1033000)
,p_name=>'P2_EMPNO'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Emp&nbsp;No'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'EMPNO'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1034000)
,p_name=>'P2_ENAME'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Employee&nbsp;Name'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ENAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1035000)
,p_name=>'P2_HIREDATE'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Hire&nbsp;Date'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'HIREDATE'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1036000)
,p_name=>'P2_JOB'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Job'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'JOB'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1037000)
,p_name=>'P2_MGR'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Manager'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'MGR'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1038000)
,p_name=>'P2_SAL'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Salary'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'SAL'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1039000)
,p_name=>'P2_SEQ'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>''
,p_display_as=>'NATIVE_HIDDEN'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'SEQ'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1040000)
,p_name=>'P2_STATUS'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'Status'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'STATUS'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1041000)
,p_name=>'P2_XMLTYPE'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(1030000)
,p_prompt=>'XMLType'
,p_display_as=>'NATIVE_TEXTAREA'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'XMLTYPE'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1042000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1030000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Add Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1043000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Add_Edit_Collection_Member_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1030000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1044000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1029000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1045000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1029000)
,p_button_name=>'DELETE_MEMBER'
,p_button_image_alt=>'Delete Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1046000)
,p_button_sequence=>50
,p_button_plug_id=>wwv_flow_imp.id(1029000)
,p_button_name=>'UPDATE_MEMBER'
,p_button_image_alt=>'Update Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>3
,p_name=>'Administration'
,p_step_title=>'Administration'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1047000)
,p_plug_name=>'Administration'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>4
,p_name=>'Application_Theme_Style_Form'
,p_step_title=>'Application_Theme_Style_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1048000)
,p_plug_name=>'Application_Theme_Style_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1049000)
,p_plug_name=>'Application Theme Style'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as DESKTOP_THEME_STYLE_ID from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1050000)
,p_name=>'P4_DESKTOP_THEME_STYLE_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1049000)
,p_prompt=>'Desktop Theme Style'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>true
,p_source=>'DESKTOP_THEME_STYLE_ID'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1051000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1049000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Apply Changes'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1052000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Application_Theme_Style_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1049000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1053000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1048000)
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


prompt --application/pages/page_00005
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>5
,p_name=>'Create_Collection_Form'
,p_step_title=>'Create_Collection_Form'
,p_page_mode=>'MODAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1054000)
,p_plug_name=>'Create_Collection_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1055000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1054000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1056000)
,p_plug_name=>'Create Collection'
,p_plug_display_sequence=>30
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as NAME from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1057000)
,p_name=>'P5_NAME'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1056000)
,p_prompt=>'Collection Name'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>true
,p_source=>'NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1058000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1056000)
,p_button_name=>'FORM_2_SUBMIT'
,p_button_image_alt=>'Create Collection'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1059000)
,p_process_sequence=>30
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Create_Collection_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1056000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1060000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1054000)
,p_button_name=>'CREATE_REPLACE'
,p_button_image_alt=>'Create/Replace Collection'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>6
,p_name=>'Data_Synchronization'
,p_step_title=>'Data_Synchronization'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1061000)
,p_plug_name=>'Data_Synchronization'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1062000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1061000)
,p_button_name=>'ADD_MEMBER'
,p_button_image_alt=>'Add Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1063000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1061000)
,p_button_name=>'APPLY_COLLECTION'
,p_button_image_alt=>'Apply Collection'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1064000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1061000)
,p_button_name=>'POPULATE'
,p_button_image_alt=>'Populate Collection from EBA_DEMO_CS_EMP '
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>7
,p_name=>'Help'
,p_step_title=>'Help'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1065000)
,p_plug_name=>'Help'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>8
,p_name=>'Login_Page_Form'
,p_step_title=>'Login_Page_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1066000)
,p_plug_name=>'Login_Page_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1067000)
,p_plug_name=>'Login Page'
,p_plug_display_sequence=>20
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as PASSWORD, cast(null as varchar2(4000)) as USERNAME from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1068000)
,p_name=>'P8_PASSWORD'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1067000)
,p_prompt=>'Password'
,p_display_as=>'NATIVE_PASSWORD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>true
,p_placeholder=>'password'
,p_source=>'PASSWORD'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1069000)
,p_name=>'P8_USERNAME'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1067000)
,p_prompt=>'Username'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>true
,p_placeholder=>'username'
,p_source=>'USERNAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1070000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1067000)
,p_button_name=>'FORM_1_SUBMIT'
,p_button_image_alt=>'Sign In'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1071000)
,p_process_sequence=>20
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Login_Page_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1067000)
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>9
,p_name=>'Modify_Collection_Form'
,p_step_title=>'Modify_Collection_Form'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1072000)
,p_plug_name=>'Modify_Collection_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1073000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1072000)
,p_button_name=>'ADD_MEMBER_ADD_ANOTHER'
,p_button_image_alt=>'Add Member & Add Another'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1074000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1072000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1075000)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(1072000)
,p_button_name=>'DELETE_COLLECTION'
,p_button_image_alt=>'Delete Collection'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1076000)
,p_plug_name=>'Modify Collection'
,p_plug_display_sequence=>50
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ATTR1, cast(null as varchar2(4000)) as ATTR2, cast(null as varchar2(4000)) as ATTR3, cast(null as varchar2(4000)) as ATTR4, cast(null as varchar2(4000)) as ATTR5, cast(null as date) as DATE_ATTR1, cast(null as date) as DATE_ATTR2, cast(null as date) as DATE_ATTR3, cast(null as varchar2(4000)) as NAME, cast(null as number) as NUM_ATTR1, cast(null as number) as NUM_ATTR2, cast(null as number) as NUM_ATTR3 from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1077000)
,p_name=>'P9_ATTR1'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Character Attribute 1'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1078000)
,p_name=>'P9_ATTR2'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Character Attribute 2'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1079000)
,p_name=>'P9_ATTR3'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Character Attribute 3'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1080000)
,p_name=>'P9_ATTR4'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Character Attribute 4'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR4'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1081000)
,p_name=>'P9_ATTR5'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Character Attribute 5'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR5'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1082000)
,p_name=>'P9_DATE_ATTR1'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Date Attribute 1'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1083000)
,p_name=>'P9_DATE_ATTR2'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Date Attribute 2'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1084000)
,p_name=>'P9_DATE_ATTR3'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Date Attribute 3'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1085000)
,p_name=>'P9_NAME'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Collection Name'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1086000)
,p_name=>'P9_NUM_ATTR1'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Numeric Attribute 1'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1087000)
,p_name=>'P9_NUM_ATTR2'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Numeric Attribute 2'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1088000)
,p_name=>'P9_NUM_ATTR3'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(1076000)
,p_prompt=>'Numeric Attribute 3'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1089000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1076000)
,p_button_name=>'FORM_4_SUBMIT'
,p_button_image_alt=>'Add Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1090000)
,p_process_sequence=>50
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Modify_Collection_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1076000)
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1091000)
,p_button_sequence=>60
,p_button_plug_id=>wwv_flow_imp.id(1072000)
,p_button_name=>'RESEQUENCE'
,p_button_image_alt=>'Resequence'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1092000)
,p_button_sequence=>70
,p_button_plug_id=>wwv_flow_imp.id(1072000)
,p_button_name=>'TRUNCATE_COLLECTION'
,p_button_image_alt=>'Truncate Collection'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>10
,p_name=>'Modify_Collection_Member_Form'
,p_step_title=>'Modify_Collection_Member_Form'
,p_page_mode=>'MODAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1093000)
,p_plug_name=>'Modify_Collection_Member_Form'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1094000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1093000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1095000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1093000)
,p_button_name=>'DELETE_MEMBER'
,p_button_image_alt=>'Delete Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1096000)
,p_plug_name=>'Modify Collection Member'
,p_plug_display_sequence=>40
,p_region_template_options=>'#DEFAULT#'
,p_plug_source_type=>'NATIVE_FORM'
,p_query_type=>'SQL'
,p_plug_source=>'select cast(null as varchar2(4000)) as ATTR1, cast(null as varchar2(4000)) as ATTR2, cast(null as varchar2(4000)) as ATTR3, cast(null as varchar2(4000)) as ATTR4, cast(null as varchar2(4000)) as ATTR5, cast(null as date) as DATE_ATTR1, cast(null as date) as DATE_ATTR2, cast(null as date) as DATE_ATTR3, cast(null as varchar2(4000)) as NAME, cast(null as number) as NUM_ATTR1, cast(null as number) as NUM_ATTR2, cast(null as number) as NUM_ATTR3, cast(null as varchar2(4000)) as SEQ, cast(null as varchar2(4000)) as XMLTYPE from dual'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1097000)
,p_name=>'P10_ATTR1'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Character Attribute 1'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1098000)
,p_name=>'P10_ATTR2'
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Character Attribute 2'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1099000)
,p_name=>'P10_ATTR3'
,p_item_sequence=>30
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Character Attribute 3'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1100000)
,p_name=>'P10_ATTR4'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Character Attribute 4'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR4'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1101000)
,p_name=>'P10_ATTR5'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Character Attribute 5'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'ATTR5'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1102000)
,p_name=>'P10_DATE_ATTR1'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Date Attribute 1'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1103000)
,p_name=>'P10_DATE_ATTR2'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Date Attribute 2'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1104000)
,p_name=>'P10_DATE_ATTR3'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Date Attribute 3'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'DATE_ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1105000)
,p_name=>'P10_NAME'
,p_item_sequence=>90
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Name'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'NAME'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1106000)
,p_name=>'P10_NUM_ATTR1'
,p_item_sequence=>100
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Numeric Attribute 1'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR1'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1107000)
,p_name=>'P10_NUM_ATTR2'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Numeric Attribute 2'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR2'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1108000)
,p_name=>'P10_NUM_ATTR3'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Numeric Attribute 3'
,p_display_as=>'NATIVE_NUMBER_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'NUM_ATTR3'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1109000)
,p_name=>'P10_SEQ'
,p_item_sequence=>130
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'Sequence'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_read_only_when_type=>'ALWAYS'
,p_source=>'SEQ'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1110000)
,p_name=>'P10_XMLTYPE'
,p_item_sequence=>140
,p_item_plug_id=>wwv_flow_imp.id(1096000)
,p_prompt=>'XMLType'
,p_display_as=>'NATIVE_TEXTAREA'
,p_field_template=>1610598484065263269
,p_item_template_options=>'#DEFAULT#'
,p_is_required=>false
,p_source=>'XMLTYPE'
,p_source_type=>'REGION_SOURCE_COLUMN'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1111000)
,p_button_sequence=>1000
,p_button_plug_id=>wwv_flow_imp.id(1096000)
,p_button_name=>'FORM_3_SUBMIT'
,p_button_image_alt=>'Update Member'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1112000)
,p_process_sequence=>40
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_FORM_INIT'
,p_process_name=>'Initialize Modify_Collection_Member_fields_1'
,p_form_region_id=>wwv_flow_imp.id(1096000)
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>11
,p_name=>'Remove_Collections'
,p_step_title=>'Remove_Collections'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1113000)
,p_plug_name=>'Remove_Collections'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1114000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1113000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1115000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1113000)
,p_button_name=>'REMOVE_COLLECTIONS'
,p_button_image_alt=>'Remove Collections'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'UPDATE'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>12
,p_name=>'Reset_Data'
,p_step_title=>'Reset_Data'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1116000)
,p_plug_name=>'Reset_Data'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1117000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1116000)
,p_button_name=>'CANCEL'
,p_button_image_alt=>'Cancel'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'DEFINED_BY_DA'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1118000)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(1116000)
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


prompt --application/pages/page_00013
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>13
,p_name=>'Sample_Collections___API_Examples'
,p_step_title=>'Sample_Collections___API_Examples'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1119000)
,p_plug_name=>'Sample_Collections___API_Examples'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOCSEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install(
 p_id=>wwv_flow_imp.id(1120000)
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
,p_default_application_id=>8001
,p_default_id_offset=>73028955463439562
,p_default_owner=>USER
);

wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;
wwv_flow_imp.g_varchar2_table(1) := 'BEGIN EXECUTE IMMEDIATE ''DROP TABLE EBADEMOCSEMP CASCADE CONSTRAINTS''; EXCEPTION WHEN OTHERS THEN NULL; END;'||wwv_flow.LF||
'/'||wwv_flow.LF||
''||wwv_flow.LF||
'CREATE TABLE EBADEMOCSEMP ('||wwv_flow.LF||
'    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,'||wwv_flow.LF||
'    COMM NUMBER NOT NULL,'||wwv_flow.LF||
'    DEPTNO NUMBER NOT NULL,'||wwv_flow.LF||
'    EMPNO NUMBER NOT NULL,'||wwv_flow.LF||
'    ENAME VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    HIREDATE DATE NOT NULL,'||wwv_flow.LF||
'    JOB VARCHAR2(100) NOT NULL,'||wwv_flow.LF||
'    MGR NUMBER NOT NULL,'||wwv_flow.LF||
'    SAL NUMBER NOT NULL'||wwv_flow.LF||
');'||wwv_flow.LF||
''||wwv_flow.LF||
''||wwv_flow.LF||
'';
wwv_flow_imp_shared.create_install_script(
 p_id=>wwv_flow_imp.id(1121000)
,p_install_id=>wwv_flow_imp.id(1120000)
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
