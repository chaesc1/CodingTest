#시간문제
#정수 n이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서
#3이 하나라도 포함되는 모든경우의 수를 구하는 프로그램

n = int(input())
count = 0
for i in range(n+1):#시
    for j in range(60):#분
        for k in range(60):#초
            if '3' in str(i)+str(j)+str(k): #시분초를 쭉 나열해서 3이 있는지 체크
                count += 1
print(count)
#가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있다.