#곱하기 혹은 더하기

#입력조건 
#첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어짐

#출력조건
#첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
data = input()

sum = int(data[0])

for i in range(1,len(data)):
    #data값이 0이거나 1이면 더하기를 수행
    num = int(data[i])
    if num <= 1 or sum <= 1:
        sum += num
    else:
        sum *= num

print(sum)

