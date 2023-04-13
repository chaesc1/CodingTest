#스위치 켜고 끄기

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

import sys
input = sys.stdin.readline

n = int(input()) #스위치의 개수
switch_status = list(map(int,input().split())) #초기 스위치 상태
student_num = int(input()) #학생수
student_status = [] #학생의 스위치 정보 넣을 배열

for i in range(student_num):
    student_status.append(list(map(int,input().split())))  #student_status[0] = 1 이면 남자 =2 는 여자

for stu in student_status:
    if stu[0] == 1: #남자면
        for j in range(len(switch_status)):
            if (j+1) % stu[1] == 0: #해당 번호의 스위치가 남학생이 맏은 번호의 배수면?
                #0 -> 1 / 1 -> 0
                switch_status[j] = int(not switch_status[j])
    else: #여자일땐
        for j in range(len(switch_status)):
            if stu[1] == j+1:
                minus = j-1
                plus = j+1
                switch_status[j] = int(not switch_status[j])
            #대칭인지 아닌지 체크해야해
                while True:
                    if minus >= 0 and plus < len(switch_status):#스위치 범위내에서
                        if switch_status[minus] == switch_status[plus]: #좌우 대칭이면
                            switch_status[minus] = int(not switch_status[minus])
                            switch_status[plus] = int(not switch_status[plus])
                        else: #대칭 아니면?
                            break
                    else:
                        break

                    minus -= 1
                    plus += 1
#출력 한줄에 20개 최대 21개 되면 다음줄로
cnt = 0
while cnt < len(switch_status):
    print(switch_status[cnt],end=' ')
    if cnt % 20 == 19:
        print()
    cnt += 1