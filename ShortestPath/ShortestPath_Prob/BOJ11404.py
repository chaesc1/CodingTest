#플로이드 Q37

import sys
input = sys.stdin.readline

INF = 1e9
#노드 = 도시. 간선 = 버스
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신으로 가는 버스 = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

#간선 정보 갱신
for _ in range(m):
    a,b,c = map(int,input().split())
    #해당 지역으로 가는 길 중에 가장 짧은 것만 저장
    if graph[a][b] > c:
        graph[a][b] = c

#플로이드워셜 알고리즘 점화식 적용
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

#수행된 결과 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()