time = 0
regx = 1
currsum = 0
signsum = 0
checkpoint = 20
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row == "noop":
        time += 1
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
    else:
        time += 1
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
        time += 1 
        if time == checkpoint:
            currsum = checkpoint*regx
            signsum += currsum
            checkpoint += 40
        regx+=int(row.split(' ')[1]) 
print(signsum)
