# 1: 0~9
# 2: 11~19, 22~29, 33~39 ... 88,89, 99
# 3: 111~119, 122~129 -> 100 + 2의 경우들. 10의 자리부터 계단수인건 이미 계산함
#    222~229 -> 

n = int(input())
# 각각 0,1,2,3,4,5,6,7,8,9로 시작하는 오르막 수의 수를 저장 (0으로 시작 가능)
dp = [[0 for _ in range(10)] for _ in range(n)]
dp[0] = [1,1,1,1,1,1,1,1,1,1]
for i in range(1, n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
print(sum(dp[n-1]) % 10007)