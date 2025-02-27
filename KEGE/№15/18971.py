def F(x, y):
    return (y > 10) or (x * a > y + x)

for a in range(1, 1000):
    if all(F(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break