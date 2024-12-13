import pandas as pd
import streamlit as st
from queries import business_insights, provided_query, my_query 



def database_connection():
    try:
        connection = psycopg2.connect(
            host=st.secrets["postgresql"]["host"],  
            user=st.secrets["postgresql"]["user"],  
            password=st.secrets["postgresql"]["password"], 
            database=st.secrets["postgresql"]["database"]  
        )
        return connection
    except psycopg2.Error as err:
        st.error(f"Error connecting to database: {err}")
        return None

def execute_query(query):
    try:
        conn = database_connection()
        if conn is None:
            return pd.DataFrame()  # If connection failed, return an empty DataFrame
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        conn.close()  # Close the connection after execution
        return pd.DataFrame(result, columns=column_names)
    except Exception as e:
        st.error(f"Error executing the query: {e}")
        return pd.DataFrame()

def display_results(selection, query_dict):
    st.subheader(selection)
    selected_query = st.selectbox("Choose a query", list(query_dict.keys()))
    st.write("**Query:**")
    st.code(f"{query_dict[selected_query]}")
    if st.button("Run", key=f"run_button_{selected_query}"):
        result = execute_query(query_dict[selected_query])
        if not result.empty:
            st.write("**Result:**")
            return st.dataframe(result)
        else:
            st.warning("No data returned for the query.")





st.title("Retail Sales Analysis")
st.title("SQL Querry App")
st.sidebar.title("Menu")
option=st.sidebar.radio("Choose an option",["Provided Queries", "Own Queries", "Create AI-Powered Custom Query"])

if option == "business_insights":
    display_results("business_insights", business_insights)

elif option == "provided_query":
    display_results("provided_query", provided_query)
elif option == "my_query":
    display_results("my_query", my_query)
else:
    st.write("Please select a valid option")
    
