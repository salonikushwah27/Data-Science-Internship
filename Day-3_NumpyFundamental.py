import numpy as np

#Create Numpy arrays

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3d)
print("Shape:", arr3d.shape)

# Array of zeros and ones
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print("Zeros:\n", zeros)
print("Ones:\n", ones)

# Array with a range
range_arr = np.arange(1, 11)
print("Range Array:", range_arr)

#Mathematical Operations

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square root:", np.sqrt(a))
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))

#Array shape and calculations

matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix)
print("Shape:", matrix.shape)
print("Total elements:", matrix.size)
print("Transpose:\n", matrix.T)