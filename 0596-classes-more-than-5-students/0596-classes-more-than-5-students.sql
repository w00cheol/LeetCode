SELECT
    G.class
FROM(
    SELECT
        class, count(*) as cnt
    FROM
        Courses
    GROUP BY
        class
    ) as G
Where
    G.cnt >= 5