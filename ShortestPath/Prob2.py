#전보 문제
#N개의 도시가 있다. 각각의 도시는 보내고자하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메세지를 전송할 수 있다.
#다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.

#하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면
#도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다. 예를 들어 x->y 존재하지만 y->x 앖디면 y-x 로 메세지를 보낼수 없다. 
#또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
#c라는 도시에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.

#입력조건
# 첫째 줄에 도시의 개수 N, 통로의 개수 M , 메세지를 보내고자 하는 도시 C가 주어짐 (1<= N <= 30000, 1 <= M <= 200000, 1<=C<=N)
# 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정부 XYZ가 주어짐
#이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며 메시지가 전달되는 시간이 Z라는 뜻

#출력조건
#첫째줄에 도시C에서 보낸 메세지를받는 도시의 총 개수와 총 걸리는 시간을 공배으로 구분하여 출력

#문제해결
#도시의 수, 통로의 개수가 많다. -> 우선순위큐 사용한 다익스트라 

#문제풀이

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#도시의 개수 통로의 개수 시작하는 도시 입력받아
n,m,start = map(int,input().split())

#정보를 담을 리스트 생성
graph = [[] for i in range(n+1)]
#거리를 담을 테이블 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선에 대한 자료입력
for _ in range(m):
    x,y,z = map(int,input().split())
    #x번 노드에서 y번 노드로 보내는 시간이 z만큼 걸린다.
    graph[x].append((y,z))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        #가장 최단거리가 짧은 노드에 대한 정보를 꺼내
        dist,now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드라면 무시
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
 
dijkstra(start)

#도달 할 수 있는 노드의 개수
count = 0
#도달 할 수 있는 노드중에서 가장 멀리있는 노드와 최단거리
max_distance = 0

for i in distance:
    if i != INF:
        #도달 가능하면?
        count+=1
        max_distance = max(max_distance,i)

#시작노드 제외 -> -1 해줘야해
print(count-1,max_distance)
