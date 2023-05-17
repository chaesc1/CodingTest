#nba
# 동혁이는 NBA 농구 경기를 즐겨 본다. 동혁이는 골이 들어갈 때 마다 골이 들어간 시간과 팀을 적는 이상한 취미를 가지고 있다.
# 농구 경기는 정확히 48분동안 진행된다. 각 팀이 몇 분동안 이기고 있었는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 골이 들어간 횟수 N(1<=N<=100)이 주어진다. 
# 둘째 줄부터 N개의 줄에 득점 정보가 주어진다. 
# 득점 정보는 득점한 팀의 번호와 득점한 시간으로 이루어져 있다.
# 팀 번호는 1 또는 2이다.
# 득점한 시간은 MM:SS(분:초) 형식이며, 분과 초가 한자리 일 경우 첫째자리가 0이다. 
# 분은 0보다 크거나 같고, 47보다 작거나 같으며,
# 초는 0보다 크거나 같고, 59보다 작거나 같다. 
# 득점 시간이 겹치는 경우는 없다.



n = int(input())

one = 0 #1팀 이긴 시간
two = 0 #2팀 이긴 시간 
flag = 0 #1팀이 이기면 +1 / 2팀이 이기면 -1

for _ in range(n):
    team , time = input().split() #골 넣은 팀과 시간을 입력으로 받아
    minute, sec = map(int,time.split(':')) #time 을 분,초로 나눠

    if team == '1': #1팀이 이긴다면?
        if flag == 0: #이제 막 이기게 된 경우
            one += 48*60 - (minute * 60 + sec)
        flag += 1
        if flag == 0: # 2팀에게 지던 중에 이기게 되는 경우 
            if two > 0:
                two = two - (48*60 - (minute * 60 + sec))
    else: #2팀이 이기면
        if flag == 0:
            two += 48*60 - (minute * 60 + sec)
        flag -= 1
        
        if flag == 0:
            if one > 0:
                one = one - (48*60 - (minute * 60 + sec))

print('{:0>2}:{:0>2}'.format(one//60,one%60))
print('{:0>2}:{:0>2}'.format(two//60,two%60))