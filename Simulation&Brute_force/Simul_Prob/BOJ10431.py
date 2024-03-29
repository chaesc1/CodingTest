#줄 세우기

# 우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다. 그리고 그 다음부터는 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다.

# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
# 이 과정을 반복하면 결국 오름차순으로 줄을 설 수가 있다.

# 아이들의 키가 주어지고, 어떤 순서로 아이들이 줄서기를 할 지 주어진다. 위의 방법을 마지막 학생까지 시행하여 줄서기가 끝났을 때 학생들이 총 몇 번 뒤로 물러서게 될까?

###입력
# 첫 줄에 테스트 케이스의 수 P (1 ≤ P ≤ 1000) 가 주어진다.
# 각 테스트 케이스는 테스트 케이스 번호 T와 20개의 양의 정수가 공백으로 구분되어 주어진다.
# 20개의 정수는 줄서기를 할 아이들의 키를 줄서기 차례의 순서대로 밀리미터 단위로 나타낸 것이다.
# 모든 테스트 케이스는 독립적이다.

##출력
# 각각의 테스트 케이스에 대해 테스트 케이스의 번호와 학생들이 뒤로 물러난 걸음 수의 총합을 공백으로 구분하여 출력한다.

import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    cnt = 0 
    arr = list(map(int,input().split())) #20개의 정수를 받아서 배열에 삽입
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                cnt+=1
    print(arr[0],cnt)