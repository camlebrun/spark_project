import pandas as pd
import plotly.express as px
import streamlit as st
st.title("Nombre de client par mois")
df = pd.read_csv("for_streamlit/nb_client_mois.csv")
fig = px.line(df, x="month", y="count(ID_client)", color="Adresse", labels={'count(ID_client)':'Nombre de client', 'month':'Mois'})
st.plotly_chart(fig, use_container_width = True)