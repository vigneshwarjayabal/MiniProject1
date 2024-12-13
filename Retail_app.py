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

st.sidebar.title("Navigation")
options = ['Top-Selling Products', 'Monthly Sales Analysis', 'Product Performance', 'Regional Sales Analysis', 'Discount Analysis']
selection = st.sidebar.radio("Select an option", options)

if selection == 'Top-Selling Products':
    st.header("Top-Selling Products")
    query = """
    SELECT p.product_id, p.category, p.sub_category,
    SUM(o.sale_price * o.quantity) AS total_revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.product_id, p.category, p.sub_category
    ORDER BY total_revenue DESC LIMIT 10;
    """
    data = fetch_data(query)
    st.dataframe(data)

    # Plotting top-selling products
    fig = px.bar(data, x='product_id', y='total_revenue', color='category', title="Top-Selling Products")
    st.plotly_chart(fig)

elif selection == 'Monthly Sales Analysis':
    st.header("Monthly Sales Analysis")
    query = """
    SELECT DATE_PART('year', CAST(o.order_date AS DATE)) AS year,
    DATE_PART('month', CAST(o.order_date AS DATE)) AS month,
    SUM(o.sale_price * o.quantity) AS monthly_revenue
    FROM orders o
    GROUP BY DATE_PART('year', CAST(o.order_date AS DATE)),
    DATE_PART('month', CAST(o.order_date AS DATE))
    ORDER BY year, month;
    """
    data = fetch_data(query)
    st.dataframe(data)

    # Plotting monthly sales
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x='month', y='monthly_revenue', hue='year', ax=ax)
    st.pyplot(fig)

elif selection == 'Product Performance':
    st.header("Product Performance")
    query = """
    WITH ProductPerformance AS (
        SELECT p.product_id, p.category, p.sub_category,
        SUM(o.sale_price * o.quantity) AS total_revenue,
        AVG(CASE WHEN p.cost_price = 0 THEN 0
        ELSE (o.sale_price - p.cost_price) / p.cost_price END) AS profit_margin
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        GROUP BY p.product_id, p.category, p.sub_category
    )
    SELECT product_id, category, sub_category, total_revenue, profit_margin,
    ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM ProductPerformance;
    """
    data = fetch_data(query)
    st.dataframe(data)

    # Plotting product performance
    fig = px.scatter(data, x='total_revenue', y='profit_margin', color='category', hover_name='product_id', title="Product Performance")
    st.plotly_chart(fig)

elif selection == 'Regional Sales Analysis':
    st.header("Regional Sales Analysis")
    query = """
    SELECT o.region, SUM(o.sale_price * o.quantity) AS regional_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
    FROM orders o
    GROUP BY o.region
    ORDER BY regional_revenue DESC;
    """
    data = fetch_data(query)
    st.dataframe(data)

    # Plotting regional sales
    fig = px.pie(data, names='region', values='regional_revenue', title="Regional Sales Distribution")
    st.plotly_chart(fig)

elif selection == 'Discount Analysis':
    st.header("Discount Analysis")
    discount_analysis = df.groupby('discount_percent')['discount'].agg(['mean', 'median', 'count']).reset_index()

    # Plotting discount analysis
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=discount_analysis, x='discount_percent', y='count', palette='viridis', ax=ax)
    ax.set_title('Frequency of Discount Percentages')
    ax.set_xlabel('Discount Percent')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='discount_percent', y='discount', palette='coolwarm', ax=ax)
    ax.set_title('Distribution of Discounts by Discount Percent')
    ax.set_xlabel('Discount Percent')
    ax.set_ylabel('Discount')
    st.pyplot(fig)