from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
array = list(map(int,input().split()))#정렬된 리스트
#정렬되어 있기 때문에 이진 탐색 가능/ 특정 값이 등장하는 첫번째 인덱스와 마지막 인덱스를 찾아 문제 해결가능

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

count = count_by_range(array,x,x)

if count == 0:
    print(-1)
else:
    print(count)
