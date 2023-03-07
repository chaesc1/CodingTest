#부등호

#첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다. 

import sys
input = sys.stdin.readline

k = int(input())
A = list(input().split())#부등호 배열
visited = [0] * 10 # 0 - 9 까지 중복없이 넣기위해.

max_ans = ""
min_ans = ""

def check(x,y,sign): #비교할 수 x,y/ 부등호 sign
    if sign == '<':
        return x < y
    else:
        return x > y

def backtracking(depth,num):
    global max_ans,min_ans

    if depth == k+1:
        if len(min_ans) == 0:
            min_ans = num
        else:
            max_ans = num
        return
    
    for i in range(10):
        if visited[i] == 0:
            if depth == 0 or check(num[-1],str(i),A[depth-1]):
                visited[i] = True
                backtracking(depth+1,num+str(i))
                visited[i] = False

backtracking(0,"")

print(max_ans)
print(min_ans)