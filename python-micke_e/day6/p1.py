highest = 0 
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
for temp in range(0, len(row)+1):    
    window = row[temp:temp+4]
    window = list(dict.fromkeys(window))
    if len(window) == 4:
        print(temp+4)
        exit()
