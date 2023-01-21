#두배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수
#최대 K번의 바꿔치기 연산을 수행 할수있으며 바꿔치기 연산이란 배열 A에 있는 원소하나와
#배열B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
#배열A의 모든 원소의 합이 최대가 되도록 하는것이 목표
#ex N=5,k=3
#A = [1,2,5,4,3]
#B = [5,5,6,6,5]

n, k  = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#a는 오름차순 sort / b는 내림차순 sort
a.sort()
b.sort(reverse=True)
#원소끼리 비교후 a < b 이면 swap

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))