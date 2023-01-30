a = input()

result = int(a[0])

for i in range(1,len(a)):#두번째 숫자부터 수행
    #두 수 중에서 하나라도 0 혹은 1이면 더하기 수행
    num = int(a[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)