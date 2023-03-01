# 수빈이 위치 n
# 동생 위치 k
# 수빈이 위치는 -1, +1, *2 중 하나
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
# 어떻게 이동해야하는지도 출력
# n < k인가?
from collections import deque

def check(visited, v, n):
    move = [v]
    now = v
    while now != n:
        move.append(visited[now])
        now = visited[now]
    print(len(move)-1)
    print(' '.join(map(str, move[::-1])))

def bfs(visited, n):
    queue = deque([n])
    visited[n] = n
    while queue:
        v = queue.popleft()
        if v == k:
            check(visited, v, n)
            return
        for next_node in [v-1, v+1, v*2]:
            if 0 <= next_node <= 100000 and visited[next_node] == -1:
                visited[next_node] = v  # 직전 방문 노드
                queue.append(next_node)

n, k = map(int, input().split())
# visited = {}
# visited를 딕셔너리로 선언하면 메모리 초과
# 직전 방문 노드만 저장한 후 역추적
visited = [-1 for _ in range(100001)]
bfs(visited, n)