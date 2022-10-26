SELECT
    W_1.id
FROM
    Weather W_1
LEFT JOIN
    Weather W_2
ON
    DATEDIFF(W_2.RecordDate, W_1.RecordDate) = -1
WHERE
    W_1.temperature > W_2.temperature