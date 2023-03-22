# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리: 모든 집의 치킨 거리의 합
# 두 칸 사이의 거리는 |x1-x2|+|y1-y2|
# 0: 빈칸, 1: 집, 2: 치킨집
# 치킨집을 최대 m개만 남기고 폐업, 도시의 치킨 거리 최소화
# 출력: 치킨집 최대 m개를 골랐을 때 치킨 거리의 최솟값

# 각 치킨집에 대해, 각 집에서 그 치킨집까지의 거리를 배열로 저장
# 총 합이 가장 큰 치킨집부터 삭제
# 도시의 치킨 거리는 남은 배열의 min들끼리 더하면 됨

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
res = 2*(n**3)
# 치킨집, 집 위치 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

# m개의 치킨집 선택
for loc_c in combinations(chicken, m):
    tem = 0
    # 모든 집에 대해 
    for loc_h in house:
        # m개의 치킨집까지의 거리
        dist = []
        for i in range(m):
            dist.append(abs(loc_h[0]-loc_c[i][0]) + abs(loc_h[1]-loc_c[i][1]))
            # tem += abs(loc_h[0]-loc_c[i][0]) + abs(loc_h[1]-loc_c[i][1])
        tem += min(dist)
    if tem < res:
        res = tem
print(res)

# 틀린 코드
# dist = []
# chickens = 0
# res = 0
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# # 치킨집 위치 저장
# for i in range(n):
#     if 2 not in graph[i]:
#         continue
#     for j in range(n):
#         if graph[i][j] == 2:
#             chicken.append([i, j])
# chickens = len(chicken)

# # 각각의 치킨집에 대해 집까지의 거리 저장
# # dist[i]는 i번째 집에서 각 치킨집 까지의 거리
# for i in range(n):
#     if 1 not in graph[i]:
#         continue
#     for j in range(n):
#         if graph[i][j] == 1:
#             tem = []
#             for c in chicken:
#                 tem.append(abs(i-c[0]) + abs(j-c[1]))
#             dist.append(tem)

# # 총 거리 합이 가장 큰 치킨집부터 삭제
# # -> 삭제 후 치킨 거리가 최소가 되는 치킨집 삭제
# # 하나씩 삭제해보기
# print(dist)
# while m < chickens:
#     deleted = [0 for _ in range(chickens)]  # i번째 치킨집을 삭제했을 때 최소 거리
#     for i in range(chickens):
#         for d in dist:
#             tem = d[:]
#             del tem[i]    # 현재 삭제해 볼 치킨집 인덱스
#             deleted[i] += min(tem)
#     idx = deleted.index(min(deleted))
#     for d in dist:
#         del d[idx]
#     print(idx)
#     chickens -= 1
# print(dist)
# for d in dist:
#     res += min(d)
# print(res)