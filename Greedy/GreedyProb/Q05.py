#볼링공 자르기
#서로 무게가 다른 볼링공을 고르려고 한다.
#볼링공은 총 N개 존재 -> 각각 무게가 적혀있음 / 공의 번호는 1번부터 순서대로 부여됨
#같은 무게더라도 다른 공으로 간주함 /볼링공의 무게는 1-m 까지의 자연수 형태로 존재
#두 사람이 고를 공의 조합을 구해라

#입력조건/
# 첫째 줄에 볼링공의 개수n, 공의 최대 무게 m이 공백으로 구분되어 각각 자연수 형태로 주어짐
# 둘째 줄에 각 볼링공의 무게 k가 공백으로 구분되어 각각 자연수 형태로 주어짐

#출력조건 
#첫쨰 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력


n,m = map(int,input().split())
data = list(map(int,input().split()))

#번호를 부여해
#1부터 10까지 번호를 부여할 배열
array = [0] * 11

#각 무게의 개수 카운트
for i in data:
    array[i] += 1 

result = 0

for i in range(1,m+1):
    n -= array[i]
    #print('N = ',n,end=" ")
    #print('array[i] = ',array[i],end=" ")
    result += array[i] * n
    # print('result = ',result,end=" ")

print(result)
