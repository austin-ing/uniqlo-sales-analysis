import pandas as pd
import numpy as np


df = pd.read_csv("uniqlo_sales_dataset.csv")

df.head()       # shows first 5 rows of data
df.info()       # displays summary of data types, non-null values and memory usage
df.describe()   # gives statistical summaries