#만들 수 없는 금액
#N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오

#ex) N = 5 -> 3 2 1 1 9

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1

for i in data:
    #만들 수 있는 금액이면 target에 데이터 값을 더해서 넘겨줘 
    if target >= i:
        target+=i
        continue
    else:#만들 수 없는 금액이면 break
        break
    

print(target)
    
