prompt --application/pages/page_00001
begin
--   Manifest
--     PAGE: 00001
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7940
,p_default_id_offset=>10243121705511410
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>1
,p_name=>'Basic Collections'
,p_alias=>'BASIC-COLLECTIONS'
,p_step_title=>'Basic Collections'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'ON'
,p_inline_css=>wwv_flow_string.join(wwv_flow_t_varchar2(
'section.infoRegion {',
'    border: 1px solid #9AAEC8;',
'    background-color: #DDE7F5;',
'}',
'section.infoRegion > div.uRegionHeading {',
'    background: none transparent;',
'}',
'.infoRegionIcon {',
'    position: absolute;',
'    left: 0;',
'    margin: 16px;',
'    top: 0;',
'}',
'section.infoRegion.uRegion > div.uRegionContent {',
'    position: relative;',
'    min-height: 32px;',
'    padding: 16px 16px 16px 64px;',
'}',
'.infoRegion h1 {',
'    font-weight: bold;',
'    font-size: 14px;',
'    color: #202020;',
'    text-shadow: 0 1px 0 rgba(255,255,255,.65);',
'}',
'.infoRegion p {',
'    font-size: 12px;',
'    line-height: 20px;',
'    padding: 8px 0 0 0;',
'    text-shadow: 0 1px 0 rgba(255,255,255,.25);',
'    color: #303030;',
'}',
'.infoRegion p:last-child {',
'    margin-bottom: 0 !important;',
'}',
'',
'',
'',
'div.featuredBlock{',
'	-webkit-border-radius:3px;',
'	-moz-border-radius:3px;',
'	border-radius:3px;',
'	-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.05);',
'	-moz-box-shadow:0 1px 2px rgba(0,0,0,0.05);',
'	box-shadow:0 1px 2px rgba(0,0,0,0.05);',
'	border:1px solid #E1E6EB;',
'	margin-bottom:18px',
'}',
'div.featuredBlock div.featuredIcon{',
'	background-image:url(''data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4gPHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJncmFkIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPb'
||'lVzZSIgeDE9IjUwJSIgeTE9IjAlIiB4Mj0iNTAlIiB5Mj0iMTAwJSI+PHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2ZmZmZmZiIvPjxzdG9wIG9mZnNldD0iNDAlIiBzdG9wLWNvbG9yPSIjZmZmZmZmIi8+PHN0b3Agb2Zmc2V0PSI2MCUiIHN0b3AtY29sb3I9IiNmNGY0ZjgiLz48c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3A'
||'tY29sb3I9IiNmZmZmZmYiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI2dyYWQpIiAvPjwvc3ZnPiA='');',
'	background-size:100%;',
'	background-image:-webkit-gradient(linear, 50% 0%, 50% 100%, color-stop(0%, #ffffff), color-stop(40%, #ffffff), color-stop(60%, #f4f4f8), color-stop(100%, #ffffff));',
'	background-image:-webkit-linear-gradient(top, #ffffff 0%,#ffffff 40%,#f4f4f8 60%,#ffffff 100%);',
'	background-image:-moz-linear-gradient(top, #ffffff 0%,#ffffff 40%,#f4f4f8 60%,#ffffff 100%);',
'	background-image:linear-gradient(top, #ffffff 0%,#ffffff 40%,#f4f4f8 60%,#ffffff 100%);',
'	-webkit-border-radius:3px 3px 0 0;',
'	-moz-border-radius:3px 3px 0 0;',
'	border-radius:3px 3px 0 0;',
'	padding:8px 0;',
'	min-height: 90px;',
'	text-align:center;',
'}',
'div.featuredBlock div.featuredIcon img{',
'	display:block;',
'	margin:0 auto 0 auto;',
'	-webkit-box-reflect:below -20px -webkit-gradient(linear, left top, left bottom, from(transparent), color-stop(65%, transparent), to(rgba(255,255,255,0.2)));',
'}',
'div.featuredBlock div.featuredIcon h1{',
'	font-size:12px;',
'	line-height:12px;',
'	color:#404040;',
'	margin:0 8px;',
'	padding:0;',
'	text-align:center;',
'}',
'a.blockLink,a.blockLink:hover{',
'	text-decoration:none',
'}',
'a.blockLink:hover div.featuredBlock{',
'	border:1px solid #b1bbcb',
'}',
'a.blockLink:hover div.featuredBlock div.featuredIcon{',
'	background: none #e5effb;',
'	-webkit-box-shadow: 0 0 10px rgba(50,117,199,0.25);',
'	-moz-box-shadow: 0 0 10px rgba(50,117,199,0.25);',
'	box-shadow: 0 0 10px rgba(50,117,199,0.25);',
'}',
'.regionDivider {',
'	border-top: 2px solid #F0F0F0 !important;',
'	padding-top: 8px;;',
'}'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'18'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1234749299943344552)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This use case covers the basics of creating and editing an Oracle Application Express (APEX) collection. Collections are used to support vectors of APEX se',
'ssion-based data.  APEX Collections are commonly used in place of Oracle temporary tables, but they should not be used for millions of rows per user per APEX ',
'session.</p>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8440883268528676411)
,p_plug_name=>'APEX_COLLECTIONS View'
,p_static_id=>'apex-collections-view'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2102002977963900996
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select seq_id, c001, c002, c003, c004, c005, n001, n002, n003, d001, d002, d003,  case when xmltype001 is null then null else substr(extract(xmltype001,''*'').getstringval(),1,40) || ''...'' end xmltype001, md5_original, collection_name, COLLECTION_NAME '
||'COLLECTION_NAME2',
'  from apex_collections',
''))
,p_plug_source_type=>'NATIVE_IR'
,p_ai_enabled=>false
);
wwv_flow_imp_page.create_worksheet(
 p_id=>wwv_flow_imp.id(8440883353099676411)
,p_max_row_count=>'10000'
,p_max_row_count_message=>'This query returns more than 10,000 rows, please filter your data to ensure complete results.'
,p_no_data_found_message=>'No data found.'
,p_allow_save_rpt_public=>'Y'
,p_show_nulls_as=>'-'
,p_pagination_type=>'ROWS_X_TO_Y'
,p_pagination_display_pos=>'BOTTOM_RIGHT'
,p_show_display_row_count=>'Y'
,p_report_list_mode=>'TABS'
,p_lazy_loading=>false
,p_show_detail_link=>'N'
,p_show_notify=>'Y'
,p_download_formats=>'HTML:CSV'
,p_enable_mail_download=>'N'
,p_internal_uid=>7788161179199500656
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440883773229676412)
,p_db_column_name=>'C001'
,p_display_order=>3
,p_column_identifier=>'C'
,p_column_label=>'Character<br />Attribute 1'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440883867620676412)
,p_db_column_name=>'C002'
,p_display_order=>4
,p_column_identifier=>'D'
,p_column_label=>'Character<br />Attribute 2'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440883956924676412)
,p_db_column_name=>'C003'
,p_display_order=>5
,p_column_identifier=>'E'
,p_column_label=>'Character<br />Attribute 3'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884042349676412)
,p_db_column_name=>'C004'
,p_display_order=>6
,p_column_identifier=>'F'
,p_column_label=>'Character<br />Attribute 4'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884161047676412)
,p_db_column_name=>'C005'
,p_display_order=>7
,p_column_identifier=>'G'
,p_column_label=>'Character<br />Attribute 5'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884770704676413)
,p_db_column_name=>'COLLECTION_NAME'
,p_display_order=>13
,p_column_identifier=>'M'
,p_column_label=>'Action'
,p_column_link=>'f?p=&APP_ID.:4:&SESSION.::&DEBUG.:4:P4_NAME,P4_SEQ:#COLLECTION_NAME#,#SEQ_ID#'
,p_column_linktext=>'Edit'
,p_column_link_attr=>'class="t-Button t-Button--warning"'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(1234653597657467323)
,p_db_column_name=>'COLLECTION_NAME2'
,p_display_order=>18
,p_column_identifier=>'R'
,p_column_label=>'Collection Name'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8406478541560132781)
,p_db_column_name=>'D001'
,p_display_order=>15
,p_column_identifier=>'O'
,p_column_label=>'Date<br />Attribute 1'
,p_column_type=>'DATE'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8406478646408132783)
,p_db_column_name=>'D002'
,p_display_order=>16
,p_column_identifier=>'P'
,p_column_label=>'Date<br />Attribute 2'
,p_column_type=>'DATE'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8406478738336132784)
,p_db_column_name=>'D003'
,p_display_order=>17
,p_column_identifier=>'Q'
,p_column_label=>'Date<br />Attribute 3'
,p_column_type=>'DATE'
,p_heading_alignment=>'LEFT'
,p_tz_dependent=>'N'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884673667676413)
,p_db_column_name=>'MD5_ORIGINAL'
,p_display_order=>12
,p_column_identifier=>'L'
,p_column_label=>'MD5 Original'
,p_column_type=>'STRING'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884259019676413)
,p_db_column_name=>'N001'
,p_display_order=>8
,p_column_identifier=>'H'
,p_column_label=>'Numeric<br />Attribute 1'
,p_column_type=>'NUMBER'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884345314676413)
,p_db_column_name=>'N002'
,p_display_order=>9
,p_column_identifier=>'I'
,p_column_label=>'Numeric<br />Attribute 2'
,p_column_type=>'NUMBER'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440884461067676413)
,p_db_column_name=>'N003'
,p_display_order=>10
,p_column_identifier=>'J'
,p_column_label=>'Numeric<br />Attribute 3'
,p_column_type=>'NUMBER'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440883650883676412)
,p_db_column_name=>'SEQ_ID'
,p_display_order=>2
,p_column_identifier=>'B'
,p_column_label=>'Sequence'
,p_column_type=>'NUMBER'
,p_display_text_as=>'WITHOUT_MODIFICATION'
,p_heading_alignment=>'RIGHT'
,p_column_alignment=>'RIGHT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_column(
 p_id=>wwv_flow_imp.id(8440885661941693850)
,p_db_column_name=>'XMLTYPE001'
,p_display_order=>14
,p_column_identifier=>'N'
,p_column_label=>'XML Type'
,p_column_type=>'STRING'
,p_heading_alignment=>'LEFT'
,p_use_as_row_header=>'N'
,p_available_clientside=>'N'
);
wwv_flow_imp_page.create_worksheet_rpt(
 p_id=>wwv_flow_imp.id(8440884868951676919)
,p_application_user=>'APXWS_DEFAULT'
,p_report_seq=>10
,p_report_alias=>'4502667'
,p_status=>'PUBLIC'
,p_is_default=>'Y'
,p_display_rows=>5
,p_report_columns=>'COLLECTION_NAME:COLLECTION_NAME2:SEQ_ID:C001:C002:C003:C004:C005:N001:N002:N003:D001:D002:D003:XMLTYPE001'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328919077709893873)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>40
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(1328919002858891716)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1423779425968166773)
,p_plug_name=>'Footer'
,p_static_id=>'footer'
,p_plug_display_sequence=>40
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.SAMPLEAPPFOOTER'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(8441191350185419145)
,p_plug_name=>'Tip'
,p_static_id=>'tip'
,p_region_css_classes=>'infoTextRegion'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<ol style="margin: 8px 24px;">',
'<li>Click the "Create Collection" button to create a new named collection',
'<li>Add members to the collection by clicking the "Modify Collection" button',
'<li>Modify the members of the collection by clicking the icon in the Action column in the report below',
'</ol>'))
,p_plug_column_width=>'valign=top'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8876954738779466040)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(1328919077709893873)
,p_button_name=>'Create_Collection'
,p_static_id=>'create-collection'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create Collection'
,p_button_position=>'CREATE'
,p_button_redirect_url=>'f?p=&APP_ID.:2:&SESSION.::&DEBUG.:RP,2::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(8877005631216567996)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(1328919077709893873)
,p_button_name=>'Modify_Collection'
,p_static_id=>'modify-collection'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Modify Collection'
,p_button_position=>'EDIT'
,p_button_redirect_url=>'f?p=&APP_ID.:3:&SESSION.::&DEBUG.:RP::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(2462277623549588861)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(8440883268528676411)
,p_button_name=>'RESET'
,p_static_id=>'reset'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>2350584059425431644
,p_button_image_alt=>'Reset'
,p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'
,p_button_redirect_url=>'f?p=&APP_ID.:&APP_PAGE_ID.:&SESSION.::&DEBUG.:RP,&APP_PAGE_ID.,RIR::'
,p_icon_css_classes=>'fa-undo-alt'
);
wwv_flow_imp.component_end;
end;
/
