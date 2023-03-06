#주난의 난

#입력
# 첫째 줄에 주난이가 위치한 교실의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 300)
# 둘째 줄에 주난이의 위치 x1, y1과 범인의 위치 x2, y2가 주어진다. (1 ≤ x1, x2 ≤ N, 1 ≤ y1, y2 ≤ M)
# 이후 N×M 크기의 교실 정보가 주어진다. 
#0은 빈 공간, 1은 친구, *는 주난, #는 범인을 뜻한다.
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(str,input().rstrip())))

visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #좌표 안에서,방문하지 않은곳
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                if graph[nx][ny] == "1" or graph[nx][ny] == "#":
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif graph[nx][ny] == "0":
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))

bfs(x1-1,y1-1)
print(visited[x2-1][y2-1])
