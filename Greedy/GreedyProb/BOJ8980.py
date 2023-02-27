#택배

#입력의 첫 줄은 마을 수 N과 트럭의 용량 C가 빈칸을 사이에 두고 주어진다
#다음 줄에, 보내는 박스 정보의 개수 M이 주어진다
# M개의 각 줄에 박스를 보내는 마을번호, 
#박스를 받는 마을번호, 보내는 박스 개수(1이상 10,000이하 정수)를 나타내는 양의 정수가 빈칸을 사이에 두고 주어진다

import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())
box_info = []

for _ in range(m):
    start,end,amount = map(int,input().split())
    box_info.append([start,end,amount])

box_info.sort(key= lambda x:x[1]) #end 기준으로 오름차순 정렬

remains = [c] * (n+1)#수용가능한 양으로 배열 초기화

result = 0
for s,e,a in box_info:
    tmp = c
    for i in range(s,e):
        tmp = min(tmp,remains[i])
    tmp = min(tmp,a)
    for i in range(s,e):
        remains[i] -= tmp
    result += tmp

print(result)