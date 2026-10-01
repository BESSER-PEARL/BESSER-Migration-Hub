<Screen id="Background_Load_Form" title="Background_Load_Form" _order={1}>
<Frame id="$main" type="main" padding="8px 12px">
<Form id="Background_Load_fields_1" showBody={true} showFooter={true}>
<Text id="Background_Load_fields_1_title" value="Background Load" />
<Body >
<TextInput id="P17_ERROR_ROWS" formDataKey="P17_ERROR_ROWS" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<FileButton id="P17_FILE" formDataKey="P17_FILE" label="Upload a File" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P17_FILE_NAME" formDataKey="P17_FILE_NAME" label="Loaded File" placeholder="" required={false} disabled={false} readOnly={true} />
<TextInput id="P17_LOAD_EXEC_ID" formDataKey="P17_LOAD_EXEC_ID" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P17_PROCESSED_ROWS" formDataKey="P17_PROCESSED_ROWS" label="" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Background_Load_fields_1_submit" text="Load Data" submit={true} submitTargetId="Background_Load_fields_1" />

</Footer>

</Form>
<Button id="Clear" text="Clear" />
</Frame>
</Screen>