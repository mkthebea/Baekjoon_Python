import sys
input = sys.stdin.readline

m = int(input())
S = set()
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        c, n = cmd[0], int(cmd[1])
        if c == 'add':
            S.add(n)
        elif c == 'remove':
            S.discard(n)
        elif c == 'toggle':
            if n in S:
                S.remove(n)
            else:
                S.add(n)
        elif c == 'check':
            if n in S:
                print(1)
            else:
                print(0)