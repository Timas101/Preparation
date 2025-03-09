def Check(num, count):
    if count > 3 and num >= 51:
        return count == 3
    if count % 2 == 0:
        return Check(num + 1, count + 1) or Check(num + 4, count + 1) or Check(num * 2, count + 1)
    else:
        return Check(num + 1, count + 1) and Check(num + 4, count + 1) and Check(num * 2, count + 1)
    


for num in range(1, 51):
    if Check(num, 1):
        print(num)
