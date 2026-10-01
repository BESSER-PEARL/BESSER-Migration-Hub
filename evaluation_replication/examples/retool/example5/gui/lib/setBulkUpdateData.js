// Collect all currently displayed (filtered) rows for bulk update
const displayedRows = membersTable.displayedData || [];

if (displayedRows.length === 0) {
  utils.showNotification({
    title: "No rows to update",
    description: "Apply filters first to select which members to update.",
    notificationType: "warning"
  });
  return;
}

bulkUpdateData.setValue(displayedRows);
isBulkUpdate.setValue(true);
confirmBulkUpdate.show();
