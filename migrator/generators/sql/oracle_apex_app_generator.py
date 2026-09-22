"""Oracle APEX Full Application Generator for BESSER B-UML domain models.

Produces a single self-contained SQL file that:

1. Creates all tables (plain DDL, identical to OracleApexSQLGenerator output).
2. Creates a complete Oracle APEX application with:
   - APEX Accounts authentication
   - Side-navigation menu with one entry per entity
   - Global page (0) and home page (1)
   - Interactive-report list page per class (even page numbers: 2, 4, 6, …)
   - Modal form page per class (odd page numbers: 3, 5, 7, …) with
     Create / Apply Changes / Delete buttons and NATIVE_FORM_DML auto-DML.

Usage
-----
Run the generated ``oracle_apex_app.sql`` file in Oracle APEX SQL Workshop →
SQL Scripts (or import it via App Builder → Import → Application).  No prior
APEX application export is required.
"""
from __future__ import annotations

import os
import random
import re
from typing import Optional

from besser.BUML.metamodel.structural import DomainModel, Class

from .oracle_apex_sql_generator import OracleApexSQLGenerator


class OracleApexFullAppGenerator:
    """Generate a self-contained APEX application SQL from a B-UML DomainModel."""

    APEX_VERSION = "2024.11.30"
    APEX_RELEASE = "24.2.6"

    # Universal Theme 42 template IDs — applied on import by App Builder.
    _BTN_TMPL   = 4073839297780169708
    _FIELD_TMPL = 1610598484065263269   # Optional / Required label above

    def __init__(
        self,
        model: DomainModel,
        gui_model=None,
        output_dir: str = None,
        output_filename: str = "oracle_apex_app.sql",
        app_id: Optional[int] = None,
        app_name: Optional[str] = None,
    ):
        self.model = model
        self.gui_model = gui_model
        self.output_dir = output_dir or os.getcwd()
        self.output_filename = output_filename
        # Pick a random ID in the 1000–9000 range when none is supplied so
        # successive imports don't collide with each other or with samples.
        self.app_id = app_id if app_id is not None else random.randint(1000, 9000)
        self.app_name = app_name or (model.name or "Generated_App")
        # Large random ID offset — mirrors real APEX exports (e.g. 43061406402105851).
        # Added to every wwv_flow_imp.id(N) call so component IDs are globally
        # unique and don't collide with leftover metadata from previous imports.
        self._id_offset = random.randint(10**14, 10**17)

        self._ddl = OracleApexSQLGenerator(model, output_dir, "_tmp_ddl.sql")

        # ID counter — each call to _uid() returns a unique large integer.
        self._ctr = 1_000_000
        self._auth_id = self._uid()
        self._nav_list_id = self._uid()
        self._nav_bar_list_id = self._uid()

    # ── ID helpers ────────────────────────────────────────────────────────────

    def _uid(self) -> int:
        self._ctr += 1000
        return self._ctr

    def _wid(self, n: int) -> str:
        return f"wwv_flow_imp.id({n})"

    # ── Block wrappers ────────────────────────────────────────────────────────

    def _comp_begin(self) -> str:
        return (
            "begin\n"
            "wwv_flow_imp.component_begin (\n"
            f" p_version_yyyy_mm_dd=>'{self.APEX_VERSION}'\n"
            f",p_release=>'{self.APEX_RELEASE}'\n"
            ",p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)\n"
            f",p_default_application_id=>{self.app_id}\n"
            f",p_default_id_offset=>{self._id_offset}\n"
            ",p_default_owner=>USER\n"
            ");\n"
        )

    @staticmethod
    def _comp_end() -> str:
        return "wwv_flow_imp.component_end;\nend;\n/\n\n"

    # ── Model helpers ─────────────────────────────────────────────────────────

    def _classes(self) -> list[Class]:
        try:
            classes = list(self.model.classes_sorted_by_inheritance())
        except Exception:
            from besser.BUML.metamodel.structural import Class as _Class
            classes = [t for t in self.model.types if isinstance(t, _Class)]
        return classes

    def _tbl(self, name: str) -> str:
        return self._ddl._table_name(name).upper()

    def _col(self, name: str) -> str:
        return self._ddl._col_name(name).upper()

    # ── DDL section ───────────────────────────────────────────────────────────

    def _ddl_section(self) -> str:
        lines: list[str] = [
            "--",
            "-- SECTION 1: TABLE DDL",
            "--",
            "",
        ]

        enum_map = self._ddl._get_enum_map()
        classes = list(self.model.classes_sorted_by_inheritance())
        class_names = {c.name for c in classes}
        fk_map, nm_tables = self._ddl._compute_fk_columns(class_names)
        sorted_cls = self._ddl._topo_sort(classes, fk_map)

        lines.extend(self._ddl._drop_section(sorted_cls, nm_tables))
        lines += ["--------------------------------------------------",
                  "-- TABLES",
                  "--------------------------------------------------", ""]

        for cls in sorted_cls:
            tname = self._tbl(cls.name)
            parent = self._ddl._find_parent(cls)
            parent_tname = self._tbl(parent.name) if parent else None

            col_defs = ["    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY"]
            fk_cols: list[str] = []
            constraints: list[str] = []

            if parent is not None:
                pfk = f"{parent_tname.lower()}_id"
                fk_cols.append(f"    {pfk} NUMBER NOT NULL")
                constraints.append(f"    FOREIGN KEY ({pfk}) REFERENCES {parent_tname}(id)")

            for attr in sorted(cls.attributes, key=lambda a: a.name):
                cname = self._col(attr.name)
                if cname == 'ID':
                    continue  # already the identity PK
                tname_lower = tname.lower()
                ttype = attr.type.name
                nn = "" if attr.is_optional else " NOT NULL"

                if ttype == "bool":
                    col_defs.append(f"    {cname} NUMBER(1) DEFAULT 0{nn}")
                    constraints.append(
                        f"    CONSTRAINT chk_{tname_lower}_{cname} CHECK ({cname} IN (0, 1))"
                    )
                elif ttype in enum_map:
                    vals = enum_map[ttype]
                    mlen = max((len(v) for v in vals), default=20)
                    col_defs.append(f"    {cname} VARCHAR2({max(mlen + 4, 20)}){nn}")
                    vs = ", ".join(f"'{v}'" for v in vals)
                    constraints.append(
                        f"    CONSTRAINT chk_{tname_lower}_{cname} CHECK ({cname} IN ({vs}))"
                    )
                else:
                    col_defs.append(f"    {cname} {self._ddl._col_type(ttype, enum_map)}{nn}")

            seen: set = set()
            for fk_col, ref_tbl, is_uniq in fk_map.get(cls.name, []):
                key = (fk_col, ref_tbl)
                if key in seen:
                    continue
                seen.add(key)
                fk_cols.append(f"    {fk_col} NUMBER NOT NULL")
                constraints.append(f"    FOREIGN KEY ({fk_col}) REFERENCES {ref_tbl}(id)")
                if is_uniq:
                    constraints.append(
                        f"    CONSTRAINT uq_{tname.lower()}_{fk_col} UNIQUE ({fk_col})"
                    )

            all_cols = col_defs + fk_cols + constraints
            lines += [f"-- {cls.name}", f"CREATE TABLE {tname} (", ",\n".join(all_cols), ");", ""]

        seen_jct: set = set()
        for t1, t2, c1, c2 in nm_tables:
            jn = f"{t1}_{t2}"
            if jn in seen_jct:
                continue
            seen_jct.add(jn)
            lines += [
                f"CREATE TABLE {jn} (",
                f"    {c1} NUMBER NOT NULL,",
                f"    {c2} NUMBER NOT NULL,",
                f"    PRIMARY KEY ({c1}, {c2}),",
                f"    FOREIGN KEY ({c1}) REFERENCES {t1}(id),",
                f"    FOREIGN KEY ({c2}) REFERENCES {t2}(id)",
                ");", "",
            ]

        return "\n".join(lines) + "\n"

    # ── APEX envelope ─────────────────────────────────────────────────────────

    def _set_environment(self) -> str:
        return (
            "--\n"
            "-- APEX APPLICATION\n"
            "-- Import via App Builder → Import → Application.\n"
            "-- Tables are created by the Supporting Objects install script\n"
            "-- embedded at the end of this file.\n"
            "--\n\n"
            "prompt --application/set_environment\n"
            "set define off verify off feedback off\n"
            "whenever sqlerror exit sql.sqlcode rollback\n"
            "begin\n"
            "wwv_flow_imp.import_begin (\n"
            f" p_version_yyyy_mm_dd=>'{self.APEX_VERSION}'\n"
            f",p_release=>'{self.APEX_RELEASE}'\n"
            ",p_default_workspace_id=>nvl(wwv_flow_application_install.get_workspace_id,0)\n"
            f",p_default_application_id=>nvl(wwv_flow_application_install.get_application_id,{self.app_id})\n"
            f",p_default_id_offset=>{self._id_offset}\n"
            ",p_default_owner=>USER\n"
            ");\n"
            "wwv_flow.g_import_in_progress := true;\n"
            f"wwv_flow.g_flow_id := nvl(wwv_flow_application_install.get_application_id,{self.app_id});\n"
            "end;\n"
            "/\n\n"
        )

    def _end_environment(self) -> str:
        return (
            "prompt --application/end_environment\n"
            "begin\n"
            "wwv_flow_imp.import_end(\n"
            "  p_auto_install_sup_obj => nvl(\n"
            "    wwv_flow_application_install.get_auto_install_sup_obj, false));\n"
            "commit;\n"
            "end;\n"
            "/\n"
            "set verify on feedback on define on\n"
            "prompt  ...done\n"
        )

    # ── Authentication ─────────────────────────────────────────────────────────

    def _authentication(self) -> str:
        lines = [
            "prompt --application/shared_components/security/authentications/apex_accounts",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_authentication(",
            f" p_id=>{self._wid(self._auth_id)}",
            ",p_name=>'Application Express Accounts'",
            ",p_static_id=>'apex-accounts'",
            ",p_scheme_type=>'NATIVE_APEX_ACCOUNTS'",
            ",p_invalid_session_type=>'LOGIN'",
            ",p_logout_url=>'f?p=&APP_ID.:1:&SESSION.'",
            ",p_use_secure_cookie_yn=>'N'",
            ",p_ras_mode=>0",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    def _login_page(self) -> str:
        """Page 101 (alias LOGIN) — required by NATIVE_APEX_ACCOUNTS.

        Template IDs are intentionally omitted (p_step_template, p_plug_template)
        so APEX uses its workspace defaults instead of hardcoded IDs from a
        different workspace that would cause ORA-01403 at render time.
        Button and field templates reuse the same constants as the rest of the app.
        """
        region_uid = self._uid()
        button_uid = self._uid()
        usr_item_uid = self._uid()
        pwd_item_uid = self._uid()
        proc_get_cookie_uid = self._uid()
        proc_set_cookie_uid = self._uid()
        proc_login_uid = self._uid()
        proc_clear_uid = self._uid()

        lines = [
            "prompt --application/pages/page_00101",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            " p_id=>101",
            ",p_name=>'Login'",
            ",p_alias=>'LOGIN'",
            ",p_step_title=>'Sign In'",
            ",p_reload_on_submit=>'A'",
            ",p_warn_on_unsaved_changes=>'N'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_step_template=>2102634289808461002",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_page_is_public_y_n=>'Y'",
            ",p_protection_level=>'C'",
            ",p_page_component_map=>'16'",
            ");",
            "wwv_flow_imp_page.create_page_plug(",
            f" p_id=>{self._wid(region_uid)}",
            f",p_plug_name=>'{self.app_name.replace(chr(39), chr(39)+chr(39))}'",
            ",p_region_template_options=>'#DEFAULT#'",
            ",p_plug_template=>2675634334296186762",
            ",p_plug_display_sequence=>10",
            ",p_plug_item_display_point=>'ABOVE'",
            ",p_location=>null",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'expand_shortcuts', 'N',",
            "  'output_as', 'HTML')).to_clob",
            ");",
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(button_uid)}",
            ",p_button_sequence=>10",
            f",p_button_plug_id=>{self._wid(region_uid)}",
            ",p_button_name=>'LOGIN'",
            ",p_button_action=>'SUBMIT'",
            ",p_button_template_options=>'#DEFAULT#'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_is_hot=>'Y'",
            ",p_button_image_alt=>'Sign In'",
            ",p_button_position=>'NEXT'",
            ");",
            "wwv_flow_imp_page.create_page_item(",
            f" p_id=>{self._wid(usr_item_uid)}",
            ",p_name=>'P101_USERNAME'",
            ",p_is_required=>true",
            ",p_item_sequence=>10",
            f",p_item_plug_id=>{self._wid(region_uid)}",
            ",p_prompt=>'Username'",
            ",p_placeholder=>'username'",
            ",p_source_type=>'ALWAYS_NULL'",
            ",p_display_as=>'NATIVE_TEXT_FIELD'",
            ",p_cSize=>64",
            ",p_cMaxlength=>100",
            ",p_field_template=>2042262243893469891",
            ",p_item_template_options=>'#DEFAULT#'",
            ",p_restricted_characters=>'WEB_SAFE'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'disabled', 'N',",
            "  'submit_when_enter_pressed', 'N',",
            "  'subtype', 'TEXT',",
            "  'trim_spaces', 'NONE')).to_clob",
            ");",
            "wwv_flow_imp_page.create_page_item(",
            f" p_id=>{self._wid(pwd_item_uid)}",
            ",p_name=>'P101_PASSWORD'",
            ",p_is_required=>true",
            ",p_item_sequence=>20",
            f",p_item_plug_id=>{self._wid(region_uid)}",
            ",p_prompt=>'Password'",
            ",p_placeholder=>'password'",
            ",p_source_type=>'ALWAYS_NULL'",
            ",p_display_as=>'NATIVE_PASSWORD'",
            ",p_cSize=>64",
            ",p_cMaxlength=>100",
            ",p_field_template=>2042262243893469891",
            ",p_item_template_options=>'#DEFAULT#'",
            ",p_is_persistent=>'N'",
            ",p_restricted_characters=>'WEB_SAFE'",
            ",p_encrypt_session_state_yn=>'N'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'submit_when_enter_pressed', 'Y')).to_clob",
            ");",
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(proc_get_cookie_uid)}",
            ",p_process_sequence=>10",
            ",p_process_point=>'BEFORE_HEADER'",
            ",p_process_type=>'NATIVE_PLSQL'",
            ",p_process_name=>'Get Username Cookie'",
            ",p_process_sql_clob=>':P101_USERNAME := apex_authentication.get_login_username_cookie;'",
            ",p_process_clob_language=>'PLSQL'",
            ");",
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(proc_set_cookie_uid)}",
            ",p_process_sequence=>10",
            ",p_process_point=>'AFTER_SUBMIT'",
            ",p_process_type=>'NATIVE_PLSQL'",
            ",p_process_name=>'Set Username Cookie'",
            ",p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(",
            "  'apex_authentication.send_login_username_cookie (',",
            "  '    p_username => lower(:P101_USERNAME) );'))",
            ",p_process_clob_language=>'PLSQL'",
            ",p_error_display_location=>'INLINE_IN_NOTIFICATION'",
            ");",
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(proc_login_uid)}",
            ",p_process_sequence=>20",
            ",p_process_point=>'AFTER_SUBMIT'",
            ",p_process_type=>'NATIVE_PLSQL'",
            ",p_process_name=>'Login'",
            ",p_process_sql_clob=>wwv_flow_string.join(wwv_flow_t_varchar2(",
            "  'apex_authentication.login(',",
            "  '    p_username => :P101_USERNAME,',",
            "  '    p_password => :P101_PASSWORD );'))",
            ",p_process_clob_language=>'PLSQL'",
            ",p_error_display_location=>'INLINE_IN_NOTIFICATION'",
            ");",
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(proc_clear_uid)}",
            ",p_process_sequence=>30",
            ",p_process_point=>'AFTER_SUBMIT'",
            ",p_process_type=>'NATIVE_SESSION_STATE'",
            ",p_process_name=>'Clear Page(s) Cache'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'type', 'CLEAR_CACHE_CURRENT_PAGE')).to_clob",
            ",p_error_display_location=>'INLINE_IN_NOTIFICATION'",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    # ── Theme ──────────────────────────────────────────────────────────────────

    def _theme(self) -> str:
        """Subscribe the app to Universal Theme 42.

        Without this block APEX has no template mappings for the app, causing
        ORA-01403 at WWV_FLOW_THEME line 702 the moment any page renders.
        Template IDs here are Universal Theme blueprint IDs; the
        wwv_imp_util.get_subscription_id() call in p_reference_id translates
        them to workspace-local IDs at import time.
        """
        style_id = self._uid()
        theme_id = self._uid()
        lines = [
            "prompt --application/shared_components/user_interface/theme_style",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_theme_style(",
            f" p_id=>{self._wid(style_id)}",
            ",p_theme_id=>42",
            ",p_name=>'Vita'",
            ",p_static_id=>'VITA'",
            ",p_css_file_urls=>'#THEME_FILES#css/Vita#MIN#.css?v=#APEX_VERSION#'",
            ",p_is_current=>true",
            ",p_is_public=>true",
            ",p_is_accessible=>false",
            ");",
            self._comp_end(),
            "prompt --application/shared_components/user_interface/theme",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_theme(",
            f" p_id=>{self._wid(theme_id)}",
            ",p_theme_id=>42",
            ",p_static_id=>'universal-theme'",
            ",p_theme_name=>'Universal Theme'",
            ",p_theme_internal_name=>'UNIVERSAL_THEME'",
            ",p_version_identifier=>'26.1'",
            ",p_navigation_type=>'L'",
            ",p_nav_bar_type=>'LIST'",
            ",p_is_locked=>false",
            f",p_current_theme_style_id=>{self._wid(style_id)}",
            ",p_default_page_template=>4073832297226169690",
            ",p_default_dialog_template=>2101883943284197310",
            ",p_error_template=>2102634289808461002",
            ",p_printer_friendly_template=>4073832297226169690",
            ",p_login_template=>2102634289808461002",
            f",p_default_button_template=>{self._BTN_TMPL}",
            ",p_default_region_template=>4073835273271169698",
            ",p_default_chart_template=>4073835273271169698",
            ",p_default_form_template=>4073835273271169698",
            ",p_default_reportr_template=>4073835273271169698",
            ",p_default_wizard_template=>4073835273271169698",
            ",p_default_menur_template=>2532939663579242476",
            ",p_default_listr_template=>4073835273271169698",
            ",p_default_irr_template=>2102002977963900996",
            ",p_default_report_template=>2540130677583398057",
            ",p_default_label_template=>1610598304472262251",
            ",p_default_menu_template=>4073839682315169711",
            ",p_default_list_template=>4073837480889169704",
            ",p_default_top_nav_list_temp=>2528231041045349458",
            ",p_default_side_nav_list_temp=>2469215554099805162",
            ",p_default_nav_list_position=>'SIDE'",
            ",p_default_dialogbtnr_template=>2127905476394690047",
            ",p_default_dialogr_template=>4502917002193490937",
            ",p_default_option_label=>1610598304472262251",
            f",p_default_required_label=>{self._FIELD_TMPL}",
            ",p_default_navbar_list_template=>2849019392706229583",
            ",p_file_prefix=>nvl(wwv_flow_application_install.get_static_theme_file_prefix(42),'#APEX_FILES#themes/theme_42/26.1/')",
            ",p_files_version=>64",
            ",p_icon_library=>'FONTAPEX'",
            ",p_javascript_file_urls=>wwv_flow_string.join(wwv_flow_t_varchar2(",
            "'#APEX_FILES#libraries/apex/#MIN_DIRECTORY#widget.stickyWidget#MIN#.js?v=#APEX_VERSION#',",
            "'#THEME_FILES#js/theme42#MIN#.js?v=#APEX_VERSION#'))",
            ",p_css_file_urls=>'#THEME_FILES#css/Core#MIN#.css?v=#APEX_VERSION#'",
            ",p_reference_id=>wwv_imp_util.get_subscription_id(4073840274158169736,2000,'universal-theme',8842.261)",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    # ── Application ────────────────────────────────────────────────────────────

    def _application(self) -> str:
        alias = re.sub(r"[^A-Z0-9]", "", self.app_name.upper()) or "APP"
        safe_name = self.app_name.replace("'", "''")
        lines = [
            "prompt --application/create_application",
            self._comp_begin(),
            "wwv_imp_workspace.create_flow(",
            " p_id=>wwv_flow.g_flow_id",
            ",p_owner=>USER",
            f",p_name=>nvl(wwv_flow_application_install.get_application_name,'{safe_name}')",
            f",p_alias=>'{alias}'",
            ",p_application_tab_set=>0",
            ",p_logo_type=>'T'",
            f",p_logo_text=>'{safe_name}'",
            ",p_public_user=>'APEX_PUBLIC_USER'",
            f",p_authentication_id=>{self._wid(self._auth_id)}",
            ",p_flow_status=>'AVAILABLE_W_EDIT_LINK'",
            ",p_compatibility_mode=>'19.2'",
            ",p_theme_id=>42",
            ",p_home_url=>'f?p=&APP_ID.:1:&SESSION.'",
            ",p_theme_style_by_user_pref=>false",
            f",p_navigation_list_id=>{self._wid(self._nav_list_id)}",
            ",p_navigation_list_position=>'SIDE'",
            ",p_nav_bar_type=>'LIST'",
            f",p_nav_bar_list_id=>{self._wid(self._nav_bar_list_id)}",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    # ── Navigation ─────────────────────────────────────────────────────────────

    def _navigation(self, classes: list[Class]) -> str:
        lines = [
            "prompt --application/shared_components/navigation/lists/navigation_menu",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_list(",
            f" p_id=>{self._wid(self._nav_list_id)}",
            ",p_name=>'Navigation Menu'",
            ",p_static_id=>'navigation-menu'",
            ");",
        ]

        home_id = self._uid()
        lines += [
            "wwv_flow_imp_shared.create_list_item(",
            f" p_id=>{self._wid(home_id)}",
            ",p_list_item_display_sequence=>10",
            ",p_list_item_link_text=>'Home'",
            ",p_list_item_link_target=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.::::'",
            ",p_list_item_icon=>'fa-home'",
            ",p_list_item_current_type=>'TARGET_PAGE'",
            ");",
        ]

        for i, cls in enumerate(classes):
            page_num = 2 + i * 2
            item_id = self._uid()
            safe_label = cls.name.replace("'", "''")
            lines += [
                "wwv_flow_imp_shared.create_list_item(",
                f" p_id=>{self._wid(item_id)}",
                f",p_list_item_display_sequence=>{(i + 2) * 10}",
                f",p_list_item_link_text=>'{safe_label}'",
                f",p_list_item_link_target=>'f?p=&APP_ID.:{page_num}:&SESSION.::&DEBUG.::::'",
                ",p_list_item_icon=>'fa-table'",
                ",p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'",
                f",p_list_item_current_for_pages=>'{page_num},{page_num + 1}'",
                ");",
            ]

        lines.append(self._comp_end())

        # Nav bar list (logout)
        logout_id = self._uid()
        lines += [
            "prompt --application/shared_components/navigation/lists/navigation_bar",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_list(",
            f" p_id=>{self._wid(self._nav_bar_list_id)}",
            ",p_name=>'Navigation Bar'",
            ",p_static_id=>'navigation-bar'",
            ");",
            "wwv_flow_imp_shared.create_list_item(",
            f" p_id=>{self._wid(logout_id)}",
            ",p_list_item_display_sequence=>10",
            ",p_list_item_link_text=>'Log Out'",
            ",p_list_item_link_target=>'f?p=&APP_ID.:9999:&SESSION.::&DEBUG.::::'",
            ",p_list_item_icon=>'fa-sign-out'",
            ",p_list_item_current_type=>'NEVER'",
            ");",
            self._comp_end(),
        ]

        return "\n".join(lines)

    # ── Pages ──────────────────────────────────────────────────────────────────

    def _global_page(self) -> str:
        lines = [
            "prompt --application/pages/page_00000",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            " p_id=>0",
            ",p_name=>'Global Page'",
            ",p_step_title=>'Global Page'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_protection_level=>'D'",
            ",p_page_component_map=>'08'",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    def _home_page(self, classes: list[Class]) -> str:
        lines_html = "\n".join(
            f'<li><a href="f?p=&APP_ID.:{2 + i * 2}:&SESSION.">'
            f"{cls.name}</a></li>"
            for i, cls in enumerate(classes)
        )
        html = f"<ul>\n{lines_html}\n</ul>"
        safe_html = html.replace("'", "''")
        safe_name = self.app_name.replace("'", "''")

        region_id = self._uid()
        lines = [
            "prompt --application/pages/page_00001",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            " p_id=>1",
            f",p_name=>'{safe_name}'",
            f",p_step_title=>'{safe_name}'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_protection_level=>'C'",
            ",p_page_component_map=>'08'",
            ");",
            "wwv_flow_imp_page.create_page_plug(",
            f" p_id=>{self._wid(region_id)}",
            ",p_plug_name=>'Entities'",
            ",p_region_template_options=>'#DEFAULT#'",
            ",p_plug_display_sequence=>10",
            ",p_location=>null",
            f",p_plug_source=>'{safe_html}'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'expand_shortcuts', 'N',",
            "  'output_as', 'HTML')).to_clob",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    def _list_page(self, cls: Class, page_num: int) -> str:
        table = self._tbl(cls.name)
        form_page = page_num + 1
        safe_name = cls.name.replace("'", "''")

        region_id = self._uid()
        ws_uid = self._uid()
        btn_id = self._uid()
        da_ev_id = self._uid()
        da_ac_id = self._uid()

        # Exclude the 'id' column — it's the auto-generated PK already added
        # as the hidden P{n}_ID item and the worksheet's primary-key column.
        attrs = [a for a in sorted(cls.attributes, key=lambda a: a.name)
                 if self._col(a.name) != 'ID']

        lines = [
            f"prompt --application/pages/page_{page_num:05d}",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            f" p_id=>{page_num}",
            f",p_name=>'{safe_name}s'",
            f",p_step_title=>'{safe_name}s'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_protection_level=>'C'",
            ",p_page_component_map=>'18'",
            ");",
            "wwv_flow_imp_page.create_page_plug(",
            f" p_id=>{self._wid(region_id)}",
            f",p_plug_name=>'{safe_name}s'",
            ",p_region_template_options=>'#DEFAULT#'",
            ",p_plug_display_sequence=>10",
            ",p_query_type=>'TABLE'",
            f",p_query_table=>'{table}'",
            ",p_include_rowid_column=>false",
            ",p_plug_source_type=>'NATIVE_IR'",
            f",p_prn_page_header=>'{safe_name}s'",
            ");",
            "wwv_flow_imp_page.create_worksheet(",
            f" p_name=>'{safe_name}s'",
            ",p_max_row_count_message=>'The maximum row count for this report is #MAX_ROW_COUNT# rows.'",
            ",p_no_data_found_message=>'No data found.'",
            ",p_base_pk1=>'ID'",
            ",p_pagination_type=>'ROWS_X_TO_Y'",
            ",p_pagination_display_pos=>'BOTTOM_RIGHT'",
            ",p_report_list_mode=>'TABS'",
            ",p_lazy_loading=>false",
            ",p_show_detail_link=>'C'",
            ",p_show_notify=>'Y'",
            ",p_download_formats=>'CSV:HTML:XLSX:PDF'",
            ",p_enable_mail_download=>'Y'",
            f",p_detail_link=>'f?p=&APP_ID.:{form_page}:&APP_SESSION.::&DEBUG.:RP:"
            f"P{form_page}_ID:#ID#'",
            ",p_detail_link_text=>'<span aria-label=\"Edit\">"
            "<span class=\"fa fa-edit\" aria-hidden=\"true\"></span></span>'",
            ",p_owner=>USER",
            f",p_internal_uid=>{ws_uid}",
            ");",
            # ID column (hidden)
            "wwv_flow_imp_page.create_worksheet_column(",
            " p_db_column_name=>'ID'",
            ",p_display_order=>1",
            ",p_is_primary_key=>'Y'",
            ",p_column_identifier=>'A'",
            ",p_column_label=>'Id'",
            ",p_column_type=>'NUMBER'",
            ",p_display_text_as=>'HIDDEN_ESCAPE_SC'",
            ",p_heading_alignment=>'LEFT'",
            ",p_tz_dependent=>'N'",
            ",p_use_as_row_header=>'N'",
            ");",
        ]

        col_ids: list[str] = []
        for j, attr in enumerate(attrs):
            col = self._col(attr.name)
            label = attr.name.replace("_", " ").title().replace("'", "''")
            col_id_char = chr(ord("B") + j)
            col_type = (
                "NUMBER" if attr.type.name in ("int", "float", "bool")
                else "DATE" if attr.type.name in ("date", "datetime", "time")
                else "STRING"
            )
            lines += [
                "wwv_flow_imp_page.create_worksheet_column(",
                f" p_db_column_name=>'{col}'",
                f",p_display_order=>{j + 2}",
                f",p_column_identifier=>'{col_id_char}'",
                f",p_column_label=>'{label}'",
                f",p_column_type=>'{col_type}'",
                ",p_heading_alignment=>'LEFT'",
                ",p_tz_dependent=>'N'",
                ",p_use_as_row_header=>'N'",
                ");",
            ]
            col_ids.append(col)

        report_cols = ":".join(col_ids) or "ID"
        lines += [
            "wwv_flow_imp_page.create_worksheet_rpt(",
            " p_application_user=>'APXWS_DEFAULT'",
            ",p_report_seq=>10",
            ",p_report_alias=>'DEFAULT'",
            ",p_status=>'PUBLIC'",
            ",p_is_default=>'Y'",
            f",p_report_columns=>'{report_cols}'",
            ");",
            # Create button
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(btn_id)}",
            ",p_button_sequence=>10",
            f",p_button_plug_id=>{self._wid(region_id)}",
            ",p_button_name=>'CREATE'",
            ",p_button_action=>'REDIRECT_PAGE'",
            ",p_button_template_options=>'#DEFAULT#'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_is_hot=>'Y'",
            ",p_button_image_alt=>'Create'",
            ",p_button_position=>'RIGHT_OF_IR_SEARCH_BAR'",
            f",p_button_redirect_url=>'f?p=&APP_ID.:{form_page}:&APP_SESSION.::&DEBUG.:{form_page}::'",
            ");",
            # DA: refresh IR after modal closes
            "wwv_flow_imp_page.create_page_da_event(",
            f" p_id=>{self._wid(da_ev_id)}",
            ",p_name=>'Refresh Report After Dialog'",
            ",p_event_sequence=>10",
            ",p_triggering_element_type=>'REGION'",
            f",p_triggering_region_id=>{self._wid(region_id)}",
            ",p_bind_type=>'bind'",
            ",p_execution_type=>'IMMEDIATE'",
            ",p_bind_event_type=>'apexafterclosedialog'",
            ");",
            "wwv_flow_imp_page.create_page_da_action(",
            f" p_id=>{self._wid(da_ac_id)}",
            f",p_event_id=>{self._wid(da_ev_id)}",
            ",p_event_result=>'TRUE'",
            ",p_action_sequence=>10",
            ",p_execute_on_page_init=>'N'",
            ",p_action=>'NATIVE_REFRESH'",
            ",p_affected_elements_type=>'REGION'",
            f",p_affected_region_id=>{self._wid(region_id)}",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    def _form_page(self, cls: Class, page_num: int) -> str:
        table = self._tbl(cls.name)
        pk_item = f"P{page_num}_ID"
        safe_name = cls.name.replace("'", "''")

        region_id     = self._uid()
        btn_cancel_id = self._uid()
        btn_delete_id = self._uid()
        btn_save_id   = self._uid()
        btn_create_id = self._uid()
        pk_item_id    = self._uid()
        fetch_proc_id   = self._uid()
        process_proc_id = self._uid()
        da_ev_id      = self._uid()
        da_ac_id      = self._uid()

        # Skip 'id' — already handled as the auto-generated PK hidden item.
        attrs = [a for a in sorted(cls.attributes, key=lambda a: a.name)
                 if self._col(a.name) != 'ID']

        lines = [
            f"prompt --application/pages/page_{page_num:05d}",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            f" p_id=>{page_num}",
            f",p_name=>'Manage {safe_name}'",
            f",p_step_title=>'Manage {safe_name}'",
            ",p_page_mode=>'MODAL'",
            ",p_reload_on_submit=>'A'",
            ",p_warn_on_unsaved_changes=>'N'",
            ",p_first_item=>'AUTO_FIRST_ITEM'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_javascript_code=>'var htmldb_delete_message = ''"
            + '"DELETE_CONFIRM_MSG"'
            + "'';'",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_protection_level=>'C'",
            ",p_page_component_map=>'02'",
            ");",
            # NATIVE_FORM region
            "wwv_flow_imp_page.create_page_plug(",
            f" p_id=>{self._wid(region_id)}",
            f",p_plug_name=>'{safe_name}'",
            ",p_region_template_options=>'#DEFAULT#'",
            ",p_plug_display_sequence=>10",
            ",p_query_type=>'TABLE'",
            f",p_query_table=>'{table}'",
            ",p_include_rowid_column=>false",
            ",p_plug_source_type=>'NATIVE_FORM'",
            ");",
            # Cancel button
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(btn_cancel_id)}",
            ",p_button_sequence=>10",
            f",p_button_plug_id=>{self._wid(region_id)}",
            ",p_button_name=>'CANCEL'",
            ",p_button_action=>'DEFINED_BY_DA'",
            ",p_button_template_options=>'#DEFAULT#'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_image_alt=>'Cancel'",
            ",p_button_position=>'CLOSE'",
            ");",
            # Delete button
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(btn_delete_id)}",
            ",p_button_sequence=>20",
            f",p_button_plug_id=>{self._wid(region_id)}",
            ",p_button_name=>'DELETE'",
            ",p_button_action=>'SUBMIT'",
            ",p_button_template_options=>'#DEFAULT#'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_image_alt=>'Delete'",
            ",p_button_position=>'DELETE'",
            f",p_button_condition=>'{pk_item}'",
            ",p_button_condition_type=>'ITEM_IS_NOT_NULL'",
            ",p_database_action=>'DELETE'",
            ");",
            # Save button
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(btn_save_id)}",
            ",p_button_sequence=>30",
            f",p_button_plug_id=>{self._wid(region_id)}",
            ",p_button_name=>'SAVE'",
            ",p_button_action=>'SUBMIT'",
            ",p_button_template_options=>'#DEFAULT#:t-Button--hot'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_image_alt=>'Apply Changes'",
            ",p_button_position=>'CHANGE'",
            f",p_button_condition=>'{pk_item}'",
            ",p_button_condition_type=>'ITEM_IS_NOT_NULL'",
            ",p_database_action=>'UPDATE'",
            ");",
            # Create button
            "wwv_flow_imp_page.create_page_button(",
            f" p_id=>{self._wid(btn_create_id)}",
            ",p_button_sequence=>40",
            f",p_button_plug_id=>{self._wid(region_id)}",
            ",p_button_name=>'CREATE'",
            ",p_button_action=>'SUBMIT'",
            ",p_button_template_options=>'#DEFAULT#:t-Button--hot'",
            f",p_button_template_id=>{self._BTN_TMPL}",
            ",p_button_image_alt=>'Create'",
            ",p_button_position=>'CREATE'",
            f",p_button_condition=>'{pk_item}'",
            ",p_button_condition_type=>'ITEM_IS_NULL'",
            ",p_database_action=>'INSERT'",
            ");",
            # Hidden PK item
            "wwv_flow_imp_page.create_page_item(",
            f" p_id=>{self._wid(pk_item_id)}",
            f",p_name=>'{pk_item}'",
            ",p_item_sequence=>10",
            f",p_item_plug_id=>{self._wid(region_id)}",
            ",p_use_cache_before_default=>'NO'",
            ",p_source=>'ID'",
            ",p_source_type=>'DB_COLUMN'",
            ",p_display_as=>'NATIVE_HIDDEN'",
            ",p_protection_level=>'S'",
            ",p_attributes=>wwv_flow_t_plugin_attributes("
            "wwv_flow_t_varchar2('value_protected','Y')).to_clob",
            ");",
        ]

        # One text item per attribute
        for j, attr in enumerate(attrs):
            item_id = self._uid()
            item_name = f"P{page_num}_{self._col(attr.name)}"
            col = self._col(attr.name)
            prompt = attr.name.replace("_", " ").title().replace("'", "''")
            lines += [
                "wwv_flow_imp_page.create_page_item(",
                f" p_id=>{self._wid(item_id)}",
                f",p_name=>'{item_name}'",
                f",p_item_sequence=>{(j + 2) * 10}",
                f",p_item_plug_id=>{self._wid(region_id)}",
                ",p_use_cache_before_default=>'NO'",
                f",p_prompt=>'{prompt}'",
                f",p_source=>'{col}'",
                ",p_source_type=>'DB_COLUMN'",
                ",p_display_as=>'NATIVE_TEXT_FIELD'",
                ",p_cSize=>64",
                ",p_cMaxlength=>255",
                f",p_field_template=>{self._FIELD_TMPL}",
                ",p_item_template_options=>'#DEFAULT#'",
                ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
                "  'disabled','N',",
                "  'submit_when_enter_pressed','N',",
                "  'subtype','TEXT',",
                "  'trim_spaces','NONE')).to_clob",
                ");",
            ]

        # Fetch process: loads the row after page load (AFTER_HEADER)
        lines += [
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(fetch_proc_id)}",
            ",p_process_sequence=>10",
            ",p_process_point=>'AFTER_HEADER'",
            ",p_process_type=>'NATIVE_FORM_FETCH'",
            f",p_process_name=>'Fetch Row from {safe_name}'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            f"  'primary_key_column', 'ID',",
            f"  'primary_key_item', '{pk_item}',",
            f"  'table_name', '{table}')).to_clob",
            ");",
            # DML process: insert / update / delete based on button pressed
            "wwv_flow_imp_page.create_page_process(",
            f" p_id=>{self._wid(process_proc_id)}",
            ",p_process_sequence=>20",
            ",p_process_point=>'AFTER_SUBMIT'",
            ",p_process_type=>'NATIVE_FORM_PROCESS'",
            f",p_process_name=>'Process Row of {safe_name}'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'lock_row', 'Y',",
            "  'primary_key_column', 'ID',",
            f"  'primary_key_item', '{pk_item}',",
            f"  'return_key_into_item', '{pk_item}',",
            "  'supported_operations', 'I:U:D',",
            f"  'table_name', '{table}')).to_clob",
            ",p_process_error_message=>'#SQLERRM#'",
            ",p_error_display_location=>'INLINE_IN_NOTIFICATION'",
            ",p_process_when=>'CREATE,SAVE,DELETE'",
            ",p_process_when_type=>'REQUEST_IN_CONDITION'",
            ",p_process_success_message=>'Action Processed.'",
            ");",
            # DA: Cancel button → close dialog without saving
            "wwv_flow_imp_page.create_page_da_event(",
            f" p_id=>{self._wid(da_ev_id)}",
            ",p_name=>'Cancel Dialog'",
            ",p_event_sequence=>10",
            ",p_triggering_element_type=>'BUTTON'",
            f",p_triggering_button_id=>{self._wid(btn_cancel_id)}",
            ",p_bind_type=>'bind'",
            ",p_execution_type=>'IMMEDIATE'",
            ",p_bind_event_type=>'click'",
            ");",
            "wwv_flow_imp_page.create_page_da_action(",
            f" p_id=>{self._wid(da_ac_id)}",
            f",p_event_id=>{self._wid(da_ev_id)}",
            ",p_event_result=>'TRUE'",
            ",p_action_sequence=>10",
            ",p_execute_on_page_init=>'N'",
            ",p_action=>'NATIVE_DIALOG_CANCEL'",
            ");",
            self._comp_end(),
        ]

        return "\n".join(lines)

    # ── GUI-model page generation ─────────────────────────────────────────────

    @staticmethod
    def _classify_screen(name: str):
        """Classify a GUI screen name into list/form/other, returning (kind, entity).

        Handles multiple source-platform naming conventions:
        - Oracle APEX parser: ``Entity_List`` / ``Entity_Form``
        - Mendix parser:      ``Entity_page`` / ``Entity_form_page``
                              (also ``Entity_from_page`` — common export typo)

        All comparisons are case-insensitive.
        Returns ('list'|'form'|'other', entity_name_or_None).
        """
        lower = name.lower()
        # Underscore-separated form suffixes (check most-specific first)
        for suffix in ('_form_page', '_from_page', '_view_edit', '_viewedit',
                       '_edit', '_form', '_create', '_new', '_add', '_detail',
                       '_update', '_show'):
            if lower.endswith(suffix):
                return 'form', name[:len(name) - len(suffix)]
        # Underscore-separated list suffixes
        for suffix in ('_list', '_page', '_overview', '_browse', '_index', '_all'):
            if lower.endswith(suffix):
                return 'list', name[:len(name) - len(suffix)]
        # CamelCase without underscore separator (e.g. TaskOverview, TaskEdit)
        for suffix in ('viewedit', 'edit', 'form', 'create', 'detail', 'update'):
            if lower.endswith(suffix) and len(name) > len(suffix):
                return 'form', name[:len(name) - len(suffix)]
        for suffix in ('overview', 'list', 'browse', 'index'):
            if lower.endswith(suffix) and len(name) > len(suffix):
                return 'list', name[:len(name) - len(suffix)]
        return 'other', None

    def _assign_gui_page_numbers(self) -> list:
        """Pair list/form GUI screens and assign consecutive page numbers.

        List screens get even numbers (2, 4, 6, …); the corresponding form
        screen gets the immediately following odd number (3, 5, 7, …).  This
        matches the template's hard-coded detail-link assumption
        (screen_number + 1 = form page).

        Returns [(screen, page_num, entity_name_or_None)] where entity_name
        is set only for form screens (to look up the domain model class).
        """
        all_screens: list = []
        modules_iter = (self.gui_model.modules.values()
                        if isinstance(self.gui_model.modules, dict)
                        else self.gui_model.modules)
        for module in modules_iter:
            all_screens.extend(module.screens)

        # Group by entity name derived from screen name convention
        entity_groups: dict = {}  # entity -> {'list': screen, 'form': screen}
        others: list = []

        for screen in all_screens:
            kind, entity = self._classify_screen(screen.name)
            if kind == 'list':
                entity_groups.setdefault(entity, {})['list'] = screen
            elif kind == 'form':
                entity_groups.setdefault(entity, {})['form'] = screen
            else:
                others.append(screen)

        # Second pass: screens with unrecognised names (e.g. BESSER generator
        # produces 'wrapper', 'wrapper_2', …).  Try to identify the entity from
        # screen.description or screen.route_path.
        class_names_lower = {c.name.lower(): c.name for c in self._classes()}
        unmatched = []
        for screen in others:
            entity = None
            desc = (getattr(screen, 'description', None) or '').strip()
            route = (getattr(screen, 'route_path', None) or '').strip().lstrip('/')
            for candidate in (desc, route):
                if candidate.lower() in class_names_lower:
                    entity = class_names_lower[candidate.lower()]
                    break
            if entity is not None:
                entity_groups.setdefault(entity, {})['list'] = screen
            else:
                unmatched.append(screen)

        result: list = []
        page_num = 2

        for entity in sorted(entity_groups.keys()):
            group = entity_groups[entity]
            if 'list' in group:
                result.append((group['list'], page_num, entity, 'list'))
            page_num += 1          # list page always occupies this slot
            if 'form' in group:
                result.append((group['form'], page_num, entity, 'form'))
            page_num += 1          # form page always occupies this slot

        for screen in sorted(unmatched, key=lambda s: s.name):
            result.append((screen, page_num, None, 'other'))
            page_num += 1

        return result

    def _find_class_for_entity(self, entity_name: str):
        """Return the domain model Class whose name matches entity_name."""
        for cls in self._classes():
            if cls.name == entity_name:
                return cls
        # case-insensitive
        el = entity_name.lower()
        for cls in self._classes():
            if cls.name.lower() == el:
                return cls
        # strip underscores
        clean = el.replace('_', '')
        for cls in self._classes():
            if cls.name.lower().replace('_', '') == clean:
                return cls
        return None

    @staticmethod
    def _extract_page_content(sql: str) -> str:
        """Strip the standalone import_begin/end wrapper; keep create_page SQL.

        The UIPagesSQLGenerator template produces a standalone file with its own
        import_begin at the top and import_end at the bottom.  We only want the
        page creation block (prompt + begin/end block) so it can be embedded
        inside the combined app SQL whose import_begin is already at the top.
        """
        # Match the 'prompt --application/pages/page_NNN' line (create, not delete)
        m = re.search(r'^prompt --application/pages/page_\d+\s*$', sql, re.MULTILINE)
        if not m:
            return ""
        end_m = re.search(
            r'^begin\s*\nwwv_flow_imp\.import_end',
            sql[m.start():],
            re.MULTILINE | re.IGNORECASE,
        )
        if end_m:
            content = sql[m.start(): m.start() + end_m.start()].rstrip()
        else:
            content = sql[m.start():].rstrip()
        return content

    def _generate_ir_page_from_gui(self, screen, page_num: int) -> str:
        """Generate an Interactive Report page SQL from a GUI model list screen.

        Calls UIPagesSQLGenerator (Jinja2 template), reads the output file,
        strips the standalone wrapper, and returns the embeddable page SQL.
        Returns "" if the screen produces no page content (e.g. no DataList).
        """
        import tempfile
        try:
            from migrator.generators.sql.sql_generator_ui import UIPagesSQLGenerator
            from besser.BUML.metamodel.gui import DataList
        except ImportError:
            return ""

        # UIPagesSQLGenerator only produces useful IR SQL when the screen has
        # at least one DataList component. Without it the template emits a
        # minimal empty-page stub — skip the round-trip and return "" early.
        if not any(isinstance(v, DataList) for v in getattr(screen, 'view_elements', [])):
            return ""

        fname = f"page_{page_num:05d}.sql"
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                UIPagesSQLGenerator(
                    model=self.model,
                    gui_model=self.gui_model,
                    app_id=str(self.app_id),
                    screen=screen,
                    screen_number=page_num,
                    workspace_name="GENERATED",
                    user_name="USER",
                    output_file_name=fname,
                    output_dir=tmpdir,
                ).generate()
            except Exception:
                return ""

            out_file = os.path.join(tmpdir, fname)
            if not os.path.exists(out_file):
                return ""
            with open(out_file, 'r', encoding='utf-8') as fh:
                content = fh.read()

        return self._extract_page_content(content)

    def _navigation_gui(self, assignments: list) -> str:
        """Navigation menu built from GUI model screens (one entry per entity)."""
        # Build page-map: entity -> [list_page_num, form_page_num]
        page_map: dict = {}
        for screen, page_num, entity, kind in assignments:
            if kind == 'list':
                page_map.setdefault(entity, [None, None])[0] = page_num
            elif kind == 'form':
                page_map.setdefault(entity, [None, None])[1] = page_num

        lines = [
            "prompt --application/shared_components/navigation/lists/navigation_menu",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_list(",
            f" p_id=>{self._wid(self._nav_list_id)}",
            ",p_name=>'Navigation Menu'",
            ",p_static_id=>'navigation-menu'",
            ");",
        ]
        home_id = self._uid()
        lines += [
            "wwv_flow_imp_shared.create_list_item(",
            f" p_id=>{self._wid(home_id)}",
            ",p_list_item_display_sequence=>10",
            ",p_list_item_link_text=>'Home'",
            ",p_list_item_link_target=>'f?p=&APP_ID.:1:&SESSION.::&DEBUG.::::'",
            ",p_list_item_icon=>'fa-home'",
            ",p_list_item_current_type=>'TARGET_PAGE'",
            ");",
        ]

        for i, entity in enumerate(sorted(page_map.keys())):
            list_pn, form_pn = page_map[entity]
            if list_pn is None:
                continue  # no list page → skip from nav
            item_id = self._uid()
            safe_label = entity.replace("'", "''").replace('_', ' ')
            active_pages = str(list_pn)
            if form_pn is not None:
                active_pages += f",{form_pn}"
            lines += [
                "wwv_flow_imp_shared.create_list_item(",
                f" p_id=>{self._wid(item_id)}",
                f",p_list_item_display_sequence=>{(i + 2) * 10}",
                f",p_list_item_link_text=>'{safe_label}'",
                f",p_list_item_link_target=>'f?p=&APP_ID.:{list_pn}:&SESSION.::&DEBUG.::::'",
                ",p_list_item_icon=>'fa-table'",
                ",p_list_item_current_type=>'COLON_DELIMITED_PAGE_LIST'",
                f",p_list_item_current_for_pages=>'{active_pages}'",
                ");",
            ]

        lines.append(self._comp_end())

        # Nav bar (logout)
        logout_id = self._uid()
        lines += [
            "prompt --application/shared_components/navigation/lists/navigation_bar",
            self._comp_begin(),
            "wwv_flow_imp_shared.create_list(",
            f" p_id=>{self._wid(self._nav_bar_list_id)}",
            ",p_name=>'Navigation Bar'",
            ",p_static_id=>'navigation-bar'",
            ");",
            "wwv_flow_imp_shared.create_list_item(",
            f" p_id=>{self._wid(logout_id)}",
            ",p_list_item_display_sequence=>10",
            ",p_list_item_link_text=>'Log Out'",
            ",p_list_item_link_target=>'f?p=&APP_ID.:9999:&SESSION.::&DEBUG.::::'",
            ",p_list_item_icon=>'fa-sign-out'",
            ",p_list_item_current_type=>'NEVER'",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    def _home_page_gui(self, assignments: list) -> str:
        """Home page with links to each entity list page (from GUI model)."""
        list_links = []
        for screen, page_num, entity_raw, kind in assignments:
            if kind == 'list':
                entity = (entity_raw or screen.name).replace('_', ' ')
                safe_entity = entity.replace("'", "''")
                list_links.append(
                    f'<li><a href="f?p=&APP_ID.:{page_num}:&SESSION.">'
                    f'{safe_entity}</a></li>'
                )

        html = '<ul>\n' + '\n'.join(list_links) + '\n</ul>'
        safe_html = html.replace("'", "''")
        safe_name = self.app_name.replace("'", "''")
        region_id = self._uid()

        lines = [
            "prompt --application/pages/page_00001",
            self._comp_begin(),
            "wwv_flow_imp_page.create_page(",
            " p_id=>1",
            f",p_name=>'{safe_name}'",
            f",p_step_title=>'{safe_name}'",
            ",p_autocomplete_on_off=>'OFF'",
            ",p_page_template_options=>'#DEFAULT#'",
            ",p_protection_level=>'C'",
            ",p_page_component_map=>'08'",
            ");",
            "wwv_flow_imp_page.create_page_plug(",
            f" p_id=>{self._wid(region_id)}",
            ",p_plug_name=>'Entities'",
            ",p_region_template_options=>'#DEFAULT#'",
            ",p_plug_display_sequence=>10",
            ",p_location=>null",
            f",p_plug_source=>'{safe_html}'",
            ",p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2(",
            "  'expand_shortcuts', 'N',",
            "  'output_as', 'HTML')).to_clob",
            ");",
            self._comp_end(),
        ]
        return "\n".join(lines)

    # ── Supporting Objects (DDL embedded inside the APEX import envelope) ────────

    def _format_varchar2_table(self, sql: str) -> list[str]:
        """Format SQL text as g_varchar2_table assignments using ||wwv_flow.LF||.

        Each element holds complete SQL lines. Value length is capped at 4000
        chars per element (content + one byte per newline).
        """
        sql_lines = sql.split('\n')
        result: list[str] = []
        idx = 1
        bucket: list[str] = []
        bucket_len = 0

        def flush() -> None:
            nonlocal idx
            parts = [f"'{ln}'" for ln in bucket]
            body = "||wwv_flow.LF||\n".join(parts) + "||wwv_flow.LF||\n''"
            result.append(f"wwv_flow_imp.g_varchar2_table({idx}) := {body};")
            idx += 1

        for line in sql_lines:
            escaped = line.replace("'", "''")
            contrib = len(line) + 1  # content + the LF we represent
            if bucket_len + contrib > 4000 and bucket:
                flush()
                bucket = []
                bucket_len = 0
            bucket.append(escaped)
            bucket_len += contrib

        if bucket:
            flush()

        return result

    def _drop_sql(self) -> str:
        """Simple PL/SQL DROP blocks for the Supporting Objects deinstall script."""
        classes = list(self.model.classes_sorted_by_inheritance())
        class_names = {c.name for c in classes}
        fk_map, nm_tables = self._ddl._compute_fk_columns(class_names)
        sorted_cls = self._ddl._topo_sort(classes, fk_map)

        lines: list[str] = []
        seen_jct: set = set()
        for t1, t2, _, _ in nm_tables:
            jn = f"{t1}_{t2}"
            if jn in seen_jct:
                continue
            seen_jct.add(jn)
            lines.append(
                f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {jn} CASCADE CONSTRAINTS';"
                f" EXCEPTION WHEN OTHERS THEN NULL; END;"
            )
            lines.append("/")
        for cls in reversed(sorted_cls):
            tname = self._tbl(cls.name)
            lines.append(
                f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {tname} CASCADE CONSTRAINTS';"
                f" EXCEPTION WHEN OTHERS THEN NULL; END;"
            )
            lines.append("/")
        return "\n".join(lines) + "\n"

    def _create_tables_sql(self) -> str:
        """CREATE TABLE DDL for the Supporting Objects install script.

        Drops any existing tables first so the script is idempotent — a
        second import (or re-install) won't fail with ORA-00955.
        """
        enum_map = self._ddl._get_enum_map()
        classes = list(self.model.classes_sorted_by_inheritance())
        class_names = {c.name for c in classes}
        fk_map, nm_tables = self._ddl._compute_fk_columns(class_names)
        sorted_cls = self._ddl._topo_sort(classes, fk_map)

        lines: list[str] = []

        # Drop in reverse order (junction tables first, then entity tables).
        # EXCEPTION WHEN OTHERS silently ignores ORA-00942 (table doesn't exist).
        seen_jct_d: set = set()
        for t1, t2, _, _ in nm_tables:
            jn = f"{t1}_{t2}"
            if jn in seen_jct_d:
                continue
            seen_jct_d.add(jn)
            lines.append(
                f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {jn} CASCADE CONSTRAINTS';"
                f" EXCEPTION WHEN OTHERS THEN NULL; END;"
            )
            lines.append("/")
        for cls in reversed(sorted_cls):
            tname = self._tbl(cls.name)
            lines.append(
                f"BEGIN EXECUTE IMMEDIATE 'DROP TABLE {tname} CASCADE CONSTRAINTS';"
                f" EXCEPTION WHEN OTHERS THEN NULL; END;"
            )
            lines.append("/")
        lines.append("")

        for cls in sorted_cls:
            tname = self._tbl(cls.name)
            tname_lower = tname.lower()
            parent = self._ddl._find_parent(cls)
            parent_tname = self._tbl(parent.name) if parent else None

            col_defs = ["    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY"]
            fk_cols: list[str] = []
            constraints: list[str] = []

            if parent is not None:
                pfk = f"{parent_tname.lower()}_id"
                fk_cols.append(f"    {pfk} NUMBER NOT NULL")
                constraints.append(f"    FOREIGN KEY ({pfk}) REFERENCES {parent_tname}(id)")

            for attr in sorted(cls.attributes, key=lambda a: a.name):
                cname = self._col(attr.name)
                if cname == 'ID':
                    continue  # already the identity PK
                ttype = attr.type.name
                nn = "" if attr.is_optional else " NOT NULL"
                if ttype == "bool":
                    col_defs.append(f"    {cname} NUMBER(1) DEFAULT 0{nn}")
                    constraints.append(
                        f"    CONSTRAINT chk_{tname_lower}_{cname} CHECK ({cname} IN (0, 1))"
                    )
                elif ttype in enum_map:
                    vals = enum_map[ttype]
                    mlen = max((len(v) for v in vals), default=20)
                    col_defs.append(f"    {cname} VARCHAR2({max(mlen + 4, 20)}){nn}")
                    vs = ", ".join(f"'{v}'" for v in vals)
                    constraints.append(
                        f"    CONSTRAINT chk_{tname_lower}_{cname} CHECK ({cname} IN ({vs}))"
                    )
                else:
                    col_defs.append(f"    {cname} {self._ddl._col_type(ttype, enum_map)}{nn}")

            seen: set = set()
            for fk_col, ref_tbl, is_uniq in fk_map.get(cls.name, []):
                key = (fk_col, ref_tbl)
                if key in seen:
                    continue
                seen.add(key)
                fk_cols.append(f"    {fk_col} NUMBER NOT NULL")
                constraints.append(f"    FOREIGN KEY ({fk_col}) REFERENCES {ref_tbl}(id)")
                if is_uniq:
                    constraints.append(
                        f"    CONSTRAINT uq_{tname_lower}_{fk_col} UNIQUE ({fk_col})"
                    )

            all_cols = col_defs + fk_cols + constraints
            lines += [f"CREATE TABLE {tname} (", ",\n".join(all_cols), ");", ""]

        seen_jct: set = set()
        for t1, t2, c1, c2 in nm_tables:
            jn = f"{t1}_{t2}"
            if jn in seen_jct:
                continue
            seen_jct.add(jn)
            lines += [
                f"CREATE TABLE {jn} (",
                f"    {c1} NUMBER NOT NULL,",
                f"    {c2} NUMBER NOT NULL,",
                f"    PRIMARY KEY ({c1}, {c2}),",
                f"    FOREIGN KEY ({c1}) REFERENCES {t1}(id),",
                f"    FOREIGN KEY ({c2}) REFERENCES {t2}(id)",
                ");", "",
            ]

        return "\n".join(lines) + "\n"

    def _supporting_objects(self) -> str:
        """Embed DDL as APEX Supporting Objects (deinstall + install scripts).

        Structure mirrors real APEX 24.x exports:
        1. create_install  — registers the supporting objects + DROP deinstall script
        2. create_install_script — the CREATE TABLE install script, linked via p_install_id
        """
        install_id = self._uid()
        script_id = self._uid()

        # Block 1: create_install (deinstall = DROP tables)
        b1 = [
            "prompt --application/deployment/definition",
            self._comp_begin(),
            "wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;",
        ] + self._format_varchar2_table(self._drop_sql()) + [
            "wwv_flow_imp_shared.create_install(",
            f" p_id=>{self._wid(install_id)}",
            ",p_deinstall_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)",
            ",p_required_free_kb=>100",
            ");",
            self._comp_end(),
        ]

        # Block 2: create_install_script (install = CREATE TABLE)
        b2 = [
            "prompt --application/deployment/installscripts/create_tables",
            self._comp_begin(),
            "wwv_flow_imp.g_varchar2_table := wwv_flow_imp.empty_varchar2_table;",
        ] + self._format_varchar2_table(self._create_tables_sql()) + [
            "wwv_flow_imp_shared.create_install_script(",
            f" p_id=>{self._wid(script_id)}",
            f",p_install_id=>{self._wid(install_id)}",
            ",p_name=>'create_tables'",
            ",p_sequence=>10",
            ",p_script_type=>'INSTALL'",
            ",p_script_clob=>wwv_flow_imp.varchar2_to_clob(wwv_flow_imp.g_varchar2_table)",
            ");",
            self._comp_end(),
        ]

        return "\n".join(b1) + "\n" + "\n".join(b2)

    # ── Entry point ────────────────────────────────────────────────────────────

    def generate(self) -> str:
        """Write the full APEX app SQL to <output_dir>/<output_filename>.

        Returns the absolute path to the generated file.
        """
        os.makedirs(self.output_dir, exist_ok=True)
        file_path = os.path.join(self.output_dir, self.output_filename)

        classes = self._classes()

        parts: list[str] = []
        # File starts with the APEX import header — no plain DDL preamble.
        # DDL is embedded as a Supporting Objects install script at the end.
        parts.append(self._set_environment())
        parts.append(self._application())
        parts.append(self._theme())
        parts.append(self._authentication())
        parts.append(self._login_page())

        if self.gui_model is not None:
            assignments = self._assign_gui_page_numbers()
            parts.append(self._navigation_gui(assignments))
            parts.append(self._global_page())
            parts.append(self._home_page_gui(assignments))
            for screen, page_num, entity_name, kind in assignments:
                if kind == 'list':
                    sql = self._generate_ir_page_from_gui(screen, page_num)
                    if sql:
                        parts.append(sql)
                    else:
                        # IR generation produced nothing (no DataList) —
                        # fall back to domain-model list page
                        cls = self._find_class_for_entity(entity_name) if entity_name else None
                        if cls is not None:
                            parts.append(self._list_page(cls, page_num))
                elif kind == 'form' and entity_name is not None:
                    cls = self._find_class_for_entity(entity_name)
                    if cls is not None:
                        parts.append(self._form_page(cls, page_num))
                # other screen types are skipped for now
        else:
            parts.append(self._navigation(classes))
            parts.append(self._global_page())
            parts.append(self._home_page(classes))
            for i, cls in enumerate(classes):
                list_page = 2 + i * 2
                form_page = 3 + i * 2
                parts.append(self._list_page(cls, list_page))
                parts.append(self._form_page(cls, form_page))

        parts.append(self._supporting_objects())
        parts.append(self._end_environment())

        with open(file_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(parts))

        print(f"Oracle APEX full app SQL generated: {file_path}")
        return file_path
