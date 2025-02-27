mass = [int(i[:-1]) for i in list(open('17_19749.txt'))]
maxnumost = max(mass) % 7
minnumost = min(mass) % 3
maxsum = 0
count = 0
right = True
for i in range(0, len(mass) - 3):
    nums = [mass[i], mass[i+1], mass[i+2]]
    count_ost_tr = 0
    count_ost_sev = 0

    for x in nums:
        if x % 3 == minnumost:
            count_ost_tr += 1
        if x % 7 == maxnumost:
            count_ost_sev +=1
        if count_ost_tr > 1:
            right = False
            
    
    if count_ost_sev < 2:
        right = False
    
    if right:
        count += 1
        maxsum = max(maxsum, sum(nums))

print(count, maxsum)
print('Goyda')