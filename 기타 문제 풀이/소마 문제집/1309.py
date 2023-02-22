n = int(input())

dp = [1, 1]
for _ in range(1, n):
    a = dp[0] + 2 * dp[1]
    b = dp[0] + dp[1]
    dp = [a, b]

print((dp[0] + 2*dp[1]) % 9901)  