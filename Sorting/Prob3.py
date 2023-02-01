#성적이 낮은 순서로 학생 출력
#입력 : 학생수 N , 문자열 A와 점수 B 주어져
#성적이 낮은 순서대로 정렬

n = int(input())

#N명의 데이터 입력받아
array = []
for i in range(n):
    data_input = input().split()
    #문자열은 그대로,숫자는 int로 형변환 후에 저장
    array.append((data_input[0],int(data_input[1])))

#키를 이용 -> 점수를 기준으로 정렬
array = sorted(array,key = lambda  item:item[1])

for i in array:
    print(i,end=" ")