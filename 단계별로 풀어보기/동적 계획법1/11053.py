n = int(input())
num = list(map(int, input().split()))
dp = [0] * n    
dp[0] = 1
for i in range(1,n):
    tem = dp[:i]
    for j in range(i):
        if num[j] >= num[i]:
            tem[j] = 0
    dp[i] = max(tem) + 1
print(max(dp))
