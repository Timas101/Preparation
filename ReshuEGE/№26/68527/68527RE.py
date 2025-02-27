f = open('1_26.txt')
n = int(f.readline())

a = []

for i in range(n):
    x = int(f.readline())
    a.append(x)

a.sort(reverse=True)

count = 1

diam = a[0]
for i in range(1, len(a)):
    if diam - a[i] >= 4:
        count += 1
        diam = a[i]

print(diam, count)
