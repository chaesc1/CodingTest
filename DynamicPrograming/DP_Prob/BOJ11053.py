#가장 긴 증가하는 부분수열 
#LIS
#수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

#예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 
#가장 긴 증가하는 부분 수열은 A = {10, 20, 30,  50} 이고, 길이는 4이다.

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

d = [1] * n #부분수열의 길이

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i],d[j] + 1)

print(max(d))
