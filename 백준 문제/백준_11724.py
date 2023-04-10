import sys
"""재귀 제한을 풀어주어야 함"""
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# n은 노드 개수, m은 간선 개수
n, m = map(int, input().split())

tree = [[0] * n for _ in range(n)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a][b] = tree[b][a] = 1

"""확인용 배열을 생성"""
chk = [False] * n

def dfs(i):
    for x in range(n):
        if tree[i][x] and not chk[x]:
            chk[x] = True
            dfs(x)

for i in range(n):
    if not chk[i]:
        chk[i]==True
        dfs(i)
        cnt += 1

print(cnt)