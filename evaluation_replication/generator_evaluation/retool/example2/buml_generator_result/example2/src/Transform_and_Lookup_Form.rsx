<Screen id="Transform_and_Lookup_Form" title="Transform_and_Lookup_Form" _order={11}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Clear_3" text="Clear" />
<Form id="Transform_and_Lookup_fields_1" showBody={true} showFooter={true}>
<Text id="Transform_and_Lookup_fields_1_title" value="Transform and Lookup" />
<Body >
<TextInput id="P15_ERROR_ROW_COUNT" formDataKey="P15_ERROR_ROW_COUNT" label="" placeholder="" required={false} disabled={false} readOnly={false} />
<FileButton id="P15_FILE" formDataKey="P15_FILE" label="Upload a File" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P15_FILE_NAME" formDataKey="P15_FILE_NAME" label="Loaded File" placeholder="" required={false} disabled={false} readOnly={true} />
</Body>
<Footer >
<Button id="Transform_and_Lookup_fields_1_submit" text="Load Data" submit={true} submitTargetId="Transform_and_Lookup_fields_1" />

</Footer>

</Form>
</Frame>
</Screen>