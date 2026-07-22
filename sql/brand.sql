SELECT
    card_brand,
    COUNT(*) AS qtd_transacoes,
    SUM(amount) AS tpv
FROM transactions
GROUP BY card_brand
ORDER BY tpv DESC;