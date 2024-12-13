import streamlit as st
from sqlalchemy import create_engine
host = 'miniprojectdb.cv8yqowiopcb.ap-south-1.rds.amazonaws.com'
port = '5432'
database = 'postgres'
user = 'postgres'
password = 'dhoni00728'

connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)