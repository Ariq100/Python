#Queue
# Logic error for the Queue

class Queue:
    def __init__(self):
        self.__OutQueue = []
        self.__InQueue = []
    
    def Push(self, Item):
        self.__InQueue.append(Item)

    def Pop(self):
        if (len(self.__OutQueue) > 0):
            return self.__OutQueue.pop()
        else:
            length = len(self.__InQueue)
            for i in range(1, length):
                self.__OutQueue.append(self.__InQueue[length - i])
            self.__InQueue = []
            return self.__OutQueue.pop()

def Menu():
    print(f"1. Add to Queue \n 2. Pop from Queue \n 3. Display Queue \n 4. Exit")
    UserInput = int(input("Enter your choice: "))
    
    return UserInput

def UserChose(UserInput):
    if (UserInput == 1):
        Item = str(input("Enter Something: "))
        User1.Push(Item)
    elif (UserInput == 2):
        print(User1.Pop())

User1 = Queue()

UserInput = Menu()

while (UserInput != 4):
    UserChose(UserInput)
    UserInput = Menu()








# for x in range(0, i):
#     UserInput = str(input("Enter: "))
    
#     lineIn.append(UserInput)


# length = len(lineIn)

# for i in range(0, length):
#     lineOut.append(lineIn[length - i - 1])

# for i in range(0, len(lineOut)):
#     print(lineOut.pop())