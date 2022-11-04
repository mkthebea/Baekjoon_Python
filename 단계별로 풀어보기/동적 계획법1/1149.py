n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
# print(cost)

dp = [0] * n
dp[0] = min(cost[0])
pre = cost[0].index(dp[0])

for i in range(1, n):
    tem = cost[i][:]
    del tem[pre]
    dp[i] = min(tem)
    # dp[i] = min(filter(lambda c : cost[i].index(c) != pre, cost[i]))
    if pre != cost[i].index(dp[i]):
        pre = cost[i].index(dp[i])
    else:
        tem2 = list(filter(lambda c : cost[i][c] == dp[i], range(n)))
        pre = tem2[1]
    # print(pre)

print(sum(dp))