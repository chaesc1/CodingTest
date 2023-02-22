#Q34 병사 배치하기
#최장증가수열 문제 -> 연습하고 공부하자

n = int(input())
array = list(map(int,input().split()))
dp = [1] * (n)

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))