#Queue
# Do it with Classes and Functions 

class Queue:
    def init(self):
        self.OutQueue = []
        self.InQueue = []
    
    def Push(self, Item,InQueue):
        self.InQueue.append(item)
        
    def LengthOfQueue(self, Queue):
        return len(self.Queue)

    def Pop(self, InQueue, OutQueue):
        self.length = len(self.InQueue)
        
        if (LengthOfQueue(self.OutQueue) <= 0):
            return OutQueue.pop()
        else:
            for i in range(0, length):
                self.OutQueue.append(self.InQueue[length - i - 1])
            self.OutQueue.pop()

def Menu():
    print(f"1. Add to Queue \n 2. Pop from Queue \n 3. Display Queue \n 4. Exit")
    UserInput = int(input("Enter your choice: "))
    
    return UserInput

def UserChose(UserInput):
    if (UserInput == 1):
        Item = str(input("Enter Something: "))
        User1.Push(Item, InQueue)
    elif (UserInput == 2):
        User1.Pop(User1.InQueue, User1.OutQueue)
    # elif (UserInput == 3):
    #     for i in range(0, LengthOfQueue())
        

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