n = int(input())
a = list(map(int, input().split()))
left = [0] * n
left[0] = 1
for i in range(1, n):
    smaller = list(filter(lambda x : x < a[i], a[0:i]))
    if len(smaller) == 0:
        left[i] = 1
    else:
        left[i] = max(smaller) + 1

right = [0] * n
right[-1] = 1
for i in range(n-2, -1, -1):
    smaller = list(filter(lambda x : x < a[i], a[i + 1:n]))
    if len(smaller) == 0:
        right[i] = 1
    else:
        right[i] = max(smaller) + 1
res = [0] * n
for i in range(n):
    res[i] = left[i] + right[i]
print(max(res) - 1)