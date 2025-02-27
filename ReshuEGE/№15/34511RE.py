def F(x):
    return (x & 25 != 0) <= ((x & 19 == 0) <=  (x & a != 0))

for a in range(1, 1000):
    if all(F(x) for x in range(1, 1000)):
        print(a)
        break