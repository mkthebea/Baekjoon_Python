def dfs(pl, mi, mul, div, idx, tem_res):
    global n, max_res, min_res, A
    # 탐색이 끝나면 최대, 최소 업데이트
    if idx == n:
        max_res = max(max_res, tem_res)
        min_res = min(min_res, tem_res)
        return
    
    if pl > 0:
        dfs(pl - 1, mi, mul, div, idx + 1, tem_res + A[idx])
    if mi > 0:
        dfs(pl, mi - 1, mul, div, idx + 1, tem_res - A[idx])
    if mul > 0:
        dfs(pl, mi, mul - 1, div, idx + 1, tem_res * A[idx])
    if div > 0:
        dfs(pl, mi, mul, div - 1, idx + 1, int(tem_res / A[idx]))

n = int(input())
A = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())   # 각 연산자의 개수
max_res = -1000000000
min_res = 1000000000
dfs(pl, mi, mul, div, 1, A[0])
print(max_res)
print(min_res)

# 시간 초과 코드
# from itertools import permutations

# n = int(input())
# A = list(map(int, input().split()))
# cnt = list(map(int, input().split()))   # 각 연산자의 개수
# max_res = -1000000000
# min_res = 1000000000
# # 0:+, 1:-, 2:*, 3://
# operators = []
# for i in range(4):
#     for _ in range(cnt[i]):
#         operators.append(i)

# for o in permutations(operators):
#     tem = A[0]
#     for i in range(n-1):
#         if o[i] == 0:
#             tem += A[i+1]
#         elif o[i] == 1:
#             tem -= A[i+1]
#         elif o[i] == 2:
#             tem *= A[i+1]
#         else:
#             if tem < 0:
#                 tem = -((-tem) // A[i+1])
#             else:
#                 tem //= A[i+1]
#     if tem < min_res:
#         min_res = tem
#     if tem > max_res:
#         max_res = tem

# print(max_res)
# print(min_res)

