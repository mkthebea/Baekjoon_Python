# 네 개의 명령어 D, S, L, R
# 레지스터: 0 <= n < 10000 저장
# n의 각 자릿수 d1, d2, d3, d4
# D: n*2, 9999보다 크면 %10000. 즉 n*2%10000
# S: n-1 n이 0이라면 9999
# L: 각 자릿수를 왼편으로 회전. d1 d2 d3 d4 -> d2 d3 d4 d1
# R: 각 자릿수를 오른편으로 회전. d1 d2 d3 d4 -> d4 d1 d2 d3
# A를 B로 바꾸는 최소한의 명령어 생성
# 0001 = 1 0100 = 100 0이 포함된 경우 주의

# str -> int -> str 과정에서 시간 초과가 나는듯
# 다 int로 구현

# visited가 딕셔너리이고 매번 not in으로 순회
# 2차원 리스트 사용 (X)
# 큐에 path까지 함께 저장, visited는 bool 배열

# 불필요한 if문, 변수 할당 줄이기

import sys
input = sys.stdin.readline
from collections import deque

def bfs(A, B, visited):
    queue = deque([(A, '')])
    visited[A] = True
    while queue:
        v, path = queue.popleft()
        if v == B:
            print(path)
            return
        # D
        D = (v*2)%10000
        if not visited[D]:
            queue.append((D, path + 'D'))
            visited[D] = True
        # S
        S = (v-1)%10000
        if not visited[S]:
            queue.append((S, path + 'S'))
            visited[S] = True
        # L
        L = (v%1000) * 10 + v//1000
        if not visited[L]:
            queue.append((L, path + 'L'))
            visited[L] = True
        # R
        R = (v%10)*1000 + (v//10)
        if not visited[R]:
            queue.append((R, path + 'R'))
            visited[R] = True

t = int(input())    # 테스트 케이스 수
for _ in range(t):
    A, B = map(int, input().split())
    visited = [False for _ in range(10000)]    # 각 상태가 되기까지의 명령어
    bfs(A, B, visited)