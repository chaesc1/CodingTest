#올림픽

#  두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면,
# 금메달 수가 더 많은 나라 
# 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 

#입력
# 입력의 첫 줄은 국가의 수 N(1 ≤ N ≤ 1,000)과 등수를 알고 싶은 국가 K(1 ≤ K ≤ N)가 빈칸을 사이에 두고 주어진다.
# 각 국가는 1부터 N 사이의 정수로 표현된다. 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 
# 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어진다. 전체 메달 수의 총합은 1,000,000 이하이다.

#출력
# 출력은 단 한 줄이며, 입력받은 국가 K의 등수를 하나의 정수로 출력한다. 
# 등수는 반드시 문제에서 정의된 방식을 따라야 한다. 

import sys
input = sys.stdin.readline

n,k = map(int,input().split()) 
arr = []

for _ in range(n):
    arr.append(list(map(int,input().split()))) # 2차원배열 생성

arr.sort(key=lambda x : (-x[1], -x[2], -x[3])) #금 은 동 순으로 정렬

for i in range(n):
    if arr[i][0] == k:
        index = i 

for i in range(n):
    if arr[i][1:] == arr[index][1:]:
        print(i+1)
        break

