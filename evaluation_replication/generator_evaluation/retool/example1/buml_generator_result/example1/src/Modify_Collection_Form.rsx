<Screen id="Modify_Collection_Form" title="Modify_Collection_Form" _order={3}>
<Frame id="$main" type="main" padding="8px 12px">
<Button id="Add_Member_Add_Another" text="Add Member &amp; Add Another" />
<Button id="Cancel_2" text="Cancel" />
<Button id="Delete_Collection" text="Delete Collection" />
<Form id="Modify_Collection_fields_1" showBody={true} showFooter={true}>
<Text id="Modify_Collection_fields_1_title" value="Modify Collection" />
<Body >
<TextInput id="P3_ATTR1" formDataKey="P3_ATTR1" label="Character Attribute 1" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_ATTR2" formDataKey="P3_ATTR2" label="Character Attribute 2" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_ATTR3" formDataKey="P3_ATTR3" label="Character Attribute 3" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_ATTR4" formDataKey="P3_ATTR4" label="Character Attribute 4" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_ATTR5" formDataKey="P3_ATTR5" label="Character Attribute 5" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P3_DATE_ATTR1" formDataKey="P3_DATE_ATTR1" label="Date Attribute 1" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P3_DATE_ATTR2" formDataKey="P3_DATE_ATTR2" label="Date Attribute 2" placeholder="" required={false} disabled={false} readOnly={false} />
<Date id="P3_DATE_ATTR3" formDataKey="P3_DATE_ATTR3" label="Date Attribute 3" placeholder="" required={false} disabled={false} readOnly={false} />
<TextInput id="P3_NAME" formDataKey="P3_NAME" label="Collection Name" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P3_NUM_ATTR1" formDataKey="P3_NUM_ATTR1" label="Numeric Attribute 1" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P3_NUM_ATTR2" formDataKey="P3_NUM_ATTR2" label="Numeric Attribute 2" placeholder="" required={false} disabled={false} readOnly={false} />
<NumberInput id="P3_NUM_ATTR3" formDataKey="P3_NUM_ATTR3" label="Numeric Attribute 3" placeholder="" required={false} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Modify_Collection_fields_1_submit" text="Add Member" submit={true} submitTargetId="Modify_Collection_fields_1" />

</Footer>

</Form>
<Button id="Resequence" text="Resequence" />
<Button id="Truncate_Collection" text="Truncate Collection" />
</Frame>
</Screen>