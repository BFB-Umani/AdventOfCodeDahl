moves = {"U": 1, "D": -1, "R": 1, "L": -1}
knots = {i: [(0, 0)] for i in range(10)}
def getdist(point1x, point1y, point2x, point2y):
    dist = abs(point1x - point2x) + abs(point1y - point2y)
    if point1x == point2x and dist >= 2:
        return (point2x, point1y - 1 if point1y > point2y else point1y + 1)
    if point1y == point2y and dist >= 2:
        return (point1x - 1 if point1x > point2x else point1x + 1, point2y)
    if dist > 2:
        if point1x > point2x:
            return (point2x + 1, point2y + 1 if point1y > point2y else point2y - 1)
        if point1x < point2x:
            return (point2x - 1, point2y + 1 if point1y > point2y else point2y - 1)
    return (point2x, point2y)

file = open("input.txt", "r")
for row in  file:
    row = row.strip()
    if row != "":
        d, n = row.split()[0], int(row.split()[1])
        for i in range(n):
            hx, hy = knots[0][-1]
            hx += moves[d] if d in ["R", "L"] else 0
            hy += moves[d] if d in ["U", "D"] else 0
            knots[0].append((hx, hy))
            for k in range(1, 10):
                tx, ty = getdist(*knots[k-1][-1], *knots[k][-1])
                knots[k].append((tx, ty))

print(len(set(knots[9])))
