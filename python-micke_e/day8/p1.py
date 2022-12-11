colnr = 0
rownr = 0
visiblecount = 0
cordsyst = []
visiblecords = []
edgegheight = 0
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    colnr = len(row)
    rownr += 1
    cordsyst.append(list(row))
visiblecount = 2*rownr + 2*(colnr-2)
for x in range (1, colnr-1):
    check = True 
    highest = 0
    for y in range(1, rownr-1):
        edgegheight = int(cordsyst[y-1][x])
        if edgegheight > highest:
            highest = edgegheight
        if ((check and int(cordsyst[y][x]) > edgegheight) and (int(cordsyst[y][x]) > highest)):
            if int(cordsyst[y][x]) > highest:
                highest = int(cordsyst[y][x])
            cords = [y,x]
            if not cords in visiblecords:
                visiblecords.append(cords)
for x in range (1, colnr-1):
    check = True 
    highest = 0
    for y in range(rownr-2,0,-1):
        edgegheight = int(cordsyst[y+1][x])
        if edgegheight > highest:
            highest = edgegheight
        if ((check and int(cordsyst[y][x]) > edgegheight) and (int(cordsyst[y][x]) > highest)):
            if int(cordsyst[y][x]) > highest:
                highest = int(cordsyst[y][x])
            cords = [y,x]
            if not cords in visiblecords:
                visiblecords.append(cords)
for y in range(1, rownr-1):
    check = True
    highest = 0 
    for x in range (1, colnr-1):
        edgegheight = int(cordsyst[y][x-1])
        if edgegheight > highest:
            highest = edgegheight
        if ((check and int(cordsyst[y][x]) > edgegheight) and (int(cordsyst[y][x]) > highest)):
            if int(cordsyst[y][x]) > highest:
                highest = int(cordsyst[y][x])
            cords = [y,x]
            if not cords in visiblecords:
                visiblecords.append(cords)
for y in range(1, rownr-1):
    check = True
    highest = 0 
    for x in range (colnr-2,0,-1):
        edgegheight = int(cordsyst[y][x+1])
        if edgegheight > highest:
            highest = edgegheight
        if ((check and int(cordsyst[y][x]) > edgegheight) and (int(cordsyst[y][x]) > highest)):
            if int(cordsyst[y][x]) > highest:
                highest = int(cordsyst[y][x])
            cords = [y,x]
            if not cords in visiblecords:
                visiblecords.append(cords)
print(len(visiblecords)+visiblecount)
