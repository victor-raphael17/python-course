# Lambda function

def plus15(x):
    return x + 15

plus10 = lambda x: x + 10

print(plus10(5))  # Output: 15

print(plus15(5))  # Output: 20

# A lambda can contain any expression, including conditional expressions

# check if length is greater than 1

check = lambda character: len(character) == 1

print(check("a"))  # Output: True

# Map with lambda

prices = ["$10.00", "$20.00", "$30.00", "$40.00", "$50.00"]

prices_to_float = lambda p: float(p.replace("$", ""))

float_prices = list(map(prices_to_float, prices))

print(float_prices, type(float_prices))

# Filter with lambda, task: remove any values below 100

values = [50, 75, 100, 125, 150, 175, 200]

above_99 = lambda p: p > 99

filtered_values = list(filter(above_99, values))

print(filtered_values, type(filtered_values))

# Task: keep just the students with grades above 70

students = [
    ["Alice", 25],
    ["Bob", 65],
    ["Charlie", 95]
]

clear_grade = lambda row: row[1] > 70

filtered_students = list(filter(clear_grade, students))

#if students[0][1] < 70:
#    students.pop(0)

print(filtered_students)
