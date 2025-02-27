def F(x, y):
    return ((x >= 27) or ((2 * x) < (3 * y)) or (((x + 2) * (y - 3)) < a))

for a in range(0, 1000):
    if all(F(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break