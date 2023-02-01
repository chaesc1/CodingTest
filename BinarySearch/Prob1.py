#부품찾기
#N개의 부품이 존재함
#ex) N = 5 [8,3,7,9,2]
#손님은 M개의 부품이 있는지 없는지 체크 해달라고 함
#ex) M = 3 [5,7,9]
#요청한 부품의 순서대로 부품을 확인해 부품이 있으면 yes,없으면 no를 출력

def binarySearch(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
A = list(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

for i in B:
    result = binarySearch(A,i,0,n-1)

    if result == None:
        print("no",end=" ")
    else:
        print("yes",end=" ")