# Logical Operators

print(3 < 5 == 5)

print(3 > 1 and 5 < 1)

print(3 > 1 or 5 < 1)

# Not operator

print(3 > 1) # True

print(not(3 > 1)) # Original: True -> Negation: False

print(not(False)) # Original: False -> Negation: True

print(not(True)) # Original: True -> Negation: False

# Chained Comparisons

print(5 == 5 or 8 > 5 and 6 < 4) # true

# and has higher precedence than or, but you still should use parentheses for clarity

print(5 == 5 or (8 > 5 and 6 < 4)) # true

# you can also use parentheses to change precedence

print((5 == 5 or 8 > 5) and 6 < 4) # false

# Practical Example
# See if a user is allowed to access a resource, they are allowed if they are logged in or in guest
# mode, but not if they are banned

allow_user = False

is_logged_in = True

guest_mode = False

banned_user = False

allow_user = (is_logged_in or guest_mode) and not banned_user

print(allow_user)
