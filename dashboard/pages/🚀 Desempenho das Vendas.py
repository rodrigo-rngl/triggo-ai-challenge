import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

data_path = Path(__file__).resolve().parent.parent.parent / "data/clean_general_df.csv.gz"

# Título do dashboard
st.title("Dashboard: Desempenho de Vendas da Olist")

# PREPARAÇÃO DOS DADOS
df = pd.read_csv(data_path)

df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], errors='coerce')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')

# Cálculo do tempo de entrega em dias
df['delivery_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

# Limpeza: apenas pedidos com avaliação e entrega concluída
reviews_df = df.dropna(subset=['review_score', 'delivery_time'])
sellers_df = df.dropna(subset=['seller_id', 'review_score', 'delivery_time'])

# AGRUPAMENTO PARA GRÁFICO
performance = (
    sellers_df.groupby('seller_id')
    .agg(
        total_sales=('order_id', 'nunique'),
        mean_score=('review_score', 'mean'),
        delivery_mean_time=('delivery_time', 'mean')
    )
    .reset_index()
)

top_sales = performance.sort_values(by='total_sales', ascending=False).head(10)
avaliados = performance[performance['total_sales'] >= 30].sort_values(by='mean_score', ascending=False).head(10)
rapidos = performance[performance['total_sales'] >= 30].sort_values(by='delivery_mean_time').head(10)

# PERSONALIZAÇÕES
personalized_color = {
    1: "#d73027",  # vermelho
    2: "#fc8d59",  # laranja claro
    3: "#fee08b",  # amarelo
    4: "#589ef2",  # verde claro
    5: "#1a9850",  # verde escuro
}

# APRESENTAÇÃO
# Relação entre Avaliação e Tempo de Entrega
st.header("📈 Avaliação vs Tempo de Entrega")

st.subheader("Dispersão: Avaliação x Tempo de Entrega")
hist = px.histogram(
    reviews_df, x="delivery_time", color="review_score",
    nbins=100, barmode="overlay", opacity=0.6,
    color_discrete_map= personalized_color,
    labels={"delivery_time": "Tempo de Entrega (dias)", "review_score": "Nota de Avaliação"}
)
hist.update_layout(legend_title_text="Nota", bargap=0.1)
st.plotly_chart(hist)


st.subheader("Boxplot: Tempo de Entrega por Nota")
box = px.box(reviews_df, x='review_score', y='delivery_time',
             color= 'review_score',
             color_discrete_map= personalized_color,
             labels={'review_score': 'Nota de Avaliação', 'delivery_time': 'Tempo de Entrega (dias)'})
st.plotly_chart(box)

# Dashboard de Desempenho dos Vendedores
st.header("🧑‍💼 Desempenho dos Vendedores")

# Ranking dos 10 melhores por volume de vendas
st.subheader("🏆 Top 10 Vendedores por Volume de Vendas")
fig1 = px.bar(
    top_sales,
    x='seller_id',
    y='total_sales',
    title='Volume de Vendas por Vendedor',
    labels={'seller_id': 'Vendedor', 'total_sales': 'Total de Vendas'},
    color= 'total_sales',
    color_continuous_scale= px.colors.sequential.Greens,
    text_auto=True
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

# Ranking por avaliação média (com mínimo de 30 pedidos)
st.subheader("🌟 Top Vendedores por Avaliação (mínimo 30 pedidos)")
fig2 = px.bar(
    avaliados,
    x='seller_id',
    y='mean_score',
    title='Avaliação Média por Vendedor',
    labels={'seller_id': 'Vendedor', 'mean_score': 'Nota Média'},
    text_auto=".2f",
    color='mean_score',
    color_continuous_scale= px.colors.sequential.Greens
)
fig2.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig2, use_container_width=True)

# Ranking por entrega mais rápida (mínimo de 30 pedidos)
st.subheader("⚡ Vendedores com Entrega Mais Rápida (mínimo 30 pedidos)")
fig3 = px.bar(
    rapidos,
    x='seller_id',
    y='delivery_mean_time',
    title='Tempo Médio de Entrega por Vendedor',
    labels={'seller_id': 'Vendedor', 'delivery_mean_time': 'Entrega Média (dias)'},
    text_auto=".2f",
    color='delivery_mean_time',
    color_continuous_scale=px.colors.sequential.Greens_r
)
fig3.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig3, use_container_width=True)