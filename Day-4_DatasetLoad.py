# 1. Import Pandas
import pandas as pd

# 2. Load a CSV dataset
df = pd.read_csv("student_sales_data.csv")   # replace with your actual file name/path

# 3. View rows
print(df.head())       # first 5 rows
print(df.tail())       # last 5 rows

# 4. View columns
print(df.columns)      # list of column names

# 5. View dataset information
print(df.info())       # data types, non-null counts
print(df.shape)        # (rows, columns)
print(df.describe())   # statistical summary (numeric columns)