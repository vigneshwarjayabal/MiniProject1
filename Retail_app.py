import pandas as pd
import pg8000  # Alternative PostgreSQL library
import streamlit as st
from queries import business_insights, provided_query, my_query

# Database connection
def database_connection():
    try:
        # Establish connection using pg8000
        connection = pg8000.connect(
            host=st.secrets["postgresql"]["host"],  
            user=st.secrets["postgresql"]["user"],  
            password=st.secrets["postgresql"]["password"], 
            database=st.secrets["postgresql"]["database"],
            port=int(st.secrets["postgresql"]["port"])  # Ensure port is an integer
        )
        return connection
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None

# Execute a query and return results
def execute_query(query):
    connection = database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            cursor.close()
            connection.close()
            return pd.DataFrame(result, columns=columns)
        except Exception as e:
            st.error(f"Error executing query: {e}")
            return None
    else:
        st.error("No database connection.")
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
