from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, queue):
    global n, m
    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]
        if x > 0 and graph[x-1][y] == 0:
            queue.append([x-1, y])
            graph[x-1][y] = graph[x][y] + 1
        if x < n-1 and graph[x+1][y] == 0:
            queue.append([x+1, y])
            graph[x+1][y] = graph[x][y] + 1
        if y > 0 and graph[x][y-1] == 0:
            queue.append([x, y-1])
            graph[x][y-1] = graph[x][y] + 1
        if y < m-1 and graph[x][y+1] == 0:
            queue.append([x, y+1])
            graph[x][y+1] = graph[x][y] + 1

        # print("------------------")
        # for _ in graph:
        #     print(_)

m, n = map(int, input().split())    # m:가로, n:세로
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

# done = True
queue = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
        # elif box[i][j] == 0:
        #     done = False
# 처음부터 모든 토마토가 익어있는 경우
# 어차피 모든 칸이 1 아니면 -1이기 때문에 0 출력됨
# if done:   
#     print(0)
if len(queue) == 0:      # 익은 토마토가 하나도 없는 경우
    print(-1)
else:
    bfs(box, queue)
    res = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                print(-1)
                exit()
        if max(box[i]) > res:
            res = max(box[i])
    print(res-1)
    # res = sum(box, [])
    # if 0 in res:   # 토마토가 모두 익지 못할 경우
    #     print(-1)
    # else:
    #     print(max(res)-1)



### 여러 개의 큐 사용 ###
# 이렇게 할 필요 없음, 인덱스 에러 남

# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(graph, starts):
#     global n, m
#     queues = []
#     for s in starts:
#         queues.append(deque([s]))   #  각각의 시작점에 대한 큐 생성

#     # 거리(일수) 저장
#     while len(queues) != 0:    
#         # for i in range(len(queues)):
#         #     v = queues[i].popleft()
#             # x, y = v[0], v[1]
#             # if x > 0 and graph[x-1][y] == 0:
#             #     queues[i].append([x-1, y])
#             #     graph[x-1][y] = graph[x][y] + 1
#             # if x < n-1 and graph[x+1][y] == 0:
#             #     queues[i].append([x+1, y])
#             #     graph[x+1][y] = graph[x][y] + 1
#             # if y > 0 and graph[x][y-1] == 0:
#             #     queues[i].append([x, y-1])
#             #     graph[x][y-1] = graph[x][y] + 1
#             # if y < m-1 and graph[x][y+1] == 0:
#             #     queues[i].append([x, y+1])
#             #     graph[x][y+1] = graph[x][y] + 1
#             # # print("i: ", i)
#             # if len(queues[i]) == 0:
#             #     del queues[i]     # 큐 하나 다 쓰면 제거
#             #     i -= 1
#         for tem_queue in queues:
#             v = tem_queue.popleft()
#             x, y = v[0], v[1]
#             if x > 0 and graph[x-1][y] == 0:
#                 tem_queue.append([x-1, y])
#                 graph[x-1][y] = graph[x][y] + 1
#             if x < n-1 and graph[x+1][y] == 0:
#                 tem_queue.append([x+1, y])
#                 graph[x+1][y] = graph[x][y] + 1
#             if y > 0 and graph[x][y-1] == 0:
#                 tem_queue.append([x, y-1])
#                 graph[x][y-1] = graph[x][y] + 1
#             if y < m-1 and graph[x][y+1] == 0:
#                 tem_queue.append([x, y+1])
#                 graph[x][y+1] = graph[x][y] + 1

#             if len(tem_queue) == 0:
#                 queues.remove(tem_queue)     # 큐 하나 다 쓰면 제거
            
#             # print("------------------")
#             # for _ in graph:
#             #     print(_)
            
# m, n = map(int, input().split())    # m:가로, n:세로
# box = []
# for _ in range(n):
#     box.append(list(map(int, input().split())))

# zero = 0
# starts = []
# for i in range(n):
#     for j in range(m):
#         if box[i][j] == 1:
#             starts.append([i, j])
#         elif box[i][j] == 0:
#             zero += 1

# if zero == 0:   # 처음부터 모든 토마토가 익어있는 경우
#     print(0)
# elif len(starts) == 0:      # 익은 토마토가 하나도 없는 경우
#     print(-1)
# else:
#     bfs(box, starts)
#     if 0 in sum(box, []):   # 토마토가 모두 익지 못할 경우
#         print(-1)
#     else:
#         print(max(sum(box, []))-1)