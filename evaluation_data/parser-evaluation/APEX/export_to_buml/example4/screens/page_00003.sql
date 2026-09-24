prompt --application/pages/page_00003
begin
--   Manifest
--     PAGE: 00003
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>7910
,p_default_id_offset=>12904184294728383
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page(
 p_id=>3
,p_name=>'Project Tracking'
,p_alias=>'PROJECT-TRACKING'
,p_step_title=>'Project Tracking'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'ON'
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'17'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3180805570994336933)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>10
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(7276395641541487089)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(1333121074445950221)
,p_plug_name=>'SQL Source'
,p_static_id=>'sql-source'
,p_region_template_options=>'#DEFAULT#:is-collapsed:t-Region--noBorder:t-Region--scrollBody'
,p_plug_template=>2665811232373458102
,p_plug_display_sequence=>30
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_plug_source_type=>'PLUGIN_COM.ORACLE.APEX.DISPLAY_SOURCE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'attribute_01', 'task_tree')).to_clob
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3183931168300835166)
,p_plug_name=>'Task_Tracking_Tabs'
,p_static_id=>'task-tracking-tabs'
,p_region_template_options=>'#DEFAULT#:t-Region--noPadding:t-Region--scrollBody:t-Region--hideHeader js-addHiddenHeadingRoleDesc'
,p_component_template_options=>'#DEFAULT#:t-MediaList--cols t-MediaList--2cols'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_list_id=>wwv_flow_imp.id(3183930372868835147)
,p_plug_source_type=>'NATIVE_LIST'
,p_list_template_id=>2069471208528591807
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3171018478566341311)
,p_plug_name=>'Task Tree'
,p_static_id=>'task-tree'
,p_region_name=>'task_tree'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>20
,p_plug_new_grid_row=>false
,p_plug_new_grid_column=>false
,p_plug_item_display_point=>'ABOVE'
,p_query_type=>'SQL'
,p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select case when connect_by_isleaf = 1 then 0',
'            when level = 1             then 1',
'            else                           -1',
'       end as status, ',
'       level, ',
'       label||'': ''||name as title, ',
'       case when item_type = ''P'' then ''fa-file-text-o''',
'            when item_type = ''S'' then ''fa-caret-square-o-right''',
'            when item_type = ''T'' then ''fa-minus-square-o''',
'       else null',
'       end as icon, ',
'       id as value, ',
'       case when tooltip is not null then name||'' - ''||tooltip||''% complete''',
'            else name',
'       end as tooltip,',
'       case when item_type = ''P'' then ',
'               apex_util.prepare_url(''f?p=''||:app_id||'':7:''||:app_session||'':T:::P3_SELECTED_NODE,P7_PROJ_ID:''||id||'',''||id)',
'            when item_type = ''T'' then',
'               apex_util.prepare_url(''f?p=''||:app_id||'':9:''||:app_session||'':T:::P3_SELECTED_NODE,P9_PROJ_ID,P9_TASK_ID:''||id||'',''||link)',
'            when item_type = ''S'' then ',
'               apex_util.prepare_url(''f?p=''||:app_id||'':10:''||:app_session||'':T:::P3_SELECTED_NODE,P10_PROJ_ID,P10_ROWID:''||id||'',''||link)',
'       end as link ',
' from (',
'select ''P'' item_type,',
'       t.label label,',
'       to_char(a.PROJ_ID) id,',
'       null parent,',
'       a.project_name name,',
'       a.status tooltip,',
'       null link',
'  from eba_demo_tree_projects a, (select wwv_flow_lang.system_message(''PROJECT'') label from dual) t',
'union all',
'select ''T'' item_type,',
'       u.label label,',
'       to_char(b.proj_id)||''-''||to_char(b.task_id) id,',
'       to_char(b.proj_id) parent,',
'       b.task_name name,',
'       null tooltip,',
'       b.proj_id||'',''||b.task_id link',
'  from eba_demo_tree_task b, (select wwv_flow_lang.system_message(''TASK'') label from dual) u',
'union all',
'select ''S'' item_type,',
'       v.label label,',
'       to_char(c.proj_id)||''-''||to_char(c.task_id)||''-''||to_char(c.sub_id) id,',
'       to_char(c.proj_id)||''-''||to_char(c.task_id) parent,',
'       c.sub_name name,',
'       null tooltip,',
'       c.proj_id||'',''||c.rowid link',
'  from eba_demo_tree_subtask c, (select wwv_flow_lang.system_message(''SUBTASK'') label from dual) v',
')',
'start with parent is null',
'connect by prior id = parent',
'order siblings by name'))
,p_lazy_loading=>false
,p_plug_source_type=>'NATIVE_JSTREE'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'activate_node_link_with', 'S',
  'hierarchy_level_column', 'LEVEL',
  'icon_css_class_column', 'ICON',
  'icon_type_css_class', 'fa',
  'link_column', 'LINK',
  'node_label_column', 'TITLE',
  'node_status_column', 'STATUS',
  'node_value_column', 'VALUE',
  'selected_node_page_item', 'P3_SELECTED_NODE',
  'static_tree_id', 'projTrackTree',
  'tooltip_column', 'TOOLTIP',
  'tree_hierarchy', 'LEVEL',
  'tree_tooltip', 'DB')).to_clob
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3171018877726341313)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3171018478566341311)
,p_button_name=>'CONTRACT_ALL'
,p_static_id=>'contract-all'
,p_button_action=>'DEFINED_BY_DA'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Collapse All'
,p_button_position=>'EDIT'
,p_warn_on_unsaved_changes=>null
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3171019078165341313)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(3171018478566341311)
,p_button_name=>'EXPAND_ALL'
,p_static_id=>'expand-all'
,p_button_action=>'DEFINED_BY_DA'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Expand All'
,p_button_position=>'EDIT'
,p_warn_on_unsaved_changes=>null
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3188250668833912139)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(3171018478566341311)
,p_button_name=>'RESET_TREE'
,p_static_id=>'reset-tree'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#:t-Button--iconLeft'
,p_button_template_id=>2084305881903810008
,p_button_image_alt=>'Reset Tree'
,p_button_position=>'EDIT'
,p_button_redirect_url=>'f?p=&APP_ID.:3:&SESSION.::&DEBUG.:3::'
,p_icon_css_classes=>'fa-undo-alt'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3180800795170164108)
,p_name=>'P3_SELECTED_NODE'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3171018478566341311)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(1510585351183552330)
,p_name=>'collapse'
,p_static_id=>'collapse'
,p_event_sequence=>10
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(3171018877726341313)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(1510585449348552331)
,p_event_id=>wwv_flow_imp.id(1510585351183552330)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-tree-collapse'
,p_action=>'NATIVE_TREE_COLLAPSE'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(3171018478566341311)
);
wwv_flow_imp_page.create_page_da_event(
 p_id=>wwv_flow_imp.id(1510585480632552332)
,p_name=>'expand'
,p_static_id=>'expand'
,p_event_sequence=>20
,p_triggering_element_type=>'BUTTON'
,p_triggering_button_id=>wwv_flow_imp.id(3171019078165341313)
,p_bind_type=>'bind'
,p_execution_type=>'IMMEDIATE'
,p_bind_event_type=>'click'
);
wwv_flow_imp_page.create_page_da_action(
 p_id=>wwv_flow_imp.id(1510585577491552333)
,p_event_id=>wwv_flow_imp.id(1510585480632552332)
,p_event_result=>'TRUE'
,p_action_sequence=>10
,p_execute_on_page_init=>'N'
,p_static_id=>'native-tree-expand'
,p_action=>'NATIVE_TREE_EXPAND'
,p_affected_elements_type=>'REGION'
,p_affected_region_id=>wwv_flow_imp.id(3171018478566341311)
);
wwv_flow_imp.component_end;
end;
/
