import pandas as pd
from sqlalchemy import create_engine
import streamlit as st

business_insigths = {
  "Top-Selling Products":"SELECT p.product_id, p.category,p.sub_category,SUM(o.sale_price * o.quantity) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ORDER BY total_revenue DESC LIMIT 10;",
  "Monthly Sales Analysis":"SELECT DATE_PART('year', CAST(o.order_date AS DATE)) AS year, DATE_PART('month', CAST(o.order_date AS DATE)) AS month, SUM(o.sale_price * o.quantity) AS monthly_revenue FROM orders o GROUP BY DATE_PART('year', CAST(o.order_date AS DATE)), DATE_PART('month', CAST(o.order_date AS DATE)) ORDER BY year, month;",
  "Product Performance":"WITH ProductPerformance AS ( SELECT p.product_id, p.category,p.sub_category,SUM(o.sale_price * o.quantity) AS total_revenue, AVG(CASE WHEN p.cost_price = 0 THEN 0 ELSE (o.sale_price - p.cost_price) / p.cost_price END) AS profit_margin FROM orders o JOIN  products p ON  o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ) SELECT product_id,category,sub_category total_revenue, profit_margin, ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank FROM ProductPerformance;",
  "Regional Sales Analysis":"SELECT o.region, SUM(o.sale_price * o.quantity) AS regional_revenue, COUNT(DISTINCT o.order_id) AS total_orders FROM orders o GROUP BY o.region ORDER BY regional_revenue DESC;",
  }

provided_query = {
  "Find top 10 highest revenue generating products" :"SELECT p.product_id, p.category, p.sub_category,SUM(o.sale_price * o.quantity) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ORDER BY total_revenue DESC LIMIT 10;",
  "Find the top 5 cities with the highest profit margins":"SELECT city,CASE WHEN SUM(sale_price * quantity) = 0 THEN 0  ELSE SUM(profit) / SUM(sale_price * quantity) * 100 END AS profit_margin FROM orders GROUP BY city ORDER BY profit_margin DESC LIMIT 5;",
  "Calculate the total discount given for each category":"SELECT p.category,SUM(o.discount) AS total_discount  FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category;",
  "Find the average sale price per product category":"SELECT p.category,AVG(o.sale_price) AS average_sale_price  FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category;",
  "Find the region with the highest average sale price":"SELECT region ,AVG(sale_price) AS average_sale_price  FROM orders GROUP BY region ORDER BY average_sale_price DESC LIMIT 1;",
  "Find the total profit per category":"SELECT p.category,SUM(o.profit) AS total_profit FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category;",
  "Identify the top 3 segments with the highest quantity of orders":"SELECT segment,SUM(quantity) AS total_quantity FROM orders GROUP BY segment ORDER BY total_quantity DESC LIMIT 3;",
  "Determine the average discount percentage given per region":"SELECT o.region,AVG(p.discount_percent) AS average_discount_percentage FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY o.region;",
  "Find the product category with the highest total profit":"SELECT p.category, SUM(o.profit) AS total_profit FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category ORDER BY total_profit DESC LIMIT 1;",
  "Calculate the total revenue generated per year":"SELECT DATE_PART('year', CAST(order_date AS DATE)) AS year, SUM(sale_price * quantity) AS total_revenue FROM orders GROUP BY DATE_PART('year', CAST(order_date AS DATE)) ORDER BY year;"
}

my_query = {
  "Identify the month with the highest sales revenue":"SELECT DATE_PART('month', CAST(order_date AS DATE)) AS month, SUM(sale_price * quantity) AS total_revenue FROM orders GROUP BY DATE_PART('month', CAST(order_date AS DATE)) ORDER BY total_revenue DESC LIMIT 1;",
  "Find the average profit margin for each product category":"SELECT p.category, AVG(CASE WHEN (o.sale_price * o.quantity) = 0 THEN 0 ELSE (o.profit / (o.sale_price * o.quantity)) * 100 END) AS average_profit_margin FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category;",
  "Calculate the percentage contribution of each region to total sales":"SELECT region,SUM(sale_price * quantity) / (SELECT SUM(sale_price * quantity) FROM orders) * 100 AS sales_percentage FROM orders GROUP BY region ORDER BY sales_percentage DESC;",
  "Find the sub-category with the highest number of orders":"SELECT p.sub_category, SUM(o.quantity) AS total_quantity FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.sub_category ORDER BY total_quantity DESC LIMIT 1;",
  "Determine the top 3 states with the highest discounts given":"SELECT state, SUM(discount) AS total_discount FROM orders GROUP BY state ORDER BY total_discount DESC LIMIT 3;",
  "Find the Top 3 Profitable Products by product_id and Category":"SELECT p.product_id, p.category,p.sub_category, SUM(o.profit) AS total_profit FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ORDER BY total_profit DESC LIMIT 3;",
   "Calculate the total number of orders per shipping mode":"SELECT ship_mode, COUNT(order_id) AS total_orders FROM orders GROUP BY ship_mode ORDER BY total_orders DESC;",
  "Find the customer segment with the highest average sale":"SELECT segment, AVG(sale_price) AS average_sale_price FROM orders GROUP BY segment ORDER BY average_sale_price DESC LIMIT 1;",
  "Calculate the total profit generated per year":"SELECT DATE_PART('year', CAST(order_date AS DATE)) AS year, SUM(profit) AS total_profit FROM orders GROUP BY DATE_PART('year', CAST(order_date AS DATE)) ORDER BY year;",
  "Identify the least profitable region":"SELECT region, SUM(profit) AS total_profit FROM orders GROUP BY region ORDER BY total_profit ASC LIMIT 1;"

}

def database_connection():
    try:
        
        connection_string = (
            f"postgresql+psycopg2://{st.secrets['postgresql']['user']}:"  # Updated for PostgreSQL
            f"{st.secrets['postgresql']['password']}@"
            f"{st.secrets['postgresql']['host']}/"
            f"{st.secrets['postgresql']['database']}"
        )
        engine = create_engine(connection_string)
        return engine
    except Exception as err:
        st.error(f"Error connecting to the database: {err}")
        return None


def execute_query(query):
    try:
        engine = database_connection()
        if engine is not None:
            with engine.connect() as connection:
                result = pd.read_sql_query(query, connection)
            return result
        else:
            st.error("Database connection failed.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error executing the query: {e}")
        return pd.DataFrame()


def display_results(selection, query):
    st.subheader(selection)
    selected_query = st.selectbox("Choose a query", list(query.keys()))
    st.write("**Query:**")
    st.code(f"{query[selected_query]}")
    if st.button("Run", key=f"run_button_{selected_query}"):
        result = execute_query(query[selected_query])
        if not result.empty:
            st.write("**Result:**")
            return st.dataframe(result)
        else:
            st.warning("No data returned for the query.")


st.title("Retail Order Data Analysis")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose Analysis Type",
    ["Business Insights", "Provided Query", "My Query"]
)
if option == "Business Insights":
    display_results("Business Insights",business_insigths)
elif option == "Provided Query":
    display_results("Provided Query", provided_query)
elif option == "My Query":
    display_results("My Query", my_query)
else:
    st.write("Please select a valid option.")
