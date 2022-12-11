time = 0
time2 = -1
regx = 1
currsum = 0
signsum = 0
checkpoint = 40
textrow = ""
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row == "noop":
        time += 1
        time2 += 1
        if time2 == regx or time2 == regx -1 or time2 == regx+1:
            textrow += "#"
        else:
            textrow += " "
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
            time2 = -1
            print(textrow)
            textrow = ""
    else:
        time += 1
        time2 += 1
        if time2 == regx or time2 == regx -1 or time2 == regx+1:
            textrow += "#"
        else:
            textrow += " "
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
            time2 = -1
            print(textrow)
            textrow = ""    
        time += 1 
        time2 += 1
        if time2 == regx or time2 == regx -1 or time2 == regx+1:
            textrow += "#"
        else:
            textrow += " "
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
            time2 = -1
            print(textrow)
            textrow = "" 
        regx+=int(row.split(' ')[1])  
