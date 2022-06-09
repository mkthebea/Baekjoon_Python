# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오

# 1) 1부터 n까지의 한수를 하나하나 찾기. 자릿수로 분리해서 차이가 동일한지 확인. 


s = []
def finds(n):
    for i in range(1, int(n) + 1):
        x = list(map(int, str(i)))[1:]
        y = list(map(int, str(i)))[:-1]
        gap = set(map(lambda x,y:x-y, x, y))
        if len(gap) == 1 or len(gap) == 0:
            s.append(i)
n = input()
finds(n)
print(len(s))
