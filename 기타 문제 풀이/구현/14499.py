# 주사위의 모든 면엔 0이 적혀있음
# 지도 좌표 (r,c) r:위쪽 거리 c: 왼쪽 거리
# 지도의 칸에는 정수가 쓰여있음
# 주사위를 굴렸을 때
#   이동한 칸에 0 -> 주사위 바닥면 수가 칸에 복사됨
#   이동한 칸이 0 아님 -> 칸에 쓰여있는 수가 주사위 바닥면으로 복사, 칸은 0
# 지도의 바깥으로 이동하려는 경우 무시

# 마주보는 주사위 면의 합(인덱스)은 7

# 밑면 6
# 오른쪽: 3 1 4 6 반복
# 왼쪽: 4 1 3 6 반복
# 아래: 5 1 2 6 반복
# 위: 2 1 5 6 반복

# 밑면 1 
# 오른쪽: 4 6 3 1 반복

# -> 밑면 4,6,3,1 반복됨

# 밑면 5
# 오른쪽: 3 2 4 5 반복

# 각 면의 상하좌우만 알면 모두 구할 수 있다!




# 지도 세로 n 가로 m
# 1:오른 2:왼 3:위 4:아래
n, m, x, y, k = map(int, input().split())
my_map = []
cube = [0,0,0,0,0,0]    # i-1번째 자리에 써있는 수
next_num = [[3,4,2,5], [3,4,6,1], [6,1,2,5], [1,6,2,5], [3,4,1,6], [3,4,5,2]] # i-1면이 바닥에 있을 때 우좌상하 이동 시 아래로 오는 면
# -> 주사위를 굴릴 때마다 방향도 바뀐다. 의미 없다,,
now = 6 # 현재 밑면
for i in range(n):
    my_map.append(list(map(int, input().split())))
move = list(map(int, input().split()))
# print(n,m,x,y,my_map,move)s
for i in move:
    updated = False
    if i == 1:  # 오른쪽
        if y + 1 < m:
            updated = True
            y += 1  # 위치 이동
            now = next_num[now-1][0]    # 밑면 업데이트
    elif i == 2:    # 왼쪽
        if y - 1 >= 0:
            updated = True
            y -= 1  # 위치 이동
            now = next_num[now-1][1]    # 밑면 업데이트
    elif i == 3:    # 위
        if x - 1 >= 0:
            updated = True
            x -= 1  # 위치 이동
            now = next_num[now-1][2]    # 밑면 업데이트
    else:   # 아래
        if x + 1 < n:
            updated = True
            x += 1  # 위치 이동
            now = next_num[now-1][3]    # 밑면 업데이트

    if updated:
        if my_map[x][y] == 0:
            my_map[x][y] = cube[now-1]
        else:
            cube[now-1] = my_map[x][y]
            my_map[x][y] = 0
        print(i, now)
        print(cube[6-now])  # 윗면 출력
    else:
        print("false")