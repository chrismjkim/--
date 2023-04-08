import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)
cnt = 0
for p in coin:
    cnt += k//p
    k -= (k//p)*p
print(cnt)