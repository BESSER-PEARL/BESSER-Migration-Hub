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
p_default_application_id=>149417,
p_default_id_offset=>0,
p_default_owner=>'WKSP_NAMEOFWORKSPACE'
);
end;
/

prompt APPLICATION 149417 - MyFirstModule

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
 p_id=>10,
p_name=>'Staff',
p_alias=>'STAFF1',
p_step_title=>'Staff',
p_autocomplete_on_off=>'OFF',
p_page_template_options=>'#DEFAULT#',
p_protection_level=>'C',
p_help_text=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>To find data enter a search term into the search dialog, or click on the column headings to limit the records returned.</p>',
'',
'<p>You can perform numerous functions by clicking the <strong>Actions</strong> button. This includes selecting the columns that are displayed / hidden and their display sequence, plus numerous data and format functions.  You can also define additiona'
||'l views of the data using the chart, group by, and pivot options.</p>',
'',
'<p>If you want to save your customizations select report, or click download to unload the data. Enter you email address and time frame under subscription to be sent the data on a regular basis.<p>',
'',
'<p>For additional information click Help at the bottom of the Actions menu.</p> ',
'',
'<p>Click the <strong>Reset</strong> button to reset the interactive report back to the default settings.</p>')),
p_page_component_map=>'18'
);


wwv_flow_imp_page.create_page_plug(
p_id => 8708,
p_plug_name=>'Staffs',
p_region_template_options=>'#DEFAULT#',
p_plug_display_sequence=>10,
p_query_type=>'TABLE',
p_query_table=>'STAFF',
p_include_rowid_column=>false,
p_plug_source_type=>'NATIVE_IR',
p_prn_page_header=>'Staff'
);

-- for row in list
wwv_flow_imp_page.create_worksheet(
p_name=>'Staff'
,p_max_row_count_message=>'The maximum row count for this report is #MAX_ROW_COUNT# rows.  Please apply a filter to reduce the number of records in your query.'
,p_no_data_found_message=>'No data found.'
,p_base_pk1=>'ID'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_report_list_mode=>'TABS'
,p_lazy_loading=>false
,p_show_detail_link=>'C'
,p_show_notify=>'Y'
,p_download_formats=>'CSV:HTML:XLSX:PDF'
,p_enable_mail_download=>'Y'
,p_detail_link=>'f?p=&APP_ID.:11:&APP_SESSION.::&DEBUG.:RP:P11_ID:\#ID#\'
,p_detail_link_text=>'<button style="            position: relative;            top: auto;            left: auto;            bottom: auto;            right: auto;            text-align: Alignment.LEFT;            background-color: #FFC107;            color: #000000;            border: #FFA000;">Edit</button>'
,p_owner=>'ATEFEH.NIRUMAND@LIST.LU'
,p_internal_uid=>76608987145708126528
);


wwv_flow_imp_page.create_worksheet_column(
p_db_column_name=>'ID'
,p_display_order=>0
,p_is_primary_key=>'Y'
,p_column_identifier=>'A'
,p_column_label=>'ID'
,p_column_type=>'NUMBER'
,p_display_text_as=>'HIDDEN_ESCAPE_SC'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);

wwv_flow_imp_page.create_worksheet_column(
p_db_column_name=>'FAMILYNAME'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'FamilyName'
,p_column_link=>'f?p=&APP_ID.:6:&APP_SESSION.::&DEBUG.:6,RR:IR_ID:\#FAMILYNAME#\'
,p_column_linktext=>'#FAMILYNAME#'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);

wwv_flow_imp_page.create_worksheet_column(
p_db_column_name=>'GIVENNAME'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'GivenName'
,p_column_link=>'f?p=&APP_ID.:6:&APP_SESSION.::&DEBUG.:6,RR:IR_ID:\#GIVENNAME#\'
,p_column_linktext=>'#GIVENNAME#'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
);






wwv_flow_imp_page.create_worksheet_rpt(
p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'766090505'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_report_columns=>'FAMILYNAME:GIVENNAME'
,p_sort_column_1=>'FAMILYNAME'
,p_sort_direction_1=>'ASC'
);
wwv_flow_imp_page.create_page_button(
p_button_sequence=>10,
p_button_plug_id=>8708,
p_button_name=>'ADD STAFF'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Add Staff'
,p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'
,p_button_redirect_url=>'f?p=&APP_ID.:11:&APP_SESSION.::&DEBUG.:11::'
);

wwv_flow_imp_page.create_page_plug(
p_plug_name=>'Breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2531463326621247859
,p_plug_display_sequence=>20
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4072363345357175094
);


wwv_flow_imp_page.create_page_da_event(

 p_id=>3872,  -- give it a unique ID
 p_name=>'Edit Report - Dialog Closed',
 p_event_sequence=>10,
 p_triggering_element_type=>'REGION',
 p_triggering_region_id=>8708,
 p_bind_type=>'bind',
 p_execution_type=>'IMMEDIATE',
 p_bind_event_type=>'apexafterclosedialog'
);

wwv_flow_imp_page.create_page_da_action(


 p_id=>3872,  -- unique ID for the action
 p_event_id=>3872,  -- link to parent DA event
 p_event_result=>'TRUE',
 p_action_sequence=>10,
 p_execute_on_page_init=>'N',
 p_action=>'NATIVE_REFRESH',
 p_affected_elements_type=>'REGION',
 p_affected_region_id=>8708
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