
"Write a Python program to perform matrix multiplication using lists of lists."

def matrix_multiply(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


matrix1 = [
    [1, 2],
    [3, 4,]
]
matrix2 = [
    [5, 1],
    [2, 4]
]
result = matrix_multiply(matrix1, matrix2)

for i in result:
    print(i)
