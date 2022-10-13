# import math

# 동적 계획법
def count_num(num, k):
    count = 0
    while num != 0:
        num //= k
        count += num
    return count
n, m = map(int,input().split())
print(min(count_num(n,5) - count_num(m,5) - count_num(n-m,5), count_num(n,2) - count_num(m,2) - count_num(n-m,2)))

# 시간 초과
# res = math.factorial(n) // (math.factorial(m) * math.factorial(n-m))
# count = 0
# while(True):
#     if(res % 10 != 0):
#         break
#     count += 1
#     res //= 10
# print(count)