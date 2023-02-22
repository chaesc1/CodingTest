#Q33 - 퇴사

n = int(input())
t = []#시간을 담을 배열
p = []#금액을 담을 배열
dp = [0] * (n+1)
max_val = 0

for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

for i in range(n-1,-1,-1):#맨뒤에서부터 거꾸로 
    time = t[i] + i 

    #시간내에 가능하면?
    if time <= n:
        dp[i] = max(p[i] + dp[time],max_val)
        max_val = dp[i]
    else:
        #기간을 벗어나면
        dp[i] = max_val

print(max_val)