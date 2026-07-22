SELECT
    m.segment,
    SUM(t.amount) AS tpv
FROM transactions t
JOIN merchants m
    ON t.merchant_id = m.merchant_id
GROUP BY m.segment
ORDER BY tpv DESC;