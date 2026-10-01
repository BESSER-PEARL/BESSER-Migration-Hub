prompt --application/pages/page_groups
begin
--   Manifest
--     PAGE GROUPS: 9110
--   Manifest End
wwv_flow_imp.component_begin (
 p_version_yyyy_mm_dd=>'2026.03.30'
,p_release=>'26.1.0'
,p_default_workspace_id=>20
,p_default_application_id=>9110
,p_default_id_offset=>14093677360354599
,p_default_owner=>'ORACLE'
);
wwv_flow_imp_page.create_page_group(
 p_id=>wwv_flow_imp.id(2629810413665037930)
,p_group_name=>'Administration'
,p_static_id=>'administration'
);
wwv_flow_imp.component_end;
end;
/
