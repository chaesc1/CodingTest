#용액

# 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액의 특성값이 0에 가장 가까운 용액이다. 
# 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

#left right 둘로 나눠서 합이 0보다 작으면 left + 1 // 0보다 크면 right - 1
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
lNum = 0
rNum = 0

left_side = 0
right_side = n-1

minNum = sys.maxsize

while left_side < right_side:
    value = data[left_side] + data[right_side]
    
    if abs(value) < minNum:
        lNum = left_side
        rNum = right_side
        minNum = abs(value)

    if value < 0:
        left_side += 1
    elif value > 0:
        right_side -= 1
    else:
        break

print(data[lNum], data[rNum])