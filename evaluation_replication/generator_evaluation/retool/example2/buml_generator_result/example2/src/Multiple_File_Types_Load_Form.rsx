<Screen id="Multiple_File_Types_Load_Form" title="Multiple_File_Types_Load_Form" _order={8}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Clear_2" text="Clear" />
<Form id="Multiple_File_Types_Load_fields_1" showBody={true} showFooter={true}>
<Text id="Multiple_File_Types_Load_fields_1_title" value="Multiple File Types Load" />
<Body >
<TextInput id="P16_ERROR_ROW_COUNT" formDataKey="P16_ERROR_ROW_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<FileButton id="P16_FILE" formDataKey="P16_FILE" label="Upload a File" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P16_FILE_NAME" formDataKey="P16_FILE_NAME" label="Loaded File" placeholder="" required={false} disabled={false} readOnly={true} />
<TextInput id="P16_FILE_TYPE" formDataKey="P16_FILE_TYPE" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P16_PROCESSED_ROW_COUNT" formDataKey="P16_PROCESSED_ROW_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<Select id="P16_XLSX_WORKSHEET" formDataKey="P16_XLSX_WORKSHEET" label="XLSX Worksheet" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Multiple_File_Types_Load_fields_1_submit" text="Load Data" submit={true} submitTargetId="Multiple_File_Types_Load_fields_1" />

</Footer>

</Form>
</Frame>
</Screen>