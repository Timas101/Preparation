s = open(r"C:\Users\timof\Documents\Preparation\Diferent\k7a-3\k7a-3.txt").readline()

s = s.replace('E', ' ').replace('B', ' ')
s = s.split()

print(max(len(x) for x in s))