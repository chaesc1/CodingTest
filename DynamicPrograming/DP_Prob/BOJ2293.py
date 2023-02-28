#동전1

n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

dp[0] = 1 
#인덱스가 0 인것은 1개만 사용했을때를 나타내기
#dp[i] -> i원을 만들 때 가능한 경우의 수
for coins in coin:
    for i in range(1,k+1):
        if i - coins >= 0:
            dp[i] += dp[i-coins]

print(dp[k])