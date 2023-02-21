import sys
sys.setrecursionlimit(10**9)

def dfs(graph, v, heard):
    if heard[v] == 1:   # 진실을 아는 사람일 경우
        for i in graph[v]:
            if heard[i] == 0:
                heard[i] = 1
                dfs(graph, i, heard)

n, m = map(int, input().split())
t = list(map(int,input().split()))    # 진실을 아는 사람들
del t[0]

# 아무 것도 못들은 사람: 0, 진실을 아는 사람: 1
heard = [0 for _ in range(n+1)]
for i in t:
    heard[i] = 1

# 같은 파티에 오는 사람들끼리 연결
graph = [[] for _ in range(n+1)]
parties = []
for _ in range(m):
    party = list(map(int, input().split()))
    del party[0]
    parties.append(party)
    for a in party:
        for b in party:
            if a != b:
                graph[a].append(b)

for i in t:
    dfs(graph, i, heard) # 진실을 아는 사람들에 대해 dfs

res = 0
for party in parties:
    possible = True
    for p in party:
        if heard[p] == 1:
            possible = False
            break
    if possible:
        res += 1

print(res)

# 그래프 모를 때 푼거..(오답)
# 아무 것도 모르는 사람: 0
# 진실을 아는 or 들은 사람: 1
# 거짓말을 들은 사람: 2 (가상)

# 1,2가 같이 있는 경우가 생기면 안됨(이도저도 못하게 되니까)
# -> 진실을 아는 사람이 참여하는 파티의 참여자들을 모두 1로 바꿔서 2가 될 일이 없도록 함

# people, party  = map(int, input().split())
# pList = [0 for i in range(people)]
# truePeople = list(map(int,input().split()))
# for i in range(truePeople[0]):
#     pList[truePeople[i + 1] - 1] = 1

# parties = []
# for p in range(party):
#     tem1 = list(map(int,input().split()))
#     tem2 = []
#     for i in range(tem1[0]):
#         tem2.append(pList[tem1[i + 1] - 1])
#     if 1 in tem2:
#         for i in range(tem1[0]):
#             pList[tem1[i + 1] - 1] = 1
#     parties.append(tem1[1:])

# for participants in parties:
#     t = []
#     for i in range(len(participants)):
#         t.append(pList[participants[i] - 1])
#     if 1 in t:
#         for i in range(len(participants)):
#             pList[participants[i] - 1] = 1

# count = 0
# for participants in parties:
#     for i in range(len(participants)):
#         if pList[participants[i] - 1] == 1:
#             break
#         elif i == len(participants) -1 :
#             count += 1

# print(count)