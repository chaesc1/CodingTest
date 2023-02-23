#숫자 고르기
#씨발 모르겠다

import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u,visited):
    visited.add(u)
    checked[u] = 1
    for v in graph[u]:
        if v not in visited:
            dfs(v,visited.copy())
        else: #사이클이 생기면
            result.extend(list(visited))
            return
        
n = int(input().strip())
graph = defaultdict(list)

for i in range(1,n+1):
    v = int(input().strip())
    graph[v].append(i)

checked = [0 for _ in range(n+1)]
result = []
for i in range(1,n+1):
    if not checked[i]:
        dfs(i,set([]))

result.sort()
print(len(result))
for x in result:
    print(x)