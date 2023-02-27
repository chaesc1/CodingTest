#크게 만들기

#N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(input())
stack = []
delN = k

for i in range(n):
    #k번, stack에 숫자가 빌때까지, 스택에 최근들어온 수가 비교할 숫자보다 작으면
    while delN > 0 and stack:
        if stack[len(stack)-1] < arr[i]:
            stack.pop()
            delN -= 1
        else:
            break
    stack.append(arr[i])

print(''.join((stack[:n-k])))