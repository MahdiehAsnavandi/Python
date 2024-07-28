from math import *
n = int(input())
count = 0
all_square_roots = []
while count < n:
    numbers = int(input())
    if numbers > 0:
        square_root = sqrt(numbers)
        all_square_roots.append(square_root)
    count = count + 1

for i in all_square_roots:
    print("%.4f" % (floor(i * 10000)/10000))
