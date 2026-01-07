# break - you can use that to break the execution of the loop

for i in (1,2,3):
    print("pinrto")
    break

# continue - you can use that to skip one iteration of the loop,
# without stoping the rest of the loop itself

names = ["dante", "jair", "pedro", "", "fernando"]

for name in names:
    if (bool(name) == False):
        continue # this will skip the "" value
    print(name)

# pass is a placeholder to help you build your logic, the final solution shouldn't have one

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekends = ["Sunday", "Saturday"]

for day in days:
    if day in weekends:
        continue
    print(f"workday: {day}")

# Example o break use

emails = [
    "data@gmail.com",
    "baraa@outlook.com",
    "DROP TABLE USERS;",
    "maria@gmail.com"
]

for email in emails:
    if ";" in email:
        print("SQL INJECTION DETECTED")
        break
    print(f"Processing email: {email}")
