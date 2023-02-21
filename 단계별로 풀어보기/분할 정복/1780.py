import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def cut(x, y, n):
    global paper, cnt
    finished = True
    first = paper[x][y]
    for i in range(n):
        if not finished:
            break
        for j in range(n):
            if first != paper[x+i][y+j]:
                finished = False
                break
    
    if finished:        # 현재 종이가 단색이면
        if first == '-1':
            cnt[0] += 1
        elif first == '0':
            cnt[1] += 1
        else:
            cnt[2] += 1
    else:
        cut(x, y, n//3)
        cut(x, y + n//3, n//3)
        cut(x, y + 2*n//3, n//3)
        cut(x + n//3, y, n//3)
        cut(x + n//3, y + n//3, n//3)
        cut(x + n//3, y + 2*n//3, n//3)
        cut(x + 2*n//3, y, n//3)
        cut(x + 2*n//3, y + n//3, n//3)
        cut(x + 2*n//3, y + 2*n//3, n//3)

n = int(input())
paper = []
cnt =[0, 0, 0]
for _ in range(n):
    paper.append(list(input().strip().split()))
cut(0, 0, n)
for c in cnt:
    print(c)