import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(graph, x, y, visited):
    global n
    global cnt
    visited[x][y] = True
    cnt += 1
    # 인접 노드(상하좌우) 재귀 호출
    if x > 0:
        if not visited[x-1][y]:
            dfs(graph, x-1, y, visited)
    if y > 0:
        if not visited[x][y-1]:
            dfs(graph, x, y-1, visited)
    if x < n - 1:
        if not visited[x+1][y]:
                dfs(graph, x+1, y, visited)
    if y < n -1:
        if not visited[x][y+1]:
                dfs(graph, x, y+1, visited)


def int_to_bool(n):
    if n == '0':
        return True
    else:
        return False

n = int(input())
my_map = []
visited = []
for _ in range(n):
    tem = list(input().strip())
    my_map.append(tem)
    visited.append(list(map(int_to_bool, tem)))

res = []
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(my_map, i, j, visited)
            res.append(cnt)
            cnt = 0

res.sort()
print(len(res))
for i in res:
    print(i)