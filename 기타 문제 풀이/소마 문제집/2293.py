import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1

# 각 코인별로
for c in coin:
    # k원까지 돌면서
    for i in range(c, k+1):
        if i-c >= 0:
            # i원을 만드는 방법의 수 = i-c원을 만드는 방법의 수 (c 하나 사용하면 됨)
            # i-c원을 만들 방법이 없다면 i원을 만드는 방법도 없음
            # i-c가 0인 경우 = c원을 만드는 경우이므로 dp[0]을 1로 설정해 동전 하나만 사용할 수 있도록 설정
            dp[i] += dp[i-c]
print(dp[k])
