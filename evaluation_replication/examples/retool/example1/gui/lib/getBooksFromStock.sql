SELECT * FROM books
WHERE title || author || ISBN || category ILIKE '%{{searchInventoryTextInput.value}}%' order by title ASC;