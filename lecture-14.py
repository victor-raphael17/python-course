# Membership Operators: in, not in

print("apple" in "banana, pêssego e uva") # False

print("apple" not in "banana, pêssego e uva") # True

list = [1, 2, 3, 4, 5]

print(3 in list) # True

print(6 not in list) # True

# Task: ensure the domain is not banned

domain = "gmail.com"

banned_domains = ["banned.com", "spam.com", "fake.com"]

is_domain_safe = (domain not in banned_domains)

print(is_domain_safe) # True

# Identity Operators: is, is not. This checks if two variables point to the same object id in memory.

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # True
print(x is y) # False

x = 10
y = 10

print(x == y) # True
print(x is y) # True

x = 12
y = x

print(x == y) # True
print(x is y) # True

x = True
y = True

print(x is y) # True
print(x is not y) # False

# Task: Validate an email address, it must be filled and not empty

# Always use 'is not' to check for None, instead of '!=', because None is a singleton in Python.

email = ""

print(email is not None and email != "") # False

email = "email@gmail.com"

print(email is not None and email != "") # True
