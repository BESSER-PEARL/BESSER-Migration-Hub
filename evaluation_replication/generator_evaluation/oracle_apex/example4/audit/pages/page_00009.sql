prompt --application/pages/page_00009
begin
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2024.11.30'
,p_release=>'24.2.6'
,p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)
,p_default_application_id=>8004
,p_default_id_offset=>12645642186646158
,p_default_owner=>USER
);

wwv_flow_imp_page.create_page(
 p_id=>9
,p_name=>'Project_Dashboard'
,p_step_title=>'Project_Dashboard'
,p_page_mode=>'NORMAL'
,p_autocomplete_on_off=>'OFF'
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1101000)
,p_plug_name=>'Project_Dashboard'
,p_plug_display_sequence=>10
,p_region_template_options=>'#DEFAULT#'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(1102000)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1101000)
,p_button_name=>'CREATE'
,p_button_image_alt=>'Create'
,p_button_template_id=>4073839297780169708
,p_button_template_options=>'#DEFAULT#'
,p_button_position=>'BOTTOM'
,p_button_action=>'SUBMIT'
,p_database_action=>'INSERT'
);
wwv_flow_imp.component_end;
end;
/


