# Types

x = 4.3
y = 3
z = 3 + 4j

print(type(x))  # float
print(type(y))  # int
print(type(z))  # complex

# Convert string to int

x = "5"
fixed_x = int(x)
print(type(fixed_x))  # int

# Get only int part of float

x = 5.7
fixed_x = int(x)
print(fixed_x)  # 5

# Convert int to float

x = 5
fixed_x = float(x)
print(fixed_x)  # 5.0

# Convert string to float

x = "5.7"
fixed_x = float(x)
print(fixed_x)  # 5.7

# Convert int/float to complex

x = 3
y = 4.5

fixed_x = complex(x, y)

print(fixed_x)  # (3+4.5j)

# Basic Math Operators

print(3 + 4)    # Addition: 7
print(10 - 2)   # Subtraction: 8
print(5 * 6)    # Multiplication: 30
print(8 / 2)    # Division: 4.0

# Floor Division

print(7 / 2)    # Division: 3.5

print(7 // 2)   # Floor Division: 3

# Remainder

# Usually used to check if a number is even or odd.

# The modulus operator (%) returns the remainder of a division operation.

# For example, 7 divided by 3 is 2 with a remainder of 1.

print(7 % 3)    # Remainder: 1

# Exponentiation

print(2 ** 3)   # 2 raised to the power of 3

# Shortcuts

x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # 8

# Absolute Value

# Returns the absolute value of a number

# It's useful for distance calculations and when you need to ensure a non-negative result.

x = 2 - 10 # -8
print(abs(x))  # 8

# Rounding Numbers

price = 7.56789

print(round(price))      # 8
print(round(price, 2))   # 7.57 # As you can see, it rounded up two decimal places.

# Floor

# Floor is not a built-in function, so we need to import it from the math module.

import math

price = 7.56789

print(math.floor(price))  # 7

# Ceiling

# Ceiling is also not a built-in function, so we need to import it from the math module
# we already did that above.

price = 7.12345

print(math.ceil(price))   # 8

# Random numbers

import random

x = random.random()  # Returns a random float between 0.0 and 1.0

print(x)

y = random.randint(1, 10)  # Returns a random integer between 1 and 10 (inclusive)

# Validation

# is_integer() method checks if a float is an integer value.

x = 7.0 # In this case, mathematicaly, 7.0 is equal to 7, which is an integer.
        # However, in Python, 7.0 is of type float.

print(x.is_integer())  # True

print(type(x)) # Float

x = 7.5

print(x.is_integer())  # False

# isinstance() function checks if an object is an instance of a specified type.

x = 33.33

print(isinstance(x, float))  # True

print(isinstance(x, int))    # False

x = 5.0

print(isinstance(x, float))  # True

print(isinstance(x, int))    # False

x = 5

print(isinstance(x, int))    # True

print(isinstance(x, float))  # False
