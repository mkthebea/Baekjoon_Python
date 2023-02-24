from itertools import permutations

n, m = map(int, input().split())
num = [i+1 for i in range(n)]
for i in permutations(num, m):
    print(' '.join(map(str,i)))