#뱀

#사과를 먹으면 뱀길이가 늘어남 뱀이 이리저리 기어다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남
#게임은 n*n정사각 보드 위에서 진행/ 몇몇칸에는 사과가 놓여져 있음
#보드의 상하좌우 끝에는 벽이 존재 
#게임을 시작할 때 뱀은 맨 위 좌측에 위치하고 뱀의 길이는 1임
#뱀은 처음에 오른쪽을 향함

#규칙
#1.뱀은 몸길이를 늘려 머리를 다음칸에 위치시킴
#2.만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다
#3.만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌/ 즉 몸길이는 변하지 않는다.

#입력조건
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  
# 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

n = int(input())
k = int(input())

#맵정보 초기화
board = [[0]*(n+1) for _ in range(n+1)]

#사과가 있는곳 1로 표시
for _ in range(k):
    a,b = map(int,input().split())
    board[a][b] = 1

l = int(input())
direction_info = []

for _ in range(l):
    x,c = input().split()
    direction_info.append((int(x),c))

#동쪽 부터 보고있기때문에 동(시작)-남-서-북 (0,0)-> (0,1)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(dir,c):
    #왼쪽 회전 (0->3->2->1) -1
    #오른쪽 회전(0->1->2->3) +1
    if c == "L":#왼쪽으로 90도 회전 
        dir = (dir - 1)%4
    else:
        dir = (dir + 1)%4
    return dir

def play():
    x = 1
    y = 1 #뱀 시작 위치.
    board[x][y] = 2 #한번들린 위치를 2로 표시
    time = 0 #지나간 초
    index = 0 #방향 인덱스
    direction = 0
    q = [(x,y)]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        #뱀이 맵 안에 있고,몸통이 없는 위치면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 2:
            #사과가 없다면 이동후에 꼬리제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2 #방문표시하고
                q.append((nx,ny))
                px,py = q.pop(0) #꼬리 제거
                board[px][py] = 0
            #사과가 있다면 이동후에 꼬리를 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2 #방문표시하고     
                q.append((nx,ny))
        else:
            #벽이나 뱀의 몸통에 부딫히면?
            time += 1
            break #종료6
        #다음 위치로 이동
        x,y = nx,ny
        time += 1

        if index < 1 and time == direction_info[index][0]: #회전할 시간이면??
            direction = turn(direction,direction_info[index][1])
            index += 1
    return time

print(play())