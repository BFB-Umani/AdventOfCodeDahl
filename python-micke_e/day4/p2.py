highest = 0
temp = 0 
list1 = []
list2 = []
templeft = []
tempright = [] 
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        row = row.split(',')
        templeft = row[0].split('-')
        tempright = row[1].split('-')
        for left in range (int(templeft[0]), int(templeft[1])+1):
            list1.append(left)
        for right in range (int(tempright[0]), int(tempright[1])+1):
            list2.append(right)
        for item in list1:
            if item in list2:
                temp += 1
                break
        list1 = []
        list2 = []
        templeft = []
        tempright = []
print(temp)

