import streamlit as st
from pyspark.sql import SparkSession
from pyspark.sql.functions import month, countDistinct, desc, sum, row_number, count, to_date, avg, round 
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("projet").getOrCreate()

produit = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv("Data/for_streamlit/BD_produits.csv")
produit = produit.withColumn("Stock_actuel", produit["Stock_actuel"].cast(IntegerType()))

# Convertir SparkDataFrame en pandas DataFrame pour l'affichage dans Streamlit
produit_pdf = produit.toPandas()
st.write("Tous les stocks")
st.dataframe(produit_pdf)

st.write("Stock inférieur à 10")
produit = produit.filter(produit["Stock_actuel"] < 10)
produit_pdf = produit.toPandas()
st.dataframe(produit_pdf)
