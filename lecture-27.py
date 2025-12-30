# How to add, remove and modify elements in a list in Python

letters = ['a', 'b', 'c']

print(letters)

# appending an element to the end of the list

letters.append('d')

print(letters)

letters.append('e')

print(letters)

# inserting an element at a specific index

letters = ['a', 'b', 'c']

letters.insert(0, 'x')

print(letters)

letters.insert(2, 'y')

print(letters)

# Add new row to the end of a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

matrix.append([10, 11, 12])

print(matrix)

# Add new row at the start of a matrix

matrix.insert(0, [0, 0, 0])

print(matrix)
