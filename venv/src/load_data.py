import pandas as pd
import numpy as np


df = pd.read_csv("uniqlo_sales_dataset.csv")

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