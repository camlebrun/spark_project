import pandas as pd
import plotly.express as px
import streamlit as st
st.title("Nombre de client par mois")
df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/nb_client_mois.csv")
fig = px.line(df, x="month", y="count(ID_client)", color="Adresse", labels={'count(ID_client)':'Nombre de client', 'month':'Mois'})
st.plotly_chart(fig, use_container_width = True)



code = '''nb_client_mensuel = df_finale.groupBy(["Adresse", month("Date").alias("month")] ).agg({"ID_client": "count"}).alias("nb_client_mensuel")
nb_client_mensuel.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/nb_client_mensuel.exp')   

df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/nb_client_mois.csv")
fig = px.line(df, x="month", y="count(ID_client)", color="Adresse", labels={'count(ID_client)':'Nombre de client', 'month':'Mois'})
st.plotly_chart(fig, use_container_width = True)'''

with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")