x = input("Enter a drink = ")

def get_drink_by_profession(x):
    if x == "jabroni":
        print("Patron Tequila")
    elif x == "school counselor":
        print("Anything with Alchohol")
    elif x == "Programmer":
        print("Hipster Craft Beer")
    elif x == "Bike Gang Member":
        print("Moonshine")
    elif x == "Politician":
        print("YOur tax dollars")
    elif x == "Rapper":
        print("Cristal")
    elif x == "anything else":
        print("Beer")
    else:
        print("There was a problem retriving the data")

print(get_drink_by_profession(x))

