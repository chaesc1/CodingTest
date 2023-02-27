#행복 유치원

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
data = list(map(int,input().split()))

cost = []
for i in range(n-1):
    cost.append(data[i+1] - data[i])

cost.sort()

print(sum(cost[:n-k]))