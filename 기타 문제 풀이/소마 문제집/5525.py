# I와 O가 교대로 나오는 문자열 Pn

n = int(input())    # I: n+1개, O: n개, 전체 길이 2n+1
m = int(input())    # s의 길이
s = input()
test = ['I', 'O']
res = 0
for i in range(m - 2*n):
    if s[i] == 'O':
        continue
    flag = True
    for j in range(1, 2*n + 1):
        if s[i+j] != test[j%2]:
            flag = False
            break
    if flag:
        res += 1
print(res)