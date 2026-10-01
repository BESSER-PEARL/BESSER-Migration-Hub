<Modal id="checkoutModal" buttonText="Open Modal" hidden="true">
  <Text
    id="text2"
    _disclosedFields={{ array: [] }}
    value="#### {{booksInventoryTable.selectedRow.data.title}}"
    verticalAlign="center"
  />
  <Image
    id="image4"
    _disclosedFields={{ array: [] }}
    horizontalAlign="center"
    src="{{booksInventoryTable.selectedRow.data.cover_image}}"
  />
  <Text
    id="text3"
    _disclosedFields={{ array: [] }}
    value="###### by {{booksInventoryTable.selectedRow.data.author}}"
    verticalAlign="center"
  />
  <TextInput
    id="textInput30"
    _disclosedFields={{ array: [] }}
    label="Price"
    placeholder="Enter value"
    value="{{booksInventoryTable.selectedRow.data.price}}"
  />
  <Select
    id="select10"
    data="{{ getDiscountCodes.data }}"
    emptyMessage="No options"
    label="Discount Code"
    overlayMaxHeight={375}
    placeholder="Select an option"
    showSelectionIndicator={true}
    values="{{ item.discount_code }}"
  />
  <TextInput
    id="textInput31"
    _disclosedFields={{ array: [] }}
    label="Discount Percent"
    placeholder="Enter value"
    value="{{getDiscountPercent.data.discount_percent['0']*100}}"
  />
  <TextInput
    id="textInput33"
    _disclosedFields={{ array: [] }}
    label="Discount Code ID"
    placeholder="Enter value"
    value="{{getDiscountPercent.data.discount_code_id['0']}}"
  />
  <TextInput
    id="textInput32"
    _disclosedFields={{ array: [] }}
    label="Total"
    placeholder="Enter value"
    value="{{calculateCheckoutTotal.value}}"
  />
  <Button
    id="button11"
    _disclosedFields={{ array: [] }}
    style={{ ordered: [{ background: "success" }] }}
    text="Checkout"
  >
    <Event
      event="click"
      method="trigger"
      params={{ ordered: [] }}
      pluginId="createNewOrder"
      type="datasource"
      waitMs="0"
      waitType="debounce"
    />
  </Button>
</Modal>
