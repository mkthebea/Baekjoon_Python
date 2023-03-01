from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, visited):
    global n, m
    queue = deque([[x, y]])
    graph[x][y] = 0
    visited[x][y] = True
    while queue:
        v = queue.popleft()
        dx, dy = v[0], v[1]

        if dx - 1 >= 0 and not visited[dx-1][dy]:
            queue.append([dx-1, dy])
            visited[dx-1][dy] = True
            graph[dx-1][dy] = graph[dx][dy] + 1

        if dx + 1 < n and not visited[dx+1][dy]:
            queue.append([dx+1, dy])
            visited[dx+1][dy] = True
            graph[dx+1][dy] = graph[dx][dy] + 1

        if dy - 1 >= 0 and not visited[dx][dy-1]:
            queue.append([dx, dy-1])
            visited[dx][dy-1] = True
            graph[dx][dy-1] = graph[dx][dy] + 1

        if dy + 1 < m and not visited[dx][dy+1]:
            queue.append([dx, dy+1])
            visited[dx][dy+1] = True
            graph[dx][dy+1] = graph[dx][dy] + 1

# 0: 갈 수 없는 땅 1: 갈 수 있는 땅 2: 목표 지점
# 탐색 결과 갈 수 없는 위치는 -1 출력
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
# graph에는 각 칸의 거리를 저장
graph = []
start = []
for i in range(n):
    tem = list(map(int, input().split()))
    graph.append(tem)
    for j in range(m):
        if tem[j] == 0:
            visited[i][j] = True    # 갈 수 없는 땅은 이미 방문했다고 표시
        elif tem[j] == 2:
            start = [i, j]

bfs(graph, start[0], start[1], visited)
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            graph[i][j] = -1
    print(' '.join(map(str,graph[i])))