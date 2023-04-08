# 배열은 삽입 / 삭제가 시간복잡도가 O(n)이므로 시간이 오래 걸린다.
"""
n = int(input())

pile = [i+1 for i in range(n)]
for _ in range(n-1):
    pile.pop(0)
    pile.append(pile.pop(0))
print(pile[0])
"""

# Deque를 사용하면 해결

from collections import deque as dq

n = int(input())

# pile = [i for i in range(1, n+1)]
pile = dq(range(1, n+1))

for _ in range(n-1):
    pile.popleft()
    pile.append(pile.popleft())
print(pile[0])