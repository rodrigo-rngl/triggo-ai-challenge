import streamlit as st

st.set_page_config(page_title="Desafio Técnico triggo.ai - Dashboard de Vendas", layout="wide")

# Título e introdução
st.title("Desafio Técnico Triggo.ai – Dashboard de Vendas Olist")
st.markdown("""
Bem-vindo ao painel interativo desenvolvido como parte do Teste Técnico do processo seletivo para o **Bootcamp Triggo.ai – Programa Trainee de Excelência em Engenharia de Dados e DataOps**.

---

### 🎯 **Objetivo do Projeto**

Você foi contratado como **Engenheiro de Dados Júnior** por uma empresa brasileira de e-commerce. Sua missão é analisar o histórico de vendas da empresa para extrair **insights valiosos e orientações estratégicas** por meio de visualizações intuitivas e dados confiáveis.

Este dashboard foi construído com **Python**, **Pandas**, **Plotly** e **Streamlit**, e simula desafios reais enfrentados na área de Dados.

---

### 📊 O que você encontrará neste dashboard:

#### 1. **Evolução das Vendas ao Longo do Tempo**
- Visualização de pedidos por mês
- Filtros por **estado do cliente** e **categoria de produto**

#### 2. **Mapa de Calor de Vendas**
- Concentração de pedidos por **região e estado**, com base nas **coordenadas geográficas dos clientes**

#### 3. **Avaliações e Logística**
- Relação entre a **nota de avaliação dos clientes** e o **tempo de entrega**
- Distribuição e padrões logísticos identificáveis por nota

#### 4. **Desempenho dos Vendedores**
- Ranking por:
  - **Volume de vendas**
  - **Satisfação do cliente**
  - **Tempo médio de entrega**

---

### 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework de Visualização:** Streamlit + Plotly
- **Manipulação de Dados:** Pandas
- **Base de Dados:** Conjunto de vendas e avaliações de um e-commerce brasileiro

---

### 📂 Use o **menu lateral à esquerda** para navegar pelos diferentes painéis.
""")