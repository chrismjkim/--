# <기본 입출력 함수>
"""
map(int, input().split())
"""

# <빠른 입출력 함수>
"""
import sys
for _ in range(100000):
    n = int(sys.stdin.readline())
"""

# <배열>
"""
삽입, 삭제: O(N)
탐색: O(1)
"""

# 벡터(동적배열)
"""
삽입, 삭제: O(N)
탐색: O(1)
파이썬의 list는 기본적으로 동적배열
"""

# 연결 리스트(Linked List): PS에서는 자주 안 쓰임
"""
삽입, 삭제: O(1)
탐색: O(N)
"""

# 스택(Stack)
"""
선입후출(FILO)인 자료구조
파이썬에서는 리스트로 구현
"""
# 스택에서의 후입선출 구현
"""
s = []
for i in range(5):
    s.append[n]
s.pop(-1)
"""

# 큐(Queue)
"""
삽입, 삭제: O(1)

from collections import deque as dq
dq.append(): 선입
dq.popleft(): 선출
"""

# 힙, 우선순위 큐(Heap, Priority Queue)
"""
완전이진트리 형태의 자료

삽입, 삭제: O(log2_N)

루트 정점(root node): 최상단 노드 , 인덱스 0

import heapq as hq

pq = []
hq.heappush(pq, 456): 자료 추가(배치는 알아서)
hq.heappop(): 자료 삭제
"""

# 맵(Map), 딕셔너리(Dictionary)
"""
C++에서 Map은 red-black tree로, 파이썬에서 Dictionary는 hash로 구성

키(Key)와 값(Value)를 갖는 자료구조(예: JSON)

Key는 유일, Value는 중복 가능

삽입, 삭제: Map은 O(logN), Dictionary는 O(1)

{}로 정의

"""

# 집합(Set)
"""
원소끼리 중복 X
삽입, 삭제: C++는 O(logN), 파이썬은 O(1)
s = set()
s.add(10): 10이라는 원소 추가
s.remove(10): 10이라는 원소 삭제
s.clear(): 모든 원소 삭제
"""


# 예제문제 1
"""백준 9012번, 스택 이용"""

for _ in range(int(input())):
    stk = []
    isVPS = True
    for pr in input():
        if pr=='(':
            stk.append(pr)

        else:
            if stk:
                stk.pop(-1)
            else:
                isVPS = False
                break
    if stk:
        isVPS = False
    print("YES" if isVPS else "NO")
        