from itertools import combinations

n, m = map(int, input().split())
num = [i+1 for i in range(n)]
for i in combinations(num, m):
    print(' '.join(map(str, i)))