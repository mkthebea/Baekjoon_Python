from collections import deque
n, k = map(int, input().split())

visited = [0 for _ in range(100001)]
queue = deque([n])
while queue:
    v = queue.popleft()
    if v == k:
        break
    for i in [v-1, v+1, 2*v]:
        if 0 <= i <= 100000 and visited[i] == 0:
            queue.append(i)
            visited[i] = visited[v] + 1

print(visited[k])