#처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다
#선택정렬에 비해 구현 난이도가 높지만/ 일반적으로 더 효율적으로 동작합니다.

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):# i부터 0까지 1씩 감소시키면서 반복하는 문법
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break


print(array)