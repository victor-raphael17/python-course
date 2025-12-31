email = "blablabla@gmail.com"

password = "asdfghjk "

password_is_valid = False

password = password.strip()

if not bool(password):
    print("Password must be filled")

elif (len(password) < 8):
    print("Password must be at least 8 characters long")

elif not any(character.isupper() for character in password):
    print("At least one character must be upper case")

elif not any(character.islower() for character in password):
    print("At least one character must be lower case")    

elif (password == email):
    print("The password must be different from the email")

elif password.count(" "):
    print("The password must not have blank spaces")

elif not (password[0].isalnum() and password[-1].isalnum()):
    print("The password must start or end with an alphanumerical digit")

else:
    password_is_valid = True
    print("Your password is valid")
