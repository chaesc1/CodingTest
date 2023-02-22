#숨바꼭질3

#걷기 -> 1초걸림 순간이동 -> 0초

from collections import deque

n,k = map(int,input().split())
arr = [-1] * 100001
result = 0

def bfs(start):
    q = deque()
    q.append(start)
    arr[start] = 0

    while q:
        now = q.popleft()

        if now == k:
            print(arr[k])
            break
        for next in (now*2,now+1,now-1):
            if 0<=next<100001 and arr[next] == -1:
                #순간이동 하는경우 
                if next == now * 2:
                    arr[next] = arr[now]
                    q.appendleft(next)#가중치가 다른경우 두개의 큐를 만들어서 풀어야하는데 그때 appendleft를 사용가능하다.
                #걷는경우
                else:
                    arr[next] = arr[now] + 1
                    q.append(next)


bfs(n)