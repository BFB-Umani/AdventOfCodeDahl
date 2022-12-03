tot = 0
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        row = row.split(' ')
        opp = row[0]
        you = row[1]
        if opp == "A" and you =="X":
            tot += 4
        if opp == "A" and you =="Y":
            tot += 8
        if opp == "A" and you =="Z":
            tot += 3
        if opp == "B" and you =="X":
            tot += 1
        if opp == "B" and you =="Y":
            tot += 5
        if opp == "B" and you =="Z":
            tot += 9
        if opp == "C" and you =="X":
            tot += 7
        if opp == "C" and you =="Y":
            tot += 2
        if opp == "C" and you =="Z":
            tot += 6
print(tot)

