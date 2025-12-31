# Check wheter any filename appears more than once in a list
# Print "Duplicate found" if a duplicate exists, otherwise print "All files are unique"

files = [
    ' report.csv',
    ' data.xls',
    ' summary.docx',
    ' report.csv ',
    ' data.csv '
]

for i in range(0, len(files)):
    files[i] = files[i].strip()

if len(files) != len(set(files)):
    print("Duplicated found")
else:
    print("All files are unique")
