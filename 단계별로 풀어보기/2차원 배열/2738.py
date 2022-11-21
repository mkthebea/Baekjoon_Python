n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    tem = list(map(int, input().split()))
    for j in range(m):
        A[i][j] += tem[j]
for _ in range(n):
    print(' '.join(list(map(str, A[_]))))
