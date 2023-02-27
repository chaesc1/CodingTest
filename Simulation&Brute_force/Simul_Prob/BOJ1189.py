#컴백홈

#첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다. 
#두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.
#[r-1][0] -> [0][c-1]
from collections import deque
import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
graph = [list(input()) for _ in range(r)]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,K):
    global answer
    if k == K:
        if x == 0 and y == (c-1): #도착지점이면
            answer+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] != 'T':
            graph[nx][ny] = 'T' #방문표시
            dfs(nx,ny,K+1)
            graph[nx][ny] = '.'#다시 초기화

#시작 지점 방문표시
graph[r-1][0] = 'T'
dfs(r-1,0,1)
print(answer)

