prompt --application/pages/page_00012
begin
--   Manifest
--     PAGE: 00012
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
 p_id=>12
,p_name=>'Sample Collections - API Examples'
,p_alias=>'SAMPLE-COLLECTIONS-API-EXAMPLES'
,p_step_title=>'Sample Collections - API Syntax'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_autocomplete_on_off=>'ON'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'11'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309898385710155383)
,p_plug_name=>'About this page'
,p_static_id=>'about-this-page'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'<p>This page lists some of the PL/SQL page processes used in this demonstration application.</p>'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309897183024135670)
,p_plug_name=>'apex_collection.add_member'
,p_static_id=>'apex-collection-add-member'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>',
'--',
'-- This application uses the Application Level Date format to control the default date format for the application.',
'-- Without this, then you would need to specify explict date format masks in the TO_DATE conversions.',
'--',
'apex_collection.add_member(',
'    p_collection_name => :P3_NAME,',
'    p_c001            => :P3_ATTR1,',
'    p_c002            => :P3_ATTR2,',
'    p_c003            => :P3_ATTR3,',
'    p_c004            => :P3_ATTR4,',
'    p_c005            => :P3_ATTR5,',
'    p_n001            => :P3_NUM_ATTR1,',
'    p_n002            => :P3_NUM_ATTR2,',
'    p_n003            => :P3_NUM_ATTR3,',
'    p_d001            => to_date(:P3_DATE_ATTR1),',
'    p_d002            => to_date(:P3_DATE_ATTR2),',
'    p_d003            => to_date(:P3_DATE_ATTR3),',
'    p_generate_md5    => ''YES'' );',
'commit;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1341102192095892218)
,p_plug_name=>'apex_collection.create_collection_from_query2'
,p_static_id=>'apex-collection-create-collection-from-query'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>80
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>apex_collection.create_collection_from_query2(',
'    p_collection_name => ''EMPCollection'',',
'    p_query           => ''select empno, sal, comm, deptno, null, hiredate, null, null, null, null, ename, job, mgr, ''''O'''' original_flag from eba_demo_cs_emp order by ename'',',
'    p_generate_md5    => ''YES'');',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309896776435058046)
,p_plug_name=>'apex_collection.create_or_truncate_collection'
,p_static_id=>'apex-collection-create-or-truncate-collection'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>apex_collection.create_or_truncate_collection( p_collection_name => :P2_NAME );',
'commit;</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309897903933151112)
,p_plug_name=>'apex_collection.delete_collection'
,p_static_id=>'apex-collection-delete-collection'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>50
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>apex_collection.delete_collection(',
'    p_collection_name => :P3_NAME );',
'--',
'commit;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309897580038144277)
,p_plug_name=>'apex_collection.resequence_collection'
,p_static_id=>'apex-collection-resequence-collection'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>40
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>apex_collection.resequence_collection(',
'    p_collection_name => :P3_NAME );',
'commit;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309900093460167101)
,p_plug_name=>'apex_collection.truncate_collection'
,p_static_id=>'apex-collection-truncate-collection'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>60
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>apex_collection.truncate_collection (',
'    p_collection_name => :P3_NAME );',
'--',
'commit;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1341102482183898877)
,p_plug_name=>'apex_collection.update_member_attribute'
,p_static_id=>'apex-collection-update-member-attribute'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>90
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>',
'for c1 in (select n001 empno, seq_id',
'             from apex_collections',
'            where collection_name = ''EMPCOLLECTION''',
'           order by seq_id) loop',
'    ',
'    l_rowxml := dbms_xmlgen.getxml( ''select * from eba_demo_cs_emp where empno = '' || c1.empno );',
'    apex_collection.update_member_attribute( ',
'        p_collection_name => ''EMPCollection'',',
'        p_seq             => c1.seq_id,',
'        p_xmltype_number  => 1,',
'        p_xmltype_value   => XMLType(l_rowxml));',
'end loop;',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1309901089958213329)
,p_plug_name=>'apex_collections'
,p_static_id=>'apex-collections'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>70
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<pre>select seq_id editlink,',
'    seq_id, ',
'    n001, ',
'    n002, ',
'    n003, ',
'    n004, ',
'    d001, ',
'    c001, ',
'    c002, ',
'    c003, ',
'    c004 status',
'from apex_collections',
'where collection_name = ''EMPCOLLECTION''',
'</pre>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1328922402081910368)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>10
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(1328919002858891716)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp.component_end;
end;
/
