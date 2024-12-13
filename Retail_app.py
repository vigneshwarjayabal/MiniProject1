import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from db_utils import execute_query
from queries import queries

# App Title
st.title("Retail Order Data Analysis")
st.sidebar.header("Business Insights")

# Sidebar for Query Selection
selected_query = st.sidebar.selectbox("Select an Insight", list(queries.keys()))

# Execute and Display Query
if selected_query:
    st.subheader(selected_query)
    query = queries[selected_query]

    # Run the selected query
    try:
        result = execute_query(query)
        st.write(result)

        # Visualize the Data
        if len(result.columns) >= 2:
            st.bar_chart(result.set_index(result.columns[0]))
        if len(result.columns) >= 2:
            st.line_chart(result.set_index(result.columns[0]))

    except Exception as e:
        st.error(f"An error occurred: {e}")
