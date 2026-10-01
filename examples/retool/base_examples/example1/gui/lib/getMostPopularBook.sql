SELECT 
    b.title,
    b.author,
    SUM(o.total_amount) AS total_sales,
    b.category as Category,
    COUNT(*) AS total_books_sold
FROM 
    books b 
    JOIN orders o ON b.book_id = o.book_id 
    LEFT JOIN discount_codes d ON o.discount_code_id = d.discount_code_id 
WHERE 
    o.created_at >= CURRENT_DATE - INTERVAL '{{reportDateRange.value}}'
GROUP BY 
    b.book_id
ORDER BY 
    total_sales DESC;
