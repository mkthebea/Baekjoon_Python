import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global count
    visited[v] = count
    count += 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort(reverse=True)

dfs(graph, r, visited)
for i in range(1, n+1):
    print(visited[i])