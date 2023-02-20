#괄호변환

#균형잡힌 괄호 문자열 -> (,) 의 개수가 같으면
#올바른 괄호 문자열 -> (,) 의 개수와 짝 모두 맞는 문자열

#u,v로 나누는 함수
def divide(p):
    open = 0
    close = 0

    for i in range(len(p)):
        if p[i] == '(': #여는 괄호면?
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i+1],p[i+1:]

def check_proper(p):
    stack = []
    #스택에 ( 가 들어오면 푸시하고 짝이 나오면 팝 한다.
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if not stack:#스택에 없다면
                return False
        
    return True


def solution(p):
    answer = ''
    
    #입력이 빈 문자열인 경우/빈 문자열 반환
    if p == '':
        return ""

    #과정2 : p를 두 균형잡힌 괄호 문자열 u,v 로 나눔 
    #u: 균형잡힌 괄호 문자열로 더이상 분리 불가능 / v: 빈 문자열이 될 수 있음
    u,v = divide(p)

    #과정3 : 문자열 u가 올바른 괄호 문자열인지 체크후 맞으면 u 에 이어 붙힘
    if check_proper(u):
        #과정 3-1 u가 올바른 문자열이면 재귀적으로 v에 대해 1단계 수행
        return u + solution(v)
    #과정4 : 올바른 괄호 문자열이 아니라면 아래 과정 수행
    else:
        #4-1 
        answer = "("
        #4-2
        answer += solution(v)
        #4-3
        answer += ")"

        #4-4 u의 첫 번째와 마지막 문자를 제거하고,나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙힘
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer

p = input()

u,v = divide(p)
print("u: ",u)
print("v: ",v)