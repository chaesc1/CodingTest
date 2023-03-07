#부분수열의 합

import sys
input = sys.stdin.readline

n,s = map(int,input().split())
data = list(map(int,input().split()))

cnt = 0

def solution(depth,sum): 
    global cnt

    if depth >= n: #base case 인덱스가 숫자 개수보다 많으면
        return
    
    sum += data[depth]
    
    if sum == s:
        cnt += 1

    solution(depth+1,sum) #해당수를 포함하는 경우
    solution(depth+1,sum-data[depth]) #해당 수를 포함하지 않는 경우
solution(0,0)
print(cnt)