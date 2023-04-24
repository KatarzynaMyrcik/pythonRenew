#exercice lists 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[2][2])

for row in matrix:
    for column in row:
        print(column)
