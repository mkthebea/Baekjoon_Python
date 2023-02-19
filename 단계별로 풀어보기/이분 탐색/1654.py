# 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결하는 방법
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용
# 보통 반복문으로 구현

import sys
input = sys.stdin.readline

k, n = map(int, input().split())    # k:갖고 있는 랜선 수, n:필요한 랜선 수
lan = []
for _ in range(k):
    lan.append(int(input()))

res = 0
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lan:
        cnt += l // mid  # 중간값의 길이로 랜선을 잘랐을 때 얻을 수 있는 랜선의 수
    
    if cnt < n:
        end = mid - 1
    else:   # 원하는 개수 달성 했지만 더 크게 잘라도 될 수 있으므로 res에 저장하고 더 큰 범위 탐색
        res = mid
        start = mid + 1

print(res)
