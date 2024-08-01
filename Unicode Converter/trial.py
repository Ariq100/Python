import unicodedata

lines = ['%72%101%108%108%111 %87%111%114%108%100%33', '', '%79%110%103']

HexNum = ''
Line = ""

for x in range(0, len(lines)):
    for item in lines[x]:   
        if (item != ' ' and item != '%'):
            HexNum = HexNum + str(item)
        elif (item == ' '):
            Line = Line + " "
        elif (item == '%'):
            print(HexNum)
            # HexCode = int(HexNum)
            Line = Line + unicodedata.normalize('NFD', HexNum)
            
        HexNum = ''
        
    lines[x] = Line
    Line = ""

print(lines)