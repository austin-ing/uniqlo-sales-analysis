import sqlite3
import pandas as pd
import os

# checks that a folder has been created for database and queries
os.makedirs("database", exist_ok=True)
os.makedirs("queries", exist_ok=True)

df = pd.read_csv("../data/uniqlo_sales_cleaned_data.csv")

conn = sqlite3.connect('database/uniqlo_sales.db')

# open
df.to_sql('sales', conn, if_exists='replace', index=False)

# INSERT SQL QUERIES
query_top_products = """
SELECT product_name, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY product_name
ORDER BY total_units_sold DESC
LIMIT 20;
"""

query_revenue_by_cat = """
SELECT product_category, subcategory, SUM(price * units_sold) AS total_revenue
FROM sales
GROUP BY product_category, subcategory
ORDER BY total_revenue DESC;
"""

query_sales_by_gender = """
SELECT gender, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY gender
ORDER BY total_units_sold DESC;
"""

query_sales_by_size = """
SELECT size, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY size
ORDER BY total_units_sold DESC;
"""

query_sales_by_color = """
SELECT color, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY color
ORDER BY total_units_sold DESC;
"""

query_avg_discount_rate = """
SELECT AVG(discount_applied) AS avg_discount_rate
FROM sales;
"""
query_impact_on_revenue = """
SELECT SUM(price * units_sold * (1 - discount_applied)) AS discounted_revenue
FROM sales;
"""
query_inventory_turnover = """
SELECT product_name, SUM(inventory_level) AS total_inventory, restock_indicator
FROM sales
GROUP BY product_name, restock_indicator
ORDER BY total_inventory DESC;
"""
query_sales_trend_by_season = """
SELECT season, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY season
ORDER BY season;
"""
query_sales_trend_by_channel = """
SELECT channel, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY channel
ORDER BY total_units_sold DESC;
"""

queries = {
    "top_products": query_top_products,
    "revenue_by_cat": query_revenue_by_cat,
    "gender_based_trends": query_sales_by_gender,
    "sales_by_size": query_sales_by_size,
    "sales_by_color": query_sales_by_color,
    "avg_discount_rate": query_avg_discount_rate,
    "impact_on_revenue": query_impact_on_revenue,
    "inventory_turnover": query_inventory_turnover,
    "sales_trend_by_season": query_sales_trend_by_season,
    "sales_trend_by_channel": query_sales_trend_by_channel
}

for name, query in queries.items():
    df_result = pd.read_sql_query(query, conn)
    df_result.to_csv(f"queries/{name}.csv", index=False)


conn.close()                # close when done