num=[]
for _ in range(5):
    num.append(int(input()))
num.sort()
print(int(sum(num)/5))
print(num[2])