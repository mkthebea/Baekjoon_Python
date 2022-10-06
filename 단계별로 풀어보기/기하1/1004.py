t = int(input())    #테스트 케이스의 개수
result = []

for i in range(t):
    xs, ys, xe, ye = list(map(int, input().split()))

    n = int(input())    #행성계의 개수
    count = 0
    for j in range(n):
        xc, yc, r = list(map(int, input().split()))
        difStart = (xs - xc) ** 2 + (ys - yc) ** 2
        difEnd = (xe - xc) ** 2 + (ye - yc) ** 2
        if (difStart < r ** 2 or difEnd < r ** 2):
            count += 1
        if (difStart < r ** 2 and difEnd < r ** 2):
            count -= 1
    result.append(count)

for i in result:
    print(i)
