import math

n = input()
count = [0] * 10
for i in n:
    count[int(i)] += 1
if count[6] > count[9]:
    count[6] = math.ceil((count[6] - count[9]) / 2) + count[9]
    count[9] = 0
else:
    count[9] = math.ceil((count[9] - count[6]) / 2) + count[6]
    count[6] = 0
print(max(count))