import math

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))