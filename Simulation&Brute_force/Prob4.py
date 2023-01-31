#문자열 재정렬
#알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어짐
#이때 알파벳을 오름차순으로 정렬하여 이어서 출력, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
#ex k1ka5cb7 -> abckk13

data = input()
Ldata = []
sum = 0
for i in range(len(data)):
    if ord(data[i]) >= 65 and ord(data[i]) <= 90:
        Ldata.append(data[i])
    else:
        sum += int(data[i])

Ldata.sort()
s = ''.join(Ldata)
print(s,sum,sep="")
