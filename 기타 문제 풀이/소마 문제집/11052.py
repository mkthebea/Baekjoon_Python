# 8가지 등급이 있는 카드
# 카드팩의 종류는 n가지: 카드 1~n개가 포함된 카드팩
# 개수가 적은 팩이라도 가격이 비싸면 높은 등급이 많을 것
# 돈을 최대한 많이 지불해서 카드 n개를 구매
# 카드가 i개 포함된 카드팩의 가격은 Pi원

n = int(input())
p = list(map(int, input().split()))

# n개의 카드를 사기 위해 지불할 수 있는 금액의 최댓값
# 0개의 카드를 사는데는 0원
dp = [0 for _ in range(n+1)]
dp[1] = p[0]    # 1개의 카드를 사는데는 1개 카드팩 가격
for i in range(2, n+1):
    # i개의 카드를 살 수 있는 경우의 수
    tem = [p[i-1]]  # i개 카드팩 가격
    for j in range(1, i):
        # i-j개 살 수 있는 가격 + j개 카드팩 가격
        tem.append(dp[i-j] + p[j-1])
    dp[i] = max(tem)
print(dp[-1])