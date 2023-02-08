import streamlit as st
import pandas as pd


df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/top3.csv")
df.set_index('Nom_produit', inplace=True)
st.write("Top 3 des ventes par magasin")
st.dataframe(df, width= 1000)

df_ca = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/top3_ca.csv")
df_ca.set_index('Nom_produit', inplace=True)

st.write("Top 3 des ventes par magasin CA")
st.dataframe(df_ca, width= 1000)
code = '''df_grouped = df_finale.groupBy("Nom_produit").agg(count("Nom_produit").alias("TOP"))
df_grouped = df_grouped.sort(desc("TOP"))

window = Window.orderBy(desc("TOP"))
df_grouped = df_grouped.withColumn("Rank", row_number().over(window))
df_top_3 = df_grouped.filter(df_grouped["Rank"] <= 3)
df_top_3.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_top_3.exp')

#1b_bis. Les produits les plus vendus par magasins CA
df_grouped = df_finale.groupBy("Nom_produit").agg(sum("Montant").alias("CA"))
df_grouped = df_grouped.sort(desc("CA"))

window = Window.orderBy(desc("CA"))
df_grouped = df_grouped.withColumn("Rank", row_number().over(window))
df_top_3_CA = df_grouped.filter(df_grouped["Rank"] <= 3)
df_top_3_CA.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_top_3_CA.exp')
'''



with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")



