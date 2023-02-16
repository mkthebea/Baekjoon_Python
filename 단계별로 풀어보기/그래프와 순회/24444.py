import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [0] * (n + 1)
count = 2
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()

queue = deque([r])
visited[r] = 1
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = count
            count += 1
            queue.append(i)

for i in range(1, n+1):
    print(visited[i])