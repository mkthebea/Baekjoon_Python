a, b, c = map(int, input().split())

def sol(a, b, c):
    if b == 1:
        return a % c
    res = sol(a, b//2, c)
    if b % 2 == 0:
        return (res*res) % c
    else:
        return (res*res*a) % c

print(sol(a, b, c))

# a / c = x + y
# a = cx + y
# a*a = cx*cx + 2cxy + y*y
# a*a /c = Q + (y*y)/c
# 나머지를 구해서 나머지만 곱하기

# c**n = c**n/2 * c**n/2  (n이 짝수일 경우)
# c**n = c**(n-1)/2 * c**(n-1)/2 * c

# 시간 초과
# res = 1
# for _ in range(b):
#     res = (a * res) % c
# print(res%c)