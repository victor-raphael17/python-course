# Match - Case

country = "USA"

match country:
    case "USA" | "United States":
        print("US")
    case "France":
        print("France")
    case "India":
        print("India")
    case _:
        print("Invalid input")
