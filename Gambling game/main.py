import random

def ConvertMoney():
    money = int(input("Enter the amount of dollars you would like to deposit: $"))
    
    points = round(money * 3)
    
    return points

# def PointsCount():
#     Points = ConvertMoney()

def CashOut(points):
    money = points / 3
    
    return money

def Game():
    items = ["Apple", "Banana", "GrapeFruit"]
    count = 0
    DisplayItems= []
    print(items)
    
    UserChoice = input("Enter your Lucky item: ")
    
    for x in range(3):
        DisplayItems.append(random.choice(items))
    
    print (f"Display: {DisplayItems}")
    
    for x in range(3):
        if (DisplayItems[x] == UserChoice):
            count = count + 1
            
    if (count == 3):
        return True
    else:
        return False
    
def WinOrLose(points):
    result = Game()
    
    if(result == True):
        points = points + 2
        print(f"You won!!! +2 points\nYour current points are {points}")
    else:
        points = points - 2
        print(f"You lost!!! -2 points\nYour current points are {points}")
        
    return points


points = ConvertMoney()

while(points != 0):
    print(f"1.Add Money\n2.Play Game\n3.Cashout\n4.Exit\n\n                      Points: {points}")
    choice = int(input("Enter your choice: "))
    
    if (choice == 1):
        points = points + ConvertMoney()
    elif (choice == 2):
        points = WinOrLose(points)
    elif (choice == 3):
        money = CashOut(points)
        break         
    elif (choice == 4):
        print("Thank you for playing!")
        break


print(f"&{money} Withdrawn")