colnr = 0
rownr = 0
visiblecount = 0
cordsyst = []
max = 0
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    colnr = len(row)
    rownr += 1
    cordsyst.append(list(row))
visiblecount = 2*rownr + 2*(colnr-2)
for ixrow, row in enumerate(cordsyst):
    for ixentry, entry in enumerate(row):
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        full = False
        for test in range(ixrow-1, -1, -1):
            if int(entry) > int(cordsyst[test][ixentry]) and not full:
                temp1 += 1
            else:
                temp1 += 1
                break
        for test in range(ixrow + 1, rownr):
            if int(entry) > int(cordsyst[test][ixentry]) and not full:
                temp2 += 1
            else:
                temp2 += 1
                break
        for test in range(ixentry-1, -1, -1):
            if int(entry) > int(cordsyst[ixrow][test]) and not full:
                temp3 += 1
            else:
                temp3 += 1
                break
        for test in range(ixentry + 1, rownr):
            if int(entry) > int(cordsyst[ixrow][test]) and not full:
                temp4 += 1
            else:
                temp4 += 1
                break
        if temp1*temp2*temp3*temp4 > max:
            max = temp1*temp2*temp3*temp4
print(max)