# Check wheter any filename appears more than once in a list
# Print "Duplicate found: {repeated file}" if a duplicate exists and remove it from the list,
# otherwise print "All files are unique"

files = [
    'data.xls',
    'report.csv',
    'summary.docx',
    'report.csv',
    'data.csv'
]

print(f"Initial state\n\n{files}")

#files = [file.strip() for file in files]

#for i in range(0, len(files)):
#    files[i] = files[i].strip()

aux = 1
counter = 0

for i in range(0, len(files)):

    for i2 in range(aux, len(files)):

        if (files[i] == files[i2]):
            print(f"Duplicate found: {files[i]}")
            files[i] = ""
            counter += 1
            break

    aux += 1

if counter < 1:
    print("All files are unique")
    
files_aux = []

for file in files:
    if file:
        files_aux.append(file)

files = files_aux

print(f"Final state\n\n{files}")
