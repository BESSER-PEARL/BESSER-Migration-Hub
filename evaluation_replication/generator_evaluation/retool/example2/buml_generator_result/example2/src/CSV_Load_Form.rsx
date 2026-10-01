<Screen id="CSV_Load_Form" title="CSV_Load_Form" _order={2}>
<Frame id="$main" type="main" padding="8px 12px">
<Form id="CSV_Load_fields_1" showBody={true} showFooter={true}>
<Text id="CSV_Load_fields_1_title" value="CSV Load" />
<Body >
<TextInput id="P11_COPY_PASTE_ERROR_ROW_COUNT" formDataKey="P11_COPY_PASTE_ERROR_ROW_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextArea id="P11_DATA" formDataKey="P11_DATA" label="Copy and Paste Delimited Data" placeholder="" required={false} disabled={false} readOnly={false} />
<FileButton id="P11_FILE" formDataKey="P11_FILE" label="Upload a File" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P11_FILE_ERROR_ROW_COUNT" formDataKey="P11_FILE_ERROR_ROW_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P11_FILE_NAME" formDataKey="P11_FILE_NAME" label="Loaded File" placeholder="" required={false} disabled={false} readOnly={true} />
<TextInput id="P11_PASTED_DATA" formDataKey="P11_PASTED_DATA" label="Pasted Data" placeholder="" required={false} disabled={false} readOnly={true} />
</Body>
<Footer >
<Button id="CSV_Load_fields_1_submit" text="Load Data" submit={true} submitTargetId="CSV_Load_fields_1" />

</Footer>

</Form>
<Button id="Clear_Data" text="Clear" />
<Button id="Clear_File" text="Clear" />
<Button id="Load_File" text="Load Data" />
<Button id="Next" text="Next" />
</Frame>
</Screen>