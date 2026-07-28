import pandas as pd

# Load your dataset
df = pd.read_csv("student_sales_data.csv")   # replace with your actual file name

# 1. Total
total_price = df["Price"].sum()
total_quantity = df["Quantity"].sum()
print("Total Price:", total_price)
print("Total Quantity:", total_quantity)

# 2. Average
avg_price = df["Price"].mean()
avg_quantity = df["Quantity"].mean()
print("Average Price:", avg_price)
print("Average Quantity:", avg_quantity)

# 3. Minimum
min_price = df["Price"].min()
min_quantity = df["Quantity"].min()
print("Minimum Price:", min_price)
print("Minimum Quantity:", min_quantity)

# 4. Maximum
max_price = df["Price"].max()
max_quantity = df["Quantity"].max()
print("Maximum Price:", max_price)
print("Maximum Quantity:", max_quantity)

# 5. Count
count_orders = df["OrderID"].count()
print("Total Orders (Count):", count_orders)

# Bonus: all-in-one summary
print(df.describe())