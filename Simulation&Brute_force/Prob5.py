#게임개발
#N x M 크기의 정사각형

n,m = map(int,input().split())

#맵을 0 으로 초기화
d = [[0]*m for _ in range(n)]
x,y,direction = map(int,input().split()) #현재 위치하는 x,y좌표, 보고있는 방향 입력

#시작 위치는 방문처리
d[x][y] = 1

#맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북 동 남 서 방향지정
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽회전 함수 정의
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#게임 시작
count = 1 # 방문한 칸의 수
turn_count = 0 #회전한 횟수
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전후에 정면의 땅이 움직잃수 있는 땅(0) 이면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 #방문표시
        x = nx
        x = ny #좌표 초기화
        count += 1
        turn_count = 0
        continue
    else:
        turn_count+=1
    #네 방향 모두 갈 수 없는 땅인경우
    if turn_count == 4:
        #한칸 뒤로 이동
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0: #뒤로가기 가능하면?
            x = nx
            y = ny
        else: #뒤에 바다가 존재하면 즉 뒤로가기 불가능 하면?
            break
        turn_count = 0

print(count)
