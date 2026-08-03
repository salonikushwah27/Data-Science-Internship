import pandas as pd

# Load your dataset
df = pd.read_csv("student_sales_data.csv")   # replace with your actual file name

# 1. Handle missing values
print(df.isnull().sum())          # check missing values per column
df = df.dropna()                  # option 1: remove rows with missing values
# df = df.fillna(0)               # option 2: fill missing values with 0 (alternative)

# 2. Remove duplicate records
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

# 3. Correct data types
print(df.dtypes)                  # check current data types
df["OrderID"] = df["OrderID"].astype(int)
df["Price"] = df["Price"].astype(float)

# Final check
print(df.info())
print(df.shape)