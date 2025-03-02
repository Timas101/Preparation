def DelFount(num):
    aray_delit = []
    for delitel in range(2, int(num**0.5)+1):
        if num % delitel == 0:
            aray_delit.append(delitel)
            aray_delit.append(num//delitel)
    return aray_delit
            

count = 0
for num in range(500000, 10**10):
    aray_delitel = DelFount(num)
    for delitel in aray_delitel:
        if delitel % 10 == 3 and delitel != num and delitel != 3:
            count += 1
            print(num, delitel)
            break
        if count == 5:
            break
    if count == 5:
        break
