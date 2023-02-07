from pyspark.sql import SparkSession
from pyspark.sql.functions import month, countDistinct
spark = SparkSession.builder.appName("projet").getOrCreate()
store = spark.read.option("header", "true").option("inferSchema", "true").csv("/Users/camille/repo/Hetic/BigData/spark_projet/store.csv")
user_info = spark.read.option("header", "true").option("inferSchema", "true").csv("/Users/camille/repo/Hetic/BigData/spark_projet/user_info.csv")
produit = spark.read.option("header", "true").option("inferSchema", "true").csv("/Users/camille/repo/Hetic/BigData/spark_projet/product.csv")
transaction = spark.read.option("header", "true").option("inferSchema", "true").csv("/Users/camille/repo/Hetic/BigData/spark_projet/trans.csv")

df_inter_1 = user_info.join(transaction, user_info.id_user == transaction.id_user, 'inner') \
                    .select(user_info.id_user, user_info.frist_name, user_info.name, user_info.city, transaction.id_store,
                            transaction.id_transac, transaction.id_product, transaction.date, transaction.amount)
#df_inter_1.show()
df_inter_2 = df_inter_1.join(store, df_inter_1.id_store == store.id_store, 'inner') \
                    .select(df_inter_1.id_user, df_inter_1.frist_name, df_inter_1.city, df_inter_1.amount,
                            df_inter_1.id_transac, df_inter_1.id_store, df_inter_1.id_product, df_inter_1.date, store.ville, store.name)
df_finale = df_inter_2.join(produit, df_inter_2.id_product == produit.id_product, 'inner').select(df_inter_2.id_user, df_inter_2.frist_name, df_inter_2.city, df_inter_2.amount,df_inter_2.id_transac, df_inter_2.id_store, df_inter_2.id_product, df_inter_2.date, df_inter_2.ville, df_inter_2.name, produit.Name, produit.unitprice, produit.cat    )
df_finale = df_finale.alias('df_finale')

nb_client_per_store = df_finale.groupBy("id_store").count().alias("nb_client")
nb_client_per_store.collect()
nb_client_per_store.write.options(header='True', delimiter=',').csv("nb_client.csv")

nb_clients_unique_store_month = df_finale.groupBy(["id_store", month("date").alias("month")]).agg(countDistinct("id_user"))
courses_menselle = df_finale.groupBy(["id_user", month("date").alias("month")] ).agg({"amount": "sum"}).alias("courses_menselle")
CA_month = df_finale.groupBy(["id_store", month("date").alias("month")] ).agg({"amount": "sum"}).alias("courses_menselle")