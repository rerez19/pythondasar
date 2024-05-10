import numpy as np

# Creating a 1-dimensional array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)

# Creating a 2-dimensional array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr2d)

# Reshaping an array
reshaped_arr = arr1d.reshape(5, 1)
print("\nReshaped Array:")
print(reshaped_arr)

# Accessing elements of an array
print("\nElement at index 2 of arr1d:", arr1d[2])
print("Element at row 1, column 2 of arr2d:", arr2d[1, 2])

# Performing mathematical operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
sum_array = arr1 + arr2
print("\nSum of two arrays:")
print(sum_array)

# Matrix multiplication
mul_array = np.dot(arr1, arr2)
print("\nMatrix multiplication result:")
print(mul_array)
