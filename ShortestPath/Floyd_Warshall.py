# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.

INF = int(1e9)

n = int(input())
m = int(input())
#2차원 리스트만들고 모든값을 INF로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에게 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    #a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int,input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행 min(AB , Ak + KB)
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행된 결과를 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        #도달 할 수 없는 경우, 무한 출력
        if graph[i][j] == INF:
            print("INF")
        else:
            print(graph[i][j],end=" ")
    print()