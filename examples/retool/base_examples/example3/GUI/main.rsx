<App>
  <Include src="./functions.rsx" />
  <Include src="./src/editModal.rsx" />
  <Include src="./src/setupGuideModal.rsx" />
  <Frame
    id="$main"
    isHiddenOnDesktop={false}
    isHiddenOnMobile={false}
    padding="8px 12px"
    paddingType="normal"
    sticky={false}
    type="main"
  >
    <Text
      id="pageTitle"
      marginType="normal"
      value="### Products"
      verticalAlign="center"
    />
    <Button id="setupGuideBtn" marginType="normal" text="Setup Guide">
      <Event
        id="fa1b2c3d"
        event="click"
        method="show"
        params={{}}
        pluginId="setupGuideModal"
        type="widget"
        waitMs="0"
        waitType="debounce"
      />
    </Button>
    <Modal
      id="createModal"
      buttonText="Add product"
      closeOnOutsideClick={true}
      events={[]}
      modalHeightType="auto"
    >
      <Form
        id="CreateProductForm"
        disableSubmit="{{ insertProduct.isFetching }}"
        footerPadding="4px 12px"
        footerPaddingType="normal"
        headerPadding="4px 12px"
        headerPaddingType="normal"
        loading="{{ insertProduct.isFetching }}"
        marginType="normal"
        padding="12px"
        paddingType="normal"
        requireValidation={true}
        resetAfterSubmit={true}
        showBody={true}
        showFooter={true}
        showHeader={true}
      >
        <Header>
          <Text
            id="createFormTitle"
            marginType="normal"
            value="#### New product"
            verticalAlign="center"
          />
        </Header>
        <Body>
          <TextInput
            id="createName"
            formDataKey="name"
            label="Name"
            labelPosition="top"
            marginType="normal"
            placeholder="Enter product name"
            required={true}
          />
          <TextArea
            id="createDescription"
            autoResize={true}
            formDataKey="description"
            label="Description"
            labelPosition="top"
            marginType="normal"
            minLines={2}
            placeholder="Enter description"
          />
          <Select
            id="createCategory"
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
            <Option id="a1b2c" value="Electronics" />
            <Option id="d3e4f" value="Clothing" />
            <Option id="g5h6i" value="Books" />
          </Select>
        </Body>
        <Footer>
          <Button
            id="createClearBtn"
            marginType="normal"
            styleVariant="outline"
            text="Clear"
          >
            <Event
              id="aa11bb22"
              event="click"
              method="clear"
              params={{ ordered: [] }}
              pluginId="CreateProductForm"
              type="widget"
              waitMs="0"
              waitType="debounce"
            />
          </Button>
          <Button
            id="createSubmitBtn"
            marginType="normal"
            submit={true}
            submitTargetId="CreateProductForm"
            text="Create"
          />
        </Footer>
        <Event
          id="cc33dd44"
          event="submit"
          method="trigger"
          params={{ ordered: [] }}
          pluginId="insertProduct"
          type="datasource"
          waitMs="0"
          waitType="debounce"
        />
      </Form>
    </Modal>
    <Table
      id="productsTable"
      cellSelection="none"
      changesetArray={[]}
      clearChangesetOnSave={true}
      data="{{ Array.isArray(selectProducts.data) ? selectProducts.data : [{ id: 1, name: 'Organic Green Tea', description: 'Premium loose leaf', category: 'Beverages', price: 12.99, created_at: '2024-01-15' }, { id: 2, name: 'Vitamin D3 1000IU', description: 'Daily supplement', category: 'Supplements', price: 8.49, created_at: '2024-02-20' }, { id: 3, name: 'Almond Butter', description: 'Smooth, no added sugar', category: 'Food', price: 6.99, created_at: '2024-03-10' }] }}"
      defaultSelectedRow={{ mode: "index", indexType: "display", index: 0 }}
      enableSaveActions={true}
      heightType="auto"
      primaryKeyColumnId="c01a1"
      rowHeight="medium"
      searchMode="caseInsensitive"
      selectedDataIndexes={[]}
      selectedRowKeys={[]}
      selectedRows={[]}
      selectedSourceRows={[]}
      showBorder={true}
      showFooter={true}
      showHeader={true}
      sortArray={[]}
      templatePageSize={20}
    >
      <Column
        id="c01a1"
        alignment="left"
        editable={false}
        format="string"
        key="id"
        label="ID"
        position="center"
        size={60}
      />
      <Column
        id="c02b2"
        alignment="left"
        format="string"
        key="name"
        label="Name"
        position="center"
        size={200}
      />
      <Column
        id="c03c3"
        alignment="left"
        format="multilineString"
        key="description"
        label="Description"
        position="center"
        size={300}
      />
      <Column
        id="c04d4"
        alignment="left"
        format="tag"
        formatOptions={{ automaticColors: true }}
        key="category"
        label="Category"
        position="center"
        size={120}
      />
      <Column
        id="c05e5"
        alignment="right"
        format="decimal"
        formatOptions={{ showSeparators: true, notation: "standard" }}
        key="price"
        label="Price"
        position="center"
        size={100}
      />
      <Column
        id="c06f6"
        alignment="left"
        format="datetime"
        key="created_at"
        label="Created"
        position="center"
        size={140}
      />
      <Action id="a01a1" icon="bold/interface-edit-pencil" label="Edit">
        <Event
          id="ee55ff66"
          event="clickAction"
          method="run"
          params={{ map: { src: "editModal.show()" } }}
          pluginId=""
          type="script"
          waitMs="0"
          waitType="debounce"
        />
      </Action>
      <Action
        id="a02b2"
        icon="bold/interface-delete-bin-5-alternate"
        label="Delete"
      >
        <Event
          id="11aa22bb"
          event="clickAction"
          method="trigger"
          params={{ ordered: [] }}
          pluginId="deleteProduct"
          type="datasource"
          waitMs="0"
          waitType="debounce"
        />
      </Action>
    </Table>
  </Frame>
</App>
