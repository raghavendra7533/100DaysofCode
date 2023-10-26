# Calculate the sum of the diagonals of a square matrix using the length operator and for loop
matrix = [[2, 1, 3, 5],
          [1, 2, 1, 6],
          [4, 1, 1, 7],
          [3, 5, 6, 7]]

sum_of_the_matrix = 0
length_of_matrix = len(matrix)
for i in range(length_of_matrix):
    sum_of_the_matrix += matrix[i][i]
    if i != (length_of_matrix-1)-i:
        sum_of_the_matrix += matrix[i][(length_of_matrix-1)-i]


print(sum_of_the_matrix)
