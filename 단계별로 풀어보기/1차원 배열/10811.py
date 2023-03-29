n, m = map(int, input().split())
bascket = [i+1 for i in range(n)]
bascket.insert(0, 0)

for _ in range(m):
    i, j= map(int, input().split())
    bascket[i:j+1] = bascket[j:i-1:-1]

bascket.pop(0)
print(' '.join(list(map(str, bascket))))