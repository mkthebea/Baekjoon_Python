t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    units = a % 10
    if units == 0:
        print(10)
    elif units in [1, 5, 6]:
        print(units)
    elif units in [4, 9]:
        if b % 2 == 0:
            print((units ** 2) % 10)
        else:
            print(units)
    else:
        if b % 4 == 0:
            print((units ** 4) % 10)
        else:
            print(((units ** (b % 4)) % 10))