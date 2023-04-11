import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[0]*m for _ in range(n)]
for r in range(n):
    maze[r] = list(input().strip())

# check 배열 생성
check = [[False]*m for _ in range(n)]

"""def validRoute(r, c):
    try:
        if check[r][c] or maze[r][c]==0 or r<0 or c<0:
            return False
        else: 
            return True
    except:
        return False"""
def validCoord(r, c):
    return 0<=r<n and 0<=c<m and maze[r][c]==0 and check[r][c] # return 뒤의 식의 True/False 값을 반환함

def bfs(r, c, depth):
    depth += 1
    check[r][c] = True
    if r==n-1 and c==m-1:
        print(depth)
    else:
        if validCoord(r-1, c):
            bfs(r-1, c, depth)
        if validCoord(r+1, c):
            bfs(r+1, c, depth)
        if validCoord(r, c+1):
            bfs(r, c+1, depth)
        if validCoord(r, c-1):
            bfs(r, c-1, depth)
bfs(0, 0, 0)
