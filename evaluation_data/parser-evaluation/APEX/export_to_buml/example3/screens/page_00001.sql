prompt --application/pages/page_00001
begin
--   Manifest
--     PAGE: 00001
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
 p_id=>1
,p_name=>'Home'
,p_alias=>'HOME'
,p_step_title=>'Sample DocGen'
,p_reload_on_submit=>'A'
,p_autocomplete_on_off=>'OFF'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_page_component_map=>'13'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1882485398558930914)
,p_plug_name=>'About'
,p_static_id=>'about'
,p_region_template_options=>'#DEFAULT#:t-Region--hideHeader js-addHiddenHeadingRoleDesc:t-Region--noUI:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'Welcome to the <strong>Sample Document Generator</strong> Application. This application contains a few examples to generate PDF documents using JSON data and DOCX templates.'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1858937939293284827)
,p_plug_name=>'DWROLE grant is missing'
,p_static_id=>'dwrole-grant-is-missing'
,p_parent_plug_id=>wwv_flow_imp.id(1858937747377284825)
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--danger'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>10
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_function_body_language=>'PLSQL'
,p_plug_source=>'return ''<pre>grant DWROLE to '' || :WORKSPACE_SCHEMA || '';</pre>'';'
,p_lazy_loading=>false
,p_plug_source_type=>'NATIVE_DYNAMIC_CONTENT'
,p_plug_display_condition_type=>'NOT_EXISTS'
,p_plug_display_when_condition=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select 1',
'  from user_role_privs',
' where granted_role  = ''DWROLE'''))
,p_plug_header=>'Please execute the following as ADMIN user:'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1882486177436930922)
,p_plug_name=>'Examples'
,p_static_id=>'examples'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2074200852440250129
,p_plug_display_sequence=>60
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select list_entry_id as id,',
'       display_sequence,',
'       entry_text as title,',
'       entry_attribute_01 as description,',
'       entry_attribute_02 as screenshot_img_path,',
'       entry_attribute_03 as template_path,',
'       entry_attribute_04 as static_id,',
'       ''Screenshot of ''||entry_text||'' PDF document'' as alt',
'  from apex_application_list_entries',
' where application_id = :APP_ID',
'   and list_name = ''Examples''',
' order by display_sequence asc'))
,p_lazy_loading=>false
,p_plug_source_type=>'NATIVE_CARDS'
,p_plug_query_num_rows_type=>'SCROLL'
,p_show_total_row_count=>false
);
wwv_flow_imp_page.create_card(
 p_id=>wwv_flow_imp.id(1882486280727930923)
,p_region_id=>wwv_flow_imp.id(1882486177436930922)
,p_layout_type=>'GRID'
,p_grid_column_count=>2
,p_title_adv_formatting=>false
,p_title_column_name=>'TITLE'
,p_sub_title_adv_formatting=>true
,p_sub_title_html_expr=>'<h4 class="a-CardView-subTitle">&DESCRIPTION!RAW.</h4>'
,p_body_adv_formatting=>false
,p_second_body_adv_formatting=>false
,p_media_adv_formatting=>false
,p_media_source_type=>'STATIC_URL'
,p_media_url=>'#APP_IMAGES#&SCREENSHOT_IMG_PATH.'
,p_media_display_position=>'FIRST'
,p_media_appearance=>'WIDESCREEN'
,p_media_sizing=>'FIT'
,p_media_description=>'&ALT.'
,p_pk1_column_name=>'ID'
);
wwv_flow_imp_page.create_card_action(
 p_id=>wwv_flow_imp.id(1882486402004930924)
,p_card_id=>wwv_flow_imp.id(1882486280727930923)
,p_action_type=>'BUTTON'
,p_position=>'PRIMARY'
,p_display_sequence=>10
,p_label=>'Generate PDF'
,p_static_id=>'action'
,p_link_target_type=>'REDIRECT_PAGE'
,p_link_target=>'f?p=&APP_ID.:1:&SESSION.:&STATIC_ID.:&DEBUG.:::'
,p_link_attributes=>'title="Generate PDF Document"'
,p_button_display_type=>'TEXT_WITH_ICON'
,p_icon_css_classes=>'fa-print'
,p_is_hot=>true
,p_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_condition_expr1=>'P1_PRIVS_MISSING_YN'
,p_condition_expr2=>'N'
,p_exec_cond_for_each_row=>true
);
wwv_flow_imp_page.create_card_action(
 p_id=>wwv_flow_imp.id(1875384403288832776)
,p_card_id=>wwv_flow_imp.id(1882486280727930923)
,p_action_type=>'BUTTON'
,p_position=>'SECONDARY'
,p_display_sequence=>20
,p_label=>'JSON'
,p_static_id=>'action-2'
,p_link_target_type=>'REDIRECT_PAGE'
,p_link_target=>'f?p=&APP_ID.:1:&SESSION.:JSON:&DEBUG.::P1_STATIC_ID:&STATIC_ID.'
,p_link_attributes=>'title="Download JSON Document"'
,p_button_display_type=>'ICON'
,p_icon_css_classes=>'fa-file-json-o'
,p_is_hot=>false
);
wwv_flow_imp_page.create_card_action(
 p_id=>wwv_flow_imp.id(1875384500278832777)
,p_card_id=>wwv_flow_imp.id(1882486280727930923)
,p_action_type=>'BUTTON'
,p_position=>'SECONDARY'
,p_display_sequence=>30
,p_label=>'Template'
,p_static_id=>'action-3'
,p_link_target_type=>'REDIRECT_URL'
,p_link_target=>'#APP_IMAGES#&TEMPLATE_PATH.'
,p_link_attributes=>'download title="Download MS Word Document"'
,p_button_display_type=>'ICON'
,p_icon_css_classes=>'fa-file-word-o'
,p_is_hot=>false
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1859339660447414426)
,p_plug_name=>'Installed on Oracle Cloud'
,p_static_id=>'installed-on-oracle-cloud'
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'EXPRESSION'
,p_plug_display_when_condition=>'apex_application_global.g_cloud'
,p_plug_display_when_cond2=>'PLSQL'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1859339626203414425)
,p_plug_name=>'Not installed on Oracle Cloud'
,p_static_id=>'not-installed-on-oracle-cloud'
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--danger'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>20
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>'In order to work properly, this application must be installed in an APEX Service or Autonomous Database in the Oracle Cloud.'
,p_plug_display_condition_type=>'EXPRESSION'
,p_plug_display_when_condition=>'not apex_application_global.g_cloud'
,p_plug_display_when_cond2=>'PLSQL'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1858938120939284828)
,p_plug_name=>'OCI$RESOURCE_PRINCIPAL is missing'
,p_static_id=>'oci-resource-principal-is-missing'
,p_parent_plug_id=>wwv_flow_imp.id(1858937747377284825)
,p_region_template_options=>'#DEFAULT#:t-Alert--horizontal:t-Alert--defaultIcons:t-Alert--danger'
,p_plug_template=>2042159785845301134
,p_plug_display_sequence=>20
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_function_body_language=>'PLSQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'return ''Please execute the following as ADMIN user:<pre>begin',
'    dbms_cloud_admin.enable_resource_principal();',
'    dbms_cloud_admin.enable_resource_principal(username => '''''' || :WORKSPACE_SCHEMA || '''''');',
'end</pre>'';'))
,p_lazy_loading=>false
,p_plug_source_type=>'NATIVE_DYNAMIC_CONTENT'
,p_plug_display_condition_type=>'NOT_EXISTS'
,p_plug_display_when_condition=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select 1',
'  from all_credentials',
' where credential_name  = ''OCI$RESOURCE_PRINCIPAL'''))
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1858938194631284829)
,p_plug_name=>'Prerequisites'
,p_static_id=>'prerequisites'
,p_parent_plug_id=>wwv_flow_imp.id(1859339660447414426)
,p_region_template_options=>'#DEFAULT#:js-useLocalStorage:is-expanded:t-Region--scrollBody'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>10
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'<p>This application can only be used on an Autonomous Database on OCI.</p>',
'<strong>Configuration steps:</strong>',
'<ol>',
'    <li><a target="_blank" rel="noopener noreferrer" href="https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_document_generator.htm#functions_pbf_catalog_document_generator">Configure the Document Generator Function</a>'
||'</li>',
'    <li>Create an Object Storage Bucket</li>',
'    <li>Create a Dynamic Group for the Autonomous Database',
'        <code><pre>resource.id = ''&lt;db_ocid>''</pre></code></li>',
'    </li>',
'     <li>Create a Policy for the Dynamic Group to manage objects and invoke the function',
'        <code><pre>',
'Allow dynamic-group &lt;group_name> to manage objects in compartment &lt;compartment_name>',
'Allow dynamic-group &lt;group_name> to manage buckets in compartment &lt;compartment_name>',
'Allow dynamic-group &lt;group_name> to use functions-family in compartment &lt;compartment_name>',
'        </pre></code>',
'    </li>',
'     <li>Enable the Resource Principal in the database as <code>ADMIN</code> user',
'        <code><pre>',
'EXEC DBMS_CLOUD_ADMIN.ENABLE_RESOURCE_PRINCIPAL();',
'EXEC DBMS_CLOUD_ADMIN.ENABLE_RESOURCE_PRINCIPAL(username => ''&WORKSPACE_SCHEMA.'');',
'        </pre></code>',
'    </li>',
'     <li>Grant the role <code>DWROLE</code> to the workspace schema as <code>ADMIN</code> user',
'        <code><pre>grant DWROLE to &WORKSPACE_SCHEMA.;</pre></code>',
'    </li> ',
'     <li>Configure the "OCI Document Generator - Print Document" Plug-In Component Settings',
'    </li>  ',
'</ol>'))
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1858937747377284825)
,p_plug_name=>'Privs'
,p_static_id=>'privs'
,p_parent_plug_id=>wwv_flow_imp.id(1859339660447414426)
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>4502917002193490937
,p_plug_display_sequence=>20
,p_plug_display_point=>'SUB_REGIONS'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_display_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_plug_display_when_condition=>'P1_PRIVS_MISSING_YN'
,p_plug_display_when_cond2=>'Y'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(2629818009174037943)
,p_plug_name=>'Sample Document Generator'
,p_static_id=>'sample-document-generator'
,p_region_template_options=>'#DEFAULT#'
,p_plug_template=>2675494171183407654
,p_plug_display_sequence=>30
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'BELOW'
,p_location=>null
,p_plug_source=>'Demonstration of invoking the Oracle Document Generator Pre-Built Function in APEX.'
,p_region_image=>'#APP_FILES#icons/app-icon-512.png'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1859339429037414423)
,p_name=>'P1_PRIVS_MISSING_YN'
,p_item_sequence=>70
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(1893616287575720519)
,p_name=>'P1_STATIC_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(1882486177436930922)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(1859339513309414424)
,p_computation_sequence=>10
,p_computation_item=>'P1_PRIVS_MISSING_YN'
,p_static_id=>'p1-privs-missing-yn'
,p_computation_point=>'BEFORE_HEADER'
,p_computation_type=>'FUNCTION_BODY'
,p_computation_language=>'PLSQL'
,p_computation=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_priv_count pls_integer;',
'begin',
'    select sum(priv)',
'      into l_priv_count',
'      from (select 1 as priv',
'              from all_credentials',
'             where credential_name  = ''OCI$RESOURCE_PRINCIPAL''',
'             union all',
'            select 1',
'              from user_role_privs',
'             where granted_role  = ''DWROLE'');',
'    ',
'    return ',
'        case ',
'            when nvl( l_priv_count, 0 ) < 2 ',
'            then ''Y''',
'            else ''N''',
'        end;',
'end;'))
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1893616195377720518)
,p_process_sequence=>80
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Download JSON'
,p_static_id=>'download-json'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'declare',
'    l_sql       varchar2( 32767 );',
'    l_context   pls_integer;',
'    l_data      sys.json_object_t;',
'    l_clob      clob;',
'    l_export    apex_data_export.t_export;',
'    l_static_id varchar2(100) := v(''P1_STATIC_ID'');',
'begin',
'',
'    select attribute_01 as sql_query,',
'           attribute_03 as filename',
'      into l_sql,',
'           l_export.file_name',
'      from apex_application_page_proc',
'     where page_id = 1',
'       and condition_expression1 = l_static_id;',
'',
'    l_context := apex_exec.open_query_context(',
'        p_location  => apex_exec.c_location_local_db,',
'        p_sql_query => l_sql );',
'',
'    if apex_exec.next_row( p_context => l_context ) then',
'',
'        l_data := sys.json_object_t( apex_exec.get_clob( l_context, 1 ) );',
'',
'        l_export.content_blob   := l_data.to_blob();',
'        l_export.format         := apex_data_export.c_format_json;',
'        l_export.mime_type      := ''application/json'';',
'',
'        apex_data_export.download(',
'            p_export    => l_export );',
'',
'    end if;',
'',
'end;'))
,p_process_clob_language=>'PLSQL'
,p_process_when=>'JSON'
,p_process_when_type=>'REQUEST_EQUALS_CONDITION'
,p_internal_uid=>34681176403474144
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1893615493975720511)
,p_process_sequence=>40
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'PLUGIN_COM.ORACLE.APEX.DOCGEN'
,p_process_name=>'Print Employees'
,p_static_id=>'print-employees'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', wwv_flow_string.join(wwv_flow_t_varchar2(
    'select json_object( ',
    '        ''currentDate''   value to_char( sysdate, ''DD MON YYYY'' ),',
    '        ''employees''     value',
    '            json_arrayagg( ',
    '                json_object(''name''      value e.ename,',
    '                           ''job''        value e.job,',
    '                           ''hiredate''   value to_char( e.hiredate, ''DD MON YYYY''),',
    '                           ''salary''     value e.sal,',
    '                           ''commission'' value nvl(e.comm,0),',
    '                           ''department'' value d.dname,',
    '                           ''location''   value d.loc,',
    '                           ''manager''    value nvl(m.ename,''-'') ) pretty ) ) as report_data',
    '  from eba_demo_dg_emp e',
    '  join eba_demo_dg_dept d',
    '    on e.deptno = d.deptno',
    '  left join eba_demo_dg_emp m',
    '    on e.mgr = m.empno')),
  'attribute_02', 'templates/employees.docx',
  'attribute_03', 'employees')).to_clob
,p_process_when=>'EMPLOYEES'
,p_process_when_type=>'REQUEST_EQUALS_CONDITION'
,p_internal_uid=>34680475001474137
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1858938301965284830)
,p_process_sequence=>70
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'PLUGIN_COM.ORACLE.APEX.DOCGEN'
,p_process_name=>'Print Employees per Department'
,p_static_id=>'print-employees-per-department'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', wwv_flow_string.join(wwv_flow_t_varchar2(
    'select json_serialize(',
    '                json_object(',
    '                    ''departments'' value ',
    '                        json_arrayagg(',
    '                            json_object(',
    '                                ''id'' value d.deptno,',
    '                                ''dname'' value d.dname,',
    '                                ''loc'' value d.loc,',
    '                                ''page'' value ''true'',',
    '                                ''employees'' value',
    '                                    (',
    '                                        select json_arrayagg(',
    '                                            json_object(',
    '                                                ''ename'' value e.ename,',
    '                                                ''job'' value e.job,',
    '                                                ''mgr'' value nvl( m.ename, ''-'' ),',
    '                                                ''hiredate'' value to_char( e.hiredate, ''DD MON YYYY''),',
    '                                                ''sal'' value e.sal,',
    '                                                ''comm'' value nvl( e.comm, 0 )',
    '                                            )',
    '                                        returning clob)',
    '                                        from eba_demo_dg_emp e',
    '                                        left join eba_demo_dg_emp m',
    '                                          on e.mgr = m.empno',
    '                                        where e.deptno = d.deptno',
    '                                    )',
    '                            returning clob)',
    '                        returning clob)',
    '                returning clob)',
    '            returning clob pretty) as data',
    'from eba_demo_dg_dept d',
    'where exists (select 1 ',
    '                from eba_demo_dg_emp ',
    '               where deptno = d.deptno)')),
  'attribute_02', 'templates/emp_per_dept.docx',
  'attribute_03', 'emp-per-dept')).to_clob
,p_process_when=>'EMP_PER_DEPT'
,p_process_when_type=>'REQUEST_EQUALS_CONDITION'
,p_internal_uid=>7675465400984308
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(1893616515450720521)
,p_process_sequence=>60
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'PLUGIN_COM.ORACLE.APEX.DOCGEN'
,p_process_name=>'Print Orders'
,p_static_id=>'print-orders'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', wwv_flow_string.join(wwv_flow_t_varchar2(
    'select json_object( ',
    '    ''order'' value',
    '    json_object(',
    '        ''id''        value o.order_id,',
    '        ''date''      value to_char(o.order_datetime, ''DD MON YYYY''),',
    '        ''customer''  value c.full_name,',
    '        ''email''     value c.email_address,',
    '        ''count''     value count(i.line_item_id),',
    '        ''items''     value json_arrayagg(',
    '            json_object (',
    '                ''id''            value i.line_item_id,',
    '                ''unitPrice''     value i.unit_price,',
    '                ''quantity''      value i.quantity,',
    '                ''total''         value (i.unit_price * i.quantity),',
    '                ''productName''   value p.product_name',
    '            )',
    '        order by i.line_item_id  ) )',
    '    ) as data',
    '  from eba_demo_dg_orders sample(1) o ',
    '  join eba_demo_dg_customers c',
    '    on c.customer_id = o.customer_id',
    '  join eba_demo_dg_order_items i',
    '    on i.order_id = o.order_id',
    '  join eba_demo_dg_products p',
    '    on i.product_id = p.product_id',
    ' group by o.order_id,',
    '       o.order_datetime,',
    '       c.full_name,',
    '       c.email_address')),
  'attribute_02', 'templates/customer-order.docx',
  'attribute_03', 'customer-order')).to_clob
,p_process_when=>'ORDER'
,p_process_when_type=>'REQUEST_EQUALS_CONDITION'
,p_internal_uid=>34681496476474147
);
wwv_flow_imp.component_end;
end;
/
