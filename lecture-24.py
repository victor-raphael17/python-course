# Indexing & Slicing, Index for single items and Slicing for multiple items

#           0    1    2
letters = ["a", "b", "c"]
#          -3   -2   -1

print(letters)          # ['a', 'b', 'c']

print(letters[0])       # 'a'
print(letters[1])       # 'b'
print(letters[2])       # 'c'

print(letters[-1])      # 'c'
print(letters[-2])      # 'b'
print(letters[-3])      # 'a'

letters = ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]

print(letters)
print(type(letters))  # <class 'tuple'>, immutable

letters = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
] # matrix

print(letters)
print(type(letters))  # <class 'list'>, mutable

print(letters[0])       # ['a', 'b', 'c']
print(letters[1])       # ['d', 'e', 'f']
print(letters[2])       # ['g', 'h', 'i']

print(letters[0][0])    # 'a'
print(letters[0][1])    # 'b'
print(letters[0][2])    # 'c'
print(letters[1][0])    # 'd'
print(letters[1][1])    # 'e'
print(letters[1][2])    # 'f'
print(letters[2][0])    # 'g'
print(letters[2][1])    # 'h'
print(letters[2][2])    # 'i'

print(letters[-1]) # negative indexing
print(letters[-1][-1]) # negative indexing

# Slicing

letters = ["a", "b", "c", "d", "e"]

# letters[<start>:<end>] # start is inclusive, but the end is exclusive

# instead of using letters[0:<end>] you can use just letters[:<end>]

# instead of using letters[<start>:<last index +1>] you can use just letters[<begin>:]

print(letters[:2])    # ['a', 'b']
print(letters[2:])    # ['c', 'd', 'e']

letters = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

print(letters[:2]) # first two rows
print(letters[-2:]) # last two rows

print(letters[2][:2]) # two first elements of the third row
print(letters[-1][:2]) # two first elements of the last row
