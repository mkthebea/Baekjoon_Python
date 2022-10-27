n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[n])




# 메모리 초과
# fac = [0] * n
# fac[1] = 1
# for i in range(2, n):
#     fac[i] = i * fac[i - 1]
# # print(fac)

# res = 1
# for i in range(1, int(n/2) + 1):
#     # res += math.factorial(n-i) / (math.factorial(i) * math.factorial(n - (2 * i)))
#     if n == (2 * i):
#         res += 1
#     else:
#         res += int(fac[n-i] / (fac[i] * fac[n - (2 * i)])
#     # print(tem)
# print(res % 15746)


# n=4
# 00=0 1
# 00=1 3!/2! = 3
# 00=2 2!/2! = 1

# n=5
# 00=0 1
# 00=1 4!/3! = 4
# 00=2 3!/2! = 3

# n=i
# 00=j 개면
# 경우의 수: (i-j)!/j! * (i-2j)!
