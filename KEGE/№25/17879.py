from math import sqrt

def MFound(num):
    delitel = list()
    for delit in range(2, int(sqrt(num))):
        if num % delit == 0:
            delitel.append(delit)
            delitel.append(num // delit)
    if delitel:
        del_max = max(delitel)
        del_min = min(delitel)
        m = del_max + del_min
        return m
    else:
        return 0


count = 0
for num  in range(800000, 801000):
    if MFound(num) % 10 == 4:
        print(num, MFound(num))
        count += 1
    if count >= 5:
        break
