# While Loops

# while loop to print 1 to 3

i = 1

while i < 4:
    print(i)
    i += 1

# While loop to count 1 to 5

counter = 1

while counter <= 5:
    print("Counter is at:", counter)
    counter += 1

# White a program that keeps asking "Do you agree?" until the user types "yes"

answer = ""

while answer.lower() != "yes":
    answer = input("Do you agree? (yes/no)\n")

# While true

# Build a infinite money generator

money = 0

while True:
    print("Generating money... 💰")
    
    money += 10
    
    print(f"You have ${money}")
    
    isEnoughMoney = input("Do you want to stop? (yes/no)\n")
    
    if isEnoughMoney.lower() == "yes":
        break

# Write a program that keeps asking "Do you agree?" until the user types "yes"
# Max of 3 attempts
# Yes within three attempts -> print "Thank you for agreeing!"
# No within three attempts -> print "You have exhausted your attempts."
# If you know how many times to loop, use a for loop mainly
# or a normal while loop, not a while true loop

for i in range(3):
    answer = input("Do you agree? (yes or no)\n").lower()
    
    if answer == "yes":
        print("Very good")
        break

    if i == 2:
        print("You exceeded your attempts")
