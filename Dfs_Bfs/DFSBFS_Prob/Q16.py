#연구소 

#연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 
#직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
#연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

#0은 빈칸 1은 벽 2는 바이러스가 있는곳

#입력조건
#첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
#둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#빈 칸의 개수는 3개 이상이다.

#행 N 열 M
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = [] #처음맵 정보
final = [[0] * (m) for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

#동 남 서 북 방향벡터
dx = [1,0,-1,0]
dy = [0,-1,0,1]

result = 0
#바이러스 퍼지는 함수
def spread(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #바이러스가 퍼질수있는 조건
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if final[nx][ny] == 0:
                final[nx][ny] = 2
                spread(nx,ny)

#안전영역 계산하는 함수
def countArea():
    count = 0
    for i in range(n):
        for j in range(m):
            if final[i][j] == 0:
                count+=1
    return count

#메인(울타리 설치하면서 안전지역 계산)
def solution(count):#울타리 수를 매개변수로
    global result
    
    if count == 3: #울타리 3개 -> 바이러스 전파->안전지역 계산

        for i in range(n):
            for j in range(m):
                final[i][j] = data[i][j]
        #바이러스 전파
        for i in range(n):
            for j in range(m):
                if final[i][j] == 2:
                    spread(i,j)
        #안전영역 계산
        result = max(result,countArea())
        return
    
    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                solution(count)
                data[i][j] = 0
                count -= 1
            
solution(0)
print(result)