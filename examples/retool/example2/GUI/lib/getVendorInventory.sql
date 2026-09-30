SELECT 
    i.sku,
    iv.available_quantity,
    iv.vendor_name
FROM 
    inventory i
INNER JOIN 
    vendor_inventory iv 
ON 
    i.id = iv.sku;