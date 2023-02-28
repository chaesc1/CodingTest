#RGB거리

#규칙
#1.1번 집의 색은 2번 집의 색과 같지 않아야 한다
#2.N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
#3.i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

#입력
#첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
#둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
#집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

import sys
input = sys.stdin.readline

n = int(input())
color = []

for i in range(n):
    color.append(list(map(int,input().split())))
for i in range(1,len(color)):
    
    #빨간집
    color[i][0] = min(color[i-1][1],color[i-1][2]) + color[i][0]    
    #녹색집
    color[i][1] = min(color[i-1][0],color[i-1][2]) + color[i][1]
    #파란집
    color[i][2] = min(color[i-1][0],color[i-1][1]) + color[i][2]
    #print(color[i][0],color[i][1],color[i][2]) #총 합.

print(min(color[n-1][0],color[n-1][1],color[n-1][2]))
