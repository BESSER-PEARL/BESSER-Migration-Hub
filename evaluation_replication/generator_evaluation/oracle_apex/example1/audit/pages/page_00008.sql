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


