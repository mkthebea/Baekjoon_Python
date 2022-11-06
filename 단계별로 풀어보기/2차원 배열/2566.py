maxnum, x, y = 0, 0, 0
for i in range(9):
    tem = list(map(int, input().split()))
    maxtem = max(tem)
    if maxnum < maxtem:
        maxnum = maxtem
        x = i + 1
        y = tem.index(maxtem) + 1
if maxnum == 0:
    x, y = 1, 1
print(maxnum)
print(x, y)