n = int(input())
files =[input() for _ in range(n)]
pattern = ''
for i in range(len(files[0])):
    tem = files[0][i]
    flag = True
    for j in range(n):
        if tem != files[j][i]:
            flag = False
            break
    if flag:
        pattern += tem
    else:
        pattern += '?'
print(pattern)