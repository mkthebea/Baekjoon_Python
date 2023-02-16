import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(graph, x, y):
    global n, m
    graph[x][y] = 0
    if x > 0:
        if graph[x-1][y] == 1:
            dfs(graph, x-1, y)
    if x < m - 1:
        if graph[x+1][y] == 1:
            dfs(graph, x+1, y)
    if y > 0:
        if graph[x][y-1] == 1:
            dfs(graph, x, y-1)
    if y < n - 1:
        if graph[x][y+1] == 1:
            dfs(graph, x, y+1)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    loc = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        loc[x][y] = 1
    for i in range(m):
        for j in range(n):
            if loc[i][j] == 1:
                dfs(loc, i, j)
                cnt += 1
    print(cnt)