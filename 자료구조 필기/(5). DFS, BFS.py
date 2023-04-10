# DFS (깊이 우선 탐색)
"""
- 모든 노드를 살펴보게 되는 완전탐색 알고리즘임
- stack 또는 재귀함수를 이용해 구현
- 진행할 수 있는 정점이 없으면 회귀하는 방식
"""

"""<<코드 구현>>"""
# 배열 정의
adj = [[0] * 13 for _ in range(13)]
# 간선 연결 ex) 0->1, 0->7 간선 연결
adj[0][1] = adj[0][7] = 1 

def dfs(now): #now: 현재 방문한 노드 번호
    for nxt in range(13):
        if adj[now][nxt]: #현재 노드에서 다음 노드로 이어지는 간선이 존재하는가?
            dfs(nxt) # 다음 노드 번호 탐색

dfs(0) # 0번(루트정점)에서 시작해 함수 호출

# BFS (너비 우선 탐색)
"""
- 마찬가지로 완전탐색
- queue를 사용해서 구현
- 모든 다음 정점을 탐색한 후에 다음 정점으로 진행
- 큐에 루트 정점에서 갈 수 있는 노드 대기 -> pop
"""

from collections import deque as dq

def bfs():
    list = dq()
    list.append(0)
    while list:
        now = list.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                list.append(nxt)

# DFS와 BFS의 공통점, 차이점
"""
<공통점>
두 알고리즘 모두 그래프 탐색 완전 알고리즘이다

<차이점>
두 노드 사이의 최단거리를 찾는 데에는 BFS가 유리하다
"""

# 인접행렬과 인접리스트의 시간복잡도
"""
인접행렬: O(V^2)
인접리스트: O(V + E)
"""