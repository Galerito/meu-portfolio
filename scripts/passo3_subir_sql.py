import pandas as pd
import sqlite3

# 1. Carregar o dado limpo
df = pd.read_csv('dados/vendas_limpas.csv')

# 2. Conectar ao Banco de Dados (se não existir, ele cria na hora)
# O arquivo se chamará 'meu_projeto.db'
conexao = sqlite3.connect('dados/meu_projeto.db')

# 3. Enviar os dados para o SQL
# Criaremos uma tabela chamada 'vendas'
df.to_sql('vendas', conexao, if_exists='replace', index=False)

print("---" * 10)
print("✅ DADOS CARREGADOS NO SQL COM SUCESSO!")
print("Banco de dados criado: dados/meu_projeto.db")
print("---" * 10)

# Fechar conexão
conexao.close()