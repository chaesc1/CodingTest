#순차탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
#이진탐색: 정렬되어있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
#-> 이진탐색은 시작점 끝점 중간점을 탐색범위로 지정함

def binary_search(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    #찾은경우 mid 인덱스 반환
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n,target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

