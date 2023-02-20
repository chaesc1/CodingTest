#인구이동 백준 16234

#문제
#N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
#r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 
#모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다

#인구 이동의 규칙 / 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속
#1.국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
#2.위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
#3.국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
#4.연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
#5.연합을 해체하고, 모든 국경선을 닫는다.

#인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성
from collections import deque

n,l,r = map(int,input().split())

#나라 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def process(x,y,index):
    united = [] #연합된 나라
    united.append((x,y))

    q = deque()
    q.append((x,y))

    visited[x][y] = index #현재 연합의 번호를 할당
    population  = graph[x][y]
    count = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    #연합에 추가
                    visited[nx][ny] = index
                    population += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
            
    for i,j in united:
        graph[i][j] = population // count


total_count = 0

#더이상 움직일 수 없을때 까지 반복
while True:
    visited = [[-1] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1: #아직 방문하지 않은 나라면?
                process(i,j,index)
                index += 1
    
    if (index == n*n):#모든 인구 이동이 끝난 경우
        break
    total_count += 1

print(total_count)

