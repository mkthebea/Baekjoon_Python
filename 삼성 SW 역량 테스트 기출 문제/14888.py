from itertools import permutations

n = int(input())
A = list(map(int, input().split()))
cnt = list(map(int, input().split()))   # 각 연산자의 개수
max_res = 0
min_res = 1000000000
# 0:+, 1:-, 2:*, 3://
operators = []
for i in range(4):
    for _ in range(cnt[i]):
        operators.append(i)

for o in permutations(operators):
    tem = A[0]
    for i in range(n-1):
        if o[i] == 0:
            tem += A[i+1]
        elif o[i] == 1:
            tem -= A[i+1]
        elif o[i] == 2:
            tem *= A[i+1]
        else:
            if tem < 0:
                tem = -((-tem) // A[i+1])
            else:
                tem //= A[i+1]
    if tem < min_res:
        min_res = tem
    if tem > max_res:
        max_res = tem

print(max_res)
print(min_res)

