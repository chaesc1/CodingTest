#적록색약

#적록색약일 경우 R과 G를 같은 색으로 판단해

# 일반 사람이 볼때 구역수 -> r을 g로 바꿔 -> 적록색약 구역 카운트
from collections import deque
import sys 
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #좌표 안에서만 / 같은색 / 방문하지 않은곳 
            if 0<= nx < n and graph[x][y] == graph[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1 #방문표시
                q.append((nx,ny))

#적록색약이 아닌 경우
visited = [[0] * (n) for _ in range(n)]
res1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            res1 += 1
            
#적록색약인 경우 -> 녹색을 적색으로 바꿔
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * (n) for _ in range(n)]
res2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            res2 += 1

print(res1, res2)
