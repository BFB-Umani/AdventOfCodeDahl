
highest = 0
highest2 = 0
highest3 = 0 
temp = 0 
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        row = int(row)
        temp += row
    else:
        #print(temp)
        if temp >= highest:
            highest3 = highest2
            highest2 = highest
            highest = temp
        elif temp >= highest2:
             highest3 = highest2
             highest2 = temp
        elif temp >= highest3:
             highest3 = temp
        temp = 0
print(highest+highest2+highest3)