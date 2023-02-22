#1로 만들기

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1) # 1<=N<=10^6

#바텀업 방식 -> 반복문을 이용해서 적은 문제부터 차근차근 답을 도출
#d[2] = d[1] + 1
for i in range(2,n+1):
    d[i] = d[i-1] + 1

    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)

    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)

print(d[n])