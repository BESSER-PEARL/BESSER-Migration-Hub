<GlobalFunctions>
  <Folder id="books">
    <SqlQueryUnified
      id="updateBook"
      actionType="UPDATE_BY"
      changeset={'[{"key":"publisher","value":"{{form1.data.publisher}}"}]'}
      changesetIsObject={true}
      changesetObject="{{form5.data}}"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={
        '[{"key":"isbn","value":"{{booksInventoryTable.selectedRow.data.isbn}}","operation":"="}]'
      }
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="books"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getBooksFromStock"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <SqlQueryUnified
      id="getBooksFromStock"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getBooksFromStock.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      resourceTypeOverride=""
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="deleteBook"
      actionType="DELETE_BY"
      confirmationMessage="## Are you sure you want to delete the book {{booksInventoryTable.selectedRow.data.title}}?"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={
        '[{"key":"book_id","value":"{{booksInventoryTable.selectedRow.data.book_id}}","operation":"="}]'
      }
      requireConfirmation={true}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="books"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getBooksFromStock"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <RESTQuery
      id="searchBookByBookName"
      enableTransformer={true}
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query="https://openlibrary.org/search.json?q={{searchBookOnlineTextInput.value}}&fields=title,author_name,isbn,cover_i,edition_count,edition_key,first_publish_year,score,subject,ia"
      resourceName="REST-WithoutResource"
      resourceTypeOverride=""
      runWhenModelUpdates={false}
      transformer=""
    />
    <Function
      id="transformerSearchBooksByBookName"
      funcBody={include("./lib/transformerSearchBooksByBookName.js", "string")}
    />
    <SqlQueryUnified
      id="getBooksDataForModal"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getBooksDataForModal.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      resourceTypeOverride=""
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <JavascriptQuery
      id="openAddBookModal"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/openAddBookModal.js", "string")}
      resourceName="JavascriptQuery"
      showSuccessToaster={false}
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    />
    <SqlQueryUnified
      id="addBookFromModal"
      actionType="INSERT"
      changeset={
        '[{"key":"title","value":"Testing Book"},{"key":"publisher","value":"Harper Collins"},{"key":"author","value":"Test Author"},{"key":"category","value":"Python"},{"key":"isbn","value":"123"},{"key":"publication_date","value":"Mar 19, 2023"},{"key":"ratings","value":"4.0"},{"key":"price","value":"12"},{"key":"quantity","value":"10"}]'
      }
      changesetIsObject={true}
      changesetObject="{{form4.data}}"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="books"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getBooksFromStock"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <JavascriptQuery
      id="closeAddBookModal"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/closeAddBookModal.js", "string")}
      resourceName="JavascriptQuery"
      showSuccessToaster={false}
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    />
    <RESTQuery
      id="INACTIVE_getBookDetailsFromOpenLibrary"
      cacheKeyTtl={300}
      enableCaching={true}
      enableTransformer={true}
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query="http://openlibrary.org/api/books?format=json&bibkeys=ISBN:{{booksInventoryTable.selectedRow.data.isbn}}&jscmd=data&type=/type/edition|/type/work"
      resourceName="REST-WithoutResource"
      resourceTypeOverride=""
      transformer="return Object.entries(data)[0][1];"
    />
    <JavascriptQuery
      id="openCheckoutModal"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/openCheckoutModal.js", "string")}
      resourceName="JavascriptQuery"
      showSuccessToaster={false}
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    />
    <JavascriptQuery
      id="closeCheckoutModal"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/closeCheckoutModal.js", "string")}
      resourceName="JavascriptQuery"
      showSuccessToaster={false}
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    />
  </Folder>
  <Folder id="discountCodes">
    <SqlQueryUnified
      id="deleteDiscountCode"
      actionType="DELETE_BY"
      confirmationMessage="### Are you sure you want to delete the discount code {{discountCodesTable.selectedRow.data.discount_code}}?"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={
        '[{"key":"discount_code_id","value":"{{discountCodesTable.selectedRow.data.discount_code_id}}","operation":"="}]'
      }
      requireConfirmation={true}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="discount_codes"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getDiscountCodes"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <SqlQueryUnified
      id="addDiscountCode"
      actionType="INSERT"
      changeset="[]"
      changesetIsObject={true}
      changesetObject="{{form3.data}}"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="discount_codes"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getDiscountCodes"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <SqlQueryUnified
      id="getDiscountCodes"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getDiscountCodes.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="updateDiscountCodes"
      actionType="BULK_UPDATE_BY_KEY"
      bulkUpdatePrimaryKey="discount_code_id"
      changesetIsObject={true}
      changesetObject="{{discountCodesTable.recordUpdates}}"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={'[{"key":"","value":"","operation":"="}]'}
      records="{{discountCodesTable.recordUpdates}}"
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="discount_codes"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    />
    <SqlQueryUnified
      id="getDiscountPercent"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getDiscountPercent.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
  </Folder>
  <Folder id="sale">
    <SqlQueryUnified
      id="createNewOrder"
      actionType="INSERT"
      changeset={
        '[{"key":"total_amount","value":"{{textInput32.value}}"},{"key":"book_id","value":"{{booksInventoryTable.selectedRow.data.book_id}}"},{"key":"discount_code_id","value":"{{textInput33.value}}"}]'
      }
      confirmationMessage="### Are you sure you want to buy the book - {{booksInventoryTable.selectedRow.data.title}} for ${{textInput32.value}}?"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      requireConfirmation={true}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="orders"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="updateInventoryAfterSale"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="closeCheckoutModal"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <SqlQueryUnified
      id="deleteOrder"
      actionType="DELETE_BY"
      confirmationMessage="## Are you sure you want to delete the order {{ordersTable.selectedRow.data.order_id}}?"
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={
        '[{"key":"order_id","value":"{{ordersTable.selectedRow.data.order_id}}","operation":"="}]'
      }
      requireConfirmation={true}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="orders"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getOrdersJoin"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <SqlQueryUnified
      id="updateInventoryAfterSale"
      actionType="UPDATE_BY"
      changeset={
        '[{"key":"quantity_in_stock","value":"{{booksInventoryTable.selectedRow.data.quantity_in_stock - 1}}"}]'
      }
      editorMode="gui"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      filterBy={
        '[{"key":"book_id","value":"{{booksInventoryTable.selectedRow.data.book_id}}","operation":"="}]'
      }
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      runWhenModelUpdates={false}
      tableName="books"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
    >
      <Event
        event="success"
        method="trigger"
        params={{ ordered: [] }}
        pluginId="getBooksFromStock"
        type="datasource"
        waitMs="0"
        waitType="debounce"
      />
    </SqlQueryUnified>
    <Function
      id="calculateCheckoutTotal"
      funcBody={include("./lib/calculateCheckoutTotal.js", "string")}
    />
  </Folder>
  <Folder id="Orders">
    <SqlQueryUnified
      id="getOrdersJoin"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getOrdersJoin.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      resourceTypeOverride=""
      runWhenModelUpdates={false}
      runWhenPageLoads={true}
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
  </Folder>
  <Folder id="Reports">
    <SqlQueryUnified
      id="getSalesData"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getSalesData.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getMostPopularBook"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getMostPopularBook.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getMostPopularCategory"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getMostPopularCategory.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getSalesOverTime"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getSalesOverTime.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getDiscountReport"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getDiscountReport.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getInStock"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getInStock.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
    <SqlQueryUnified
      id="getOutOfStock"
      errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
      query={include("./lib/getOutOfStock.sql", "string")}
      resourceDisplayName="retool_db"
      resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
      transformer="// type your code here
// example: return formatDataAsArray(data).filter(row => row.quantity > 20)
return data"
      warningCodes={[]}
    />
  </Folder>
  <SqlQueryUnified
    id="getOrders"
    errorTransformer="// The variable 'data' allows you to reference the request's data in the transformer. 
// example: return data.find(element => element.isError)
return data.error"
    query={include("./lib/getOrders.sql", "string")}
    resourceDisplayName="retool_db"
    resourceName="34065358-ee82-4b8f-974f-0b7b918d3034"
    runWhenModelUpdates={false}
    runWhenPageLoads={true}
    transformer="let orders = {{formatDataAsArray(getOrders.data)}}
let books = {{formatDataAsArray(getBooksFromStock.data)}}
let discount_codes = {{formatDataAsArray(getDiscountCodes.data)}}
    
orders.forEach(order => {
  let foundBook;
  let foundCode;

  books.forEach(book => {
    if (book.hasOwnProperty('book_id') && book.book_id === order.book_id) {
      foundBook = book;
      order.title = foundBook.title;
    }
  });
  
  discount_codes.forEach(discount_code => {
    if (discount_code.hasOwnProperty('discount_code_id') && discount_code.discount_code_id === order.discount_code_id) {
      foundCode = discount_code;
      order.discount_percent = foundCode.discount_percent;
    }
  });
  
});

return(orders)"
    warningCodes={[]}
  />
</GlobalFunctions>
