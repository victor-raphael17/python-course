# for-else will be used only when you have used "break" in your loop, the else section will only
# be executed if the loop finished succesfully

# check for even number example

items = [1, 3, 5, 7, 4]

for num in items:
    if num % 2 == 0:
        print(f"Even number found, {num}") 
        break
else:
    print("All numbers are odd")

# check if file ends with .csv

files = ["data.csv", "report.csv", "pulga.csv"]

for file in files:
    if not file.endswith(".csv"):
        continue
    print(f"Processing {file}")
