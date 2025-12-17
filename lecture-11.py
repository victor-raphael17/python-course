# Flow control

# bool() function is used to check the truthiness of a value

x = True

print(bool(x))  # True

x = False

print(bool(x))  # False

x = None

print(bool(x))  # False

x = 123

print(bool(x))  # True

x = 0

print(bool(x))  # False

x = -1

print(bool(x))  # True

x = "pato"

print(bool(x))  # True

x = ""

print(bool(x))  # False

# any() function returns True if any element of the iterable is true

email = ""

cellphone = "d"

social_media = ""

x = any([email, cellphone, social_media])

print(x)  # True, if cellphone was empty, would be False

# all() function returns True if all elements of the iterable are true

email = "a"

cellphone = "d"

social_media = ""

x = all([email, cellphone, social_media])

print(x)  # False, because social_media is empty
