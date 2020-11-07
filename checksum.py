# Asking the user to input a number for the checksum
x = int(input("Enter a number = "))
# Storing the things that I will need often
y = 256

# using a loop for this seems very efficient for me
if x > y :
    # Used another variable to store step 2 and 3.
    a = int(x / y)
    z = a * y
    # I tried to make it as small as possible.
    print(f"The check sum of {x} is "+ str(x - z))
else:
    print(f"The check sum of x is {x} as it is inside the range of 0 to 256")
    

 
     