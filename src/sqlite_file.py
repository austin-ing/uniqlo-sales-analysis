import sqlite3
import pandas as pd

df = pd.read_csv("data/uniqlo_sales_cleaned_data.csv")

conn = sqlite3.connect('data/uniqlo_sales.db')

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
df_top_products = pd.read_sql_query(query_top_products, conn)
df_top_products.to_csv("exports/top_selling_products.csv", index=False)

query_revenue_by_cat = """
SELECT product_category, subcategory, SUM(price * units_sold) AS total_revenue
FROM sales
GROUP BY product_category, subcategory
ORDER BY total_revenue DESC;
"""
df_revenue_by_cat = pd.read_sql_query(query_revenue_by_cat, conn)
df_revenue_by_cat.to_csv("exports/revenue_by_category.csv", index=False)

query_sales_by_gender = """
SELECT gender, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY gender
ORDER BY total_units_sold DESC;
"""
df_sales_by_gender = pd.read_sql_query(df_sales_by_gender, conn)
df_sales_by_gender.to_csv("edports/sales_by_gender.csv", index=False)

query_sales_by_size = """
SELECT size, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY size
ORDER BY total_units_sold DESC;
"""
df_sales_by_size = pd.read_sql_query(query_sales_by_size, conn)
df_sales_by_size.to_csv("exports/sales_by_size.csv", index=False)

query_sales_by_color = """
SELECT color, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY color
ORDER BY total_units_sold DESC;
"""
df_sales_by_color = pd.read_sql_query(query_sales_by_color, conn)
df_sales_by_color.to_csv("exports/sales_by_color.csv", index=False)



queries = {
    "gender_based_trends": query_gender_based_trends,
    "sales_by_size": query_sales_by_size,
    "sales_by_color": query_sales_by_color
}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"exports/{name}.csv", index=False)


conn.close()                # close when done