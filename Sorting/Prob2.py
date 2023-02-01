#위에서 아래로
#입력 : 수열에 속해 있는 수의 개수 N이 주어짐

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array,reverse=True)

for i in array:
    print(i,end=" ")