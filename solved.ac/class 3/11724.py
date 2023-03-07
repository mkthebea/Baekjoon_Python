# 연결 요소: 나누어진 각각의 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)

print(count)