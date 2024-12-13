import streamlit as st
import psycopg2
import pandas as pd

# Connect to PostgreSQL
def connect_to_db():
    connection = psycopg2.connect(
        host="your-aws-host",
        database="your-database-name",
        user="your-username",
        password="your-password",
        port="your-port"
    )
    return connection

# Fetch data
def fetch_data(query):
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

