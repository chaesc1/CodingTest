#IF문 좀 대신 써줘

import sys
import bisect
input = sys.stdin.readline

n,m = map(int,input().split())

name = []
power = [-1]

for _ in range(n):
    n,p = input().split()
    name.append(n)
    power.append(int(p))

for _ in range(m):
    num = int(input())
    index = bisect.bisect_left(power,num)
    print(name[index-1])

