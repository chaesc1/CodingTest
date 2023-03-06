#녹색 옷 입은 애가 젤다지?

#입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다. (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다.
# 이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어진다. 
# 도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻이다. 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수다.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  

dx = [-1,1,0,0]
dy = [0,0,-1,1]


count = 0
while True:
    count+=1
    n = int(input())

    if n == 0:
        break
    #정보를 담을 리스트
    graph = []
    #거리를 담을 테이블 무한으로 초기화
    distance = [[False] * n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int,input().split())))

    hq = []
    heapq.heappush(hq,(graph[0][0],0,0))#잃은돈,좌표 삽입
    distance[0][0] = 0

    while hq:
        cost,x,y = heapq.heappop(hq)
        #출력
        if x == n-1 and y == n-1:
            print(f'Problem {count}: {cost}')
            break
        #상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and distance[nx][ny] == False:
                distance[nx][ny] = True
                heapq.heappush(hq,(cost + graph[nx][ny],nx,ny))

