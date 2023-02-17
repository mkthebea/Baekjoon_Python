from collections import deque
import sys
input = sys.stdin.readline

### 최단거리의 길이를 찾을 땐 dis 배열을 따로 만들어서 각 노드의 거리를 저장하자 ###

def bfs(graph, x, y, dis):
    global n, m
    queue = deque([[x, y]])
    graph[x][y] = 0     # 시작점 방문처리
    dis[x][y] = 1   # 시작점 거리 1
    while queue:
        v = queue.popleft()
        dx, dy = v[0], v[1]
        if dx > 0 and graph[dx-1][dy] == 1:
            queue.append([dx-1, dy])
            graph[dx-1][dy] = 0   # 방문처리
            dis[dx-1][dy] = dis[dx][dy] + 1
            
        if dx < n-1 and graph[dx+1][dy] == 1:
            queue.append([dx+1, dy])
            graph[dx+1][dy] = 0   # 방문처리
            dis[dx+1][dy] = dis[dx][dy] + 1

        if dy > 0 and graph[dx][dy-1] == 1:
            queue.append([dx, dy-1])
            graph[dx][dy-1] = 0   # 방문처리
            dis[dx][dy-1] = dis[dx][dy] + 1

        if dy < m-1 and graph[dx][dy+1] == 1:
            queue.append([dx, dy+1])
            graph[dx][dy+1] = 0   # 방문처리
            dis[dx][dy+1] = dis[dx][dy] + 1

n, m = map(int, input().split())
dis = [[0 for _ in range(m)] for _ in range(n)]
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input().strip()))))

bfs(maze, 0, 0, dis)
print(dis[n-1][m-1])