n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

# dp 저장시 i번째에는 i번째 와인을 마시지 않는 경우까지 고려하여 최댓값을 넣어야 함
dp = [0] * n
dp[0] = wine[0]
# 인덱스 에러 방지를 위해 n 체크
if n >= 2:
    dp[1] = dp[0] + wine[1]
if n >= 3:
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i-1])
print(max(dp))