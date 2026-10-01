SELECT
    b.category AS category,
    COUNT(*) AS total_books_sold
FROM
    books b
    JOIN orders o ON b.book_id = o.book_id
WHERE
    o.created_at >= CURRENT_DATE - INTERVAL '{{reportDateRange.value}}'
GROUP BY
    b.category
ORDER BY
    total_books_sold DESC;