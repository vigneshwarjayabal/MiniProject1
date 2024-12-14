import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
from queries import business_insights, provided_query, my_query

def database_connection():
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{st.secrets['postgresql']['user']}:{st.secrets['postgresql']['password']}@{st.secrets['postgresql']['host']}:{st.secrets['postgresql']['port']}/{st.secrets['postgresql']['database']}"
        )
        return engine
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

def fetch_query_results(query):
    engine = database_connection()
    if engine:
        try:
            df = pd.read_sql(query, con=engine)
            return df
        except Exception as e:
            st.error(f"Error executing query: {e}")
            return None
    return None

# Display results in Streamlit
def display_results(query_name, query):
    st.subheader(f"Results for {query_name}")
    data = execute_query(query)
    if data is not None:
        st.write(data)
    else:
        st.write("No results to display.")

# Main Streamlit app logic
st.title("Retail Order Data Analysis")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose Analysis Type",
    ["Business Insights", "Provided Query", "My Query"]
)

if option == "Business Insights":
    display_results("Business Insights", business_insights)
elif option == "Provided Query":
    display_results("Provided Query", provided_query)
elif option == "My Query":
    display_results("My Query", my_query)
else:
    st.write("Please select a valid option.")
