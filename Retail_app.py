import streamlit as st

conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT * FROM orders;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
