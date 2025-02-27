def dev(num):
    DelitList = set()
    for delit in range(2,  int(num ** 0.5) + 1):
        if num % delit == 0:
            DelitList |= {delit, num // delit}
    return sum(DelitList) // (len(DelitList) or 1)

for num in range(700000 - 1, 600000, -1):
    m = dev(num)
    if  m % 1000 == 313:
        print(num, m)