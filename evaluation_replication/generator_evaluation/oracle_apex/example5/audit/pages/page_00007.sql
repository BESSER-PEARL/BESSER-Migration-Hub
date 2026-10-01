prompt --application/pages/page_00007
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8005
,p_default_id_offset=>49461010066525635
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>7
,p_name=>'Debounce_and_Throttle'
,p_step_title=>'Debounce_and_Throttle'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1094000)
,p_plug_name=>'Debounce_and_Throttle'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp.component_end;
end;
/


