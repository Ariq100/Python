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
HexItems = ""

for x in range(0, len(lines)):
    for item in lines[x]:   
        if (item != ' '):
            HexItems = HexItems + "%" + str(ord(item))
        else:
            HexItems = HexItems + " "
            
    lines[x] = HexItems
    HexItems = ""
    
WriteFile(filename, lines)