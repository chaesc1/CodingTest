#1로만들기 -> dynamicPrograming


#정수 X를 입력받아
x = int(input())

# 1<=X<=30000
d = [0] * 30001

#바텀업 방식 -> 반복문을 이용하요 적운 문제부터 차근차근 답을 도출
#d[2] = d[1] + 1
for i in range(2,x+1):
    d[i] = d[i-1] + 1 #d연산

    #a연산
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
    #b연산
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    #c연산
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)

print(d[x])
