SELECT 
    DATE_TRUNC('day', created_at) AS order_day,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_sales
FROM 
    orders o
WHERE 
    o.created_at >= CURRENT_DATE - INTERVAL '{{reportDateRange.value}}'
GROUP BY 
    order_day 
ORDER BY 
    order_day;
