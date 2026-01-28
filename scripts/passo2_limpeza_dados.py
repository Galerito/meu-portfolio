import pandas as pd
import os

# 1. Carregar os dados que geramos no passo anterior
df = pd.read_csv('dados/vendas_brutas.csv')

print("Análise inicial dos dados:")
print(df.info()) # Mostra se há valores nulos e os tipos de colunas
print("\nQuantidade de valores nulos por coluna:")
print(df.isnull().sum())

# 2. TRATAMENTO DE NULOS
# Vamos preencher os valores vazios da 'valor_venda' com a média dos preços
media_precos = df['valor_venda'].mean()
df['valor_venda'] = df['valor_venda'].fillna(media_precos)

# 3. CONVERSÃO DE TIPOS
# Garantir que a coluna de data seja reconhecida como data pelo Python
df['data_pedido'] = pd.to_datetime(df['data_pedido'])

# 4. CRIAR NOVAS COLUNAS (Feature Engineering)
# Vamos extrair o mês e o ano para facilitar a análise no Power BI depois
df['mes_ano'] = df['data_pedido'].dt.to_period('M')

# 5. SALVAR O DADO PRONTO
df.to_csv('dados/vendas_limpas.csv', index=False)

print("\n---" * 10)
print("✅ LIMPEZA CONCLUÍDA!")
print("Arquivo salvo em: dados/vendas_limpas.csv")
print("---" * 10)