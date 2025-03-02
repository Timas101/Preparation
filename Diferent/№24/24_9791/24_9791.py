s = open(r"C:\Users\timof\Documents\Preparation\Diferent\№24\24_9791\24_9791.txt").readline()
alp = 'GHIJKLMNOPQRSTUVWXYZ'
for st in alp:
    s = s.replace(st, ' ')

s = s.split()
print(max(len(x) for x in s))