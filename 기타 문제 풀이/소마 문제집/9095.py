t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    # 순서 구분
    for i in range(1, n+1):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i] += dp[i-j]
    print(dp[n])
