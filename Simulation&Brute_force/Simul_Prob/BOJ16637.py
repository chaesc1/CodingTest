#괄호추가하기
#길이가 n인 수식이 있다. 수식은 0보다 크거나 같고 9보다 작거나 같은 정수와 연산자(+,-,x)로 이루어져있다. 
#연산자 우선순위는 모두 동일 -> 수식을 계산할떈 왼쪽부터 순서대로 계산
#수식에 괄호를 추가하면.괄호 안에 있는 식을 먼저 계산해야해 
#괄호 안에는 연산자가 하나만 들어 있어야 한다 -> 중첩된 괄호 사용 안된다.
#
# 수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.
#8*3+5 -> 0 1 2 3 4 
#         8 * 3 + 5
import sys
input = sys.stdin.readline

n = int(input())
data = input()
result = -1e9

def op(num1,operator,num2):
    if operator == '+':
        return num1 + num2
    if operator == '*':
        return num1 * num2
    if operator == '-':
        return num1 - num2
    
def dfs(index,value):
    global result
    
    #베이스 케이스.
    if index == n-1:
        result = max(result,value)
        return
    
    if index + 2 < n:#괄호 안묵고 쭉 계산
        dfs(index + 2, op(value,data[index+1],int(data[index+2])))
    if index + 4 < n:
        dfs(index+4,op(value,data[index+1],op(int(data[index+2]),data[index+3],int(data[index+4]))))
dfs(0,int(data[0]))
print(result)