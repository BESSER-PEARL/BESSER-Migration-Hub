<Container
  id="container1"
  hoistFetching={true}
  showBody={true}
  showHeader={true}
>
  <Header>
    <Text
      id="containerTitle1"
      _disclosedFields={{ array: [] }}
      value="#### Store Inventory"
      verticalAlign="center"
    />
  </Header>
  <View id="a6e1b" viewKey="View 1">
    <TableLegacy
      id="booksInventoryTable"
      _columns={[
        "title",
        "quantity_in_stock",
        "book_id",
        "isbn",
        "author",
        "category",
        "price",
        "cover_image",
        "bookshelf",
        "created_at",
        "last_updated_at",
      ]}
      _columnSummaryTypes={{
        ordered: [
          { price: "sum" },
          { ratings: "average" },
          { publication_date: "" },
          { category: "" },
          { publisher: "" },
          { book_id: "" },
        ],
      }}
      _columnSummaryValues={{
        ordered: [
          { price: "" },
          { ratings: "" },
          { publication_date: "" },
          { category: "" },
          { publisher: "" },
          { book_id: "" },
        ],
      }}
      _columnVisibility={{
        ordered: [
          { bookshelf: false },
          { publication_date: false },
          { image_url: false },
          { author: true },
          { cover_image: false },
          { ratings: false },
          { isbn: true },
          { publisher: false },
          { description: false },
        ],
      }}
      _compatibilityMode={false}
      actionButtons={[
        {
          ordered: [
            { actionButtonText: "Checkout" },
            { actionButtonType: "runQuery" },
            { actionButtonQuery: "openCheckoutModal" },
            { actionButtonInternalUrlPath: "" },
            { actionButtonInternalUrlQuery: "" },
            { actionButtonUrl: "" },
            { actionButtonNewWindow: false },
            { actionButtonDisabled: "" },
          ],
        },
      ]}
      columnAlignment={{
        ordered: [
          { price: "right" },
          { ratings: "left" },
          { publication_date: "left" },
          { category: "left" },
          { publisher: "left" },
          { book_id: "left" },
        ],
      }}
      columnFormats={{
        ordered: [
          { price: "CurrencyDataCell" },
          { ratings: "RatingDataCell" },
          { publication_date: "DateDataCell" },
          { category: "SingleTagDataCell" },
          { publisher: "SingleTagDataCell" },
          { book_id: "TextDataCell" },
        ],
      }}
      columnMappers={{ ordered: [{ category: "" }, { publisher: "" }] }}
      columnTypeProperties={{
        ordered: [
          {
            price: {
              ordered: [
                { showSeparators: true },
                { currency: "USD" },
                { padDecimal: true },
              ],
            },
          },
          { ratings: { ordered: [] } },
          { publication_date: { ordered: [{ dateFormat: "MMM d, yyyy" }] } },
          {
            category: {
              ordered: [
                { optionData: "{{ currentColumn }}" },
                { colorMode: "auto" },
                { allowCustomValue: true },
                { optionLabels: { array: [] } },
                { optionColors: { array: [] } },
                { optionValues: { array: [] } },
              ],
            },
          },
          {
            publisher: {
              ordered: [
                { optionData: "{{ currentColumn }}" },
                { colorMode: "auto" },
                { allowCustomValue: true },
                { optionLabels: { array: [] } },
                { optionColors: { array: [] } },
                { optionValues: { array: [] } },
              ],
            },
          },
          { book_id: { ordered: [] } },
        ],
      }}
      columnWidths={[
        { object: { id: "title", value: 202 } },
        { object: { id: "ratings", value: 172 } },
        { object: { id: "publication_date", value: 138 } },
        { object: { id: "publisher", value: 185 } },
        { object: { id: "author", value: 132 } },
        { object: { id: "__retool__action_list", value: 124 } },
        { object: { id: "isbn", value: 148 } },
        { object: { id: "category", value: 154 } },
        { object: { id: "last_updated_at", value: 178 } },
      ]}
      data="{{ formatDataAsArray(getBooksFromStock.data) }}"
      defaultSortByColumn="last_updated_at"
      defaultSortDescending={true}
      doubleClickToEdit={true}
      hidden=""
      showBoxShadow={false}
    />
    <Form
      id="form5"
      hidden=""
      hoistFetching={true}
      initialData="{{booksInventoryTable.selectedRow.data}}"
      requireValidation={true}
      resetAfterSubmit={true}
      scroll={true}
      showBody={true}
      showFooter={true}
      showHeader={true}
    >
      <Header>
        <Text
          id="formTitle6"
          _disclosedFields={{ array: [] }}
          value="#### {{booksInventoryTable.selectedRow.data.title}}"
          verticalAlign="center"
        />
      </Header>
      <Body>
        <NumberInput
          id="numberInput11"
          _disclosedFields={{ array: [] }}
          currency="USD"
          formDataKey="quantity_in_stock"
          inputValue={0}
          label="Quantity in stock"
          labelWidth="50"
          placeholder="Enter value"
          required={true}
          showSeparators={true}
          showStepper={true}
          value={0}
        />
        <Image
          id="image3"
          _disclosedFields={{ array: [] }}
          horizontalAlign="center"
          src="{{booksInventoryTable.selectedRow.data.cover_image}}"
        />
        <TextInput
          id="textInput29"
          _disclosedFields={{ array: [] }}
          formDataKey="bookshelf"
          label="Bookshelf"
          labelWidth="50"
          placeholder="Enter value"
          required={true}
        />
        <NumberInput
          id="numberInput10"
          _disclosedFields={{ array: [] }}
          currency="USD"
          format="currency"
          formDataKey="price"
          inputValue={0}
          label="Price"
          labelWidth="50"
          placeholder="Enter value"
          required={true}
          showSeparators={true}
          showStepper={true}
          value={0}
        />
        <TextInput
          id="textInput24"
          _disclosedFields={{ array: [] }}
          formDataKey="book_id"
          label="Book ID"
          placeholder="Enter value"
          required={true}
        />
        <TextInput
          id="textInput25"
          _disclosedFields={{ array: [] }}
          formDataKey="title"
          label="Title"
          placeholder="Enter value"
          required={true}
        />
        <TextInput
          id="textInput26"
          _disclosedFields={{ array: [] }}
          formDataKey="author"
          label="Author"
          placeholder="Enter value"
          required={true}
        />
        <TextInput
          id="textInput27"
          _disclosedFields={{ array: [] }}
          formDataKey="isbn"
          label="Isbn"
          placeholder="Enter value"
          required={true}
        />
        <Select
          id="select9"
          data="{{ getBooksFromStock.data }}"
          emptyMessage="No options"
          formDataKey="category"
          imageByIndex="{{ item.cover_image }}"
          label="Category"
          labels="{{ item.category }}"
          overlayMaxHeight={375}
          placeholder="Select an option"
          required={true}
          showSelectionIndicator={true}
          values="  {{ item.category }}"
        />
        <TextInput
          id="textInput28"
          _disclosedFields={{ array: [] }}
          formDataKey="cover_image"
          label="Cover image"
          placeholder="Enter value"
          required={true}
        />
      </Body>
      <Footer>
        <Button
          id="button8"
          _disclosedFields={{ array: [] }}
          style={{ ordered: [{ background: "danger" }] }}
          text="Delete Book"
        >
          <Event
            event="click"
            method="trigger"
            params={{ ordered: [] }}
            pluginId="deleteBook"
            type="datasource"
            waitMs="0"
            waitType="debounce"
          />
        </Button>
        <Button
          id="formButton6"
          _disclosedFields={{ array: [] }}
          submit={true}
          submitTargetId="form5"
          text="Save"
        />
      </Footer>
      <Event
        event="submit"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="updateBook"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Form>
    <Button
      id="button10"
      _disclosedFields={{ array: [] }}
      text="Refresh Table ({{booksInventoryTable.data.title.length}} Records)"
    >
      <Event
        event="click"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getBooksFromStock"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Button>
    <Include src="./checkoutModal.rsx" />
  </View>
</Container>
