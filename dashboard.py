import streamlit as st
import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user="<username>",
    password="<password>",
    account="<account>",
    warehouse="COMPUTE_WH",
    database="CRYPTO_DB",
    schema="CRYPTO_SCHEMA"
)

st.title("📈 Real-Time Crypto Prices")

df = pd.read_sql("SELECT * FROM CRYPTO_PRICES ORDER BY event_time DESC LIMIT 100", conn)

st.dataframe(df)
