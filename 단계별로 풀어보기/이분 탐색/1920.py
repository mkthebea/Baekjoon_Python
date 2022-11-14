def binary_search(start, end, arr, finding):
    if start > end:
        return 0
    mid = int((start + end)/2)
    if arr[mid] == finding:
        return 1
    elif arr[mid] > finding:
        return binary_search(start, mid - 1, arr, finding)
    else:
        return binary_search(mid + 1, end, arr, finding)
        
n = int(input())
num = list(map(int, input().split()))
num.sort()
m = int(input())
finding = list(map(int, input().split()))
for i in range(m):
    finding[i] = binary_search(0, n-1, num, finding[i])
print('\n'.join(list(map(str,finding))))