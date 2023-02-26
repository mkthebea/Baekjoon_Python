import sys
input = sys.stdin.readline

# num에서 세 수를 골라 더했을 때 그 합이 num에 있는 경우(최대)
# x + y + z = k
# x + y = k - z
# x, y, z, k는 모두 num에 포함됨
n = int(input())
num = [int(input()) for _ in range(n)]
num_sum = set()
for x in num:
    for y in num:
        num_sum.add(x + y)
num.sort()
for k in range(n-1, -1, -1):
    for y in range(k+1):
        if num[k] - num[y] in num_sum:
            print(num[k])
            exit()