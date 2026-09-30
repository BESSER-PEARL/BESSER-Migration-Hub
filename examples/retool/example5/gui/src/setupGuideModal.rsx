<ModalFrame
  id="setupGuideModal"
  hideOnEscape={true}
  overlayInteraction="close"
  showOverlay={true}
  size="medium"
>
  <Header>
    <Text
      id="setupGuideTitle"
      marginType="normal"
      value="## 🚀 Setup Guide"
      verticalAlign="center"
    />
  </Header>
  <Body>
    <Text
      id="setupGuideText"
      marginType="normal"
      value="{{ 'Welcome! This app is loaded with **sample data** so you can click around and explore right away.\n\nWhen you are ready to wire up your real database, follow these steps:\n\n1. 🔌 **Connect your database** — Go to *Resources* in Retool and add your DB\n2. 🔄 **Update queries** — Open each query in the bottom panel and switch the Resource\n3. 📝 **Update table/column names** — Edit the SQL in each query to match your schema\n4. 🧹 **Remove mock data** — In each Table/Select, remove the mock array fallback from the data attribute\n5. 🗑️ **Delete this modal** — Remove this Setup Guide and the setupGuideBtn button\n\n✅ You are all set — happy building!' }}"
    />
  </Body>
</ModalFrame>
