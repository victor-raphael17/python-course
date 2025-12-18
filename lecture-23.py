# Create lists

empty = []
print(empty)

print(type(empty)) #<class 'list'>

print(bool(empty)) # False

letters = ['a', 'b', 'c', 'd']

print(letters) # ['a', 'b', 'c', 'd']

print(type(letters)) # <class 'list'>

print(bool(letters)) # True

numbers = [1, 2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]

# You can mix data types in a list

mixed = [1, 'two', 3.0, True, None]

print(mixed) # [1, 'two', 3.0, True, None]

# You can use the function list() to create a list from an iterable

empty = list()
print(empty) # []
print(type(empty)) # <class 'list'>

letters = "Python"

letters_list = list(letters)
print(letters_list) # ['P', 'y', 't', 'h', 'o', 'n']

numbers = range(5)
numbers_list = list(numbers)
print(numbers_list) # [0, 1, 2, 3, 4

# Nested lists / Matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(type(matrix)) # <class 'list'>

mixed_matrix = [[1, 'two', 3.0], [True, None, 'six'], [7, 8, 9]]

print(mixed_matrix) # [[1, 'two', 3.0], [True, None, 'six'], [7, 8, 9]]

print(type(mixed_matrix)) # <class 'list'>

empty_matrix = [[], [], []]

print(bool(empty_matrix)) # [[], [], []]
