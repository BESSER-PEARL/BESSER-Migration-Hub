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


