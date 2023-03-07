#색종이 붙히기

#문제
# 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 
# 색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 
# 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다.
# 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 
# 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.
# 종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자
import sys
input = sys.stdin.readline
INF = int(1e9)

map = [list(map(int,input().split())) for _ in range(10)] #10 x 10 생성
paper = [0] * 5
ans = INF

def dfs(x,y,count):
    global ans

    #x가 범위(10)을 넘어가면 y+1
    if x >= 10:
        dfs(0,y+1,count)
        return
    #y가 범위를 벗어나면 -> 최솟값 탐색 
    if y >= 10:
        ans = min(ans,count)
        return
    #map[x][y] == 0이면 다음칸 탐색해본다. (x+1,y)
    if map[x][y] == 0:
        dfs(x+1,y,count)
    else:#map[x][y] == 1이면 크기 1부터 5까지 색종이를 붙힐수 있는지 체크한다.
        for i in range(5):
            #범위를 벗어나거나 종이를 5개 모두 사용한 경우.
            if paper[i] == 5:
                continue
            if x+i >= 10 or y+i >= 10:
                continue

            flag = 0
            for j in range(x,x+i+1):
                for k in range(y,y+i+1):
                    if map[j][k] == 0: #0이 하나라도 포함되어있으면 빠져 나와야한다.
                        flag = 1 #플래그 띄워주고 반복문 탈출
                        break
                if flag:
                    break
            
            if not flag:#붙힐수 있는 자리라면? 0이 하나도 없다면?
                for j in range(x,x+i+1):
                    for k in range(y,y+i+1):
                        map[j][k] = 0 #일단 0으로 바꿔줘 -> 덮어줘
                paper[i] += 1 #종이 개수 늘려주고.
                dfs(x+i+1,y,count+1) 
                paper[i] -= 1

                for j in range(x,x+i+1):
                    for k in range(y,y+i+1):
                        map[j][k] = 1 #다시 원상 복구

dfs(0,0,0)

if ans != INF:
    print(ans)
else:
    print(-1)