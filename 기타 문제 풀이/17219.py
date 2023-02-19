import sys
input = sys.stdin.readline

n, m = map(int, input().split())
site = {}
res =''
for _ in range(n):
    url, pw = input().strip().split()
    site[url] = pw
for _ in range(m):
    res += site[input().strip()] + '\n'
print(res.strip())
