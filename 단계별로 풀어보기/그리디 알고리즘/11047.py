n,k = map(int, input().split())
coin = []
total = 0
for i in range(n):
    coin.append(int(input()))
coin.reverse()
for i in coin:
    if i <= k:
        count = int(k/i)
        total += count
        k -= count * i
print(total)