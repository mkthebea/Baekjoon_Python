# 0~n의 정수 k개를 더해서 그 합이 n이 되는 경우의 수
# 즉, n을 k개로 나누는 경우의 수, 0~n
n, k = map(int, input().split())

# n을 k개로 나누는 경우의 수는
# n을 k-1로 나누는 경우의 수 + n-1을 k-1로 나누는 경우의 수 + ... + 0을 k-1로 나누는 경우의 수
# 예를 들어
# 4를 3개로 나누는 경우의 수는
# 4를 2개로 (0+_+_) + 3을 2개로(1+_+_) + 2를 2개로(2+_+_) + 1을 2개로(3+_+_) + 0을 2개로(4+_+_)

# 이를 위해 이차원 dp 배열 선언
# dp[i][j] = i를 j개로 나누는 경우의 수
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# 0을 0~k개로 나누는 경우의 수를 먼저 저장
# 1을 0~k개로 나누는 경우를 계산하기 위하여, 0을 0개로 나누는 경우의 수도 1로 저장
dp[0] = [1 for _ in range(k+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # i를 j개로 나누는 경우의 수 = i를 j-1로 + i-1을 j-1로 + ...+ 0을 j-1로 
        for l in range(i+1):
            dp[i][j] += dp[i-l][j-1]

print(dp[n][k] % 1000000000)