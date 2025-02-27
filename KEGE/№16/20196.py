from sys import setrecursionlimit

setrecursionlimit(1000000000)

def F(n):
    if n < 110:
        return n
    if n >= 110:
        return n + (F(n-1))
    
print(F(2025) - F(2021))
