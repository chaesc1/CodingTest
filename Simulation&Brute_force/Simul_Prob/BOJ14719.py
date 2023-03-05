#빗물

#입력
# 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
# 따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

#출력
# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.

# 4 4
# 3 0 1 4   

#      0
#0 1 1 0
#0 1 1 0
#0 1 0 0 ---> 5개
#0,1,2,3

#2번 위치를 예를 들면 오른쪽 3,왼쪽 4 중에서 작은 3과 해당 높이 1 을 뺀 2만큼 물이 차올라야함.
#특정 위치 기준으로 양옆이 자신보다 크면 물이 고일 수 있다.즉 자신보다 더 큰 높이의 벽으로 둘러 쌓여 있어야함.
import sys
input = sys.stdin.readline

h,w = map(int,input().split())
data = list(map(int,input().split()))
result = 0

for i in range(1,w-1):
    left = max(data[:i])
    right = max(data[i+1:])

    compare = min(left,right)

    if data[i] < compare:
        result += compare - data[i]

print(result)