#Q31 ) 정수삽각형

import sys
input = sys.stdin.readline

n = int(input())

#dp테이블 초기화
dp = [] 
for _ in range(n):
    dp.append(list(map(int,input().split())))

# print(dp)
for i in range(1,n):
    for j in range(i+1):
        #왼쪽 위
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        #바로 위에서
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] += max(up_left,up)

print(max(dp[n-1]))