# Keep only students with names starting with "M"

students = [
    ["Maria", 85],
    ["Kumar", 90],
    ["Max", 60]
]

names_with_M = lambda row: row[0].startswith("M")

filtered_students = list(filter(names_with_M, students))

print(filtered_students)
