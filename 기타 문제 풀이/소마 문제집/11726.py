# 1, 2의 합으로 n을 만드는 경우의 수와 같음

n = int(input())
dp = [0 for _ in range(n)]
if n == 1:
    print(1)
    exit()
dp[0] = 1
dp[1] = 2
for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n-1])