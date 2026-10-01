SELECT
    d.discount_code,
    COUNT(o.order_id) AS times_used,
    SUM(o.total_amount) AS total_revenue
FROM
    orders o
    JOIN discount_codes d ON o.discount_code_id = d.discount_code_id
WHERE
    o.discount_code_id IS NOT NULL
    AND o.created_at >= CURRENT_DATE - INTERVAL '{{reportDateRange.value}}'
GROUP BY
    d.discount_code
ORDER BY
    times_used DESC;