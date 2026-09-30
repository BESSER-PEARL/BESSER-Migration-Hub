prompt --application/set_environment
set define off verify off feedback off
whenever sqlerror exit sql.sqlcode rollback
--------------------------------------------------------------------------------
--
-- Oracle APEX export file
--
-- You should run this script using a SQL client connected to the database as
-- the owner (parsing schema) of the application or as a database user with the
-- APEX_ADMINISTRATOR_ROLE role.
--
-- This export file has been automatically generated. Modifying this file is not
-- supported by Oracle and can lead to unexpected application and/or instance
-- behavior now or in the future.
--
-- NOTE: Calls to apex_application_install override the defaults below.
--
--------------------------------------------------------------------------------
begin
wwv_flow_imp.import_begin (
p_version_yyyy_mm_dd=>'2024.11.30',
p_release=>'24.2.6',
p_default_workspace_id=>63287066999237619267,
p_default_application_id=>100,
p_default_id_offset=>0,
p_default_owner=>'WKSP_WKSPEVAL'
);
end;
/

prompt APPLICATION 100 - SampleReporting

begin
null;
end;
/

prompt --application/pages/delete_0008
begin
wwv_flow_imp_page.remove_page (p_flow_id=>wwv_flow.g_flow_id, p_page_id=>8);
end;
/

prompt --application/pages/page_0008
begin
wwv_flow_imp_page.create_page(
-- is_main_page: True
 p_id=>8,
p_name=>'Classic_Report',
p_alias=>'CLASSIC_REPORT_P8',
p_step_title=>'Classic_Report',
p_autocomplete_on_off=>'OFF',
p_page_template_options=>'#DEFAULT#',
p_protection_level=>'C',
p_page_component_map=>'18'
);

wwv_flow_imp_page.create_page_plug(
p_id => 43514290014532686,
p_plug_name=>'Classic_Report Region',
p_region_template_options=>'#DEFAULT#',
p_plug_display_sequence=>10,
p_plug_source_type=>'NATIVE_STATIC'
);
wwv_flow_imp_page.create_page_button(
-- action_type: Cancel
p_button_sequence=>10,
p_button_plug_id=>43514290014532686,
p_button_name=>'RESET_REPORT'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_is_hot=>'N'
,p_button_image_alt=>'Reset_Report'
,p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'
,p_button_redirect_url=>'f?p=&APP_ID.:8:&APP_SESSION.::&DEBUG.:8::'
);
end;
/

prompt --application/end_environment
begin
wwv_flow_imp.import_end(p_auto_install_sup_obj => nvl(wwv_flow_application_install.get_auto_install_sup_obj, false)
);
commit;
end;
/
set verify on feedback on define on
prompt  ...done