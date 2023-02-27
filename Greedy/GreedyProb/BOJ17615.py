#볼 모으기

#1) 각 색상의 공의 개수를 카운트 -> 더 적은 수의 공을 움직이는 것이 효율적 

#2) 빨간색을 모두 오른쪽으로 옮기는 경우
#3) 빨간색을 모두 왼쪽으로 옮기는 경우
#4) 파란색을 모두 오른쪽으로 옮기는 경우
#5) 파란색을 모두 왼쪽으로 옮기는 경우
import sys
input = sys.stdin.readline

def start(color,ball):
    for _ in range(len(ball)):
        c = ball.pop()
        if c != color:
            ball.append(c)
            break
    return ball

def move(color,ball):
    ball = start(color,ball)
    #print (ball.count(color))
    return ball.count(color)

n = int(input())
arr = list(map(str,input().rstrip()))

print(min(move('R',arr[:]), move('R',arr[::-1]), move('B',arr[:]), move('B',arr[::-1])))

