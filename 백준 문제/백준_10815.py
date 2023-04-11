import sys

input = sys.stdin.readline

n = int(input())
have = sorted(map(int, input().split()))
m = int(input())
ints = map(int, input().split())

def bsearch(num):
    top = len(have)-1
    mid = len(have)//2
    down = 0
    while top-down!=1 and top-down!=0:
        if num > have[mid]:
            down = mid
            mid = (top+down+1)//2
        elif num < have[mid]:
            top = mid
            mid = (top+down+1)//2
        else:
            return 1
    if num==have[top] or num==have[down]:
        return 1
    else:
        return 0

for num in ints:
    print(bsearch(num), end=" ")