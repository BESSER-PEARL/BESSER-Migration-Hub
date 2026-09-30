const newData = []
const data = {{searchBookByBookName.data.docs}}

const matchingBooks = data.filter(book => book.cover_i);

const sortedData = matchingBooks.sort((a, b) => b.score - a.score);


return(sortedData)


// let bookObj ={}
// sortedData.forEach(result => {
//   bookObj = {
//   "title":result.title,
//   "title_suggest": result.title_suggest,
//   "isbn":result.isbn,
//   "first_published":result.first_published
//   }
//   newData.push(bookObj)
// });



// const matchingBooks = newData.filter(book => {
//   const isbnArray = book.isbn;
//   return isbnArray.some(isbn => isbn.includes(filter_text));
// });

// return matchingBooks;

