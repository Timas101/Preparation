def F(x):
    return (x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0))

for a in reversed(range(50, 121)):
    if all(F(x) for x in range(0, 1000)):
        print(a)
        break