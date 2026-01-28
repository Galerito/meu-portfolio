import sqlite3
import pandas as pd

# 1. Conectar ao banco que criamos
conexao = sqlite3.connect('dados/meu_projeto.db')

# 2. Definir a Query (Pergunta em SQL)
query = "SELECT SUM(valor_venda) AS faturamento_total FROM vendas"

# 3. Usar o Pandas para ler o resultado do SQL
resultado = pd.read_sql_query(query, conexao)

print("---" * 10)
print("📊 RESULTADO DA CONSULTA SQL:")
print(resultado)
print("---" * 10)

# 4. Outra consulta: Vendas por Categoria
query_cat = "SELECT produto_categoria, COUNT(*) AS total_pedidos FROM vendas GROUP BY produto_categoria"
resultado_cat = pd.read_sql_query(query_cat, conexao)
print("\n📦 VENDAS POR CATEGORIA:")
print(resultado_cat)

conexao.close()