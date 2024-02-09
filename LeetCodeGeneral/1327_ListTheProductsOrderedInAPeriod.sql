SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o on o.product_id=p.product_id
WHERE o.order_date >= DATE('February 1 2020') AND o.order_date < DATE('February 1 2020') + INTERVAL '1 month'
GROUP BY p.product_name
HAVING SUM(o.unit)>=100
