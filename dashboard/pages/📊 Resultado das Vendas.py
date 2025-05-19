import streamlit as st
import pandas as pd

# Título do dashboard
st.title("Dashboard: Resultado das Vendas da Olist")

# PREPARAÇÃO DOS DADOS
df = pd.read_csv("../data/clean_general_df.csv")  # Exemplo

sales_df = df.loc[~df['order_status'].isin(['unavailable', 'canceled'])].copy()

sales_df['order_delivered_customer_date'] = pd.to_datetime(sales_df['order_delivered_customer_date'], errors='coerce')

# Adiciona coluna de meses existentes do período
sales_df['month_period'] = sales_df['order_delivered_customer_date'].dt.to_period('M').dt.to_timestamp()


# SIDEBAR COM FILTROS
st.sidebar.header("Filtros")

## Filtro por estado
customer_state = sales_df['customer_state'].dropna().unique()
customer_state_selected = st.sidebar.multiselect("Estado do Cliente", options=sorted(customer_state), default=list(customer_state))

## Filtro por categoria
categories = sales_df['product_category_name'].dropna().unique()
category_selected = st.sidebar.multiselect("Categoria de Produto", options=sorted(categories), default=list(categories))


# APLICAÇÃO DOS FILTROS
line_chart_df = sales_df[['order_id', 'month_period', 'price']][
    (sales_df['customer_state'].isin(customer_state_selected)) &
    (sales_df['product_category_name'].isin(category_selected))
].copy()

map_df = sales_df[['customer_lat', 'customer_lng']].loc[
    (sales_df['customer_state'].isin(customer_state_selected)) & 
    (sales_df['product_category_name'].isin(category_selected))
].copy()

map_df.dropna(inplace= True)


# AGRUPAMENTO PARA GRÁFICO DE LINHA
sales_evolution = (
    line_chart_df.groupby('month_period').agg(n_orders= ('order_id', 'nunique'), monthly_billing= ('price', "sum")).reset_index()
)

# APRESENTAÇÃO
## GRÁFICO DE LINHA
st.subheader("📊 Evolução de Vendas por Mês")

st.line_chart(data= sales_evolution, x= 'month_period', y= 'n_orders', x_label= 'Meses do Período', y_label= 'Qnt. de Pedidos')

st.write(f"Total de pedidos: **{sales_evolution['n_orders'].sum()}**")
st.write(f"Total de faturamento: **R${round(sales_evolution['monthly_billing'].sum(), 2)}**")

## MAPA
st.subheader("🗺️ Mapa de Pedidos por Catagoria de Produto")

st.map(data= map_df, latitude= 'customer_lat', longitude= 'customer_lng')

