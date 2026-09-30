SELECT
title, author, isbn, category, quantity_in_stock
FROM
  books b
WHERE
  b.quantity_in_stock = 0