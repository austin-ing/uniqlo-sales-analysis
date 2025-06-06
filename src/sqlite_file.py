import sqlite3
import pandas as pd

df = pd.read_csv("data/uniqlo_sales_cleaned_data.csv")

conn = sqlite3.connect('data/uniqlo_sales.db')

# open
cursor = conn.cursor()

df.to_sql('sales', conn, if_exists='replace', index=False)

# INSERT SQL QUERIES

query = "SELECT * FROM sales LIMIT 10;"
results = pd.read_sql_query(query, conn)
print(results)

conn.close()                # close when done