# Update values from a list/matrix

letters = ['a', 'b', 'c', 'd', 'e']

print(letters)  # Output: ['a', 'b', 'c', 'd', 'e']

letters[2] = 'X'  # Update the third element

print(letters)  # Output: ['a', 'b', 'X', 'd', 'e']

letters[-1] = 'z'  # Update the last element

print(letters)  # Output: ['a', 'b', 'X', 'd', 'z']

# Update the content of the last list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[-1] = [0, 0, 0]  # Update the last row

print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [0, 0, 0]]

# Update the first item of the first row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][0] = "X"

print(matrix)  # Output: [['X', 2, 3], [4, 5, 6], [7, 8, 9]]

# Update the last item of the last row

matrix[-1][-1] = "Y"

print(matrix)  # Output: [['X', 2, 3], [4, 5, 6], [7, 8, 'Y']]
