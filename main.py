from pyspark.sql import SparkSession
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
                            df_inter_1.ID_tran, df_inter_1.ID_magasin, df_inter_1.Product_id, df_inter_1.Date, store.Ville_store, store.Code_postal_store)
df_finale = df_inter_2.join(produit, df_inter_2.Product_id == produit.ID_produit, 'inner').select(df_inter_2.ID_client, df_inter_2.Prenom, df_inter_2.Nom, df_inter_2.Ville_client,
df_inter_2.Code_postal_client, df_inter_2.Montant,df_inter_2.ID_tran, df_inter_2.ID_magasin, df_inter_2.Product_id, df_inter_2.Date, df_inter_2.Code_postal_store,
df_inter_2.Code_postal_store, produit.Nom_produit, produit.Categorie, produit.Categorie)
df_finale = df_finale.alias('df_finale')


# 1a. Les produits les plus vendus par magasins

df_finale = df_finale.withColumn("Montant", df_finale["Montant"].cast(IntegerType()))
df_grouped = df_finale.groupBy('Nom_produit', 'ID_magasin').agg(count('Nom_produit').alias('Total_sales'))
df_grouped = df_grouped.sort(desc('Total_sales'))

window = Window.partitionBy(df_grouped['ID_magasin']).orderBy(desc('Total_sales'))
df_grouped = df_grouped.withColumn('Rank', row_number().over(window))

df_top_10 = df_grouped.filter(df_grouped['Rank'] <= 10)
df_top_10.show()
#1b Les produits les plus vendus par magasins CA 


df_finale = df_finale.withColumn("Montant", df_finale["Montant"].cast(IntegerType()))
df_grouped = df_finale.groupBy('Nom_produit', 'ID_magasin').agg(sum('Montant').alias('CA'))
df_grouped = df_grouped.sort(desc('CA'))

window = Window.partitionBy(df_grouped['ID_magasin']).orderBy(desc('CA'))
df_grouped = df_grouped.withColumn('Rank', row_number().over(window))

df_top_10 = df_grouped.filter(df_grouped['Rank'] <= 10)
df_top_10.show()

# 1abis top 10 tous les magasins

df_grouped = df_finale.groupBy("Nom_produit").agg(count("Nom_produit").alias("TOP"))
df_grouped = df_grouped.sort(desc("TOP"))

window = Window.orderBy(desc("TOP"))
df_grouped = df_grouped.withColumn("Rank", row_number().over(window))
df_top_3 = df_grouped.filter(df_grouped["Rank"] <= 3)
df_top_3.show()

#1b_bis. Les produits les plus vendus par magasins CA
df_grouped = df_finale.groupBy("Nom_produit").agg(sum("Montant").alias("CA"))
df_grouped = df_grouped.sort(desc("CA"))

window = Window.orderBy(desc("CA"))
df_grouped = df_grouped.withColumn("Rank", row_number().over(window))
df_top_3 = df_grouped.filter(df_grouped["Rank"] <= 3)
df_top_3.show()


#2. les magasins avec le plus de clients 
df_client = df_finale.groupBy("ID_magasin").agg(countDistinct("ID_client").alias("Total_clients"))
#df_client = df_finale.groupBy("Adresse").agg(countDistinct("ID_client").alias("Total_clients"))
df_client = df_client.sort(desc("Total_clients"))

window = Window.orderBy(desc("Total_clients"))
df_client = df_client.withColumn("Rank", row_number().over(window))
df_client.show()

#3. Evolution des ventes par mois par magasin
df_finale = df_finale.withColumn("Date", to_date(df_finale["Date"], "dd-MM-yyyy"))
CA_month = df_finale.groupBy(["ID_magasin", month("Date").alias("month")] ).agg({"Montant": "sum"}).alias("courses_menselle")
#CA_month = df_finale.groupBy(["Adresse", month("Date").alias("month")] ).agg({"Montant": "sum"}).alias("courses_menselle")


#4 nombre de clients  par magasin
nb_client_per_store = df_finale.groupBy("ID_magasin").count().alias("nb_client")
#nb_client_per_store = df_finale.groupBy("Adresse").count().alias("nb_client")
nb_client_per_store.show()

#4b. nombre de clients  par magasin et mois 
nb_client_mensuel = df_finale.groupBy(["ID_magasin", month("Date").alias("month")] ).agg({"ID_client": "count"}).alias("nb_client_mensuel")
