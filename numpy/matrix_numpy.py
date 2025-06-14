import numpy as np

def input_matrix(name):
    print(f"\nEnter values for {name} (3x3 matrix):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

matrix1 = input_matrix("Matrix 1")
matrix2 = input_matrix("Matrix 2")

result = matrix1 + matrix2

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nResult (Matrix1 + Matrix2):")
print(result)