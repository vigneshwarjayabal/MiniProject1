import streamlit as st

conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT * FROM orders;', ttl="10m")

print(df)
