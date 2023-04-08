import sys

input = sys.stdin.readline
dw = []
for _ in range(9):
    dw.append(int(input()))

sum = 0
for h in dw:
    sum += h
    
for i in range(len(dw)):
    for j in range(i+1,len(dw)):
        if sum-dw[i]-dw[j]==100:
            a, b = dw[i], dw[j]
            dw.remove(a)
            dw.remove(b)
            dw = sorted(dw)
            break
    if len(dw)==7:
        break

for x in range(7):
    print(dw[x])