temp = 0
strx = ""
strings = ""
listan = []
def removeDupWithoutOrder(str):
    return "".join(set(str))
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    listan.append(row)
for nr in range (0,len(listan),3):
    for letter in removeDupWithoutOrder(listan[nr]):
        if letter in removeDupWithoutOrder(listan[nr+1]):
            strings += letter
        if letter in removeDupWithoutOrder(listan[nr+2]):
            strings += letter
    my_dict = {i:strings.count(i) for i in strings}
    for key, value in my_dict.items():
        if value == 2:
            if key.isupper():
                temp += ord(key)-38
            else:
                temp += ord(key)-96
        strx = ""
    strings = ""
print(temp)

