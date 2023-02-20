#연산자 끼워 넣기
#첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. 
#(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

n = int(input())
data = list(map(int,input().split()))
#(+,-,*,//)
add,sub,mul,div = map(int,input().split())

#최대 최솟값 초기화
min_val = 1e9
max_val = -1e9

def dfs(depth,now):
    global min_val,max_val
    global add,sub,mul,div

    if depth == n:
        max_val = max(max_val,now)
        min_val = min(min_val,now)
    else:
        if add > 0:
            add -= 1
            dfs(depth+1,now+data[depth])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(depth+1,now-data[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(depth+1,now*data[depth])
            mul += 1
        if div > 0:
            div -= 1
            dfs(depth+1,int(now/data[depth]))
            div += 1

dfs(1,data[0])
print(max_val)
print(min_val)