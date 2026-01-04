# Iterator vs Iterable

letters = ['a', 'b', 'c']

new_list = []

for l in letters:
    new_list.append(l.upper())

print(new_list)

# Iterators are objects that implement the iterator protocol, 
# which consists of the methods __iter__() and __next__().

# enumerate

letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):
    print(index, letter)

# reversed

letters = ['a', 'b', 'c']

for letter in reversed(letters):
    print(letter)

# Zip - combine two or more iterables into tuples

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for letter, number in zip(letters, numbers):
    print(letter, number)

# Make every letters from a string uppercase, normal and using map

letters = ['a', 'b', 'c']

for i in range(len(letters)):
    letters[i] = str.upper(letters[i])

print(letters)
# Now using map

# map applies a function to all the items in an input list (or any iterable)

letters = ['a', 'b', 'c']

letters = list(map(str.upper, letters))

print(letters)

# Task: Convert list items to integers

numbers = ['1', '2', '3', '4', '5']

numbers = list(map(int, numbers))

print(numbers)

# Task: Cleanup the list by removing the all unwanted spaces

names = ['  John  ', '  Jane', 'Doe  ', ' Alice ']

names = list(map(str.strip, names))

print(names)

# Filter - filter items out of an iterable based on a function that tests each
# item in the iterable to be true or false

letters = ['a', '', 'b', None, 'c', ' ', False]

letters_copy = letters.copy()

letters_copy = list(filter(None, letters_copy))

letters_copy = list(map(str.strip, letters_copy))

letters_copy = list(filter(None, letters_copy))

print(letters_copy)

# Task: Keep only alphabetic items

names = ['John', 'Jane123', 'Doe!', 'Alice', 'Bob@']

names = list(filter(str.isalpha, names))

print(names)
