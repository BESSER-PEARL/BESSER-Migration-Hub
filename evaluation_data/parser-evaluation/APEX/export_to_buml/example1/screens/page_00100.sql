prompt --application/pages/page_00100
begin
--   Manifest
--     PAGE: 00100
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
 p_id=>100
,p_name=>'Home'
,p_alias=>'HOME'
,p_step_title=>'&APP_NAME.'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
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
,p_page_component_map=>'13'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328909289072717347)
,p_plug_name=>'About this Application'
,p_static_id=>'about-this-application'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>Use this Oracle Application Express (APEX) collections sample to extend session state management to deal with arrays of session-based data.  Oracle APEX page items provides automatic session management for single value items, but does not manage a'
||'rrays of session state.  Oracle APEX collections provides the ability to manager user session state for an array ("table" of rows and columns).  The Oracle database has temporary tables, but since each page view in Oracle APEX has a stateless model, '
||'each page view in Oracle APEX is a new database session.  For this reason Oracle temporary tables can not be used for any multi page use case. Oracle APEX provides API''s to create and manage APEX collection session state.  See the example Use Cases a'
||'nd example API syntax links below to learn more about using Oracle APEX collections. </p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2133555325180962758)
,p_plug_name=>'&APP_NAME.'
,p_static_id=>'app-name'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2675494171183407654
,p_plug_display_sequence=>10
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<P>Use collections to store and manipulate large amounts of data</p>'
,p_region_image=>'#APP_FILES#icons/app-icon-512.png'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328919483942895700)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>20
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(1328919002858891716)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
,p_plug_display_condition_type=>'NEVER'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328914096060782911)
,p_plug_name=>'Collection Examples'
,p_static_id=>'collection-examples'
,p_region_name=>'EXAMPLES'
,p_region_template_options=>'#DEFAULT#'
,p_component_template_options=>'#DEFAULT#:t-Cards--featured force-fa-lg:t-Cards--displayIcons:t-Cards--3cols:t-Cards--desc-3ln:u-colors:t-Cards--animColorFill'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_list_id=>wwv_flow_imp.id(1328912986526782911)
,p_plug_source_type=>'NATIVE_LIST'
,p_list_template_id=>2888245825625742894
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1723407936420506469)
,p_plug_name=>'Footer'
,p_static_id=>'footer'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>30
,p_include_in_reg_disp_sel_yn=>'Y'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.SAMPLEAPPFOOTER'
);
wwv_flow_imp.component_end;
end;
/
