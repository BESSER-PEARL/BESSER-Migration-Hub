SELECT
    COUNT(o.order_id) AS total_books_sold,
    SUM(o.total_amount) AS total_revenue,
    AVG(o.total_amount) AS average_sale_price,
    SUM(CASE WHEN o.discount_code_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(o.order_id)::float AS discount_utilization_rate
FROM
    orders o
WHERE
    o.created_at >= CURRENT_DATE - INTERVAL '{{reportDateRange.value}}'