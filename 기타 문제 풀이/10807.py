input()
nums = input().split()
v = input()
print(len(list(filter(lambda n: n == v, nums))))