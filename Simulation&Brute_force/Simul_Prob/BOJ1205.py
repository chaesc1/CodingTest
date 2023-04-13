#등수 구하기

# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P가 주어진다. 
# 그리고 리스트에 있는 점수 N개가 비오름차순(내림차순)으로 주어지고, 태수의 새로운 점수가 주어진다
# 이때, 태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램을 작성하시오. 
# 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력한다.
# 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.

###입력
# N, 새로운 점수 new , P 가 주어짐
# P는 10보다 크거나 같고, 50보다 작거나 같은 정수,   10<= P < 50
# N은 0보다 크거나 같고, P보다 작거나 같은 정수이다   0 <= N < P

import sys
input = sys.stdin.readline

n,new,p = map(int,input().split())

if n == 0:
    print(1)
else:
    score = list(map(int,input().split()))
    if score[-1] >= new and n == p:#만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력한다.
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if score[i] <= new:
                res = i+1
                break
        print(res)