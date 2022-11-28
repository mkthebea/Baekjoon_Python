n = int(input())
pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))
width = n * 100
pos.sort(key=lambda x:x[0]) # x좌표 순으로 정렬
for i in range(n):
    for j in range(i + 1, n):
        if pos[j][0] >= pos[i][0] + 10:
            break
        if abs(pos[j][1] - pos[i][1]) >= 10:
            break
        xdif = pos[i][0] + 10 - pos[j][0]
        if pos[i][1] > pos[j][1]:
            ydif = pos[j][1] + 10 - pos[i][1]
        else:
            ydif = pos[i][1] + 10 - pos[j][1]
        width -= xdif * ydif
print(width)