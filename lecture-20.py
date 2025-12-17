# Nested loop

for x in range(1, 4):
    for y in range(1, 4):
        print(x, y)

# Nested loops can be used in data combinations

colors = ["red", "green", "blue"]

pixels = ["1", "2", "3"]

for color in colors:
    for pixel in pixels:
        print(color, pixel)

# Nested loops can also be used in hierarchy, like in dates and tables

years = [2025, 2026, 2027]

months = ["january", "february", "march", "april", "may"]

days = range(1, 31)

for y in years:
    for m in months:
        for d in days:
            print(f"report-{d}-{m}-{y}")
