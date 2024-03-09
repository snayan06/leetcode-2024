-- This query retrieves information about sales, including the product name, year, and price.
-- It uses a LEFT JOIN to include all sales records from the "Sales" table, even if there is no matching product in the "Product" table.

SELECT p.product_name, s.year, s.price
FROM Sales AS s
LEFT JOIN Product AS p ON s.product_id = p.product_id;
