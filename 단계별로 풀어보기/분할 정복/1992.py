import sys
input = sys.stdin.readline

def compress(x, y, n):
    global video, res
    first = video[x][y]
    finished = True
    for i in range(n):
        if not finished:
            break
        for j in range(n):
            if video[x+i][y+j] != first:
                finished = False
                break
    if finished:
        res += first
    else:
        res += '('
        compress(x, y, n//2)
        compress(x, y + n//2, n//2)
        compress(x + n//2, y, n//2)
        compress(x + n//2, y + n//2, n//2)
        res += ')'
        
n = int(input())
video = []
for _ in range(n):
    video.append(input().strip())
res = ''

compress(0, 0, n)
print(res)