import pandas as pd
import numpy as np
import csv


df = pd.read_csv("../data/uniqlo_sales_dataset.csv")

# data processing
df.head()                               # shows first 5 rows of data
df.info()                               # displays summary of data types, non-null values and memory usage
df.describe()                           # gives statistical summaries

cleaned_columns = []                    # Create an empty list to hold the cleaned column names

# Loop through each column name
for col in df.columns:
    col = col.strip()                   # Remove leading/trailing spaces
    col = col.lower()                   # Convert to lowercase
    col = col.replace(' ', '_')         # Replace spaces with underscores
    cleaned_columns.append(col)         # Add to new list


df.columns = cleaned_columns            # Assign cleaned column names back to the DataFrame

# data cleaning
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['revenue'] = df['price'] * df['units_sold']
df['discounted_price'] = df['price'] * (1 - df['discount_applied'])

# df = df.drop_duplicates()

duplicates = df.duplicated()
df_no_duplicates = df.drop_duplicates()             # remove duplicates

df.isnull().sum()
df = df.dropna()

df.to_csv("../data/uniqlo_sales_cleaned.csv", index=False)

df = pd.read_csv("../data/uniqlo_sales_cleaned.csv")

df.to_csv("data/uniqlo_sales_cleaned.csv", index=False)