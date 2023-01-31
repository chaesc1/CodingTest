#왕실의 나이트
#8*8 좌표평면
#나이트는 말을 타고 있기 때문에 L자 형태로 이동할 수가 있다/ 정원 밖으로는 나갈 수 없다
#1.수평으로 두 칸 이동한 뒤에 수직으로 한칸
#2.수직으로 두 칸 이동한 뒤에 수평으로
#나이트가 이동 할수있는 경우의수는?
#행 위치는 1-8로 표현/ 열 위치는 a-h로 표현

data = input()
#행
rows = int(data[1])
#열
cols = int(ord(data[0])) - int(ord("a"))+1

#L모양으로 움직일 수 있는 8가지 방법
moves = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(-1,-2),(1,2),(-1,2)]

results = 0
for move in moves:
    nextX = rows + move[0]
    nextY = cols + move[1]

    # if nextX < 1 or nextY < 1 or nextX > 8 or nextY > 8:#벗어나게 되면?
    #     continue
    # results+=1
    if nextX >= 1 and nextX <= 8 and nextY >=1 and nextY <= 8:
        results+=1

print(results)