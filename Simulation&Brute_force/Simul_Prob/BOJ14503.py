#로봇 청소기

#1.현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
#2.현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
# 1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
#3.현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
# 1 반시계 방향으로 90^\circ$ 회전한다.
# 2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3 1번으로 돌아간다.

n,m = map(int,input().split())#방크기 n x m
r,c,d = map(int,input().split()) #청소기가 놓여있는 좌표 (r,c) 와 바라보고 있는 방향 ( # $0$인 경우 북쪽, # $1$인 경우 동쪽, # $2$인 경우 남쪽, # $3$인 경우 서쪽을 바라보고 있는 것이다.)

#반시계로 회전하기 때문에 0 3 2 1 순 북 서 남 동
dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph = []
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

#첫시작 지점은 방문처리 
visited[r][c] = 1
cnt = 0

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1

    flag = False
    for _ in range(4):
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

    #범위 안에 있고,벽이 아니고, 청소 가능하다면?
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            r = nx
            c = ny
            flag = True#청소 했다 표시.
            break
    
    if flag == False:
        #후진가능하면 1번으로 . 아니면 종료
        nx = r - dx[d]
        ny = c - dy[d]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 1:
                break
            else:
                r = nx
                c = ny
        else:
            break
print(cnt)

