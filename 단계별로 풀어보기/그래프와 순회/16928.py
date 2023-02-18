from collections import deque
import sys
input = sys.stdin.readline

# 사다리나 뱀은 카운트 안함
# 주사위로 갈 수 있는 노드의 비용은 1, 사다리와 뱀은 0
# 사다리나 뱀이 있는 칸에서는 주사위 못굴린다!

# 최단거리이므로 bfs 사용
def bfs(graph, start, dis):
    queue = deque([start])
    while queue:
        v = graph[queue.popleft()]
        for i in range(1, 7):
            if v + i > 100:
                break
            next_node = graph[v + i]
            if dis[next_node] == 0:
                queue.append(next_node)
                dis[next_node] = dis[v] + 1

graph = [i for i in range(101)]
dis = [0] * 101
cnt = 0

n, m = map(int, input().split())    #n:사다리의 수, m:뱀의 수
for _ in range(n+m):
    x, y = map(int, input().split())
    graph[x] = y

bfs(graph, 1, dis)
print(dis[100])