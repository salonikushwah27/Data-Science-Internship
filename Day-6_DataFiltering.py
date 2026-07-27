import pandas as pd

# Load your dataset
df = pd.read_csv("student_sales_data.csv")   # replace with your actual file name

# 1. Filter rows (based on a condition)
filtered_df = df[df["Quantity"] > 3]          # example: rows where Quantity > 3
print(filtered_df)

# 2. Select specific columns
selected_cols = df[["OrderID", "Quantity", "Price"]]   # replace with your actual column names
print(selected_cols)

# 3. Sort the dataset
sorted_df = df.sort_values(by="Price", ascending=False)   # sort by Price, highest first
print(sorted_df)

# Save the filtered dataset (optional, but good practice for "Filtered dataset created")
filtered_df.to_csv("filtered_dataset.csv", index=False)