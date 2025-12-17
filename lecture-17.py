# for loop, example: print 1 to 5

#print("2")
#print("3")
#print("1")
#print("4")
#print("5")

# for "i" in "sequence" - sequences can be tuple, list, string or range

for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

for i in range(1, 6):
    print(f"Round: {i}")

items = (1, 2, 3, 4, "Hi")

print(type(items)) # tuple

# A tuple in Python is an ordered, immutable collection of values (written like (1, 2, 3) 
# that can hold mixed types. You use tuples to group data, access by index/slice,
# iterate or unpack (a, b = t), and — because they're immutable and hashable when their items are
# hashable — use them as dictionary keys or set elements; they have only simple methods like
# index() and count().

for item in items:
    print(f"Round: {item}")

items = [1,2,3,4,5]

print(type(items)) # list

# A list in Python is an ordered, mutable collection written with square brackets like
# [1, 2, 3] that can hold mixed types. You can change it after creation (append, extend,
# insert, pop, remove, clear), sort or reverse it, access by index/slice, iterate or unpack
# (a, b = lst[:2]), and copy it; lists are not hashable so they can’t be used as dict keys
# or set elements, which makes them perfect for dynamic, changeable collections.

for item in items:
    print(f"Round: {item}")

stringTest = "PythonDihh"

for letter in stringTest:
    print(f"Round: {letter}")

# The range() type
# range(stop)
#  - If you pass one argument it's the stop (exclusive). start defaults to 0.
#  - Example: list(range(5)) -> [0, 1, 2, 3, 4]
#
# range(start, stop)
#  - Generates values from start (inclusive) to stop (exclusive).
#  - Example: list(range(1, 6)) -> [1, 2, 3, 4, 5]
#
# range(start, stop, step)
#  - step is optional and can be positive or negative (but not zero).
#  - Values go from start to stop (exclusive), advancing by step each time.
#  - Example: list(range(0, 10, 2)) -> [0, 2, 4, 6, 8]
#  - Example (negative step): list(range(10, 0, -2)) -> [10, 8, 6, 4, 2]
#
# Notes:
#  - range() returns a range object (an iterable), not a list — convert with list()
#  - stop is always exclusive
#  - step cannot be 0 (ValueError)

# Example of for usage

# Add all the values and divide then by the amount (average)

scores = [80, 50, 60, 75]
total = 0

for score in scores:
    total += score

print(total)

# Real world case

files = [' Report.csv ', 'DATA.csv ', ' final.TXT']

# imagine that this list could be thousand times long, you could use for in this case:
# strip() to remove extra spaces, lower() to padronize the files names and replace() to move
# .txt to .csv

for i in range(len(files)):
    files[i] = files[i].strip().lower().replace('txt', 'csv')

print(files)
