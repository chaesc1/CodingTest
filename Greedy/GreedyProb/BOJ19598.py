#최소 회의실 배정

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

data.sort()

cnt = 1
room = [0]
#힙에 있는 현재 시간이 data의 시작시간보다 빠르면 꺼내고data의 end 시간을 집어 넣는다.
for start,end in data:
    if start >= room[0]:
        hq.heappop(room)
    else:
        cnt += 1
    hq.heappush(room,end)
print(cnt)