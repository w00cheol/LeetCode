SELECT
    D.name as Department,
    E.name as Employee,
    E.salary as Salary
FROM
    Employee E
INNER JOIN
    (
        SELECT
            departmentId, max(salary) as maxSalary
        FROM
            Employee
        GROUP BY
            departmentId
    ) R
ON
    R.departmentId = E.departmentId AND
    R.maxSalary = E.salary
LEFT JOIN
    Department D
ON
    D.id = E.departmentId