#어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
#1. N에서 1을 뺍니다.
#2. N을 K로 나눕니다.

n,k = map(int,input().split())
count = 0
while True:
    if n % k == 0:
        n = n//k
        count += 1
    else:
        n -= 1
        count += 1
    if n == 1:
        break
print(count)