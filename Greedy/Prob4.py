#모험가 길드 문제
#모험가 N명 모험가를 대상으로 공포도 측정
#여러그룹을 구성하는데
#공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날수 있음
#여행을 떠날 수 있는 그룹 수의 최댓값은?
#ex) n=5 , 2 3 1 2 2
a = int(input())
b = list(map(int,input().split()))
#1 2 2 2 3
b.sort()

result = 0 #num of groups
count = 0 #num of explorers

for i in b:
    count += 1
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result += 1
        count = 0

print(result)
