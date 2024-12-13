query = {
  "Top-Selling Products":"SELECT p.product_id, p.category,p.sub_category,SUM(o.sale_price * o.quantity) AS total_revenue FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ORDER BY total_revenue DESC LIMIT 10;",
  "Monthly Sales Analysis":"SELECT DATE_PART('year', CAST(o.order_date AS DATE)) AS year, DATE_PART('month', CAST(o.order_date AS DATE)) AS month, SUM(o.sale_price * o.quantity) AS monthly_revenue FROM orders o GROUP BY DATE_PART('year', CAST(o.order_date AS DATE)), DATE_PART('month', CAST(o.order_date AS DATE)) ORDER BY year, month;",
  
  "Product Performance":"WITH ProductPerformance AS ( SELECT p.product_id, p.category,p.sub_category,SUM(o.sale_price * o.quantity) AS total_revenue, AVG(CASE WHEN p.cost_price = 0 THEN 0 ELSE (o.sale_price - p.cost_price) / p.cost_price END) AS profit_margin FROM orders o JOIN  products p ON  o.product_id = p.product_id GROUP BY p.product_id, p.category,p.sub_category ) SELECT product_id,category,sub_category total_revenue, profit_margin, ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank FROM ProductPerformance;",
  
"Regional Sales Analysis":"SELECT o.region, SUM(o.sale_price * o.quantity) AS regional_revenue, COUNT(DISTINCT o.order_id) AS total_orders FROM orders o GROUP BY o.region ORDER BY regional_revenue DESC;",
  


}
