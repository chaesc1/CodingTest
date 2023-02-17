#문제 
#그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다
from collections import deque
import sys

input = sys.stdin.readline

#정점 개수 n, 간선의 개수 m, 탐색 시작 정점번호 v
n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

#양방향 그래프 연결
for _ in range(m):
    m1,m2 = map(int,input().split())
    graph[m1][m2] = graph[m2][m1] = 1

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dfs = []
bfs = []

def bfs(start):
    q = deque([start])
    visited1[start] = True

    while q:
        start = q.popleft()
        print(start,end=" ")
        for i in range(1,n+1):
            if not visited1[i] and graph[start][i]: #방문하지 않았거나 , Start와 연결되어 있다면?
                q.append(i)
                visited1[i] = True

def dfs(start):
    visited2[start] = True
    print(start,end=' ')

    for i in range(1,n+1):
            if not visited2[i] and graph[start][i]: #방문하지 않았거나 , Start와 연결되어 있다면?
                dfs(i)
dfs(v)
print()
bfs(v)
