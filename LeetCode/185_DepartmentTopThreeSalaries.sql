SELECT Department, Employee, Salary
FROM (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rank
    FROM Employee e
    JOIN Department d
    ON d.id=e.departmentId
    ORDER BY e.departmentId, e.salary DESC)
WHERE rank <= 3
