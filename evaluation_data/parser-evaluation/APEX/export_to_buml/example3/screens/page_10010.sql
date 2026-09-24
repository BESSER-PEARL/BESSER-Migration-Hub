prompt --application/pages/page_10010
begin
--   Manifest
--     PAGE: 10010
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>9110
,p_default_id_offset=>14093677360354599
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>10010
,p_name=>'About'
,p_alias=>'HELP'
,p_step_title=>'About'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_group_id=>wwv_flow_imp.id(2629810413665037930)
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'All application help text can be accessed from this page. The links in the "Documentation" region give a much more in-depth explanation of the application''s features and functionality.'
,p_page_component_map=>'03'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1882485875207930919)
,p_plug_name=>'About this Application'
,p_static_id=>'about-this-application'
,p_parent_plug_id=>wwv_flow_imp.id(2629819069580037950)
,p_region_template_options=>'#DEFAULT#:t-Region--noUI:js-headingLevel-2:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>',
'The Document Generator Pre-Built Function (PBF) generates documents in an Oracle Cloud Infrastructure (OCI) Object Storage bucket based on provided JSON data and an Office template document stored in Object Storage.',
'You can download the examples as PDF, inspect the JSON data, and open the DOCX Templates with MS Office.',
'</p>',
'<p>',
'This application uses a custom Process Type Plug-in <strong>OCI Document Generator - Print Document</strong> which leverages The Oracle Cloud Infrastructure SDK for PL/SQL to manage files on Object Storage and Invoke the Pre-Built Function.',
'You can copy this Plug-in into your own application. It has several Component Settings to specify the location of Object Storage Buckets and the Document Generator Application.',
'</p>',
'<p>To learn more about Document Generator, you can refer to this blogpost:</p>',
'<p><a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/pulse/pdf-generation-oci-pre-built-function-kris-rice-gbree/">PDF Generation with OCI Pre-Built Function</a></p>',
'<p>The official documentation can be found here:</p>',
'<p><a target="_blank" rel="noopener noreferrer" href="https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm">Document Generator Function</a></p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(1882485499636930915)
,p_name=>'Application Details'
,p_static_id=>'application-details'
,p_template=>4073835273271169698
,p_display_sequence=>30
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-AVPList--rightAligned'
,p_new_grid_row=>false
,p_grid_column_span=>3
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select aa.version app_version,',
'       to_char(aa.pages,''999G999G990'') pages,',
'       ''Oracle'' vendor',
'from apex_applications aa',
'where aa.application_id = :APP_ID'))
,p_ajax_enabled=>'Y'
,p_lazy_loading=>false
,p_query_row_template=>2101991776017792140
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>'-'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1882485545007930916)
,p_query_column_id=>1
,p_column_alias=>'APP_VERSION'
,p_column_display_sequence=>10
,p_column_heading=>'App Version'
,p_use_as_row_header=>'Y'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1882485665616930917)
,p_query_column_id=>2
,p_column_alias=>'PAGES'
,p_column_display_sequence=>20
,p_column_heading=>'Pages'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(1882485753751930918)
,p_query_column_id=>3
,p_column_alias=>'VENDOR'
,p_column_display_sequence=>30
,p_column_heading=>'Vendor'
,p_heading_alignment=>'LEFT'
,p_disable_sort_column=>'N'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1882486019517930921)
,p_plug_name=>'Features'
,p_static_id=>'features'
,p_parent_plug_id=>wwv_flow_imp.id(2629819069580037950)
,p_region_template_options=>'#DEFAULT#:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ul>',
'<li>Download documents as PDF.</li>',
'<li>Download data for the document as JSON.</li>',
'<li>Download DOCX templates.</li>',
'</ul>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1882485950661930920)
,p_plug_name=>'Getting Started'
,p_static_id=>'getting-started'
,p_parent_plug_id=>wwv_flow_imp.id(2629819069580037950)
,p_region_template_options=>'#DEFAULT#:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>Run the application as a developer; at the bottom of the page will be buttons for viewing the page in the Application Express Application Builder. Click on the "Edit Page X" button to see how the pages are defined.</p>',
'<p>If you have questions, ask them on the <a target="_blank" rel="noopener noreferrer" href="https://forums.oracle.com/ords/apexds/domain/dev-community/category/apex">Oracle APEX Forum</a>.</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2629819069580037950)
,p_plug_name=>'Help Container'
,p_static_id=>'help-container'
,p_region_template_options=>'#DEFAULT#:t-Region--removeHeader js-removeLandmark:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp.component_end;
end;
/
