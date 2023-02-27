#가희와 탑

#사전 순으로 가장 앞서는 N개의 건물 높이 정보를 출력해 주세요.

#첫째 줄에 건물의 개수 N, 가희가 볼 수 있는 건물의 개수 a, 단비가 볼 수 있는 건물의 개수 b가 공백으로 구분해서 주어집니다.

#문제의 조건에 맞는 건물들의 높이 정보가 1개 이상 존재하는 경우 N개의 건물 높이 정보 중 사전순으로 가장 앞선 것을 출력해 주세요. 
#출력 형식은 다음을 만족해야 합니다.

#1번 건물, ... , N번 건물의 높이를 공백으로 구분해서 출력해 주세요. 출력하는 수들이 모두 다를 필요는 없습니다.
#높이는 1보다 크거나 같은 정수여야 합니다.
#문제의 조건에 맞는 건물들의 높이 정보가 존재하지 않으면 첫 줄에 -1을 출력해 주세요.

import sys
input = sys.stdin.readline

n,a,b = map(int,input().split())

answer = []

for i in range(1,a):
    answer.append(i)
answer.append(max(a,b))
for i in range(b-1,0,-1):
    answer.append(i)

if len(answer) > n:
    print(-1)
else:
    print(answer[0],end=' ')
    for i in range(n-len(answer)):
        print(1,end=' ')
    for i in range(1,len(answer)):
        print(answer[i],end=' ')