# nC1 * mC1 -1 = n * m - 1 (n,m: 그 종류에 해당하는 옷 가지수)
# 옷 종류가 하나라면 가지수 = 경우의 수

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        clothes.append(input().split()[1])
    cloth_set = set(clothes)
    if(len(cloth_set) == 1):
        print(len(clothes))
    else:
        count = [1 for _ in range(len(cloth_set))]
        index = 0
        for c in cloth_set:
            for i in clothes:
                if(i == c):
                    count[index] += 1
            index += 1
        res = 1
        for n in count:
            res *= n
        print(res - 1)