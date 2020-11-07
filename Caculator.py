# Name : Ariq 
# Project : Caculator

# storing all the possible user inputs
add = ['add', 'addition', '+']
subtract = ['subtract', 'subtraction', '-']
multiply = ['mutiplication', 'multiply', '*']
divide = ['divide', 'divition', '/']
abc = ['yes', 'sure', 'yup', 'yeah', 'y']

# Instrutions:
print(f"Instructions:\n1) Input the first value.\n2) Input the second value.\n3) Input the operator.\n\nThe operators are:")

for x in add:
     print(x, end='  ')
print(' ')

for y in subtract:
     print(y, end='  ')
print(' ')
     
for t in multiply:  
     print(t, end='  ')
print(' ')
     
for u in divide:
     print(u, end='  ')
print(' ')     

# Function for user inputs
def value_input():
    input_1 = float(input("\nEnter the first value = "))
    input_2 = float(input("Enter the second value = "))
    input_operation = input("Enter the operator = ")
    operation(input_1, input_2, input_operation)


# Function for operation and contineur
def operation(input_1, input_2, input_operation):
    if input_operation.lower() in add :
        print(f"\nThe addition of {input_1} and {input_2} is " + str(input_1 + input_2))
    elif input_operation.lower() in subtract :
        print(f"\nThe subtraction of {input_1} and {input_2} is " + str(input_1 - input_2))
    elif input_operation.lower() in multiply :
        print(f"\nThe multiplication of {input_1} and {input_2} is " + str(input_1 * input_2))
    elif input_operation.lower() in divide :
        print(f"\nThe divition of {input_1} and {input_2} is " + str(input_1 / input_2))
    else:
        print("Wrong operation input!!")
    
    continuer = input("\nDo you want to continue?? = ")
    if continuer.lower() in abc:
        value_input()
    else:
        exit()
    
        
# Pogram initiater
value_input()
