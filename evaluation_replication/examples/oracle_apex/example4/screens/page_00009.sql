prompt --application/pages/page_00009
begin
--   Manifest
--     PAGE: 00009
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
 p_id=>9
,p_name=>'Create/Edit Tasks'
,p_alias=>'CREATE-EDIT-TASKS'
,p_step_title=>'Create/Edit Tasks'
,p_reload_on_submit=>'A'
,p_warn_on_unsaved_changes=>'N'
,p_first_item=>'AUTO_FIRST_ITEM'
,p_autocomplete_on_off=>'OFF'
,p_javascript_code=>wwv_flow_string.join(wwv_flow_t_varchar2(
'var htmldb_delete_message=''"DELETE_CONFIRM_MSG"'';',
'var htmldb_ch_message=''"OK_TO_GET_NEXT_PREV_PK_VALUE"'';'))
,p_step_template=>4073832297226169690
,p_page_template_options=>'#DEFAULT#'
,p_required_role=>'MUST_NOT_BE_PUBLIC_USER'
,p_protection_level=>'C'
,p_help_text=>'No help is available for this page.'
,p_page_component_map=>'02'
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3183726993191386258)
,p_plug_name=>'Breadcrumb'
,p_static_id=>'breadcrumb'
,p_region_template_options=>'#DEFAULT#:t-BreadcrumbRegion--useBreadcrumbTitle'
,p_component_template_options=>'#DEFAULT#'
,p_plug_template=>2532939663579242476
,p_plug_display_sequence=>1
,p_plug_display_point=>'REGION_POSITION_01'
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_menu_id=>wwv_flow_imp.id(7276395641541487089)
,p_plug_source_type=>'NATIVE_BREADCRUMB'
,p_menu_template_id=>4073839682315169711
);
wwv_flow_imp_page.create_page_plug(
 p_id=>wwv_flow_imp.id(3183733897638386716)
,p_plug_name=>'Create/Edit Tasks'
,p_static_id=>'create-edit-tasks'
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody:t-Region--hideHeader js-addHiddenHeadingRoleDesc'
,p_plug_template=>4073835273271169698
,p_plug_display_sequence=>10
,p_plug_item_display_point=>'ABOVE'
,p_location=>null
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'expand_shortcuts', 'N',
  'output_as', 'HTML')).to_clob
);
wwv_flow_imp_page.create_report_region(
 p_id=>wwv_flow_imp.id(3183793069707987542)
,p_name=>'Subtask Information'
,p_static_id=>'subtask-information'
,p_template=>4073835273271169698
,p_display_sequence=>20
,p_region_template_options=>'#DEFAULT#:t-Region--scrollBody'
,p_component_template_options=>'#DEFAULT#:t-Report--stretch:t-Report--altRowsDefault:t-Report--rowHighlight'
,p_source_type=>'NATIVE_SQL_REPORT'
,p_query_type=>'SQL'
,p_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select rowid, a.* from eba_demo_tree_subtask a',
'where a.task_id = :P9_TASK_ID',
'and a.proj_id = :P9_PROJ_ID'))
,p_display_when_condition=>'P9_TASK_ID'
,p_display_condition_type=>'ITEM_IS_NOT_NULL'
,p_ajax_enabled=>'Y'
,p_ajax_items_to_submit=>'P9_TASK_ID,P9_PROJ_ID'
,p_lazy_loading=>false
,p_query_row_template=>2540130677583398057
,p_query_num_rows=>15
,p_query_options=>'DERIVED_REPORT_COLUMNS'
,p_query_show_nulls_as=>' - '
,p_query_no_data_found=>'No subtasks found.'
,p_query_num_rows_type=>'NEXT_PREVIOUS_LINKS'
,p_query_row_count_max=>500
,p_pagination_display_position=>'BOTTOM_RIGHT'
,p_csv_output=>'N'
,p_prn_output=>'N'
,p_sort_null=>'L'
,p_plug_query_strip_html=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794274248987551)
,p_query_column_id=>11
,p_column_alias=>'CREATED'
,p_column_display_sequence=>11
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794785536987551)
,p_query_column_id=>16
,p_column_alias=>'CREATED_BY'
,p_column_display_sequence=>16
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793374377987551)
,p_query_column_id=>2
,p_column_alias=>'PROJ_ID'
,p_column_display_sequence=>2
,p_default_sort_column_sequence=>1
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183822889539750244)
,p_query_column_id=>1
,p_column_alias=>'ROWID'
,p_column_display_sequence=>1
,p_column_heading=>'Edit'
,p_column_link=>'f?p=&APP_ID.:10:&SESSION.::&DEBUG.::P10_ROWID,P10_PROJ_ID:#ROWID#,#PROJ_ID#'
,p_column_linktext=>'<img src="#IMAGE_PREFIX#menu/pencil2_16x16.gif" alt="Edit">'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794689767987551)
,p_query_column_id=>15
,p_column_alias=>'ROW_VERSION_NUMBER'
,p_column_display_sequence=>15
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794497020987551)
,p_query_column_id=>13
,p_column_alias=>'SUB_ASSIGN'
,p_column_display_sequence=>13
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793980789987551)
,p_query_column_id=>8
,p_column_alias=>'SUB_COMP'
,p_column_display_sequence=>8
,p_column_heading=>'Completed'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794594626987551)
,p_query_column_id=>14
,p_column_alias=>'SUB_DESC'
,p_column_display_sequence=>14
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793892212987551)
,p_query_column_id=>7
,p_column_alias=>'SUB_EST_COMP'
,p_column_display_sequence=>7
,p_column_heading=>'Estimated Completion'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793575164987551)
,p_query_column_id=>4
,p_column_alias=>'SUB_ID'
,p_column_display_sequence=>4
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793683408987551)
,p_query_column_id=>5
,p_column_alias=>'SUB_NAME'
,p_column_display_sequence=>5
,p_column_heading=>'Name'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794077434987551)
,p_query_column_id=>9
,p_column_alias=>'SUB_PRIORITY'
,p_column_display_sequence=>9
,p_column_heading=>'Priority'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793773032987551)
,p_query_column_id=>6
,p_column_alias=>'SUB_START'
,p_column_display_sequence=>6
,p_column_heading=>'Start'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794178713987551)
,p_query_column_id=>10
,p_column_alias=>'SUB_STATUS'
,p_column_display_sequence=>10
,p_column_heading=>'Status'
,p_heading_alignment=>'LEFT'
,p_derived_column=>'N'
,p_include_in_export=>'Y'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183793474742987551)
,p_query_column_id=>3
,p_column_alias=>'TASK_ID'
,p_column_display_sequence=>3
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794372085987551)
,p_query_column_id=>12
,p_column_alias=>'UPDATED'
,p_column_display_sequence=>12
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_report_columns(
 p_id=>wwv_flow_imp.id(3183794893266987551)
,p_query_column_id=>17
,p_column_alias=>'UPDATED_BY'
,p_column_display_sequence=>17
,p_hidden_column=>'Y'
,p_derived_column=>'N'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183734493702386718)
,p_button_sequence=>50
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'CANCEL'
,p_static_id=>'cancel'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Cancel'
,p_button_position=>'CLOSE'
,p_button_redirect_url=>'f?p=&APP_ID.:&LAST_VIEW.:&SESSION.::&DEBUG.:::'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183734080900386718)
,p_button_sequence=>30
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'CREATE'
,p_static_id=>'create'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Create'
,p_button_position=>'CREATE'
,p_button_condition=>'P9_TASK_ID'
,p_button_condition_type=>'ITEM_IS_NULL'
,p_database_action=>'INSERT'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183749394171386799)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3183793069707987542)
,p_button_name=>'CREATE_SUBTASK'
,p_static_id=>'create-subtask'
,p_button_action=>'REDIRECT_PAGE'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Create Subtask'
,p_button_position=>'CREATE'
,p_button_redirect_url=>'f?p=&APP_ID.:10:&SESSION.::&DEBUG.:10:P10_PROJ_ID,P10_TASK_ID:&P9_PROJ_ID.,&P9_TASK_ID.'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183734269693386718)
,p_button_sequence=>40
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'DELETE'
,p_static_id=>'delete'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#:t-Button--simple:t-Button--danger'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'Delete'
,p_button_position=>'DELETE'
,p_button_redirect_url=>'javascript:apex.confirm(htmldb_delete_message,''DELETE'');'
,p_button_execute_validations=>'N'
,p_button_condition=>'P9_TASK_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'DELETE'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183740288026386745)
,p_button_sequence=>10
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'GET_NEXT_TASK_ID'
,p_static_id=>'get-next-task-id'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'&gt;'
,p_button_position=>'NEXT'
,p_button_redirect_url=>'javascript:htmldb_goSubmit(''GET_NEXT_TASK_ID'')'
,p_button_condition=>'P9_TASK_ID_NEXT'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_button_comment=>'This button is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183740394113386745)
,p_button_sequence=>60
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'GET_PREVIOUS_TASK_ID'
,p_static_id=>'get-previous-task-id'
,p_button_action=>'REDIRECT_URL'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_image_alt=>'&lt;'
,p_button_position=>'PREVIOUS'
,p_button_redirect_url=>'javascript:htmldb_goSubmit(''GET_PREVIOUS_TASK_ID'')'
,p_button_condition=>'P9_TASK_ID_PREV'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_button_comment=>'This button is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_button(
 p_id=>wwv_flow_imp.id(3183734180306386718)
,p_button_sequence=>20
,p_button_plug_id=>wwv_flow_imp.id(3183726993191386258)
,p_button_name=>'SAVE'
,p_static_id=>'save'
,p_button_action=>'SUBMIT'
,p_button_template_options=>'#DEFAULT#'
,p_button_template_id=>4073839297780169708
,p_button_is_hot=>'Y'
,p_button_image_alt=>'Apply Changes'
,p_button_position=>'CREATE'
,p_button_condition=>'P9_TASK_ID'
,p_button_condition_type=>'ITEM_IS_NOT_NULL'
,p_database_action=>'UPDATE'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(3183734996044386721)
,p_branch_action=>'f?p=&APP_ID.:&LAST_VIEW.:&SESSION.::&DEBUG.:::&success_msg=#SUCCESS_MSG#'
,p_branch_point=>'AFTER_PROCESSING'
,p_branch_type=>'REDIRECT_URL'
,p_branch_sequence=>30
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(3183743579319386762)
,p_branch_action=>'f?p=&APP_ID.:9:&SESSION.::&DEBUG.::P9_TASK_ID:&P9_TASK_ID_NEXT.'
,p_branch_point=>'BEFORE_COMPUTATION'
,p_branch_type=>'REDIRECT_URL'
,p_branch_when_button_id=>wwv_flow_imp.id(3183740288026386745)
,p_branch_sequence=>10
,p_branch_comment=>'This button is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_branch(
 p_id=>wwv_flow_imp.id(3183743770801386762)
,p_branch_action=>'f?p=&APP_ID.:9:&SESSION.::&DEBUG.::P9_TASK_ID:&P9_TASK_ID_PREV.'
,p_branch_point=>'BEFORE_COMPUTATION'
,p_branch_type=>'REDIRECT_URL'
,p_branch_when_button_id=>wwv_flow_imp.id(3183740394113386745)
,p_branch_sequence=>20
,p_branch_comment=>'This button is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183735395619386734)
,p_name=>'P9_PROJ_ID'
,p_is_required=>true
,p_item_sequence=>20
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Project:'
,p_source=>'PROJ_ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'PROJECTS'
,p_cHeight=>1
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183737168737386740)
,p_name=>'P9_TASK_ASSIGN'
,p_item_sequence=>110
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Task Assign'
,p_source=>'TASK_ASSIGN'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>255
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183736174521386735)
,p_name=>'P9_TASK_COMP'
,p_item_sequence=>60
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Completed'
,p_source=>'TASK_COMP'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183737373754386740)
,p_name=>'P9_TASK_DESC'
,p_item_sequence=>120
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Details'
,p_source=>'TASK_DESC'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXTAREA'
,p_cSize=>64
,p_cMaxlength=>32000
,p_cHeight=>4
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'auto_height', 'N',
  'character_counter', 'N',
  'resizable', 'N',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183735980282386735)
,p_name=>'P9_TASK_EST_COMP'
,p_item_sequence=>50
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Estimated Completion'
,p_source=>'TASK_EST_COMP'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183735186561386726)
,p_name=>'P9_TASK_ID'
,p_item_sequence=>10
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_source=>'TASK_ID'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183742970886386754)
,p_name=>'P9_TASK_ID_COUNT'
,p_item_sequence=>180
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
,p_item_comment=>'This item is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183742578274386753)
,p_name=>'P9_TASK_ID_NEXT'
,p_item_sequence=>160
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
,p_item_comment=>'This item is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183742777859386754)
,p_name=>'P9_TASK_ID_PREV'
,p_item_sequence=>170
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_source_type=>'ALWAYS_NULL'
,p_display_as=>'NATIVE_HIDDEN'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'value_protected', 'Y')).to_clob
,p_item_comment=>'This item is needed for Get Next or Previous Primary Key Value process.'
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183735579636386734)
,p_name=>'P9_TASK_NAME'
,p_is_required=>true
,p_item_sequence=>5
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Task Name'
,p_source=>'TASK_NAME'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_TEXT_FIELD'
,p_cSize=>64
,p_cMaxlength=>4000
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2528236951996823187
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'disabled', 'N',
  'submit_when_enter_pressed', 'N',
  'subtype', 'TEXT',
  'trim_spaces', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183736381611386735)
,p_name=>'P9_TASK_PRIORITY'
,p_item_sequence=>70
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Priority'
,p_source=>'TASK_PRIORITY'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'PRIORITY'
,p_lov_display_null=>'YES'
,p_lov_null_text=>'- None -'
,p_cHeight=>1
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'YES'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183735781369386735)
,p_name=>'P9_TASK_START'
,p_item_sequence=>40
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_prompt=>'Start Date'
,p_source=>'TASK_START'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_DATE_PICKER_APEX'
,p_cSize=>64
,p_cMaxlength=>255
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'display_as', 'POPUP',
  'max_date', 'NONE',
  'min_date', 'NONE',
  'multiple_months', 'N',
  'show_time', 'N',
  'use_defaults', 'Y')).to_clob
);
wwv_flow_imp_page.create_page_item(
 p_id=>wwv_flow_imp.id(3183736598058386736)
,p_name=>'P9_TASK_STATUS'
,p_item_sequence=>80
,p_item_plug_id=>wwv_flow_imp.id(3183733897638386716)
,p_use_cache_before_default=>'NO'
,p_item_default=>'0'
,p_prompt=>'Status'
,p_source=>'TASK_STATUS'
,p_source_type=>'DB_COLUMN'
,p_display_as=>'NATIVE_SELECT_LIST'
,p_named_lov=>'STATUS'
,p_cHeight=>1
,p_tag_attributes=>'onchange="htmldb_item_change(this)"'
,p_field_template=>2320077351817916916
,p_item_template_options=>'#DEFAULT#'
,p_lov_display_extra=>'NO'
,p_protection_level=>'S'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'page_action_on_selection', 'NONE')).to_clob
);
wwv_flow_imp_page.create_page_computation(
 p_id=>wwv_flow_imp.id(3183749570671386799)
,p_computation_sequence=>1
,p_computation_item=>'P10_ROWID'
,p_static_id=>'p10-rowid'
,p_computation_type=>'STATIC_ASSIGNMENT'
,p_compute_when=>'CREATE'
,p_compute_when_type=>'REQUEST_EQUALS_CONDITION'
);
wwv_flow_imp_page.create_page_validation(
 p_id=>wwv_flow_imp.id(3183987473681819455)
,p_validation_name=>'Completion Date Required'
,p_static_id=>'completion-date-required'
,p_validation_sequence=>10
,p_validation=>'P9_TASK_COMP'
,p_validation_type=>'ITEM_NOT_NULL'
,p_error_message=>'#LABEL# must be specified when status is set to 100%.'
,p_validation_condition=>'P9_TASK_STATUS'
,p_validation_condition2=>'100'
,p_validation_condition_type=>'VAL_OF_ITEM_IN_COND_EQ_COND2'
,p_when_button_pressed=>wwv_flow_imp.id(3183734080900386718)
,p_associated_item=>wwv_flow_imp.id(3183736174521386735)
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183739784727386744)
,p_process_sequence=>10
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_FETCH'
,p_process_name=>'Fetch Row from EBA_DEMO_TREE_TASK'
,p_static_id=>'fetch-row-from-eba-demo-tree-task'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'primary_key_column', 'TASK_ID',
  'primary_key_item', 'P9_TASK_ID',
  'table_name', 'EBA_DEMO_TREE_TASK')).to_clob
,p_internal_uid=>3170835600432658361
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183743366318386762)
,p_process_sequence=>20
,p_process_point=>'AFTER_HEADER'
,p_process_type=>'NATIVE_FORM_PAGINATION'
,p_process_name=>'Get Next or Previous Primary Key Value'
,p_static_id=>'get-next-or-previous-primary-key-value'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'current_row_count_item', 'P9_TASK_ID_COUNT',
  'next_primary_key_item', 'P9_TASK_ID_NEXT',
  'previous_primary_key_item', 'P9_TASK_ID_PREV',
  'primary_key_column', 'TASK_ID',
  'primary_key_item', 'P9_TASK_ID',
  'table_name', 'EBA_DEMO_TREE_TASK')).to_clob
,p_internal_uid=>3170839182023658379
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183739971068386745)
,p_process_sequence=>30
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_FORM_PROCESS'
,p_process_name=>'Process Row of EBA_DEMO_TREE_TASK'
,p_static_id=>'process-row-of-eba-demo-tree-task'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'lock_row', 'Y',
  'primary_key_column', 'TASK_ID',
  'primary_key_item', 'P9_TASK_ID',
  'supported_operations', 'I:U:D',
  'table_name', 'EBA_DEMO_TREE_TASK')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_success_message=>'Action Processed.'
,p_internal_uid=>3170835786773658362
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3183740179414386745)
,p_process_sequence=>40
,p_process_point=>'AFTER_SUBMIT'
,p_process_type=>'NATIVE_SESSION_STATE'
,p_process_name=>'reset page'
,p_static_id=>'reset-page'
,p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(
  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob
,p_error_display_location=>'INLINE_IN_NOTIFICATION'
,p_process_when_button_id=>wwv_flow_imp.id(3183734269693386718)
,p_internal_uid=>3170835995119658362
);
wwv_flow_imp_page.create_page_process(
 p_id=>wwv_flow_imp.id(3187512684128739554)
,p_process_sequence=>50
,p_process_point=>'BEFORE_HEADER'
,p_process_type=>'NATIVE_PLSQL'
,p_process_name=>'Set Page Navigation'
,p_static_id=>'set-page-navigation'
,p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(
'if :REQUEST = ''T'' then ',
'    :LAST_VIEW := 3;',
'else',
'    :LAST_VIEW := 8;',
'end if;'))
,p_process_clob_language=>'PLSQL'
,p_internal_uid=>3174608499834011171
);
wwv_flow_imp.component_end;
end;
/
