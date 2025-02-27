def Del(n, m):
    if n % m == 0:
        return True
    else:
        return False
    
def BList(start, finish):
    B_List = list()
    for b in range(start, finish + 1):
        B_List.append(b)
    return sorted(B_List)

    
def F(x):
    return Del(x, a) or (Del(x, 23) <= (not (x in BList(50, 70))))

for a in reversed(range(1, 1000)):
    if all(F(x) for x in range(1, 1000)):
        print(a)
        break