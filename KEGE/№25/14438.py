from fnmatch import*

for x in range(0, 10**12, 86513):
    sqr = float(sum(map(int, str(x))) ** 0,5)
    if sqr ** 2 == sum(map(int, str(x))) and fnmatch(str(x), '17*46??8'):
        print(x, x // 86513)