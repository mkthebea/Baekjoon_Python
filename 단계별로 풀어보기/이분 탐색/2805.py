import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
max_height = max(tree)

start, end, mid = 0, max_height, 0
height = 0
while start <= end:
    mid = (start + end) // 2
    cut_tree = 0
    for t in tree:
        if t > mid:
            cut_tree += t - mid
        if cut_tree >= m:
            break
    if cut_tree >= m:
        height = mid
        start = mid + 1
    else:
        end = mid - 1
print(height)
