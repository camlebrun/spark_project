import streamlit as st
import pandas as pd

st.title("Nombre de client par magasin")
df = pd.read_csv("Data/for_streamlit/df_client.csv")
df.set_index('Adresse', inplace=True)
st.dataframe(df, width= 1000)
