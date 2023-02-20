# 이분 그래프
# 그래프의 정점의 집합을 둘로 분할하여
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있는 그래프
# 빨강, 파랑으로 나눈다 치면 모든 간선이 빨강과 파랑 꼭짓점을 이어야 함

# from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs로 구현
def is_bipartite(graph, v, colors, now_color):
    global res
    if not res:
        return
    colors[v] = now_color
    next_color = 0
    if now_color == 1:
        next_color = 2
    else:
        next_color = 1
    
    for i in graph[v]:
        if colors[i] == 0:
            is_bipartite(graph, i, colors, next_color)
        elif colors[i] == now_color:
            res = False
            return

# bfs
# def is_bipartite(graph, start, colors):
#     queue = deque([start])
#     colors[start] = 1

#     while queue:
#         v = queue.popleft()
#         # 연결 노드 색깔 결정
#         next_color = 0
#         if colors[v] == 1:
#             next_color = 2
#         else:
#             next_color = 1

#         for i in graph[v]:
#             if colors[i] == 0:
#                 queue.append(i)
#                 colors[i] = next_color
#             elif colors[i] == colors[v]:      # 연결된 노드와 같은 색깔인 노드가 있다면
#                 print("NO")
#                 return
#     print("YES")

k = int(input())    # 테스트 케이스 개수
graphs = []
colors = []     # 0, 1, 2  0은 방문 안한 정점
for _ in range(k):
    v, e = map(int, input().split())    # v:정점의 개수 e:간선의 개수
    graph = [[] for _ in range(v + 1)]  # 각 정점에 연결된 정점들
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    graphs.append(graph)
    colors.append([0 for _ in range(v + 1)])

for i in range(k):
    res = True
    for j in range(1, len(graphs[i])):
        if colors[i][j] == 0:
            is_bipartite(graphs[i], j, colors[i], 1)
            if not res:
                break
    if res:
        print("YES")
    else:
        print("NO")