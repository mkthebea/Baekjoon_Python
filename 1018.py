# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 체스판을 색칠하는 경우는 두 가지.
# 입력 받은 값에 대해 두 가지 경우 모두 탐색? 필요 X 하나에 대해서만 한 뒤 반전시키면 됨.

# 입력 받아서 제일 왼쪽 위에 있는 색을 기준으로 체스판으로 만들기 위해 색칠해야 하는 칸을 찾는다. 2차원 배열 필요 없이 일차원 배열로 만들어서 끊기만 하면 됨
# 단, 너비는 기억해야 함
# 다시 색칠해야 한다면 1, 안해도 되면 0

# 예를 들어
# W B W
# B W B
# W W W
# 라면
# 0 0 0
# 0 0 0
# 0 1 0 
# 이고
# 반전시키면
# 1 1 1
# 1 1 1
# 1 0 1
# 여기서 2 x 2 체스판을 만들어야 한다면, 1이 가장 적게 포함되어 있는 영역을 찾으면 됨.
# 이 영역은 어떻게 찾을까?
# 색칠 여부를 표현한 배열은 0 0 0 0 0 0 0 1 0 임
# # 2 x 2 체스판의 경우 (2칸 카운트 -> 1칸 건너뛰기)를 줄 마다 두 번 반복한다. 마지막 줄은 할 필요 없음
# 각 줄에 대해 (원하는 너비)칸 카운트 -> (전체 판의 너비 - 1)칸 건너뛰기
# 일일이 다 한 다음에, 시작 인덱스가 3(전체 너비)의 배수가 아닐 경우 제외. 
# 마지막 줄은 검사하지 않기 위해 반복문을 {전체 칸 수 - (원하는 높이 - 1) * (전체 너비)} 만큼만 반복.

# start = 0, count = (체스판에 필요한 칸 + 1)로 초기화 해놓고, start가 3의 배수가 아니면 break. 
# 이후 색칠할 칸의 개수가 count보다 작을 때마다 count와 start 업데이트.

# 색칠 여부 배열은 어떻게 만들까?
# 비교군 배열을 맨 왼쪽 위 색깔에 따라 만든 후 하나하나 비교해서 다를 경우 1.
# 입력 받은 배열 board = [w,b,w,b,w,b,w,w,w]
# 비교군 배열 chess = [w,b,w,b,w,b,w,b,w]
# 색칠 배열 color = []
# for i in range(len(board)):
#     if(board[i] == chess[i]):
#         color.append(0)
#     else:
#         color.append(1)



h, w = map(int, input().split())
board = []
chess = []
color = []

for i in range(h):
    for j in list(input()):
        board.append(j)

for i in range(h):
    if(i % 2 == 0):
        for j in range(w):
            if (j % 2 == 0):
                chess.append('W')
            else:
                chess.append('B')
    else:
        for j in range(w):
            if (j % 2 == 0):
                chess.append('B')
            else:
                chess.append('W')

for i in range(len(board)):
    if(board[i] == chess[i]):
        color.append(0)
    else:
        color.append(1)

# print(board, chess, color)

# 각 줄에 대해 (원하는 너비 = 8)칸 카운트 -> (전체 판의 너비 - 1)칸 건너뛰기
# 일일이 다 한 다음에, 시작 인덱스가 3(전체 너비)의 배수가 아닐 경우 제외. 
# 마지막 줄은 검사하지 않기 위해 반복문을 {전체 칸 수 - (원하는 높이 - 1) * (전체 너비)} 만큼만 반복.

colorCount1 = 64    #1 개수
colorCount0 = 64    #0 개수
for i in range(w * h - 7 * w):
    if (i % w > w - 8):
        continue
    temCount1 = 0
    temCount0 = 0
    for j in range(8):
        temCount1 += color[i + (w * j) : i + (w * j) + 8].count(1)
        temCount0 += color[i + (w * j) : i + (w * j) + 8].count(0)
    if (temCount1 < colorCount1):
        colorCount1 = temCount1
    if (temCount0 < colorCount0):
        colorCount0 = temCount0
       
print(colorCount1 if (colorCount1 < colorCount0) else colorCount0)
