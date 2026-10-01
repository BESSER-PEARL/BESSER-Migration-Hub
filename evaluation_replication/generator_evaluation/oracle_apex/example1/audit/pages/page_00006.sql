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


