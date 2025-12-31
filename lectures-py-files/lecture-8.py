# Types

# Two functions, type(), return the data type and str(), which stringify a value.

a = "bosta"

b = 10

print(type(a))

print(str(b) + " text")

# Math

# len() function returns the length of a data structure like string, list, tuple, dictionary, etc.

password = "sword"

if len(password) < 8:
    print("Weak password")

# count() method counts how many times a value appears in a data structure. Count is case sensitive.

text = """
123123123
pinto
"""

print(text.count("123")) # Output is 3
print(text.count("pinto")) # Output is 1

# Transformation

# replace() method replaces occurrences of a substring with another substring in a string.

price = "100,50"

price.replace(",", ".") # Strings are immutable, so this does not change price

print(price) # Output is still "100,50"

price = price.replace(",", ".") # We need to reassign the variable

print(price) # Output is "100.50"

# f-string

# lets you embed expressions and variables inside string literals, using curly braces {}.

age = 25
name = "Yuriih"
gaming = True

print(f"My name is {name}, I'm {age} years old.\nGaming status: {gaming}")

# split() method splits a string into a list of substrings based on a specified delimiter (default is whitespace).

stamp = "2024-06-15 14:30:00"

print(stamp.split()) # Output is ['2024-06-15', '14:30:00']

stamp = "2024-06-15"

print(stamp.split("-")) # Output is ['2024', '06', '15']

# * operator works with strings

laugh = "ha"

print(laugh * 5) # Output is "hahahahaha"

# Indexing and Slicing

text = "Hello, World!"

text =  text[0:5] # could also be text[:5]

print(text) # Output is "Hello"

textFirstLetter = text[0]

# Remove spaces

# lstrip() removes white spaces from left side of the string

# rstrip() removes white spaces from right side of the string

# strip() removes white spaces from both sides of the string

# With these methods, you can also remove specific characters by passing them as an argument.

text = " DoorDash"
text2 = "DoorDash "
text3 = " DoorDash "
text4 = "##DoorDash##"

print(text.lstrip())  # Output is "DoorDash"
print(text2.rstrip()) # Output is "DoorDash"
print(text3.strip())  # Output is "DoorDash"
print(text4.strip("#")) # Output is "DoorDash"

# Case Conversion

# lower() method converts all characters in a string to lowercase.
# upper() method converts all characters in a string to uppercase.

text = "Hello world PYTHON"

text_lower = text.lower() # Converts all characters to lowercase
print(text_lower) # Output is "hello world python"

text_upper = text.upper() # Converts all characters to uppercase
print(text_upper) # Output is "HELLO WORLD PYTHON"

# Search

phone = "+5542991476949"
isPhoneBrazilian = phone.startswith("+55") # Checks if the string starts with "+55"

print(isPhoneBrazilian) # Output is True

email = "limarcingteam@gmail.com"

isEmailGmail = email.endswith("@gmail.com") # Checks if the string ends with "@gmail.com"

isEmailValid = "@" in email # Checks if "@" is present in the string

print(isEmailGmail) # Output is True

print(isEmailValid) # Output is True

# Example of find() method + slicing

phone2 = "48-654-16548"
phone3 = "+48-654-16548"

print(phone2.find("-"))  # Output is 2

fixed_phone = phone3[phone3.find("-") + 1:]

print(fixed_phone) # Output is "654-16548"

# Validation

country = "USA"

isCountryValid = country.isalpha() # Checks if all characters in the string are alphabetic

country2 = "USA1"

isCountryValid = country.isalpha() # Checks if all characters in the string are alphabetic

print(isCountryValid) # Output is True

print(country2.isalpha()) # Output is False

phone = "1234567890"

isPhoneNumeric = phone.isdigit() # Checks if all characters in the string are numeric

print(isPhoneNumeric) # Output is True
