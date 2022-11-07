n = int(input())
dp = [0] * n
dp[0] = 0
for i in range(1, n):
    count = dp[i-1] + 1 # 이전 최솟값 + 1: -1 할 경우
    if (i + 1) % 3 == 0 and dp[((i+1)//3) - 1] + 1 < count:
        count = dp[((i+1)//3) - 1] + 1   # /3
    if (i + 1) % 2 == 0 and dp[((i+1)//2) - 1] + 1 < count:
        count = dp[((i+1)//2) - 1] + 1   # /2
    dp[i] = count
print(dp[-1])
