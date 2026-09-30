<Container
  id="tabbedContainer2"
  currentViewKey="{{ self.viewKeys[0] }}"
  hoistFetching={true}
  showBody={true}
  showHeader={true}
>
  <Header>
    <Tabs
      id="tabs1"
      itemMode="static"
      navigateContainer={true}
      targetContainerId="tabbedContainer2"
      value="{{ self.values[0] }}"
    >
      <Option id="4f6f9" value="Tab 1" />
      <Option id="b435d" value="Tab 2" />
      <Option id="52d1f" value="Tab 3" />
    </Tabs>
  </Header>
  <View id="7d34a" viewKey="Search Store Inventory">
    <TextInput
      id="searchInventoryTextInput"
      _disclosedFields={{ array: [] }}
      label="Search by title, author, category, ISBN"
      placeholder="Search by title, author, category, ISBN"
    />
    <Include src="./container1.rsx" />
  </View>
  <View id="505e6" viewKey="Add Books">
    <TextInput
      id="searchBookOnlineTextInput"
      _disclosedFields={{ array: [] }}
      label="Search by title, author, category, ISBN"
      placeholder="Search inventory"
    >
      <Event
        event="change"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="returnKeyTextInput"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </TextInput>
    <Button
      id="button9"
      _disclosedFields={{ array: [] }}
      text="Search Internet"
    >
      <Event
        event="click"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="searchBookByBookName"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </Button>
    <Modal
      id="modal1"
      buttonText="Add book to Inventory"
      hidden="true"
      modalHeightType="auto"
    >
      <Form
        id="form4"
        hoistFetching={true}
        initialData=""
        requireValidation={true}
        scroll={true}
        showBody={true}
        showFooter={true}
        showHeader={true}
      >
        <Header>
          <Text
            id="formTitle5"
            _disclosedFields={{ array: [] }}
            value="#### {{onlineBookSearchResultsTable.selectedRow.data.title}} by {{onlineBookSearchResultsTable.selectedRow.data.author_name}}"
            verticalAlign="center"
          />
        </Header>
        <Body>
          <Image
            id="image2"
            _disclosedFields={{ array: [] }}
            horizontalAlign="center"
            src="https://covers.openlibrary.org/b/id/{{onlineBookSearchResultsTable.selectedRow.data.cover_i}}.jpg"
          />
          <NumberInput
            id="numberInput8"
            _disclosedFields={{ array: [] }}
            currency="USD"
            format="currency"
            formDataKey="price"
            inputValue={0}
            label="Price"
            placeholder="Enter value"
            required={true}
            showSeparators={true}
            showStepper={true}
            value=""
          />
          <Select
            id="select8"
            data="{{onlineBookSearchResultsTable.selectedRow.data.isbn}}"
            emptyMessage="No options"
            formDataKey="isbn"
            label="ISBN"
            overlayMaxHeight={375}
            placeholder="Choose an ISBN"
            showSelectionIndicator={true}
          />
          <NumberInput
            id="numberInput9"
            _disclosedFields={{ array: [] }}
            currency="USD"
            formDataKey="quantity_in_stock"
            inputValue={0}
            label="Quantity in stock"
            placeholder="Enter value"
            required={true}
            showSeparators={true}
            showStepper={true}
            value={0}
          />
          <Select
            id="select7"
            data="{{ getBooksDataForModal.data }}"
            emptyMessage="No options"
            formDataKey="category"
            imageByIndex="{{ item.cover_image }}"
            label="Category"
            labels="{{ item.category }}"
            overlayMaxHeight={375}
            placeholder="Select a Category"
            required={true}
            showSelectionIndicator={true}
            values="{{ item.category }}"
          />
          <TextInput
            id="textInput23"
            _disclosedFields={{ array: [] }}
            formDataKey="bookshelf"
            label="Bookshelf"
            placeholder="Bookshelf Name"
          />
          <TextInput
            id="textInput18"
            _disclosedFields={{ array: [] }}
            formDataKey="book_id"
            label="Book ID"
            placeholder="Enter value"
            required={true}
            value="{{formatDataAsArray(getBooksDataForModal.data).length + 1}} "
          />
          <TextInput
            id="textInput19"
            _disclosedFields={{ array: [] }}
            formDataKey="title"
            label="Title"
            placeholder="Enter value"
            required={true}
            value="{{onlineBookSearchResultsTable.selectedRow.data.title}}"
          />
          <TextInput
            id="textInput20"
            _disclosedFields={{ array: [] }}
            formDataKey="author"
            label="Author"
            placeholder="Enter value"
            required={true}
            value="{{onlineBookSearchResultsTable.selectedRow.data.author_name['0']}}"
          />
          <TextInput
            id="textInput22"
            _disclosedFields={{ array: [] }}
            formDataKey="cover_image"
            label="Cover image"
            placeholder="Enter value"
            value="https://covers.openlibrary.org/b/id/{{onlineBookSearchResultsTable.selectedRow.data.cover_i}}.jpg"
          />
          <DateTime
            id="dateTime1"
            _disclosedFields={{ array: [] }}
            dateFormat="MMM d, yyyy"
            datePlaceholder="{{ self.dateFormat.toUpperCase() }}"
            formDataKey="created_at"
            iconBefore="bold/interface-calendar"
            label="Created at"
            minuteStep={15}
            required={true}
            value="{{ new Date() }}"
          />
          <DateTime
            id="dateTime2"
            _disclosedFields={{ array: [] }}
            dateFormat="MMM d, yyyy"
            datePlaceholder="{{ self.dateFormat.toUpperCase() }}"
            formDataKey="last_updated_at"
            iconBefore="bold/interface-calendar"
            label="Last updated at"
            minuteStep={15}
            required={true}
            value="{{ new Date() }}"
          />
        </Body>
        <Footer>
          <Button
            id="formButton5"
            _disclosedFields={{ array: [] }}
            submit={true}
            submitTargetId="form4"
            text="Submit"
          />
        </Footer>
        <Event
          event="submit"
          method="trigger"
          params={{ ordered: [] }}
          pluginId="addBookFromModal"
          type="datasource"
          waitMs="0"
          waitType="debounce"
        />
        <Event
          event="submit"
          method="trigger"
          params={{ ordered: [] }}
          pluginId="closeAddBookModal"
          type="datasource"
          waitMs="0"
          waitType="debounce"
        />
        <Event
          event="submit"
          method="setCurrentView"
          params={{ ordered: [{ viewKey: '"Store Inventory"' }] }}
          pluginId="tabbedContainer1"
          type="widget"
          waitMs="0"
          waitType="debounce"
        />
      </Form>
    </Modal>
    <TableLegacy
      id="onlineBookSearchResultsTable"
      _columns={[
        "score",
        "title",
        "author_name",
        "edition_count",
        "first_publish_year",
        "isbn",
        "cover_i",
        "ia",
        "subject",
        "edition_key",
      ]}
      _columnSummaryTypes={{ ordered: [{ category: "" }, { price: "sum" }] }}
      _columnSummaryValues={{ ordered: [{ category: "" }, { price: "" }] }}
      _columnVisibility={{
        ordered: [
          { cover_image: false },
          { created_at: false },
          { last_updated_at: false },
          { edition_key: false },
        ],
      }}
      _compatibilityMode={false}
      actionButtons={[
        {
          ordered: [
            { actionButtonText: "Add to Inventory" },
            { actionButtonType: "runQuery" },
            { actionButtonQuery: "openModal" },
            { actionButtonInternalUrlPath: "" },
            { actionButtonInternalUrlQuery: "" },
            { actionButtonUrl: "" },
            { actionButtonNewWindow: false },
            { actionButtonDisabled: "" },
          ],
        },
      ]}
      columnAlignment={{ ordered: [{ category: "left" }, { price: "right" }] }}
      columnEditable={{
        ordered: [
          { title: false },
          { title_suggest: false },
          { isbn: true },
          { first_published: false },
        ],
      }}
      columnFormats={{
        ordered: [
          { category: "SingleTagDataCell" },
          { price: "CurrencyDataCell" },
        ],
      }}
      columnMappers={{
        ordered: [
          { category: "" },
          { author_name: "{{self['0']}}" },
          { ia: "{{self['0']}}" },
        ],
      }}
      columnTypeProperties={{
        ordered: [
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
            price: {
              ordered: [
                { showSeparators: true },
                { currency: "USD" },
                { padDecimal: true },
              ],
            },
          },
        ],
      }}
      columnWidths={[
        { object: { id: "title", value: 284.4296875 } },
        { object: { id: "title_suggest", value: 183 } },
        { object: { id: "key", value: 171 } },
        { object: { id: "seed", value: 176 } },
        { object: { id: "author_name", value: 173 } },
        { object: { id: "publisher_facet", value: 148 } },
        { object: { id: "isbn", value: 285 } },
        { object: { id: "cover_i", value: 132 } },
        { object: { id: "edition_count", value: 211 } },
        { object: { id: "__retool__action_list", value: 165 } },
      ]}
      data="{{transformerSearchBooksByBookName.value}}"
      defaultSortByColumn="score"
      defaultSortDescending={true}
      doubleClickToEdit={true}
      hidden="{{searchBookOnlineTextInput.value === ''}} "
      maintainSpaceWhenHidden={false}
      rowColor="{{i === 0 ? 'green':''}}"
      showBoxShadow={false}
    />
  </View>
</Container>
