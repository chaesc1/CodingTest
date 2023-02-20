#정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
data = list(map(int,input().split()))

#log 시간 복잡도로 풀이해야해

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

count = count_by_range(data,x,x)

if count == 0:
    print(-1)
else:
    print(count)