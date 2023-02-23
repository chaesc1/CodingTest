#유기농 배추
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0#갉아 먹었으니 배추 없애

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))


for i in range(t):
    cnt = 0
    #가로 길이m, 세로길이 n, 배추가 심어져 있는 위치 개수 k
    n,m,k = map(int,input().split())
    graph = [[0]*(m) for _ in range(n)]

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt += 1
    print(cnt)