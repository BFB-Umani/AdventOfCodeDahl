temp = 0
length = 0 
left = ""
right = ""
strx = ""
def removeDupWithoutOrder(str):
    return "".join(set(str))
file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        length = int(len(row)/2)
        left = row[:length]
        #print(left)
        right = row[length:]
        for letter in left:
            if letter in right:
                strx+=letter
        strx = removeDupWithoutOrder(strx)
        for a in strx:
            if a.isupper():
                temp += ord(a)-38
            else:
                temp += ord(a)-96
        strx = ""
print(temp)
        