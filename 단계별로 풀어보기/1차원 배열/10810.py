n, m = map(int, input().split())
bascket = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        bascket[l] = k
print(' '.join(list(map(str, bascket))))