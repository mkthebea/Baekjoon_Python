n = int(input())
coord = [[0]*101 for _ in range(101)]
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            coord[x + i][y + j] = 1
res = 0
for _ in range(101):
    res += sum(coord[_])
print(res)


# 틀린 풀이: 색종이 두 장이 겹쳤을 때만 계산 가능. 여러 장이 겹쳐 있으면 이미 뺀 넓이를 또 빼서 틀린 답이 나옴
# n = int(input())
# pos = []
# for _ in range(n):
#     pos.append(list(map(int, input().split())))
# width = n * 100
# pos.sort(key=lambda x:x[0]) # x좌표 순으로 정렬
# for i in range(n):
#     for j in range(i + 1, n):
#         if pos[j][0] >= pos[i][0] + 10:
#             break
#         if abs(pos[j][1] - pos[i][1]) >= 10:
#             break
#         xdif = pos[i][0] + 10 - pos[j][0]
#         if pos[i][1] > pos[j][1]:
#             ydif = pos[j][1] + 10 - pos[i][1]
#         else:
#             ydif = pos[i][1] + 10 - pos[j][1]
#         width -= xdif * ydif
# print(width)