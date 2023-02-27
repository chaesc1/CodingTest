#베
#항구에는 크레인이 N대 있고
#이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
#모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
    sys.exit()
time = 0
#박스가 모두 없을때 까지 반복
while len(box) > 0:
    time+=1
    for cranes in crane:
        for boxes in box:
            if cranes >= boxes:#박스가 무게제한 이내면
                box.remove(boxes)
                break

print(time)

