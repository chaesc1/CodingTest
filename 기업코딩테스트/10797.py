#10부제
 
#첫 줄에는 날짜의 일의 자리 숫자가 주어지고 
#두 번째 줄에는 5대의 자동차 번호의 일의 자리 숫자가 주어진다

a = int(input())

car_list = list(map(int,input().split()))

print(car_list.count(a))