person = ["Maria", 29, "Data Engineer", "Spain"]
#name = [person[0]]
#age = [person[1]]
#profession = [person[2]]
#country = [person[3]]

# without unpacking, indexes makes code long and hard to extend

name, age, profession, country = person
# with unpacking, code is cleaner and easier to extend

print(name)
print(age)
print(profession)
print(country)

# You have to unpack all the values, otherwise you'll get an error

# You can use asterisk to unpack remaining values into a list

name, *details, country = person

print(name)
print(details)
print(country)

name, *details = person

print(name)
print(details)

*details, country = person

print(details)
print(country)

# Only one asterisk is allowed per unpacking operation

# Number of variables must match number of values unless using asterisk

# You can unpack any iterable, not just lists, e.g., tuples, strings

letters = "ABC"

a, b, c = letters

print(a, b, c)

person = ["Maria", 29, "Data Engineer", "Spain"]

name, _, role, _ = person

name, *_, country = person

print(name, country)
