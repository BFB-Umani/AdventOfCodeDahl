stackholder = [[],[],[],[],[],[],[],[],[]]
order = [1, 5, 9, 13, 17, 21, 25, 29, 33]
stop = 0
answer = ""
file = open("input.txt", "r")
for i, row in  enumerate(file):
    row = row.rstrip()
    if row != "":
        if row[1] == "1":
            row = row.strip()
            rows = int(row[-1])
            stop = i
file.seek(0)
for i, row in  enumerate(file):
    if i == stop:
        break
    row = row.rstrip()
    for ix, item in enumerate(order):
        if item <= len(row):
            if row[item] != " ":
                stackholder[ix].insert(0,row[item])
file.seek(0)
for i, row in  enumerate(file):
    row = row.rstrip()
    if i > stop + 1:
        command = row.split(' ')
        for run in range(0,int(command[1])):
            a = stackholder[int(command[3])-1].pop(-1)
            stackholder[int(command[5])-1].append(a)
for row in stackholder:
    answer += row[-1]
print(answer)



    
            