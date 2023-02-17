#특정 거리의 도시 찾기 (백준 18352)

#문제 
#어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
#이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
#예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
#1 -> 2, 1->3 , 2->3 , 2->4
#1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

#도시개수N,도로개수M,최단거리 K,출발도시 X
from collections import deque
import sys

f = sys.stdin.readline
n,m,k,x = map(int,f().split())
graph = [[] for _ in range(n+1)] #그래프 초기화

for _ in range(m):
    a,b = map(int,f().split())
    graph[a].append(b) #a에서b로 가는 단방향 그래프

distance = [-1] * (n+1)
distance[x] = 0 #시작 지점의 거리는 0으로 초기화

#Bfs 
q = deque([x])

while q:
    now = q.popleft()#현재 도시 꺼내
    for next in graph[now]:
        #방문하지 않은 도시라면? -1이라면?
        if distance[next] == -1:
            distance[next] = distance[now] + 1#최단거리 갱신
            q.append(next)

#최단거리가 k인 도시를 오름차순으로 출력해야해.
#없다면 -1출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)