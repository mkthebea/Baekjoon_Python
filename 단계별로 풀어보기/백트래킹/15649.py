n, m = map(int, input().split())

# nCm 구하기
ncm = []
for i in range(1,n+1):
    tem = list(range(i,i+m))
    ncm.append(tem)
    # for j in range(1,m+1):
    #     tem = list(range(i,i+j))
    #     ncm.append(tem)

print(ncm)


# print(list(range(1, n + 1)))