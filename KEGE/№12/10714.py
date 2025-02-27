max_len = 0
for n in range(3, 1000):
    string = '1' + n * '2'
    while '12' in string or '322' in string or '222' in string:
        if '12' in string:
            string = string.replace('12', '2', 1)
        if '322' in string:
            string = string.replace('322', '21', 1)
        if '222' in string:
            string = string.replace('222', '3', 1)
    max_len = max(len(string), max_len)

print(max_len)