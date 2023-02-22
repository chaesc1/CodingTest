#숨바꼭질2

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때,
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고,
# 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
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
            
        for next in (x*2,x+1,x-1):#큐가 빌때까지 반복
            if 0<=next<100001 and (arr[next] == -1 or arr[next] == arr[x] + 1):
                arr[next] = arr[x] + 1
                q.append(next)

n,k = map(int,input().split())
arr = [-1] * 100001
result = 0

bfs(n)

print(arr[k])
print(result)
