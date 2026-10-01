<SplitPaneFrame
  id="detailPane"
  _resizeHandleEnabled={true}
  enableFullBleed={true}
  hidden="{{ !membersTable.selectedRow.id }}"
  position="right"
  width="{{ { details: '400px', activity: '550px' }?.[detailTabs.value] ?? '400px' }}"
>
  <Include src="./detailContainer.rsx" />
</SplitPaneFrame>
