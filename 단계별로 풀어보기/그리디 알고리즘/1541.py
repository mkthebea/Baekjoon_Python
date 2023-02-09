# 괄호를 쳐서 식의 값을 최소로
# 마이너스가 나오면 다음 마이너스 전까지 모두 괄호로 묶어서 더하기

exp = input().split('-')
res = sum(map(int, exp.pop(0).split('+')))
for str in exp:
    res -= sum(map(int, str.split('+')))
print(res)