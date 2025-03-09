def Check(num, count):
    if count > 4 or num >= 51:
        return count == 4
    if count % 2 != 0:
        return Check(num + 1, count + 1) or Check(num + 4, count + 1) or Check(num * 2, count + 1)
    else:
        return Check(num + 1, count + 1) and Check(num + 4, count + 1) and Check(num * 2, count + 1)
    

for s in range(1, 51):
    if Check(s, 1):
        print(s)
