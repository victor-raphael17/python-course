email = "email@example.com"

email = email.strip()

is_email_valid = False

if (not bool(email)):
    print("string is empty")

elif (not "@" in email) or (not "." in email):
    print("string must contain @ and .")

elif (email.count("@") > 1):
    print("string must contain only one @")

elif (not email.endswith((".com", ".org", ".net"))):
    print("email doesn't ends with .com, .org or .net")

elif (len(email) >= 254):
    print("email is too long")

# The isalnum() method in Python is a built-in string method used to check if all characters
# in a string are alphanumeric. Alphanumeric characters include letters (a-z, A-Z) and numbers (0-9)

elif (not email[0].isalnum()):
    print("special characters are not allowed")

else:
    is_email_valid = True
    print("email is valid")
