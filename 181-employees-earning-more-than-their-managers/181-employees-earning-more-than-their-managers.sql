SELECT
    name as Employee
FROM
    Employee as E
WHERE
    E.salary > (
                SELECT
                    M.salary
                FROM
                    Employee as M
                WHERE
                    E.managerid = M.id
               )