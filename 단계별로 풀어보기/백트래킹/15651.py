from itertools import product
n, m = map(int, input().split())
num = [i+1 for i in range(n)]
for i in product(num, repeat=m):
    print(' '.join(map(str, i)))