#각각의 데이터가 몇번씩 나왔는지를 카운트하여 그 인덱스를 개수만큼 출력한다.

arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#모든 범위를 포함하는 리스트 선언 ( 모든 값은 0 으로 초기화)
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')