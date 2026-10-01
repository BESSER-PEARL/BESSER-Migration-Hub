<Container
  id="detailContainer"
  footerPadding="4px 12px"
  headerPadding="4px 12px"
  heightType="fixed"
  padding="12px"
  showBody={true}
  showHeader={true}
>
  <Header>
    <Text
      id="detailTitle"
      value="#### {{ membersTable.selectedRow.name }}"
      verticalAlign="center"
    />
    <Tabs
      id="detailTabs"
      itemMode="static"
      navigateContainer={true}
      targetContainerId="detailContainer"
      value="{{ self.values[0] }}"
    >
      <Option id="t1a1a" label="Details" value="details" />
      <Option id="t2b2b" label="Activity" value="activity" />
    </Tabs>
    <Button
      id="detailCloseBtn"
      horizontalAlign="right"
      iconBefore="bold/interface-delete-1"
      styleVariant="outline"
    >
      <Event
        id="f1a2b3c4"
        event="click"
        method="hide"
        params={{}}
        pluginId="detailPane"
        type="widget"
        waitMs="0"
        waitType="debounce"
      />
    </Button>
  </Header>
  <View id="detailsView" label="Details" viewKey="details">
    <Form
      id="DetailForm"
      disableSubmit="{{ updateMember.isFetching }}"
      initialData="{{ membersTable.selectedSourceRow }}"
      loading="{{ updateMember.isFetching }}"
      padding="12px"
      requireValidation={true}
      showBody={true}
      showFooter={true}
    >
      <Body>
        <TextInput
          id="detailName"
          formDataKey="name"
          label="Name"
          labelPosition="top"
          required={true}
        />
        <TextInput
          id="detailEmail"
          formDataKey="email"
          label="Email"
          labelPosition="top"
          required={true}
        />
        <Select
          id="detailDepartment"
          data="{{ Array.isArray(selectDepartments.data) ? selectDepartments.data : [{ label: 'Engineering', value: 'Engineering' }, { label: 'Marketing', value: 'Marketing' }, { label: 'Sales', value: 'Sales' }] }}"
          formDataKey="department"
          itemMode="mapped"
          label="Department"
          labelPosition="top"
          labels="{{ item.label }}"
          showSelectionIndicator={true}
          values="{{ item.value }}"
        />
        <Select
          id="detailRole"
          formDataKey="role"
          itemMode="static"
          label="Role"
          labelPosition="top"
          showSelectionIndicator={true}
        >
          <Option id="r1a1a" label="Engineer" value="Engineer" />
          <Option id="r2b2b" label="Designer" value="Designer" />
          <Option id="r3c3c" label="Manager" value="Manager" />
          <Option id="r4d4d" label="Analyst" value="Analyst" />
          <Option id="r5e5e" label="Lead" value="Lead" />
        </Select>
        <Select
          id="detailStatus"
          formDataKey="status"
          itemMode="static"
          label="Status"
          labelPosition="top"
          showSelectionIndicator={true}
        >
          <Option id="ds1a1" label="Active" value="active" />
          <Option id="ds2b2" label="On Leave" value="on_leave" />
          <Option id="ds3c3" label="Offboarded" value="offboarded" />
        </Select>
        <Date
          id="detailJoinedDate"
          formDataKey="joined_date"
          label="Joined"
          labelPosition="top"
        />
        <TextArea
          id="detailNotes"
          autoResize={true}
          formDataKey="notes"
          label="Notes"
          labelPosition="top"
          minLines={3}
        />
      </Body>
      <Footer>
        <Button
          id="detailSaveBtn"
          submit={true}
          submitTargetId="DetailForm"
          text="Save changes"
        />
      </Footer>
      <Event
        id="d5e6f7a8"
        event="submit"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="updateMember"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Form>
  </View>
  <View id="activityView" label="Activity" viewKey="activity">
    <Text
      id="activityPlaceholder"
      value="Activity log for **{{ membersTable.selectedRow.name }}** will appear here.\n\nThis view demonstrates the tabbed detail pane pattern with dynamic width — the Activity tab expands the panel to 550px to accommodate richer content."
    />
  </View>
</Container>
