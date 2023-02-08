# 회의실 한 개, 회의 n개
# 회의 시간이 겹치지 않게 최대 회의 사용

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:x[0])    # 시작 시간 기준 정렬
time.sort(key=lambda x:x[1])    # 종료 시간 기준 정렬

count = 0   # 가능한 회의의 수
end_time = 0
for i in time:
    if i[0] >= end_time:
        count += 1
        end_time = i[1]
        print(i)
print(count)