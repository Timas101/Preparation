base_array = [int(x[:-2]) for x in open(r"C:\Users\timof\Documents\Preparation\KEGE\№17\12926\17_12926.txt"]

max_two_len_num = 0
for element in base_array:
    if len(str(abs(element))) == 2:
        max_two_len_num = max(max_two_len_num, element)

max_sum_four = 0
for i in range(len(base_array) - 4):
    sum_array = base_array[i:i + 4]
    same_end_check = True
    end_int = sum_array[0] % 10
    for element in sum_array:
        if end_int != element % 10:
            same_end_check = False
    if same_end_check == True:
        max_sum_four = max(sum(sum_array), max_sum_four)

count_five = 0
sum_five_array = []
for i in range(len(base_array) - 5):
    check_array = base_array[i:i + 5]
    count_min_A = 0
    for element in check_array:
        if element < max_sum_four:
            count_min_A += 1
    if sum(check_array) % max_two_len_num == 0 and count_min_A == 1:
        sum_five_array.append(sum(check_array))
        count_five += 1
print(count_five, min(sum_five_array))


        


