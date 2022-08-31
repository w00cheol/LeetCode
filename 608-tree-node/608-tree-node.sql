SELECT DISTINCT
    Tree.id,
    (CASE
        WHEN Tree.p_id is NULL
            THEN "Root"

        WHEN TreeChild.id is NULL
            THEN "Leaf"

        ELSE "Inner"
     END
    ) AS type
FROM
    Tree
LEFT JOIN
    Tree TreeChild
ON
    TreeChild.p_id = Tree.id