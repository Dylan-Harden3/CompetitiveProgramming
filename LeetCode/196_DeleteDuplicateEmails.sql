DELETE
FROM Person p
WHERE p.email IN (
    SELECT p2.email
    FROM Person p2
    WHERE p2.email = p.email
    AND p2.id < p.id
)
