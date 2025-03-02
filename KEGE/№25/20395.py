from fnmatch import *

for i in range(840, 10 ** 10, 840):
    if fnmatch(str(i), '1?7301*320'):
        print(i, i / 8)