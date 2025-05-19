<h1 align="center"><b>Desafio Técnico - Programa Trainee triggo.ai 2025</b></h1>


<p align="center">
  <img src="img/logo-triggo-ai.png" alt="segment-map" />
</p>


> **Status:** Em andamento 🚧

<h2 align="center">
<a href=""><u>Clique aqui para visualizar o dashboard do desafio!</u></a>
</h2>



# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte do processo seletivo do **Programa Trainee triggo.ai de Excelência em Engenharia de Dados e DataOps 2025**.

Fui desafiado a atuar como Engenheiro de Dados Junior em uma empresa de e-commerce brasileira, analisando o histórico de vendas contido no dataset público da Olist para extrair **insights estratégicos**, desenvolver **modelos preditivos** e construir **dashboards interativos**.

---

# 🧠 Etapas do Projeto

## 1. **Preparação dos Dados**
- Importação e padronização de dados a partir de múltiplos arquivos CSV
- Tratamento de valores ausentes e duplicados
- Normalização de colunas e padronização de tipos
- Criação de modelo relacional com suporte a SQL (SQLite)
- Documentação detalhada de todas as transformações aplicadas

## 2. **Análise Exploratória de Dados (EDA)**
- Volume de pedidos por mês e análise de sazonalidade
- Distribuição do tempo de entrega
- Relação entre valor do frete e distância de entrega
- Categorias com maior faturamento
- Estados com maior valor médio de pedidos

## 3. **Soluções de Negócio**
- **Análise de Retenção**: cálculo da taxa de clientes recorrentes e extração de insights
- **Predição de Atraso**: modelo de classificação para prever atrasos na entrega
- **Segmentação de Clientes**: clusterização com análise de perfil e estratégias de marketing
- **Análise de Satisfação**: estudo dos fatores que mais impactam a avaliação dos clientes

## 4. **Dashboards Interativos**
- Evolução de vendas com filtros por estado e categoria
- Mapa de calor de vendas por região do Brasil
- Relação entre avaliação do cliente e tempo de entrega
- Painel de desempenho dos vendedores (vendas, satisfação, tempo de entrega)

---

# 📊 Ferramentas Utilizadas

- **Python**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `plotly`
- **SQL**: Consultas em SQLite integradas ao pandas
- **Machine Learning**: Modelos de classificação e clustering
- **Visualização de Dados**: Dashboards interativos com Plotly
- **Ambiente**: Jupyter Notebook

---

# 🗂️ Estrutura do Projeto

A estrutura princpal se expressa desta forma:

```
triggo-ai-challenge/
├── dashboard # dashboard Streamlit gerado
│ └── pages/
├── data/ # Arquivos CSV do dataset Olist
├── notebooks/ Notebooks executando as tarefas propostas
├── img/ # Imagens e gráficos utilizados
├── README.md # Este arquivo
├── requirements.txt # Dependências do projeto
```

---

# 🚀 Instruções de Execução

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/triggo-teste-tecnico.git
cd triggo-ai-challenge
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Executar Notebooks
Recomenda-se abrir o notebook no Jupyter ou Google Colab para melhor visualização e interação com os gráficos. Para acessar o dashboard em produção você pode acessar o link destacado logo no início do projeto.

<hr></hr>
<div style= "margin: 20px;"></div>


<p align= "center">Muito obrigado!</p>
<p align= "center"><b>LinkedIn</b>: <a href= "linkedin.com/in/rodrigo-rngl/">linkedin.com/in/rodrigo-rngl</a>.</p>