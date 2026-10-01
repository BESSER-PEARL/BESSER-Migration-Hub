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


