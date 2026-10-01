<Screen id="Login_Page_Form" title="Login_Page_Form" _order={2}>
<Frame id="$main" type="main" padding="8px 12px">
<Form id="Login_Page_fields_1" showBody={true} showFooter={true}>
<Text id="Login_Page_fields_1_title" value="Login Page" />
<Body >
<Password id="P101_PASSWORD" formDataKey="P101_PASSWORD" label="Password" placeholder="password" required={true} disabled={false} readOnly={false} />
<TextInput id="P101_USERNAME" formDataKey="P101_USERNAME" label="Username" placeholder="username" required={true} disabled={false} readOnly={false} />
</Body>
<Footer >
<Button id="Login_Page_fields_1_submit" text="Sign In" submit={true} submitTargetId="Login_Page_fields_1" />

</Footer>

</Form>
</Frame>
</Screen>