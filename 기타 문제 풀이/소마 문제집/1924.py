day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())
cnt = y
if x > 1:
    for i in range(1, x):
        if i == 2:
            cnt += 28
        elif i == 4 or i == 6 or i == 9 or i == 11:
            cnt += 30
        else:
            cnt += 31
print(day[cnt % 7])