# n = int(input())
# cost = 0
# km = list(map(int, input().split()))
# oil = list(map(int, input().split()))
# oil.pop(-1)

# while(len(km) > 0):
#     oil_min = min(oil)
#     min_index = oil.index(oil_min)
#     for i in range(min_index, len(km)):
#         cost += oil_min * km[i]
#     km = km[:min_index]
#     oil = oil[:min_index]
# print(cost)

# 최소 기름값을 볼 때마다 갱신해보자
n = int(input())
cost = 0
km = list(map(int, input().split()))
oil = list(map(int, input().split()))
oil.pop(-1)
min_oil = oil[0]
for i in range(n-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    cost += min_oil * km[i]
print(cost)