import streamlit as st
import pandas as pd


df = pd.read_csv("for_streamlit/top3.csv")
df.set_index('Nom_produit', inplace=True)
st.write("Top 3 des ventes par magasin")
st.dataframe(df, width= 1000)

df_ca = pd.read_csv("for_streamlit/top3_ca.csv")
df_ca.set_index('Nom_produit', inplace=True)

st.write("Top 3 des ventes par magasin CA")
st.dataframe(df_ca, width= 1000)