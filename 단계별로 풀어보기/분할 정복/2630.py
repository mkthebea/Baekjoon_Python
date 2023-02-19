import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def cut(x, y, n):
    global paper, white, blue

    # 현재 종이가 단색인지 확인
    finished = True
    first = paper[x][y]
    for i in range(n):
        if not finished:
            break
        for j in range(n):
            if first != paper[x+i][y+j]:
                finished = False
    
    if finished:
        if paper[x][y] == '1':
            blue += 1
        else:
            white += 1
    else:
        half = n//2
        cut(x, y, half)
        cut(x+half, y, half)
        cut(x, y+half, half)
        cut(x+half, y+half, half)

n = int(input())
paper= []
for _ in range(n):
    paper.append(list(input().split()))

white, blue = 0, 0
cut(0, 0, n)
print(white)
print(blue)


# 이 코드도 정답이지만 위의 코드로 개선함
# def cut(paper, n):
#     global white, blue
#     half = n // 2
#     # 4개로 나누기
#     p1, p2, p3, p4 = [], [], [], []
#     for i in range(half):
#         p1.append(paper[i][:half])
#         p2.append(paper[i][half:])
#         p3.append(paper[half+i][:half])
#         p4.append(paper[half+i][half:])

#     # 각 종이가 단색인지 확인
#     for p in [p1, p2, p3, p4]:
#         finished = True
#         first = p[0][0]
#         for i in range(half):
#             for j in range(half):
#                 if first != p[i][j]:
#                     finished = False
#         if finished:
#             if p[0][0] == '1':
#                 blue += 1
#             else:
#                 white += 1
#         else:
#             cut(p, half)

# n = int(input())
# paper= []
# test = set()    # 처음부터 단색인지 확인
# for _ in range(n):
#     tem = list(input().split())
#     paper.append(tem)
#     test.update(tuple(tem))

# if len(test) == 1:
#     if paper[0][0] == '1':
#         print(0)
#         print(1)
#     else:
#         print(1)
#         print(0)
#     exit()

# white, blue = 0, 0
# cut(paper,n)
# print(white)
# print(blue)