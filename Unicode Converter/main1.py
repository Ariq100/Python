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
Items = ""
HexNum = ""

for x in range(0, len(lines)):
    for item in lines[x]:   
        if (item != ' ' and item != '%'):
            Bytes = item.encode("UTF-32")
            HexNum = HexNum + str(Bytes)
        elif (item == ' '):
            Line = Line + " "
        elif (item == '%'):
            print(HexNum)
            # HexCode = int(HexNum)
            Line = Line + normalize(Hex)
            
        HexNum = ''
        
    lines[x] = Line
    Line = ""
    
WriteFile(filename, lines)