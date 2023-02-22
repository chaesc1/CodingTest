#숨바꼭질 1

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

        for next in (now*2,now+1,now-1):
            if 0<=next<100001:
                if arr[next] == -1 or arr[next] >= arr[now] + 1:
                    arr[next] = arr[now] + 1
                    q.append(next)

bfs(n)

print(arr[k])