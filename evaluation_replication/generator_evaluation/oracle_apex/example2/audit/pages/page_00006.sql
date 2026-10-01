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


