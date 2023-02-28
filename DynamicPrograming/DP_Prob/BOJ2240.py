#자두나무

import sys
input = sys.stdin.readline

t,w = map(int,input().split())

arr = [0]
d = [[0]*(w+1) for _ in range(t+1)]

for i in range(t+1):
    #1번 나무에서 움직이지 않은 경우

    #1번 나무에서 자두가 떨어지면
    if arr[i] == 1:
        d[i][0] = d[i-1][0] + 1
    else:
        d[i][0] = d[i-1][0]
    
    #한번이상 움직이는 것에대해서 탐색
    for j in range(1,w+1):
        #1번
        if j % 2 == 0 and arr[i] -- 1:
            