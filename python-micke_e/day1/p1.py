highest = 0
temp = 0 
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        row = int(row)
        temp += row
    else:
        if temp >= highest:
            highest = temp
        temp = 0
print(highest)