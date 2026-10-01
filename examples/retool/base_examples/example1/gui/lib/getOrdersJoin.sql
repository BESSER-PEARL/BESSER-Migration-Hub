SELECT *
FROM books
INNER JOIN orders
ON books.book_id = orders.book_id
LEFT JOIN discount_codes
ON orders.discount_code_id = discount_codes.discount_code_id
ORDER BY orders.order_id ASC;