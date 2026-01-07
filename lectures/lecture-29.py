# Copying with lists

letters = ['a', 'b', 'c', 'd', 'e']

letters_copy = letters

print("Original list:", letters)
print("Copied list:", letters_copy)

letters_copy.append('f')

print("Original list is changed: ", letters)

# In memory, both variables point to the same list object

# Shallow Copy, <list>.copy() creates a separete object in memory, but only one level deep

letters = ['a', 'b', 'c', 'd', 'e']

letters_copy = letters.copy()

print("Original list:", letters)
print("Copied list:", letters_copy)

letters_copy.append('f')

print("Original list is unchanged: ", letters)
print("Copied list after modification: ", letters_copy)

# Deep Copy, copy() doesn't work for matrix

import copy

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

matrix_copy = copy.deepcopy(matrix)

# copy.deepcopy() creates a completely separate object in memory, including all nested objects

matrix_copy[0][0] = "asdf"

print("Original matrix is unchanged: ", matrix)
print("Copied matrix after modification: ", matrix_copy)

# copy.copy() creates a shallow copy of the object, just like <list>.copy()

# Explanation with IS operator

original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"\noriginal: {original}")

copy1 = original

print(f"\noriginal is copy1: {original is copy1} - normal assignment")

copy2 = original.copy()

print(f"\noriginal is copy2: {original is copy2} - shallow copy")
print(f"\nshared lists?: {original[0] is copy2[0]} - shallow copy")

copy3 = copy.deepcopy(original)

print(f"\noriginal is copy3: {original is copy3} - deep copy")
print(f"\nshared lists?: {original[0] is copy3[0]} - deep copy")
