import streamlit as st
st.set_page_config(layout="wide")

# Create the interface
st.title("YourData X CoursePlus")
st.write('Demo version')
# Show the data as a table
def page_0():
    st.empty()
def page_2():
    st.empty()

def page3():
    st.empty()

def page4():
     st.empty()

page_names_to_funcs = {
    "🏠Home": page_0,
    "Global Picture": page_2,
    "2_Where": page3,
    "cluster" :page4
}
code = '''from pyspark.sql import SparkSession
from pyspark.sql.functions import month, countDistinct, desc, sum, row_number, count, to_date, avg, round 
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType


spark = SparkSession.builder.appName("projet").getOrCreate()
store = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/BD_magasins.csv')
user_info = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/BD_client.csv")
produit = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/BD_produits.csv")
transaction = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/BD_transactions.csv")

df_inter_1 = user_info.join(transaction, user_info.ID_client == transaction.ID_client, 'inner') \
                    .select(user_info.ID_client, user_info.Prenom, user_info.Nom, user_info.Ville_client, user_info.Code_postal_client,
                    transaction.ID_magasin,
                            transaction.ID_tran, transaction.Product_id, transaction.Date, transaction.Montant)
#df_inter_1.show()
df_inter_2 = df_inter_1.join(store, df_inter_1.ID_magasin == store.ID, 'inner') \
                    .select(df_inter_1.ID_client, df_inter_1.Prenom, df_inter_1.Nom, df_inter_1.Ville_client, df_inter_1.Code_postal_client,df_inter_1.Montant,
                            df_inter_1.ID_tran, df_inter_1.ID_magasin, df_inter_1.Product_id, df_inter_1.Date, store.Ville_store, store.Code_postal_store, store.Adresse)
df_finale = df_inter_2.join(produit, df_inter_2.Product_id == produit.ID_produit, 'inner').select(df_inter_2.ID_client, df_inter_2.Prenom, df_inter_2.Nom, df_inter_2.Ville_client,
df_inter_2.Code_postal_client, df_inter_2.Montant,df_inter_2.ID_tran, df_inter_2.ID_magasin, df_inter_2.Adresse,df_inter_2.Product_id, df_inter_2.Date, df_inter_2.Code_postal_store, produit.Nom_produit, produit.Categorie)
df_finale = df_finale.alias('df_finale')
df_finale.show()
df_finale.write.option("header", "true").csv('/Users/camille/repo/Hetic/BigData/spark_projet/Data/df_finale.exp')'''

with st.expander("Code"):
    st.markdown("This is an explanation of the code")
    st.code(code, language="python")



