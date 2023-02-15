#문자열 재정렬

s = input()
result = []
sum = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)

result.sort() #알파벳 정렬해주고

if sum != 0: #숫자가 하나라도 준재하면 result 뒤에다가 삽입
    result.append(str(sum))

print(''.join(result))