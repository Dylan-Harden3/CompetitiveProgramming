WITH Rankings AS (
    SELECT id, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM Employee
)

SELECT 
    CASE 
        WHEN EXISTS
        (
            SELECT 1
            FROM Rankings
            WHERE rank=2
        ) THEN
        (
            SELECT Salary
            FROM Rankings
            WHERE rank=2
            LIMIT 1
        ) ELSE NULL END AS SecondHighestSalary





















