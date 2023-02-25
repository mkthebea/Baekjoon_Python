import sys
input = sys.stdin.readline

n = int(input())
graph = []
# 각 칸에 도달할 수 있는 경우의 수
dp = [[0 for _ in range(n)] for  _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        move = graph[i][j]
        # 도착점일 때 멈추지 않으면 아래 if문에서 계속 자기 자신이 더해짐
        if i == n-1 and j == n-1:
            break
        if i + move < n:
            dp[i + move][j] += dp[i][j]
        if j + move < n:
            dp[i][j + move] += dp[i][j]

print(dp[n-1][n-1])


# def bfs(graph, x, y, visited):
#     global n
#     queue = deque([[x, y]])
#     visited[x][y] = True
#     cnt = 0
#     while queue:
#         v = queue.popleft()
#         dx, dy = v[0], v[1]
#         # print(dx, dy, graph[dx][dy])
#         # if dx == n-1 and dy == n-1:
#         #     cnt += 1
#         #     visited[dx][dy] = False
#         #     continue
#         move = graph[dx][dy]

#         # 다음 목적지가 도착점이면 visited 처리 안하기
#         if (dx + move == n-1 and dy == n-1) or (dx == n-1 and dy + move == n-1):
#             cnt += 1
#             continue
#         if dx + move < n and not visited[dx + move][dy]:
#             queue.append([dx + move, dy])
#             visited[dx + move][dy] = True
#         if dy + move < n and not visited[dx][dy + move]:
#             queue.append([dx, dy + move])
#             visited[dx][dy + move] = True
#     return cnt