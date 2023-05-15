#트럭 주차
# 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.
# A, B, C가 주어지고, 상근이의 트럭이 주차장에 주차된 시간이 주어졌을 때, 주차 요금으로 얼마를 내야 하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
time_table = [0] * 101

for _ in range(3):
    start , end = map(int,input().split())
    for i in range(start,end):
        time_table[i] += 1

ans = 0
for car in time_table:
    if car == 1: #1대면?
        ans += a * car
    if car == 2:
        ans += b * car
    if car == 3:
        ans += c * car

print(ans)
