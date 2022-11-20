n = int(input())
a = list(map(int, input().split()))
left = [0] * n
left[0] = 1
for i in range(1, n):
    tem = a[0:i]
    # a[i] > a[j]인 j에 대해 left[j]들을 모아놓은 리스트 필요
    smaller = [left[j] for j in range(i) if a[j] < a[i]]
    if len(smaller) == 0:
        left[i] = 1
    else:
        left[i] = max(smaller) + 1

right = [0] * n
right[-1] = 1
for i in range(n-2, -1, -1):
    tem = a[i+1:n]
    # a[i] > a[j]인 j에 대해 right[j]들을 모아놓은 리스트 필요
    smaller = [right[j] for j in range(i+1, n) if a[j] < a[i]]
    if len(smaller) == 0:
        right[i] = 1
    else:
        right[i] = max(smaller) + 1

res = [0] * n
for i in range(n):
    res[i] = left[i] + right[i]
print(max(res) - 1)