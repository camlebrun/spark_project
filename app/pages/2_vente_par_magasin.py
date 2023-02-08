import streamlit as st
import pandas as pd

df = pd.read_csv("Data/for_streamlit/df_top_10.csv")

df.set_index('Nom_produit', inplace=True)
selected_store = st.selectbox("Select a store", df["Adresse"].unique())

# Convertir selected_store en liste si ce n'est pas déjà une liste
selected_stores = [selected_store] if not isinstance(selected_store, list) else selected_store
df = df[df["Adresse"].isin(selected_stores)]
st.write("Vente par magasin")
st.dataframe(df, width= 1000)


st.write("CA par magasin")
df2 = pd.read_csv("Data/for_streamlit/top_10_CA.csv")
df2.set_index('Nom_produit', inplace=True)
df2 = df2[df2["Adresse"].isin(selected_stores)]
st.dataframe(df2, width= 1000)
