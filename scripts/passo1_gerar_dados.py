import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Garantindo que a pasta 'dados' exista para não dar erro ao salvar
if not os.path.exists('dados'):
    os.makedirs('dados')

# 1. Configuração dos dados fictícios
num_linhas = 500
categorias = ['Eletrônicos', 'Moda', 'Casa', 'Alimentos']
metodos_pagamento = ['Cartão de Crédito', 'Boleto', 'Pix']

# 2. Criando o dicionário de dados
data = {
    'id_pedido': range(1, num_linhas + 1),
    'data_pedido': [datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(num_linhas)],
    'cliente_id': [random.randint(100, 200) for _ in range(num_linhas)],
    'produto_categoria': [random.choice(categorias) for _ in range(num_linhas)],
    'valor_venda': [round(random.uniform(20.0, 500.0), 2) for _ in range(num_linhas)],
    'pagamento': [random.choice(metodos_pagamento) for _ in range(num_linhas)],
    'status': [random.choice(['Concluído', 'Concluído', 'Concluído', 'Cancelado']) for _ in range(num_linhas)]
}

# Transformando em DataFrame (Tabela)
df = pd.DataFrame(data)

# Inserindo 20 valores vazios (NaN) na coluna valor_venda para "sujar" o dado
df.loc[random.sample(range(num_linhas), 20), 'valor_venda'] = np.nan

# 3. Exportando para CSV
df.to_csv('dados/vendas_brutas.csv', index=False)

print("---" * 10)
print("✅ ARQUIVO GERADO COM SUCESSO!")
print("Caminho: dados/vendas_brutas.csv")
print("---" * 10)