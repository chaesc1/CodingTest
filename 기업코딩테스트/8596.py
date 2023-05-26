#점수계산

#OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경우에는 0으로 표시

#번 문제가 맞는 경우에는 1점으로 계산한다.
#앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점

n = int(input())
score_list = list(map(int,input().split()))

result = 0
correct = 0
for i in range(n):
    if score_list[i] == 1: #맞다면?
        correct += 1
        result += correct
    else:
        correct = 0

print(result)