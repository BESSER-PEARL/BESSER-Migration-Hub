<ModalFrame
  id="editModal"
  hidden={true}
  hideOnEscape={true}
  overlayInteraction={true}
  showOverlay={true}
  size="medium"
>
  <Header>
    <Text
      id="editTitle"
      marginType="normal"
      value="#### Edit product"
      verticalAlign="center"
    />
  </Header>
  <Body>
    <Form
      id="EditProductForm"
      disableSubmit="{{ updateProduct.isFetching }}"
      initialData="{{ productsTable.selectedSourceRow }}"
      loading="{{ updateProduct.isFetching }}"
      marginType="normal"
      padding="12px"
      paddingType="normal"
      requireValidation={true}
      showBody={true}
      showFooter={true}
    >
      <Body>
        <TextInput
          id="editName"
          formDataKey="name"
          label="Name"
          labelPosition="top"
          marginType="normal"
          placeholder="Enter product name"
          required={true}
        />
        <TextArea
          id="editDescription"
          autoResize={true}
          formDataKey="description"
          label="Description"
          labelPosition="top"
          marginType="normal"
          minLines={2}
          placeholder="Enter description"
        />
        <Select
          id="editCategory"
          emptyMessage="No options"
          formDataKey="category"
          itemMode="static"
          label="Category"
          labelPosition="top"
          marginType="normal"
          placeholder="Select category"
          required={true}
          showSelectionIndicator={true}
        >
          <Option id="j7k8l" value="Electronics" />
          <Option id="m9n0o" value="Clothing" />
          <Option id="p1q2r" value="Books" />
        </Select>
      </Body>
      <Footer>
        <Button
          id="editCancelBtn"
          marginType="normal"
          styleVariant="outline"
          text="Cancel"
        >
          <Event
            id="33cc44dd"
            event="click"
            method="hide"
            params={{}}
            pluginId="editModal"
            type="widget"
            waitMs="0"
            waitType="debounce"
          />
        </Button>
        <Button
          id="editSaveBtn"
          marginType="normal"
          submit={true}
          submitTargetId="EditProductForm"
          text="Save"
        />
      </Footer>
      <Event
        id="55ee66ff"
        event="submit"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="updateProduct"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Form>
  </Body>
</ModalFrame>
