import sys
input = sys.stdin.readline

def sol(size, cnn):
    if size == 1:
        print(cnn[0][0])
        exit()
    n = size // 2
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            tem = [cnn[i][j], cnn[i+1][j], cnn[i][j+1], cnn[i+1][j+1]]
            tem.remove(max(tem))
            res[i//2][j//2] = max(tem)
    sol(n, res)

n = int(input())
cnn = []
for _ in range(n):
    cnn.append(list(map(int, input().split())))
sol(n, cnn)