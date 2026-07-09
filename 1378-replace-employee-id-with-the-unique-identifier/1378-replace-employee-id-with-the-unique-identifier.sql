# Write your MySQL query statement below
SELECT UNIQUE_ID,NAME
FROM Employees
LEFT JOIN EmployeeUNI ON employees.id=employeeUNI.id
