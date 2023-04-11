"""import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
n = int(input())
money = sorted(map(int, input().split()))
budget = int(input())
if sum(money)<=budget:
    print(money[-1])
else:
    avg = budget//n
    cheaps = 0
    for i in range(bisect_left(money, avg)):
        cheaps += avg - money[i]

    print(avg + (cheaps + budget%n)//(len(money)-bisect_right(money, avg)))"""

# Parametric Search를 이용해서 찾자
n = int(input())
money = sorted(map(int, input().split()))
budget = int(input())

cap = money[-1]
low = 0
piv = (cap+low)//2

def aff(piv):
    return sum(min(m, piv) for m in money)<=budget

while low<piv:
    if aff(piv):
        low = piv
        piv = (piv+cap+1)//2
    else:
        cap = piv
        piv = (piv+low)//2
print(piv)
