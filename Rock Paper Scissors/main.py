import random 

def choices():
    ComputerChoices = ["Rock", "Paper", "Scissors"]
    ComputerChose = random.choice(ComputerChoices)
    
    UserChose = input("Enter your choice (Rock, Paper, Scissor) : ")
    inputs = {"Player" : UserChose, "Computer" : ComputerChose}
    
    return inputs
    
def WinOrLose(PlayerInput, ComputerInput):
    print(f"You Chose {PlayerInput}, and the Computer Chose {ComputerInput}")
    
    if (PlayerInput == ComputerInput):
        return "Its a tie"
    elif (PlayerInput == "Rock"):
        if (ComputerInput == "Paper"):
            return "You lost!!"
        elif (ComputerInput == "Scissor"):
            return "You Won!!"
    elif (PlayerInput == "Scissor"):
        if (ComputerInput == "Paper"):
            return "You Won!!"
        elif(ComputerInput == "Rock"):
            return "You lost!!"
    elif (PlayerInput == "Paper"):
        if(ComputerInput == "Scissor"):
            return "You Lost!!"
        elif (ComputerInput == "Rock"):
            return "You Won!!"
        
        
        
    # elif (PlayerInput == "Rock" and ComputerInput == "Scissor"):
    #     return "You Won!!"
    # elif (PlayerInput == "Scissor" and ComputerInput == "Scissor"):
    
choices = choices()

result = WinOrLose(choices["Player"], choices["Computer"])

print(result)