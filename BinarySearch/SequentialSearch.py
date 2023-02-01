def sequential_Search(n,target,array):
    #각 원소를 하나씩 확인하며
    for i in range(n):
        if array[i] == target:
            return i+1 #현재의 위치 반환 (배열은 0부터 시작하기때문에 +1 해줘야 현재 인덱스)

input_data = input().split()

#num of Element
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_Search(n,target,array))
