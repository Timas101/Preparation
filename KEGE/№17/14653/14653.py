massive = [int(x[:-1]) for x in open(r"C:\Users\timof\Documents\Preparation\KEGE\№17\14653\14653.txt").readlines()]

del_17_list = []
for element in massive:
    if element % 17 == 0 and element > 0:
        del_17_list.append(element)
del_17_list.sort()
summ_min_elements = del_17_list[0] + del_17_list[1]

max_end_69_sqr = -10 ** 40
for element in massive:
    if element % 100 == 69:
        max_end_69_sqr = max(max_end_69_sqr, element)
max_end_69_sqr = max_end_69_sqr ** 2

result_list = []
for i in range(len(massive) - 3):
    count_three_len = 0
    count_del_18 = 0
    pr_elment = 1
    for element in massive[i:i + 4]:
        pr_elment *= element
        if 100 <= abs(element) <= 999:
            count_three_len += 1
        if element % 18 == 0:
            count_del_18 += 1
    if count_three_len == 2 and count_del_18 == 1 and sum(massive[i:i + 4]) % summ_min_elements == 0 and pr_elment <= max_end_69_sqr:
        result_list.append(sum(massive[i:i + 4]) ** 2)

print(len(result_list), sum(result_list))
