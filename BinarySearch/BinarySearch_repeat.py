#(재귀를 이용한 이진탐색)
def binarySearch_recursive(array,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2
    #중간점 인덱스 반환
    if array[mid] == target:
        return mid
    #중간점 값보다 target이 작은경우 end 값을 mid값의 -1 로
    elif array[mid] > target:
        return binarySearch_recursive(array,target,start,mid-1)
    #중간점 값보다 target이 큰 경우 start값을 mid+1 로
    elif array[mid] < target:
        return binarySearch_recursive(array,target,start+1,end)

#반복문을 이용한 이진탐색
def binarySearch_iter(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
            # 중간점 값보다 target이 작은경우 end 값을 mid값의 -1 로
        elif array[mid] > target:
            end = mid - 1
            # 중간점 값보다 target이 큰 경우 start값을 mid+1 로
        else:
            start = mid + 1
    return None





n,target = list(map(int,input().split()))
array = list(map(int,input().split()))

result_rec = binarySearch_recursive(array,target,0,n-1)

if result_rec == None:
    print("갑이 존재하지 않습니다")
else:
    print("재귀 ",result_rec+1,"번째 수")

result_iter = binarySearch_iter(array,target,0,n-1)

if result_iter == None:
    print("갑이 존재하지 않습니다")
else:
    print("반복문 ",result_iter+1,"번째 수")