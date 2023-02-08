import pandas as pd
import plotly.express as px
import streamlit as st
st.title("Vente par catégorie")
df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/finale.csv")
nex = px.pie(df, values='count(Montant)', names='Categorie', title='Vente par catégorie')

st.plotly_chart(nex, use_container_width = True)


code = '''categorie = df_finale.groupBy(["Categorie", month("Date").alias("month")] ).agg({"Montant": "sum"}).alias("categorie")
categorie.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/categorie.exp')

df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/finale.csv")
nex = px.pie(df, values='count(Montant)', names='Categorie', title='Vente par catégorie')

st.plotly_chart(nex, use_container_width = True)
'''

with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")