# 입력 받은 수들을 A, B, C, D ... 라고 했을 때
# A, B, C, D ...를 M으로 나눈 나머지가 모두 같다 (나머지: R)
# A = M*a + R
# B = M*b + R
# C = M*c + R
# D = M*d + R
# 따라서,
# B-A = M*(b-a)
# C-B = M*(c-b)
# D-C = M*(d-c)
# 즉, M은 B-A, C-B, D-C ... 들의 공약수
# 최대공약수의 약수 = 공약수이므로 최대공약수를 먼저 구한다!

n = int(input())
numbers = []
for _ in range(0, n):
    numbers.append(int(input()))
numbers.sort()

diff = []
for i in range(0,n-1):
    diff.append(numbers[i+1] - numbers[i])

gcd = diff[0]
for i in range(len(diff)):
    # 유클리드 호제법으로 gcd 업데이트
    a = max(diff[i], gcd)
    b = min(diff[i], gcd)
    if(a == b):
        continue
    else:
        while b > 0:
            tem = a
            a = b
            b = tem % b
        gcd = a

res = set()
for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        res.add(i)
        res.add(gcd // i)   # /로 하면 틀림

res.add(gcd)
print(" ".join(map(str,sorted(res))))

# 시간 초과 코드
# m = []
# for d in range(2,numbers[1]):
#     mods = set()
#     check = True
#     for num in numbers:
#         mods.add(num%d)
#         if len(mods) > 1:
#             check = False
#             break
#     if check:
#         m.append(d)
# print(" ".join(map(str,m)))