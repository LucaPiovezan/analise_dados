import streamlit as st
import pandas as pd

itens = [
    "Pão Francês (kg)",
    "Pão de Queijo (un)",
    "Leite Integral (L)",
    "Queijo Mussarela (g)",
    "Presunto (g)",
    "Café Espesso (un)",
    "Bolo de Cenoura (fatia)",
]

precos = [
    14.90,
    2.50,
    5.80,
    12.50,
    9.80,
    6.00,
    8.50,
]

df_vendas = pd.DataFrame({
    "Item": itens,
    "Preço (R$)": precos,
})

st.title("Meu primeiro dash")
st.subheader("Python")

item_selecionado = st.selectbox("Selecione um item da padaria:", itens)

st.write(f"**{item_selecionado}** custa **R$ {df_vendas.loc[df_vendas['Item'] == item_selecionado, 'Preço (R$)'].iloc[0]:.2f}**")

st.write("Cardápio completo:")
st.dataframe(df_vendas)
