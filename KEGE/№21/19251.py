def Check(num, count):
    if count > 5 or num >= 132:
        return count == 3 or count == 5
    if count % 2 == 0:
        return Check(num + 3, count + 1) or Check(num + 6, count + 1) or Check(num * 3, count + 1)
    else:
        return Check(num + 3, count + 1) and Check(num + 6, count + 1) and Check(num * 3, count + 1)

for num in range(1, 132):
    if Check(num, 1):
        print(num)