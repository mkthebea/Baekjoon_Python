num = [i for i in range(1, 31)]
for _ in range(28):
    num.remove(int(input()))
print(num[0])
print(num[1])