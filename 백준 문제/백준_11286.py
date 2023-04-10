"""
import heapq as hq

n = int(input())
arr = []
hq.heapify(arr)

for _ in range(n):
    x = int(input())
    if x==0:
        # 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거
        
        # 비어있으면 0 출력
        if not arr:
            print("0")
    else:
        # 배열에 정수를 넣는다
        hq.heappush(arr, x)
"""


"""
문제 해결 아이디어: 힙은 튜플 안에 인덱스 번호에 따라 순차적 소팅을 한다.
when you save a set of tuples in a heap, the heap will sort the tuples by comparing their elements 
in a "lexicographic" order, which means that it will first compare the elements at the 0th index of the tuples, 
and if they are equal, it will move on to compare the elements at the 1st index, and so on.
This behavior is because when a tuple is inserted into the heap, the heap considers the first element of the tuple 
as the "priority" or "key" for sorting purposes. In the case where two tuples have the same first element, 
the heap will compare the second elements of the tuples to determine their relative order.
"""
import heapq as hq
import sys

input = sys.stdin.readline
arr = []
hq.heapify(arr)
for _ in range(int(input())):   
    x = int(input())
    if x==0:
        print(hq.heappop(arr)[1]) if arr else print("0")
    else:
        hq.heappush(arr, (abs(x), x))
