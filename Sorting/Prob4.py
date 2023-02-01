#두배열 원소 교체
#두 배열 A,B는 N개의 원소로 구성되어 있다. k번의 바꿔치기 연산을 수행
#배열 A의 모든 원소의 합이 최대가 되도록 한다.

n,k = map(int,input().split())

#배열 a,b에 원소 입력받아
a = list(map(int,input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순 정렬
b.sort(reverse=True)#내림차순정렬
#그 후에 첫 인덱스부터 비교해서 a<b인 경우 스왑

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break

print(sum(a))