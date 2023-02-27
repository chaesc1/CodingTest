#기타레슨
#다시 해보자.
import sys
input = sys.stdin.readline

def is_possible(target):
    cnt = 1
    sum = 0
    for i in data:
        sum += i
        if sum > target:
            sum = i
            cnt += 1
    return cnt <= m

n,m = map(int,input().split())
data = list(map(int,input().split()))

#무엇을 기준으로 잡을까? 사작을 모든 데이터의 합/ 끝을 데이터 중에서 제일 큰 값
start = max(data)
end = sum(data)#블루레이 크기가 가장 클떄 -> 블루레이의 개수가 한개씩 일때.

while start <= end:
    mid = (start + end) // 2
    #데이터를 하나씩 더해가면서 mid 보다 큰지 작은지 비교연산 
    if is_possible(mid):
        end = mid - 1
    else:
        start = mid + 1
print(start)