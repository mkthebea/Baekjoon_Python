# 가장 긴 증가하는 부분 수열
n = int(input())
A = list(map(int, input().split()))
dp = [[] for _ in range(n)] # 지금까지 중 가장 긴 증가하는 부분 수열 저장
dp[0] = [A[0]]
for i in range(1, n):
    pre = []
    for j in range(i-1, -1, -1):
        if A[j] < A[i] and len(pre) < len(dp[j]):
            pre = dp[j][:]
    if pre != []:
        dp[i] = pre
    dp[i].append(A[i])
dp.sort(key = lambda x:len(x))
print(len(dp[-1]))
print(' '.join(map(str, dp[-1])))