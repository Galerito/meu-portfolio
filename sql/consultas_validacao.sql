-- 1. Qual o faturamento total da empresa?
SELECT SUM(valor_venda) AS faturamento_total 
FROM vendas;

-- 2. Quantas vendas tivemos por categoria de produto?
SELECT produto_categoria, COUNT(*) AS total_pedidos
FROM vendas
GROUP BY produto_categoria;

-- 3. Quais pedidos foram cancelados?
SELECT * FROM vendas 
WHERE status = 'Cancelado';