import streamlit as st
import pandas as pd


df = pd.read_csv("/Users/camille/repo/Hetic/BigData/spark_projet/Data/for_streamlit/Total_sales_per_shop.csv")
df = df.reset_index(drop=True)
st.dataframe(df, width= 1000)