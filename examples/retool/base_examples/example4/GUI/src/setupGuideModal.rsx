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
      value="## Setup Guide"
      verticalAlign="center"
    />
  </Header>
  <Body>
    <Text
      id="setupGuideText"
      marginType="normal"
      value="{{ 'Welcome! This app demonstrates **PlotlyChart** with Statistic KPIs and a data table.\n\nTo connect your real data source:\n\n1. Open the **fetchSalesData** and **fetchCategoryData** queries in the bottom panel and update the API URL — or replace them with a database query\n2. Select each **PlotlyChart** component and update the **Data** and **Layout** JSON to map your fields\n3. Update the **Statistic** component values to reference your query data\n4. Remove the mock data fallback from the **salesTable** data property\n5. Delete this Setup Guide modal and the Setup Guide button\n\nCharts use Plotly.js — see plotly.com/javascript for layout and trace options.' }}"
    />
  </Body>
</ModalFrame>
