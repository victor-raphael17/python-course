# Remove elements from a list

# Remove everything from the list

letters = ['a', 'b', 'c']

print(letters)

letters.clear()

print(letters)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

matrix.clear()

print(matrix)

# <list>.remove(x) - removes the first occurrence of x from the list

letters = ['a', 'b', 'a']

print(letters)

letters.remove('a')

print(letters)  # Output: ['b', 'a']

# <list>.pop([i]) - removes and returns the element at index i (default is the last element)

letters = ['a', 'b', 'c']

print(letters)

_ = letters.pop(1)

print(letters)          # Output: ['a', 'c']

print(_)                # Output: 'b'

# Remove the last row from a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]   

print(matrix)

matrix.pop()

print(matrix)          # Output: [[1, 2, 3], [4, 5, 6]]

# Remove the first occurrence of number 5 from the matrix
# notice that matrix.remove(<number>) won't work here, because the elements of the 
# matrix are lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 8, 9]
]

print(matrix)

matrix[1].remove(5)

print(matrix)  # Output: [[1, 2, 3], [4, 6], [1, 8, 9]]

# Remove the first element from the last row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 8, 9]
]

print(matrix)

matrix[-1].pop(0)

print(matrix)

# Remove the last item from the first row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 8, 9]
]

matrix[0].pop()

print(matrix)  # Output: [[1, 2], [4, 5, 6], [1, 8, 9]]
