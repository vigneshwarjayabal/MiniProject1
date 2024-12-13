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
