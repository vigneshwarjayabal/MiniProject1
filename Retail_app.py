import streamlit as st
import pandas as pd
from db_config import get_db_connection
from queries import queries
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.title("Retail Order Data Analysis")
st.sidebar.header("Business Insights")

# Sidebar for Query Selection
selected_query = st.sidebar.selectbox("Select an Insight", list(queries.keys()))

# Execute Query
def execute_query(query):
    with get_db_connection() as conn:
        return pd.read_sql(query, conn)

# Display Query Result
if selected_query:
    st.subheader(selected_query)
    query = queries[selected_query]
    try:
        data = execute_query(query)
        st.write(data)

        # Visualization
        if not data.empty:
            st.bar_chart(data.set_index(data.columns[0]))
            st.line_chart(data.set_index(data.columns[0]))

    except Exception as e:
        st.error(f"An error occurred: {e}")
