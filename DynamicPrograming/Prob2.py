#개미전사
n = int(input())
foods = list(map(int,input().split()))

#앞서 계산된 결과를 저장할 공간 선언
d = [0] * 100

d[0] = foods[0]
d[1] = max(foods[0],foods[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+foods[i])

print(d[n-1])