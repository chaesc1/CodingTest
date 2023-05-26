#요세푸스 문제

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아
# 순서대로 K번째 사람을 제거한다



import sys
input = sys.stdin.readline

#현재 주파수 A와 듣고싶은 주파수 B
a,b = map(int,input().split())

n = int(input())

frequency_list = [] #주파수를 담을 리스트

for i in range(n): #즐겨찾기 버튼 개수 만큼 미리 주파수 지정
    frequency_list.append(int(input()))

#즐겨 찾기 없이 가는 방법 수
sum1 = abs(a-b)

for i in range(n):
    frequency_list[i] = abs(b-frequency_list[i]) #즐겨 찾기 버튼을 눌렀을때의 가야하는 수를 다시 갱신

sum2 = min(frequency_list)

print(min(sum1,sum2+1))


