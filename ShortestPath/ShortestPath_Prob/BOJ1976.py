#여행가자
#union_find 문제로 1717번 풀어보고 오자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,n+1):
    parent[i] = i

for i in range(1,n+1):
    graph = list(map(int,input().split()))  
    #현재 도시와 연결이 되어있는지 확인
    for j in range(1,len(graph)+1):
        if graph[j-1] == 1:
            union(i,j)
        
#여행계획
tour = list(map(int,input().split()))
res = set([find(i) for i in tour])

if len(res) == 1:
    print('YES')
else:
    print('NO')
