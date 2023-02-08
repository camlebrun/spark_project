import pandas as pd
import plotly.express as px
import streamlit as st
st.title("Vente par catégorie")
df = pd.read_csv("Data/for_streamlit/finale.csv")
fig = px.bar(df, x="Categorie", y="count(Montant)", labels={'count(Montant)':'Total des ventes'})

st.plotly_chart(fig, use_container_width = True)