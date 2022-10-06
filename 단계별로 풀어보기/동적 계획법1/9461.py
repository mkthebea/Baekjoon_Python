# P(N) = P(N-1) + P(N-5)

padovan = []

def findP(n):
    for i in range(n):
        if (i < 3):
            padovan.append(1)
        elif (i < 5):
            padovan.append(2)
        else:
            padovan.append(padovan[i-1] + padovan[i-5])

case = input()
cases = []
for i in range(int(case)):
    cases.append(int(input()))
findP(max(cases) + 1)
for i in cases:
    print(padovan[i - 1])