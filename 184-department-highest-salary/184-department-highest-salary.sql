SELECT
    D.name as Department,
    E.name as Employee,
    E.salary as Salary
FROM
    Employee E
LEFT JOIN
    (
        SELECT
            id, rank() OVER (PARTITION BY departmentId ORDER BY salary DESC) as ranking
        FROM
            Employee
    ) R
ON
    R.id = E.id
LEFT JOIN
    Department D
ON
    D.id = E.departmentId
WHERE
    R.ranking = 1