#기준데이터(피벗)을 설정하여 피벗보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
#가장 기분적으로 첫번째 데이터를 기준으로 피벗을 설정
#시간복잡도 평균 -> nlogn 최악의 경우 -> n^2(정렬된 데이터일 경우)

arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
    if start >= end: #원소가 한개인경우 종료
        return
    pivot = start #첫번째 원소를 피벗으로
    left = start+1 # 첫번째 원소 즉 피벗 다음 값을 left로 설정
    right = end #마지막 원소를 end로 설정

    while(left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if left > right:
            arr[right],arr[pivot] = arr[pivot],arr[right]
        else:
            arr[left],arr[right] = arr[right],arr[left]
    #분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr,start,right-1)#왼쪽
    quick_sort(arr,right+1,end)#오른쪽

quick_sort(arr,0,len(arr)-1)
print(arr)