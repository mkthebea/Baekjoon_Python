# python3으로 제출하면 시간 초과, pypy3으로 제출

def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)

def fibo_dynamic(n):
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    count = 0
    for i in range(2, n):
        count += 1
        f[i] = f[i - 1] + f[1 - 2]
    return count

n = int(input())
print(fibo_recursive(n), fibo_dynamic(n))
