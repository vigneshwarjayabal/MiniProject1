import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def create_connection():
    conn = psycopg2.connect(
        host = 'miniprojectdb.cv8yqowiopcb.ap-south-1.rds.amazonaws.com',
        port = '5432',
        database = 'postgres',
        user = 'postgres',
        password = 'dhoni00728'

    )
    return conn

def fetch_data(query):
    conn = create_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title('Retail Order Data Analysis')