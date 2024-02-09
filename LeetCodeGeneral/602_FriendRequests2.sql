-- Write your PostgreSQL query statement below
SELECT id, SUM(num) AS num
FROM (
SELECT requester_id AS id, COUNT(accepter_id) as num
FROM RequestAccepted
GROUP BY requester_id
UNION ALL
SELECT accepter_id AS id, COUNT(accepter_id) as num
FROM RequestAccepted
GROUP BY accepter_id)
GROUP BY id
ORDER BY num DESC
LIMIT 1
