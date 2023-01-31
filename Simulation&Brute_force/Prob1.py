#상하좌우 문제
#n*n 크기의 정사각형 공간위에 있다
#가장 왼쪽 위 좌표는 (1,1) 가장 오른쪽 아래 좌표는 (N,N)
#여행가는 상하좌우 방향으로 이동
#시작 지점은 (1,1)
#L,R,U,D 중 하나의 문자가 반복적으로 적혀 있다.
#L : 왼쪽으로 한 칸 이동 / R : 오른쪽으로 한 칸 이동 / U : 위로 한 칸 이동 / D : 아래로 한 칸 이동

n = int(input())
x,y = 1, 1 # 시작좌표
moves = input().split()

#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
types = ['L','R','U','D']

#LRUD 를 하나씩 확인한다
for move in moves:
    for i in range(len(types)):
        if move == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우
    if nx > n or ny > n or nx < 1 or ny < 1:
        continue
    #이동해
    x,y = nx,ny
print(x,y)
