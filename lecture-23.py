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


