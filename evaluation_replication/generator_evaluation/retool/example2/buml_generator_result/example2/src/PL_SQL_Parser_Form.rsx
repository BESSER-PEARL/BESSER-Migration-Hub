<Screen id="PL_SQL_Parser_Form" title="PL_SQL_Parser_Form" _order={9}>
<Frame id="$main" type="main" padding="8px 12px">
<Form id="PL_SQL_Parser_fields_1" showBody={true} showFooter={true}>
<Text id="PL_SQL_Parser_fields_1_title" value="PL/SQL Parser" />
<Body >
<FileButton id="P31_FILE" formDataKey="P31_FILE" label="Upload a File" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P31_XLSX_WORKSHEET" formDataKey="P31_XLSX_WORKSHEET" label="XLSX Worksheet" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="PL_SQL_Parser_fields_1_submit" text="Upload File" submit={true} submitTargetId="PL_SQL_Parser_fields_1" />

</Footer>

</Form>
</Frame>
</Screen>