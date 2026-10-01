<App>
  <Include src="./functions.rsx" />
  <AppStyles id="$appStyles" css="" />
  <Include src="./header.rsx" />
  <Frame
    id="$main"
    isHiddenOnDesktop={false}
    isHiddenOnMobile={false}
    sticky={false}
    type="main"
  >
    <Text
      id="text1"
      _disclosedFields={{ array: [] }}
      horizontalAlign="center"
      value="## New York's Best Small Bookstore"
      verticalAlign="center"
    />
    <Include src="./src/tabbedContainer1.rsx" />
  </Frame>
</App>
