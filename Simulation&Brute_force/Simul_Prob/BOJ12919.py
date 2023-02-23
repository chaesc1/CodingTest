#A와 B 2
# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
# S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성
#S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.


#문자열의 뒤에 A를 추가함
#문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

#Ab - > ba -> b추가 뒤집어 -> bab ->a 추가 -> baba
#Baba -> bab -> ba -> 뒤집기 -> ab -> b제거 -> a
#abaa -> aba -> aba -> ba ->b 
import sys

s = list(input())
t = list(input())

res = 0
def sol(t):
    global res
    if t==s:
        res = 1
        return
    if len(t)==0:
        return 0
    if t[-1] == 'A':
        sol(t[:-1]) #맨 마지막이 a 면 제거해줘
    if t[0] == 'B':
        #뒤집어서 제거
        sol(t[1:][::-1])
    
sol(t) 
print(res)