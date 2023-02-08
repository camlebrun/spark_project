import streamlit as st
import pandas as pd

df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/df_top_10.csv")

df.set_index('Nom_produit', inplace=True)
selected_store = st.selectbox("Select a store", df["Adresse"].unique())

# Convertir selected_store en liste si ce n'est pas déjà une liste
selected_stores = [selected_store] if not isinstance(selected_store, list) else selected_store
df = df[df["Adresse"].isin(selected_stores)]
st.write("Vente par magasin")
st.dataframe(df, width= 1000)


st.write("CA par magasin")
df2 = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/top_10_CA.csv")
df2.set_index('Nom_produit', inplace=True)
df2 = df2[df2["Adresse"].isin(selected_stores)]
st.dataframe(df2, width= 1000)




code = '''window = Window.partitionBy(df_grouped['Adresse']).orderBy(desc('Total_sales'))
df_grouped = df_grouped.withColumn('Rank', row_number().over(window))

df_top_10 = df_grouped.filter(df_grouped['Rank'] <= 3)
df_top_10.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_top_10.exp')
#1b Les produits les plus vendus par magasins CA 


df_finale = df_finale.withColumn("Montant", df_finale["Montant"].cast(IntegerType()))
df_grouped = df_finale.groupBy('Nom_produit', 'Adresse').agg(sum('Montant').alias('CA'))
df_grouped = df_grouped.sort(desc('CA'))

window = Window.partitionBy(df_grouped['Adresse']).orderBy(desc('CA'))
df_grouped = df_grouped.withColumn('Rank', row_number().over(window))

df_top_10_CA = df_grouped.filter(df_grouped['Rank'] <= 10)
df_top_10_CA.show()
df_top_10_CA.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_top_10_CA.exp')'''

with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")

