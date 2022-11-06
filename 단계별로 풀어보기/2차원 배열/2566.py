maxnum, x, y = 0, 0, 0
for i in range(9):
    tem = list(map(int, input().split()))
    maxtem = max(tem)
    if maxnum < maxtem:
        maxnum = maxtem
        x = i + 1
        y = tem.index(maxtem) + 1
# 모든 데이터가 0일 경우 처리 필요
if maxnum == 0:
    x, y = 1, 1
print(maxnum)
print(x, y)