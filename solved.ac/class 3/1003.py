t = int(input())
case = [int(input()) for _ in range(t)]
dp = [[0, 0] for _ in range(max(case) + 2)]
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, len(dp)):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
for c in case:
    print(' '.join(map(str, dp[c])))