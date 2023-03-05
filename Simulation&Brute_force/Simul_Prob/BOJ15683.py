# #감시
import copy
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
cctv = []
for i in range(n):
    graph.append(list(map(int,input().split())))



#북 동 남 서 
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

answer = 1e9#사각지대의 개수

dir = {
    1 :[[0], [1], [2], [3]],
    2:[[0, 2], [1, 3]],
    3:[[0, 1], [1, 2], [2, 3], [0, 3]],
    4:[[0, 1, 2], [1, 2, 3], [2,3,0], [3,0,1]],
    5:[[0, 1, 2, 3]],
}#cctv 1-5 번 의 방향

def watch(x,y,dir,temp):
    for d in dir:
        nx = x
        ny = y

        #이동 가능할때까지 #으로 바꿔서 반복
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 6:
                    break
                elif temp[nx][ny] == 0:
                    temp[nx][ny] = "#"
            else:
                break

def dfs(depth,graph):
    global answer
    tmp = copy.deepcopy(graph)
    #종료조건 모든 시시티비를 탐색 끝냈을때.
    if depth == cctv_cnt:
        cnt = 0 #빈칸 개수
        for i in range(n):
            cnt += tmp[i].count(0)
        answer = min(answer,cnt) #사각지대의 최소크기 구함
        return
    
    x,y,cctvlist = cctv[depth]
    #해당하는 cctv종류의 방향으로 탐색을 시작한다.
    for d in dir[cctvlist]:
        watch(x,y,d,tmp)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(graph)


cctv_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([i,j,graph[i][j]]) #cctv의 x, y좌표, cctv의 종류
            cctv_cnt+=1
dfs(0,graph)
print(answer)

# from copy import deepcopy
# import sys
# input = sys.stdin.readline
# def fill(x, y, arr, d):
#     for i in d:
#         nx, ny = x, y
#         while True:
#             nx += dx[i]
#             ny += dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if arr[nx][ny] == 6:
#                     break
#                 elif arr[nx][ny] == 0:
#                     arr[nx][ny] = "#"
#             else:
#                 break
# def dfs(arr, cnt):
#     global result
#     temp = deepcopy(arr)
#     if cnt == cctv_cnt:
#         num = 0
#         for i in range(n):
#             num += temp[i].count(0)
#         result = min(result, num)
#         return
#     x, y, cctv = q[cnt]
#     for i in direction[cctv]:
#         fill(x, y, temp, i)
#         dfs(temp, cnt + 1)
#         temp = deepcopy(arr)
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# direction = [[], 
#             [[0], [1], [2], [3]],
#             [[0, 1], [2, 3]], 
#             [[3, 0], [0, 2], [2, 1], [1, 3]],
#             [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
# n, m = map(int, input().split())
# s = []
# q = []
# cctv_cnt = 0
# result = 100000000
# for i in range(n):
#     a = list(map(int, input().split()))
#     s.append(a)
#     for j in range(len(a)):
#         if a[j] != 0 and a[j] != 6:
#             q.append([i, j, a[j]])
#             cctv_cnt += 1
# dfs(s, 0)
# print(result)