SELECT visited_on,
    SUM(amount) OVER (ORDER BY visited_on rows 6 preceding) AS amount,
    ROUND(AVG(amount) OVER (ORDER BY visited_on rows 6 preceding), 2) AS average_amount
FROM
(SELECT visited_on, SUM(amount) as amount
FROM Customer
GROUP BY visited_on)
ORDER BY visited_on
OFFSET 6
