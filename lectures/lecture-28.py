# Sorting lists

# Sort lowest to highest

letters = ['d', 'a', 'c', 'b']

print(letters)

letters.sort()

print(letters)

numbers = [4, 1, 3, 2]

print(numbers)

numbers.sort()

print(numbers)

# Sort highest to lowest

print(letters)

letters.sort(reverse = True)

print(letters)

print(numbers)

numbers.sort(reverse = True)

print(numbers)

matrix = [
    [3, "X", "X"],
    [1, "X", "X"],
    [2, "X", "X"]
]

print(matrix)

matrix.sort() # sort by first element of each row, works with strings too

print(matrix)

matrix = [
    [3, "X", "X"],
    [1, 2, "X"],
    [1, 4, "X"]
]

print(matrix)

matrix.sort() # if first elements are equal, sort by second element

print(matrix)

# Sort the second row of the matrix

matrix = [
    ["a", "b", "c"],
    ["f", "e", "d"],
    ["g", "h", "i"]
]

matrix[1].sort()

print(matrix)

# Sort the data without modifying the original list

letters = ['d', 'a', 'c', 'b']

print(letters)

letters_sorted = sorted(letters)

print(letters_sorted)

# Sort the data without modifying the original list, highest to lowest

numbers = [4, 1, 3, 2]

print(numbers)

numbers_sorted = sorted(numbers, reverse = True)

print(numbers_sorted)

# Invert the order of a list

letters = ['3', '6', '12', 'X']

print(letters)

letters.reverse()

print(letters)

# Invert the order of a list without modifying the original list

letters = ['3', '6', '12', 'X']

print(letters)

letters_reversed = list(reversed(letters))

print(letters_reversed)
