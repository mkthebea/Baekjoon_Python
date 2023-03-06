def sol(n, x, y):
    global cnt, r, c
    if n == 1:
        dx = [0, 0, 1, 1]
        dy = [0, 1, 0, 1]
        for i in range(4):
            if x+dx[i] == r and y+dy[i] == c:
                print(cnt)
                exit()
            cnt += 1
    else:
        dx = [0, 0, n//2, n//2]
        dy = [0, n//2, 0, n//2]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx <= r < nx + n//2 and ny <= c < ny + n//2:
                sol(n//2, nx, ny)
            else:
                cnt += (n//2)**2

n, r, c = map(int, input().split())
cnt = 0
sol(2**n, 0, 0)