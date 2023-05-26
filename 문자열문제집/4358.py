#생태학

#그러므로 당신은 미국 전역의 나무들이 주어졌을 때,
#각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

#프로그램은 여러 줄로 이루어져 있으며, 
#한 줄에 하나의 나무 종 이름이 주어진다. 
#어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.
import sys
from collections import defaultdict 
input = sys.stdin.readline

tree_dic = defaultdict(int) #key 값을 0으로 초기화한 딕셔너리

total = 0 #전체 문자열 수
while True:
    tree = input().rstrip()
    if not tree: 
        break
    total += 1
    tree_dic[tree] += 1

tree_res = sorted(tree_dic,key = lambda x:x[0]) #문자열 순서대로 출력

for i in tree_res:
    print('%s %.4f' %(i,tree_dic[i]/total*100))