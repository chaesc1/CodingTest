#완전 이진트리

#level
#0                  3(3) -> root
#1          6 (1)                 2(5)    
#2      1(0)       4(2)       5(4)       7(6)
#중위 순회
from sys import stdin
input = stdin.readline

k = int(input())
nums = list(map(int,input().split()))
tree = [[] for _ in range(k)]

def sol(nums,depth):
    #루트 노드를 찾는다.

    mid = len(nums) // 2

    #해당하는 깊이에 해당하는 node를 추가함
    tree[depth].append(nums[mid])

    if len(nums) == 1:
        return
    sol(nums[:mid],depth+1)#좌측 트리
    sol(nums[mid+1:],depth+1)#우측트리

sol(nums,0)

for i in tree:
    print(' '.join(map(str,i)))