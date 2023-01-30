#거스름돈문제
#가장 큰 화폐단위부터 돈을 거슬러줘
#ex 1260

n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
array = [500,100,50,10]

for coin in array:
    count += n // coin #해당화폐로 거슬러 줄 수 있는 동전의 개수 카운트
    n = n%coin
print(count)