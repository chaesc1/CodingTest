#연결 요소의 개수

#방향이 없는 그래프가 주어졌을 떄 연결 요소의 개수를 구하는 프로그램

#노드의 개수 n , 간선의 개수 m이 주어짐
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        count+=1

print(count)
