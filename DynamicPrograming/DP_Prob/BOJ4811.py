#알약

#매일 매일 약 반알을 먹는다. 손녀 선영이는 종수 할아버지에게 약이 N개 담긴 병을 선물로 주었다.

dp = [[0]*(31) for _ in range(31)]
for i in range(1,31):
    dp[0][i] = 1 #w개수 

for i in range(1,31):
    for j in range(i,31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])