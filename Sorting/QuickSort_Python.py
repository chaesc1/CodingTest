arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #피벗보다 작은 값을 왼쪽으로
    right_side = [y for y in tail if y >= pivot] #피벗보다 큰 값을 오른쪽으로

    #분할이후 왼쪽부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 리턴
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))