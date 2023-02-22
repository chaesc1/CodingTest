#숨바꼭질4

from collections import deque

def bfs(start):
    global result
    q = deque()
    q.append(start)
    arr[start] = 0

    while q:
        x = q.popleft()

        if x == k:
            result += 1
            print(arr[k])
        
            continue
            
        for next in (x*2,x+1,x-1):#큐가 빌때까지 반복
            if 0<=next<100001 and (arr[next] == -1 or arr[next] == arr[x] + 1):
                arr[next] = arr[x] + 1
                q.append(next)
                

n,k = map(int,input().split())
arr = [-1] * 100001
move = [-1] * 100001
result = 0

bfs(n)
