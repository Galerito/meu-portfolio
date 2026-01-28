Dashboard de Performance de Vendas (Python + SQL + Power BI)
📌 Sobre o Projeto
Este projeto simula um cenário real de análise de dados, onde precisei gerar dados de vendas, armazená-los de forma segura em um banco de dados e criar um dashboard interativo para tomada de decisão executiva.

🛠️ Tecnologias Utilizadas
Python (Pandas): Utilizado para a geração de 500 registros sintéticos e limpeza inicial dos dados (ETL).

SQL (SQLite): Utilizado para persistência dos dados e validação de integridade.

Power BI: Utilizado para a construção do dashboard, tratamento de localidade (padrão Americano vs. Brasileiro) e modelagem de dados.

📊 O Dashboard
O painel final fornece insights sobre:

Faturamento Total: KPI principal com o valor bruto das vendas.

Vendas por Categoria: Gráfico de colunas identificando os setores mais lucrativos (Casa, Alimentos, Moda e Eletrônicos).

Filtro Interativo: Segmentação por status do pedido (Concluído/Cancelado).

🚀 Desafios Técnicos Superados
Durante o desenvolvimento, identifiquei e resolvi um erro crítico de importação no Power BI:

Problema: O sistema estava interpretando o ponto decimal como separador de milhar, inflando o faturamento de 127 mil para 16 milhões.

Solução: Realizei o tratamento via Power Query, alterando o tipo de dado por Localidade (Inglês/EUA), garantindo a precisão de 100% nos relatórios financeiros.

💡 Como rodar o projeto
Execute o script gerar_dados.py para criar o banco de dados e o CSV.

Abra o arquivo .pbix no Power BI Desktop.

Caso os dados não carreguem, ajuste o caminho do arquivo no Power Query.