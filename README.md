# Codomax Internship

## Day 1

### Task
Environment Setup: Installed Python, VS Code, Jupyter Notebook, and Git. Created a GitHub repository.

### Tools Installed
- Python
- VS Code
- Jupyter Notebook
- Git

### Output
Ran a basic Python script that prints a welcome message to confirm the development environment was set up correctly.

---

## Day 2

### Task
Python Basics: Practiced variables, data types, operators, loops, and functions.

### Topics Covered
- Variables and data types (string, integer, float, boolean)
- Operators (addition, subtraction, multiplication, division, remainder, comparison)
- Loops (for loop, while loop)
- Functions (defining and calling functions)

### Output
Wrote and ran `Day-2_PythonBasics.py`, printing variable values, operator results, loop outputs, and a custom greeting function.

---
## Day 3

### Task
Numpy Fundamentals: Learned how to create and work with Numpy arrays, including 1D, 2D, and 3D arrays, arrays of zeros and ones, range-based arrays, mathematical operations, and array shape calculations.

### Topics Covered
- Creating 1D, 2D, and 3D Numpy arrays
- Checking array shape using `.shape`
- Generating arrays of zeros and ones with `np.zeros()` and `np.ones()`
- Creating range-based arrays using `np.arange()`
- Performing basic mathematical operations (addition, subtraction, multiplication, division) between arrays
- Using Numpy functions: `np.sqrt()`, `np.sum()`, `np.mean()`, `np.max()`, `np.min()`
- Working with matrices and checking their shape

### Output
Successfully created and printed different types of Numpy arrays (1D, 2D, 3D), performed mathematical operations between arrays, and calculated statistical values like sum, mean, max, and min using Numpy functions.

## Day 4

### Task
Pandas Basics: Imported Pandas, loaded a CSV dataset, and viewed rows, columns, and dataset information.

### Topics Covered
- Importing the Pandas library
- Loading a CSV dataset using `pd.read_csv()`
- Viewing rows using `head()` and `tail()`
- Viewing column names using `columns`
- Viewing dataset information using `info()`, `shape`, and `describe()`

### Output
Wrote and ran `Day-4_DatasetLoad.py`, successfully loading `student_sales_data.csv` and printing dataset rows, columns, shape, and statistical summary.

---

## Day 5

### Task
Data Cleaning: Cleaned a raw dataset using Pandas — handled missing values, removed duplicate records, and corrected data types.

### Steps Performed
- Loaded the dataset using `pd.read_csv()`
- Checked and handled missing values using `isnull()` and `dropna()`
- Identified and removed duplicate records using `duplicated()` and `drop_duplicates()`
- Verified and corrected column data types using `dtypes`

### Output
Produced a cleaned dataset free of missing values, duplicate records, and incorrect data types — ready for further analysis.

## Day 6

### Task
Data Filtering: Filtered and sorted the cleaned dataset using Pandas — extracted specific rows and columns, and sorted records based on a key column.

### Steps Performed
- Filtered rows based on a condition using boolean indexing (`df[df["Quantity"] > 3]`)
- Selected specific columns of interest (`OrderID`, `Quantity`, `Price`)
- Sorted the dataset by `Price` in descending order using `sort_values()`
- Saved the filtered dataset to a new CSV file using `to_csv()`

### Output
Produced a filtered and sorted dataset (`filtered_dataset.csv`) containing only the relevant rows and columns, ordered by price.

## Day 7

### Task
Data Analysis: Performed statistical analysis on the cleaned dataset using Pandas — calculated total, average, minimum, maximum, and count of key columns.

### Steps Performed
- Loaded the dataset using `pd.read_csv()`
- Calculated total price and total quantity using `sum()`
- Calculated average price and average quantity using `mean()`
- Found minimum price and quantity using `min()`
- Found maximum price and quantity using `max()`
- Counted total orders using `count()`
- Generated an overall statistical summary using `df.describe()`

### Output
Produced key statistical insights (total, average, minimum, maximum, and count) along with a complete summary of the dataset using `describe()`.

## Day 8

### Task
Data Visualization: Created visual representations of the cleaned dataset using Matplotlib — bar chart, line chart, and pie chart — to understand patterns and distributions in the data.

### Steps Performed
- Imported `matplotlib.pyplot as plt` alongside Pandas
- Created a bar chart of `Quantity` for the first 10 orders using `plt.bar()`
- Created a line chart of `Price` trend for the first 20 orders using `plt.plot()` with markers
- Created a pie chart showing the distribution of `Quantity` values using `plt.pie()` with percentage labels (`autopct`)
- Added titles, axis labels, and legends to each chart for clarity

### Output
Produced three charts (bar, line, and pie) giving a clear visual understanding of order quantities, price trends, and quantity distribution across the dataset.

### Author
[Saloni Kushwah]


