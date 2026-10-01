<Screen
  id="addInventory"
  _customShortcuts={[]}
  _hashParams={[]}
  _order={0}
  _searchParams={[]}
  browserTitle=""
  title={null}
  urlSlug=""
  uuid="0d85df8b-a4ab-46ef-9b5f-9f7b283ab9e0"
>
  <SqlQueryUnified
    id="form1SubmitToInventory"
    actionType="INSERT"
    changeset={
      '[{"key":"sku","value":"{{ skuInput.value }}"},{"key":"description","value":"{{ descriptionInput.value }}"},{"key":"quantity","value":"{{ quantityInput.value }}"},{"key":"replenish","value":"{{ replenishInput.value }}"},{"key":"location","value":"{{ locationInput.value }}"},{"key":"image_url","value":"{{ imageUrlInput.value }}"}]'
    }
    changesetObject="{{ form1.data }}"
    editorMode="gui"
    notificationDuration={4.5}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    runWhenModelUpdates={false}
    showSuccessToaster={false}
    tableName="inventory"
  />
  <SqlQueryUnified
    id="getLocations"
    query={include("../lib/getLocations.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    warningCodes={[]}
  />
  <Frame
    id="$main2"
    enableFullBleed={false}
    isHiddenOnDesktop={false}
    isHiddenOnMobile={false}
    padding="8px 12px"
    sticky={null}
    type="main"
  >
    <Container
      id="container1"
      footerPadding="4px 12px"
      headerPadding="4px 12px"
      padding="12px"
      showBody={true}
      showHeader={true}
    >
      <Header>
        <Text
          id="containerTitle1"
          value="#### Add inventory"
          verticalAlign="center"
        />
      </Header>
      <View id="b5a7d" viewKey="View 1">
        <Form
          id="form1"
          footerPadding="4px 12px"
          headerPadding="4px 12px"
          padding="12px"
          requireValidation={true}
          resetAfterSubmit={true}
          scroll={true}
          showBody={true}
          showFooter={true}
          showHeader={true}
        >
          <Header>
            <Text
              id="formTitle1"
              value="#### Inventory item"
              verticalAlign="center"
            />
          </Header>
          <Body>
            <TextArea
              id="skuInput"
              autoResize={true}
              formDataKey="sku"
              label="SKU"
              labelPosition="top"
              minLines={2}
              placeholder="Enter value"
              required={true}
            />
            <TextArea
              id="descriptionInput"
              autoResize={true}
              formDataKey="description"
              label="Description"
              labelPosition="top"
              minLines={2}
              placeholder="Enter value"
              required={true}
            />
            <NumberInput
              id="quantityInput"
              currency="USD"
              formDataKey="quantity"
              inputValue={0}
              label="Quantity"
              labelPosition="top"
              placeholder="Enter value"
              required={true}
              showSeparators={true}
              showStepper={true}
              value={0}
            />
            <NumberInput
              id="replenishInput"
              currency="USD"
              formDataKey="replenish"
              inputValue={0}
              label="Replenish"
              labelPosition="top"
              placeholder="Enter value"
              required={true}
              showSeparators={true}
              showStepper={true}
              value={0}
            />
            <Select
              id="locationInput"
              data="{{ getLocations.data }}"
              emptyMessage="No options"
              formDataKey="location"
              label="Location"
              labelPosition="top"
              labels={null}
              overlayMaxHeight={375}
              placeholder="Select an option"
              required={true}
              showSelectionIndicator={true}
              values="{{ item.location }}"
            />
            <TextInput
              id="imageUrlInput"
              formDataKey="image_url"
              label="Image URL"
              labelPosition="top"
              patternType="url"
              placeholder="retool.com"
              required={true}
              textBefore="https://"
            />
          </Body>
          <Footer>
            <Button
              id="formButton1"
              submit={true}
              submitTargetId="form1"
              text="Submit"
            />
          </Footer>
          <Event
            event="submit"
            method="trigger"
            params={{}}
            pluginId="form1SubmitToInventory"
            type="datasource"
            waitMs="0"
            waitType="debounce"
          />
        </Form>
      </View>
    </Container>
  </Frame>
</Screen>
