# Explore and analyse lists

numbers = [1, 5, 2, 4, 3]

# max(<list>) # Find the highest value in a list

print(f"Max: {max(numbers)}")

# min(<list>) # Find the lowest value in a list

print(f"Min: {min(numbers)}")

# sum(<list>) # Find the sum of all values in a list

print(f"Sum: {sum(numbers)}")

# len(<list>) # Find the length of a list

print(f"Length: {len(numbers)}")

# all(<list>) # Check if all values in a list are True

print(f"All: {all(numbers)}")

# any(<list>) # Check if any value in a list is True

print(f"Any: {any(numbers)}")

# <list>.count(<value>) # Count how many times a value appears in a list

print(f"Count 2: {numbers.count(2)}")

# <list>.index(<value>) # Find the index of the first occurrence of a value in a list

print(f"Index of 4: {numbers.index(4)}")

# in <list> # Check if a value is in a list

print(f"Is 3 in list: {3 in numbers}")

print(f"6 is not in list: {6 not in numbers}")

# == <list> # Check if two lists are equal

other_numbers = [1, 5, 2, 4, 3]

print(f"Lists are equal: {numbers == other_numbers}")
