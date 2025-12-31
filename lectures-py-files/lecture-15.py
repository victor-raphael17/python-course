# IF, Else and Elif Statements in Python

# if

score = 95

if score >= 90:
    print("You got an A!")

# if-else

if score >= 90:
    print("You got an A!")
else:
    print("You did not get an A.")

# if-elif-else

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else:
    print("You need to improve your score.")

# Nested if

if score >= 90:
    if score >= 95:
        print("You got an A+!")
    else:
        print("You got an A.")
else:
    print("You did not get an A.")

# Logical operators with if

attendance = 85

if score >= 90 and attendance >= 80:
    print("You qualify for the honor roll!")
else:
    print("You do not qualify for the honor roll.")
