import streamlit as st
import pandas as pd

st.title("Nombre de client par magasin")
df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/df_client.csv")
df.set_index('Adresse', inplace=True)
st.dataframe(df, width= 1000)


code = '''
df_client = df_finale.groupBy("Adresse").agg(countDistinct("ID_client").alias("Total_clients"))
#df_client = df_finale.groupBy("Adresse").agg(countDistinct("ID_client").alias("Total_clients"))
df_client = df_client.sort(desc("Total_clients"))

window = Window.orderBy(desc("Total_clients"))
df_client = df_client.withColumn("Rank", row_number().over(window))
df_client.show()
df_client.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_client.exp')
'''
with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")

