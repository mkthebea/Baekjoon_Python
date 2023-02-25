from itertools import combinations_with_replacement
n, m = map(int, input().split())
num = [i+1 for i in range(n)]
for i in combinations_with_replacement(num, m):
    print(' '.join(map(str, i)))