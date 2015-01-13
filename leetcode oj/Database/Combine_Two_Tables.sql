## Combine Two Tables
SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person AS P
LEFT JOIN Address AS A
ON A.PersonId = P.PersonId
