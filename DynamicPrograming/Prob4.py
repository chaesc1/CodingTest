#효율적인 화폐 구성
#N개의 줄에는 각 화폐의 가치가 주어짐 그 가치의 합이 M원이 되도록 한다.
#M원을 만들기 위한 최소한의 화폐 개수를 출력
#불가능할땐 -1 출력

n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1) #dp테이블 생성
d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j - array[i]] != 10001:#(i-k)원을 만드는 경우가 있으면
            d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])