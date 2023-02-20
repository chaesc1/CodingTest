#감시 피하기

#위치 값을 나타낼 때는 (행,열)의 형태

#입력조건
#첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6) 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다. 
#각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다. 
#해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.

#출력조건
#첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다.
# 모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.

# import sys
# input = sys.stdin.readline

# n = int(input()) #복도의 크기
# data = [] #복도의 정보
# wall = [] #빈 공간 정보
# teacher = [] #선생님 정보

# result = "NO"

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# for i in range(n):
#     data.append(list(map(str,input().split())))
#     for j in range(n):
#         if data[i][j] == 'T':
#             teacher.append((i,j))

# def check():
#     global data,teacher

#     for t in teacher:
#         for i in range(4):
#             x,y = t
#             while 0<= x < n and 0 <= y < n:
#                 if data[x][y] == 'O': #장애물이면
#                     break
#                 elif data[x][y] == 'S':#학생이면
#                     return False
                
#             x += dx[i]
#             y += dy[i]
#     return True

# def dfs(count):
#     global data,wall,teacher,result

#     if count > 3:
#         return
#     if count == 3:
#         if check() is True:
#             result = "YES"
#             return
#         else:
#             result = "NO"
    
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 'X':
#                 data[i][j] = 'O'#벽세워
#                 wall.append((i,j))
#                 dfs(count+1)
#                 if result == "YES":
#                     return
#                 wall.remove((i,j))
#                 data[i][j] = 'X'
# dfs(0)
# print(result)
#--> 시간초과
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input()) #복도의 크기
data = [] #복도의 정보
spaces = [] #빈 공간 정보
teacher = [] #선생님 정보

for i in range(n):
    data.append(list((input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i,j))
        if data[i][j] == 'X':
            spaces.append((i,j))

#특정방향으로 탐색 시작 상하좌우 (학생찾으면 True,못 찾으면 False)
def search(x,y,dir):
    #왼쪽방향 y >= 0
    if dir == 0:
        while y >= 0:
            if data[x][y] == 'S':#학생 찾으면?
                return True
            if data[x][y] == 'O':
                return False
            y-=1
    #오른쪽
    if dir == 1:
        while y < n:
            if data[x][y] == 'S':#학생 찾으면?
                return True
            if data[x][y] == 'O':
                return False
            y+=1
    #위
    if dir == 2:
        while x >= 0:
            if data[x][y] == 'S':#학생 찾으면?
                return True
            if data[x][y] == 'O':
                return False
            x-=1
    #아래
    if dir == 3:
        while x < n:
            if data[x][y] == 'S':#학생 찾으면?
                return True
            if data[x][y] == 'O':
                return False
            x+=1
    return False

#장애물 설치이후 한명이라도 감지 되는지
def solution():
    for x,y in teacher:
        #4가지 방향에 대해서 선생님이 보는 방향에 학생이 있으면 True , 없으면 False
        for i in range(4):
            if search(x,y,i):
                return True
    return False

result = False

for i in combinations(spaces,3):
    #장애물 설치해보기
    for x,y in i:
        data[x][y] = 'O'
    if not solution():
        result = True
        break
    #장애물 다시 없애기
    for x,y in i:
        data[x][y] = 'X'

if result:
    print("YES")
else:
    print("NO")

        



