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

prompt APPLICATION 100 - SampleCalendar

begin
null;
end;
/

prompt --application/pages/delete_00010
begin
wwv_flow_imp_page.remove_page (p_flow_id=>wwv_flow.g_flow_id, p_page_id=>10);
end;
/

prompt --application/pages/page_00010
begin
wwv_flow_imp_page.create_page(
-- is_main_page: True
 p_id=>10,
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