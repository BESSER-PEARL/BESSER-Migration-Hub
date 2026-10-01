<ModalFrame id="Create_Collection_Form" hidden={true} showOverlay={true}>
<Body >
<Button id="Cancel_6" text="Cancel" />
<Form id="Create_Collection_fields_1" showBody={true} showFooter={true}>
<Text id="Create_Collection_fields_1_title" value="Create Collection" />
<Body >
<TextInput id="P2_NAME" formDataKey="P2_NAME" label="Collection Name" placeholder="" required={true} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Create_Collection_fields_1_submit" text="Create Collection" submit={true} submitTargetId="Create_Collection_fields_1" />

</Footer>

</Form>
<Button id="Create_Replace" text="Create/Replace Collection" />
</Body>
</ModalFrame>