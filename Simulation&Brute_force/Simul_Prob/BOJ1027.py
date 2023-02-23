#고층 건물
# 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다
# 빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. i번째 빌딩 (1부터 시작)은 (i,0)부터 (i,높이)의 선분으로 나타낼 수 있다
# 고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다.
# 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int,input().split()))

result = 0

#기울기 구하는 공식
def inclination(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

##solution
for idx1,y1 in enumerate(buildings):
    #print(idx1,y1)
    view_max = 0
    x1 = idx1 + 1
    left_min = 1e9 #왼쪽에서 최대
    right_max = -1e9 #오른쪽에서 최대

    #왼쪽
    for idx2 in range(idx1-1,-1,-1):
        inclinationLeft = inclination(idx1+1,y1,idx2+1,buildings[idx2])#왼쪽에 있는 건물 기울기

        if inclinationLeft < left_min:#기울기 더 작다면
            left_min = inclinationLeft
            view_max += 1
    #오른쪽
    for idx3 in range(idx1+1,n):
        inclinationRight = inclination(idx1+1,y1,idx3+1,buildings[idx3])#왼쪽에 있는 건물 기울기
        
        if inclinationRight > right_max:
            right_max = inclinationRight
            view_max += 1
    result = max(result,view_max)

print(result)



