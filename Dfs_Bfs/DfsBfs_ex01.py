n, m = map(int, input().split())


def dfs(x, y):  # 좌표를 매개변수로 넣어
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문하지 않은 블럭이면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
