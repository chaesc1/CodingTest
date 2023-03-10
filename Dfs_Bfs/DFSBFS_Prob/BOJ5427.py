#불 

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.
# 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)
# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.
# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다.

#출력
# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    w,h = map(int,input().split())
    graph = []
    fire = deque()
    sang = deque()
    visited = [[0] * w for _ in range(h)]#방문표시할 데이터셋
    for j in range(h):
        a = list(input().strip())
        graph.append(a)
        for k in range(w):
            

