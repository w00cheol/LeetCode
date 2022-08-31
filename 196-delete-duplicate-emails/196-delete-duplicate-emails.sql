DELETE FROM
    Person
WHERE id NOT IN (
        SELECT
            id
        FROM (
                SELECT
                    min(id) AS id
                FROM
                    Person
                GROUP BY
                    email
        ) PersonMinId
)