# Write your MySQL query statement below
SELECT E1.NAME
FROM EMPLOYEE E1
INNER JOIN EMPLOYEE E2
ON E1.ID = E2.MANAGERID
GROUP BY e2.managerid
HAVING count(e2.managerid)>=5