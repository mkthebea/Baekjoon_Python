import math
n = math.factorial(int(input()))
count = 0
while(True):
    if(n % 10 != 0):
        break
    count += 1
    n //= 10
print(count)