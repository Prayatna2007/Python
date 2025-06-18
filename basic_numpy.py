import numpy as np


arr1 = np.array([1, 2, 3, 4, 5])
print(f"Original 1D array: {arr1}")

print(f"Array + 5: {arr1 + 5}")
print(f"Array * 2: {arr1 * 2}")


print(f"Mean of array: {np.mean(arr1)}")
print(f"Standard deviation of array: {np.std(arr1)}")
print(f"Sum of array elements: {np.sum(arr1)}")


matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal 2D array:\n{matrix}")
print(f"Transposed matrix:\n{matrix.T}")