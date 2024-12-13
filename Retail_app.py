import psycopg2
import pandas as pd
import streamlit as st


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



st.title("Retail Sales Analysis")
st.title("SQL Querry App")
st.sidebar.title("Menu")
option=st.sidebar.radio("Choose an option",["Provided Queries", "Own Queries", "Create AI-Powered Custom Query"])

if option == "Provided Queries":
    display_results("Provided Queries", Provided_Queries)

elif option == "Own Queries":
    display_results("Own Queries", Own_Queries)
