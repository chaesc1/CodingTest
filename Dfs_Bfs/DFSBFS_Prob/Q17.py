#경쟁적 전염

#번호가 낮은 종류의 바이러스부터 먼저 증식
#증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다
#S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성
#만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다

#bfs를 써야할거같은 느낌
from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        #해당 지역에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))

#낮은 번호 순으로 정렬
data.sort()
q = deque(data)

#시간,x,y 좌표 입력받어

t_s,t_x,t_y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus,time,x,y = q.popleft()

    if time == t_s:
        break
    
    #현재 위치에서 4방향 검사
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            #방문하지 않은 곳이라면 ? 바이러스 전염
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,time+1,nx,ny))

print(graph[t_x - 1][t_y - 1])
