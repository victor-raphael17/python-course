# Combining lists and nested lists

# Combine two lists into one

numbers = [1, 2, 3]

letters = ['a', 'b', 'c']

comb = numbers + letters

print(comb)

# Make multiple copies of a list

numbers2 = numbers * 2

print(numbers2)

# Create a nested list from two lists

nested = [numbers, letters]

print(nested)

# Extend a list with another list

number = [1, 2, 3]

letters = ['a', 'b', 'c']

numbers.extend(letters) # extends doesn't create a new list, it modifies the existing one

print(numbers)

# zip() is used to pair elements from two or more lists into tuples
# the output will be an iterator of tuples, so you need to convert it to a list
# python will stop at the shortest list

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4, 5]

zipped = zip(letters, numbers)

print((zipped))
print(list(zipped))

# you can also zip with more than two lists or iterables, like strings

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

zipped = zip(letters, numbers, 'XYZ')

print(list(zipped))

# Rebuild the relationship - pair customers with their IDs

ids = [1001, 1002, 1003]

customers = ['Alice', 'Bob', 'Charlie']

paired = list(zip(ids, customers))

print(paired)
