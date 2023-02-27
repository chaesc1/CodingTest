import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(input())
stack = []

for i in range(n):
    #k번, stack에 숫자가 빌때까지, 스택에 최근들어온 수가 비교할 숫자보다 작으면
    while k > 0 and stack:
        if stack[len(stack)-1] < arr[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(arr[i])
stack.sort(reverse=True)
print(''.join((stack[:n-k])))