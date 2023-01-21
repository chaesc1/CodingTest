from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        #네 방향에 대해서 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #좌표 밖이라면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0: #벽이면 무시
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return graph[n-1][m-1]

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))