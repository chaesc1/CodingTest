#그래프 탐색 알고리즘.
#스택 구현 ->
# stack = []
#
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()#7삭제
# stack.append(1)
# stack.append(4)
# stack.pop()#4삭
#
# print(stack[::-1])#최 상단 원소부터 출력
# print(stack)
#큐 구현
# from collections import deque
#
# q = deque()
#
# q.append(5)
# q.append(2)
# q.append(3)
# q.append(7)
# q.popleft()#5삭제
# q.append(1)
# q.append(4)
# q.popleft()#2삭제 3 7 1 4
#
# print(q)
# q.reverse()#역순으로 바꾸기
# print(q)

##재귀함수 : 자기자신을 다시 호출하는 함수
#
# def recursive_func(i):
#     if i == 10:#종료조건
#         return
#     print(i,"번째 재귀함수에서 ",i+1,"번째 재귀함수를 호출합니다.")
#     recursive_func(i+1)
#     print(i, "번째 재귀함수를 종료합니다")
#
# recursive_func(1)

#factorial
#반복문 구현
# def factorial_iter(n):
#     result = 1
#
#     for i in range(1,n+1):
#         result *= i
#     return  result
#
# #재귀적으로 구현
# def factorial_recursive(n):
#     if n <= 1: #n이 1 이하인 경우 1을 반환
#         return 1
#     # n! = n(n-1)
#     return n*factorial_recursive(n-1)
#
# #각각의 방식으로 구현한 n! 출력(n=5)
# print('반복적으로 구현: ',factorial_iter(5))
# print('재귀적으로 구현: ',factorial_recursive(5))

#재귀함수 -> 유클리드
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)
print(gcd(192,160))