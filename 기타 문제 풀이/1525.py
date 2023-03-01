# 3x3 표에 8개의 숫자
# 오른쪽 아래 가장 끝 칸은 비어 있어야 함(정리된 상태)
# 상하좌우 칸 중 하나가 비어있으면 숫자 이동 가능
# 표 밖으로 나가는건 안됨
# 최소 이동으로 정리된 상태 만들기
# 이동이 불가능한 경우 -1 출력

# bfs로 푸는데, 큐에 현재 퍼즐 상태를 문자열로 넣는다
# visited를 딕셔너리로 선언하여 key 퍼즐 상태를 만들기 위한 횟수를 value로 저장

from collections import deque

def bfs(puzzle, visited):
    queue = deque([puzzle])
    visited[puzzle] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        v = queue.popleft()
        if v == '123456780':
            return visited[v]
        pos = v.index('0')
        x0 = pos//3
        y0 = pos%3
        for i in range(4):
            x = x0 + dx[i]
            y = y0 + dy[i]
            if 0 <= x < 3 and 0 <= y <3:
                next_puzzle = list(v)
                next_puzzle[pos], next_puzzle[x*3+y] = next_puzzle[x*3+y], next_puzzle[pos]
                next_puzzle = ''.join(next_puzzle)
                if next_puzzle not in visited.keys():
                    queue.append(next_puzzle)
                    visited[''.join(next_puzzle)] = visited[v] + 1
    return -1

puzzle = ''
for _ in range(3):
    a, b, c = input().split()
    puzzle += a+b+c
visited = dict()
print(bfs(puzzle, visited))