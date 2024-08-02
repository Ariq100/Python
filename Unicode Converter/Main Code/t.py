def ReadFile(filename):   
    file = open(filename, "r")

    lines = file.readlines()
    lines = [lines.rstrip() for lines in lines]

    file.close()
    
    return lines
    
def WriteFile(filename, lines):
    filename1 = ""
    
    for i in filename:
        if (i == "."):
            filename1 = filename1 + "inhex" + i
        else:
            filename1 = filename1 + i
            
    file = open(filename1, "w")
    
    for item in lines:
        item = item + "\n"
        file.write(item)
        
    file.close()
   
filename = str(input("Enter the name of the file: "))

lines = ReadFile(filename)

for x in range(0, len(lines)):
    value1 = lines[x]
    
    value2 = value1.decode("UTF-32")
    
    lines[x] = value2

WriteFile(filename, lines)

# value = "Hello World!"

# value2 = str(value.encode("UTF-32"))

# value3 = bytes(value2, 'utf-32')

# value4 = value3.decode("UTF-32")

# print(value4)

# str="Hello! Welcome to Tutorialspoint."
# str_encoded= str.encode('utf_16','strict')
# print("The encoded string is: ", str_encoded)
# str_decoded=str_encoded.decode('utf_16', 'strict')
# print("The decoded string is: ", str_decoded)



# filename = str(input("Enter the name of the file: "))

# lines = ReadFile(filename)
# HexItems = ""

# for x in range(0, len(lines)):
#     for item in lines[x]:   ``
#         if (item != ' '):
#             HexItems = HexItems + "%" + str(ord(item))
#         else:
#             HexItems = HexItems + " "
            
#     lines[x] = HexItems
#     HexItems = ""
    
# WriteFile(filename, lines)