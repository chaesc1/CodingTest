#모험가 길드
#한 마을에 모함가가 N명 -> N명의 모함가를 대상으로 공포도 측정
#공포도가x인 모함가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야함
#최대 몇개의 모험가 그룹을 만들 수 있는지 check

#입력조건 
#첫째 줄에 모험가의 수 N이 주어진다.
#돌째 줄에 각모험가의 공포도의 값을 N 이하의 자연수로 주어지며,각 자연수는 공백으로 구분함

#출력 조건
#여향을 떠날 수 있는 그룹스ㅜ의 최대값을 출력

n = int(input())
data = list(map(int,input().split())) # 2 3 1 2 2 -> 1 2 2 2 3
data.sort() # 1 2 2 2 3

group = 0 #그룹의 수
count = 0 #그룹에 속한 멤버 수

for i in data:
    count += 1 #현재 인원을 멤버로 추가
    if count >= i: #인원수가 공포도 보다 크면 그룹을 결성해야해
        group += 1
        count = 0

print(group)