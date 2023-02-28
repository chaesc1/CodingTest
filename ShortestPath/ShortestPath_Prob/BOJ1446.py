#지름길

#문제

#첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다
#음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다
#지름길의 시작 위치는 도착 위치보다 작다.
import heapq
import sys
input = sys.stdin.readline

n,d = map(int,input().split())
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1,1))
for _ in range(n):
    start,end,length = map(int,input().split())
    if end > d:
        continue
    graph[start].append((end,length))

INF = int(1e9)
distance = [INF] * (d+1)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        #현재 힙큐에서 뺀것이 now 까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(0)
print(distance[d])

