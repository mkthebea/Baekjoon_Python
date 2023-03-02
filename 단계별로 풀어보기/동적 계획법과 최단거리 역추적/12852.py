# 다음 세 가지 연산 가능
# x가 3으로 나누어 떨어지면 3으로 나눔
# x가 2로 나누어 떨어지면 2로 나눔
# 1을 뺌
# 정수를 1로 만들기 위해 연산을 사용하는 횟수의 최솟값
# 1로 만드는 방법에 포함되어 있는 수 출력

# 이것은 DP다..!
# 만드는 과정은 어케 출력?
# 각 숫자를 만들 때 사용된 숫자들 모두 저장
# 사용된 숫자를 알면 연산 횟수는 자동 계산 가능

n = int(input())
dp = {}     # key: 숫자, value: 그 과정의 수 리스트
dp[1] = [1]
dp[2] = [1, 2]
for i in range(3, n+1):
    tem = [dp[i-1][:]]
    if i%3 == 0:
        tem.append(dp[i//3][:])
    if i%2 == 0:
        tem.append(dp[i//2][:])
    tem.sort(key = lambda x:len(x))
    tem[0].append(i)
    # print(i, tem)
    dp[i] = tem[0]
dp[n].reverse()
print(len(dp[n]) - 1)
print(' '.join(map(str,dp[n])))