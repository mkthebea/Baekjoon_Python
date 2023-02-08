# 회의실 한 개, 회의 n개
# 회의 시간이 겹치지 않게 최대 회의 사용

# 회의 시간이 제일 짧은 회의부터 시작

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x:x[0])    # 시작 시간 기준 정렬
time.sort(key=lambda x:x[1])    # 종료 시간 기준 정렬
# 일찍 끝나는 순서대로 정렬하되 종료 시간이 같을 경우 먼저 시작하는 회의를 앞 쪽에 정렬한다
# 시작하자마자 끝나는 회의를 카운트하기 위해서이다.
# (8,10)과 (9,10)이 있고 8시까지 회의가 있을 경우 어느 것을 선택해도 상관 없지만
# (9,10)과 (10,10)이 있을 경우 (10,10)을 먼저 선택하면 (9,10)은 선택되지 않는다. 앞의 회의가 끝난 시간을 기준으로 회의를 채워 넣기 때문이다.

count = 0   # 가능한 회의의 수
end_time = 0
for i in time:
    if i[0] >= end_time:
        count += 1
        end_time = i[1]
        print(i)
print(count)


# for i in time:
#     dur = i[1] - i[0]  # 회의 시간, 끝나는 시간은 포함 안함
#     if table[i[0] : i[1]] == [0]*dur:
#         print(i, table[i[0] : i[1]], [0]*dur)
#         for k in range(dur):
#             table[i[0] + k] = 1
#         count += 1