monkeysitems = {}
operations = {}
tests = {}
monkey = 0
trues = {}
falses = {}
inspected = {}
div = 1
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        if row.startswith("Monkey"):
            monkey = row.split(' ')[1]
            monkey = monkey[:-1]
        elif row.startswith("Starting"):
            items = row.split(':')[1]
            items = items.split(',')
            for ix, item in enumerate(items):
                items[ix] = int(item.strip())
            monkeysitems[monkey] = items
        elif row.startswith("Operation"):
            operation = row.split(':')[1]
            operation = operation[11:].split(' ')
            operations[monkey] = operation 
        elif row.startswith("Test"):
            test = int(row.split('by')[1].strip())
            tests[monkey]=test
            div = div * int(test)
        elif row.startswith("If true"):
            throw = int(row.split('monkey')[1].strip())
            trues[monkey] = throw 
        elif row.startswith("If false"):
            throwf = int(row.split('monkey')[1].strip())
            falses[monkey] = throwf
for testcount in range(0,10000):
    for key in monkeysitems:
        for item in monkeysitems[key]:
            if not key in inspected:
                inspected[key] = 1
            else:
                inspected[key] += 1
            if operations[key][0] == "*":
                if operations[key][1] == "old":
                    lvl = item * item
                else:
                    lvl = int(operations[key][1])*int(item)
            else:
                if operations[key][1] == "old":
                    lvl = item + item
                else:
                    lvl = int(operations[key][1])+int(item)
            lvl = lvl % div
            test = lvl % tests[key] == 0
            if test:
                add = monkeysitems[str(trues[key])]
                add.append(lvl)
                monkeysitems[str(trues[key])] = add
            else:
                add = monkeysitems[str(falses[key])]
                add.append(lvl)
                monkeysitems[str(falses[key])] = add
        monkeysitems[key] = []
max1=0
max2=0
for nr in inspected.values():
    if nr > max1:
        max2 = max1
        max1 = nr
    elif nr > max2:
        max2 = nr
        
print(int(max1)*int(max2))
