import sys

input = sys.stdin.readline

n, l = map(int, input().split())

leak = sorted([i for i in map(int, input().split())])
cnt = 0

while leak:
    temp = leak[0]
    while(leak[0] <= temp+l-1):
        leak.pop(0)
        if not leak:
            break
    cnt += 1

print(cnt)