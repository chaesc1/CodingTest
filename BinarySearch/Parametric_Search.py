# 최적화 문제를 결정 문제(예 혹은 아니오) 로 바꾸어 해결하는 기법
#ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

n,m = map(int,input().split()) #n=떡의 개수 m=요청한떡의 길이

a = list(map(int,input().split()))

start = 0
end = max(a)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in a:#전체 떡의 길이를 하나씩 출력해서 계산
        if x > mid: #떡의 길이가 중간점 보다 크면?
            total += x - mid #떡의 길이 - 중간길이.

    if total < m: #왼쪽부분 탐색해서 떡의 양이 부족한 경우
        end = mid - 1
    else: #떡의 양이 충분한경우
        result = mid
        start = mid + 1

print(result)