SELECT sell_date, num_sold, products
FROM (
    SELECT sell_date, COUNT(DISTINCT product) AS num_sold, STRING_AGG(DISTINCT product, ',') AS products
    FROM Activities
    GROUP BY sell_date
    ORDER BY num_sold DESC, MAX(product))
ORDER BY sell_date
