#멀티탭 스케줄링 (골드 1)

# 예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,

#1 키보드
#2 헤어드라이기
#3 핸드폰 충전기
#4 디지털 카메라 충전기
#5 키보드
#6 헤어드라이기

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
tools = list(map(int,input().split()))# ex) 2 3 2 3 1 2 7

plug = [0] * (n) #멀티탭
tool_idx = 0
tmp = 0
tmp_i = 0
count = 0
for i in tools:
    #멀티탭에 같은 전기용품이 있는경우
    if i in plug:
        pass
    #멀티탭이 아직 비어 있는 경우
    elif 0 in plug:
        plug[plug.index(0)] = i #0이 있는 곳(즉 비어있는 멀티탭)에 제품을 꼽아
    #멀티탭에 빈자리 x, 현재 꽃혀있는 것과 다를때
    else:
        for j in plug:
            #현재 꽂혀있는것이 더이상 쓰이지 않을 경우 
            if j not in tools[tool_idx:]:
                tmp = j
                break
            #현재 꽂혀있는 제품이 또 쓰이는 경우
            elif tools[tool_idx:].index(j) > tmp_i:# 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다.
                tmp = j
                tmp_i = tools[tool_idx:].index(j)
        plug[plug.index(tmp)] = i
        tmp = tmp_i = 0
        count += 1
    tool_idx += 1

print(count)
# N, K = map(int, input().split())
# scheduling = list(map(int, input().split()))

# adaptor = [0] * N
# count = 0
# scheduling_idx = 0
# tmp = 0
# tmp_i = 0

# for i in scheduling:
#     # 멀티탭에 같은 전기용품이 있을 때
#     if i in adaptor:
#         pass
#     # 멀티탭이 아직 채워지지 않았을 때
#     elif 0 in adaptor:
#         adaptor[adaptor.index(0)] = i
#     # 멀티탭에 빈자리 없고 현재 꽂혀 있는 전기용품들과 다를 때
#     else:
#         for j in adaptor:
#             # 현재 꽂혀있는 전기용품이 더 이상 사용되지 않는다면
#             if j not in scheduling[scheduling_idx:]:
#                 tmp = j
#                 break
#             #현재 꽂혀있는 전기용품이 이후에도 사용될 때
#             elif scheduling[scheduling_idx:].index(j) > tmp_i:  # 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다.
#                 tmp = j
#                 tmp_i = scheduling[scheduling_idx:].index(j)
#         adaptor[adaptor.index(tmp)] = i
#         tmp = tmp_i = 0
#         count += 1
#     scheduling_idx += 1

# print(count)