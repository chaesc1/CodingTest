#동전 2

n,k = map(int,input().split())
coins  = [int(input()) for _ in range(n)]

dp = [1e9] * (k+1)
dp[0] = 0 #0원을 만드는데 필요한 동전수는 0 이다.

for c in coins:
    for i in range(c,k+1):
        if dp[i] > 0:
            dp[i] = min(dp[i],dp[i-c]+1)

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])