# ATM 1대
# n명의 사람
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
# 당연히 일찍 끝나는 순서대로 세우면 됨

n = int(input())
p = list(map(int, input().split()))
p.sort()  # 일찍 끝나는 순서대로 정렬

for i in range(1,n):
    p[i] += p[i-1]

print(sum(p))
