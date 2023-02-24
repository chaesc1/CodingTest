#예산

#문제 국가예산의 총액은 미리정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다
#정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정함

#1.모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
#2.모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 
#  상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

#ex
# 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 
# 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 

import sys
input = sys.stdin.readline

n = int(input()) #지방의 수 
arr = list(map(int,input().split()))
m = int(input())#총예산

start = 0
end = max(arr)
total = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        total += min(i,mid)

    if total > m:#목표금액보다 크다면?
        end = mid - 1
    else:
        start = mid + 1
print(end)

# import sys
# # sys.stdin = open('input.txt')

# n = int(sys.stdin.readline())
# lis = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())

# le=0
# ri=max(lis)
# sum=0
# while le<=ri:
#     mid = (le+ri)//2
#     sum=0
#     for item in lis:
#         sum +=min(item, mid)
#     if sum>m:
#         ri=mid-1
#     else:
#         le=mid+1
# # print(sum)
# print(ri)