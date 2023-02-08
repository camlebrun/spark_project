import streamlit as st
from pyspark.sql import SparkSession
from pyspark.sql.functions import month, countDistinct, desc, sum, row_number, count, to_date, avg, round 
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType
spark = SparkSession.builder.appName("projet").getOrCreate()

produit = spark.read.option("header", "true").options(inferSchema='True',delimiter=';').csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/BD_produits.csv")



result = produit.filter(produit.Stock_actuel <= 5).collect()
if len(result) > 0:
    st.error("Products with stock lower than 2: \n" + "\n".join([row.Nom_produit for row in result]), icon="🚨")
else:
    st.write("All products have stock higher than or equal to 2")