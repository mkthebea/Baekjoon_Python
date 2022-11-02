n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))
# indexError -> n이 1,2일 때 따로 처리
if n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp = []     # 해당 계단까지의 최댓값 저장
    dp.append(score[0])
    dp.append(score[0]+score[1])
    dp.append(max(score[0]+score[2], score[1]+score[2]))
    for i in range(3, n):
        dp.append(max(score[i]+score[i-1]+dp[i-3], score[i]+dp[i-2]))
    print(dp[-1])