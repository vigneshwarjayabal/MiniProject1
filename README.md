                                                      Retail Order Data Analysis 📊
Overview

The Retail Order Data Analysis project is aimed at analyzing and optimizing sales performance using a dataset of sales transactions. By leveraging Python, Pandas, PostgreSQL, and Streamlit, this project uncovers valuable insights such as top-performing products, regional sales trends, and profit-driving subcategories. The project involves 20 SQL queries: 10 provided by GUVI and 10 framed independently for deeper business insights.

                                                        Problem Statement 🚩
:red_square: Objective:

:fast_forward: To analyze and optimize sales performance by identifying key trends, top-performing products, and growth opportunities.

:red_square: Goals:

:fast_forward: Identify products and categories contributing the most to revenue and profit.

:fast_forward: Analyze Year-over-Year (YoY) and Month-over-Month (MoM) sales trends.

:fast_forward: Highlight subcategories with the highest profit margins to guide decision-making.

                                                          Dataset 📁
:ledger: Source: Extracted from Kaggle using the Kaggle API.

:bookmark: Download Code: !kaggle datasets download ankitbansal06/retail-orders -f orders.csv

                                                        Project Workflow 🔄

Step 1: Data Extraction

:dart: Used the Kaggle API to fetch the dataset in ZIP format.

:dart: Automated the extraction process using Python (unzip CSV files for analysis).

Step 2: Data Cleaning 🧹

:dart: Library: Pandas

:dart: Steps taken to clean and standardize the dataset:

:dart: Handling Missing Values: Replaced or dropped rows with missing critical fields.

:dart: Renaming Columns: Standardized column names (e.g., Order ID → order_id).

:dart: Trimming Spaces: Removed extra spaces from text fields.

:dart:Derived Metrics:

:dart: Calculated discount, sale price, and profit as new columns.

Step 3: SQL Integration with PostgreSQL 💻

:dart: Divided the dataset into two relational tables: Orders Table and Products Table

:dart: Connected PostgreSQL with Google Colab using AWS, psycopg2-binary, and SQLAlchemy.

:dart: Established relationships using Primary Keys and Foreign Keys.

Step 4: Data Analysis with SQL 📈

Performed SQL queries to extract business insights and answer questions:

:dart: Business Insights:

:pencil: Top-Selling Products: Products generating the highest revenue.

:pencil: Monthly Sales Trends: Analyzed YoY and MoM sales growth.

:pencil: Product Performance: Ranked products using GROUP BY, HAVING, ROW_NUMBER(), and CASE WHEN.

:pencil: Regional Sales Insights: Identified high-performing regions.

:pencil: Discount Analysis: Evaluated the impact of discounts >20% on sales.

:dart: SQL Queries:

:pencil: 10 Queries provided by GUVI for basic business analysis.

:pencil: 10 Additional Queries framed independently for deeper insights.

Step 5: Streamlit Dashboard 🚀

:dart: Created an interactive Streamlit App to visualize Query outputs.

:bookmark: App Link:https://retail-order-data-analysis.streamlit.app/

                                                        Key Tools & Technologies 🛠️
:black_nib: Python: Data Cleaning and Processing

:black_nib: Pandas: Data Manipulation

:black_nib: PostgreSQL: Relational Database

:black_nib: AWS: Cloud Integration

:black_nib: Streamlit: Dashboard Visualization

:black_nib: Kaggle API: Data Extraction

                                                           Outputs 🎯

:pushpin: Identified best-selling products and their revenue contribution.

:pushpin: Highlighted monthly sales growth and decline patterns.

:pushpin: Provided insights into high-profit categories and subcategories.

:pushpin: Quantified the impact of discounts on overall sales performance.

:pushpin: Framed custom SQL queries to answer advanced business questions

                                                       Future Enhancements 🌟
:scroll: Add advanced data visualization using Plotly.

:scroll: Integrate Machine Learning to predict future sales trends.

:scroll: Optimize SQL queries for larger datasets.

                                                         Contributors 🤝
:medal_military: Vigneshwar j

                                                         Connect with Me 🔗
Feel free to reach out if you have questions or suggestions:

:globe_with_meridians: LinkedIn: www.linkedin.com/in/vigneshwarj28

:globe_with_meridians: GitHub: https://github.com/vigneshwarjayabal/MiniProject1.git






