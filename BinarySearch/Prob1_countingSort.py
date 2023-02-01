#n 가게의 부품수 입력
n = int(input())
array = [0] * 100001

#가게에 있는 전체 부품 번호 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

#m 손님이 확인 요청한 부품 개수 입력
m = int(input())
x = list(map(int,input().split()))

#손님이 확인 요청한 부품을 꺼내 하나씩 비교하면 된다.
for i in x:
    if array[i] == 1:
        print("yes",end=" ")
    else:
        print("no",end=" ")