n, m = map(int, input().split())
bascket = [i+1 for i in range(n)]
for _ in range(m):
    i, j= map(int, input().split())
    bascket[i-1], bascket[j-1] = bascket[j-1], bascket[i-1]
print(' '.join(list(map(str, bascket))))