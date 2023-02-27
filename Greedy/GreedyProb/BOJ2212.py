#센서

#고속도로 위에 N개의 센서를 설치하였다
#문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int,input().split()))
data.sort()

ans = []
for i in range(n-1):
    ans.append(data[i+1]-data[i])

ans.sort()

print(sum(ans[:n-k]))