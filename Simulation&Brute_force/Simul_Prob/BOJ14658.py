#하늘에서 별똥별이 빗발친다

#문제
# L*L 크기의 트램펄린을 준비했다. 
# 별똥별이 어디로 떨어질지는 이미 알고 있기 때문에, 욱제는 이 트램펄린으로 최대한 많은 별똥별을 우주로 튕겨낼 계획이다. 
# 하지만 학교 예산으로 트램펄린을 구매하는 욱제는 이 긴급한 와중에도 예산 심의 통과를 기다리느라 바쁘다!
# 욱제를 도와 세계를 구하자. 
# 최대한 많은 별똥별을 튕겨내도록 트램펄린을 배치했을 때, 지구에는 몇 개의 별똥별이 부딪히게 될까? 
# (별똥별이 떨어지는 위치는 겹치지 않으며 별똥별은 트램펄린의 모서리에 부딪혀도 튕겨나간다!) 트램펄린은 비스듬하게 배치 할 수 없다.

#입력
# 첫째 줄에 네 정수 N, M, L, K가 주어진다. 
# (1 ≤ N, M ≤ 500,000, 1 ≤ L ≤ 100,000, 1 ≤ K ≤ 100) N은 별똥별이 떨어지는 구역의 가로길이, M은 세로길이, L은 트램펄린의 한 변의 길이, K는 별똥별의 수를 뜻한다. 
# 이후 K개의 줄에 걸쳐 별똥별이 떨어지는 위치의 좌표 (x, y)가 주어진다. (0 ≤ x ≤ N, 0 ≤ y ≤ M)

#출력
# 욱제가 트램펄린으로 최대한 많은 별똥별을 튕겨낼 때, 지구에 부딪히는 별똥별의 개수를 출력한다.

import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())
#N은 별똥별이 떨어지는 구역의 가로길이, M은 세로길이, L은 트램펄린의 한 변의 길이, K는 별똥별의 수를 뜻한다.
stars = []

for _ in range(k):
    star_xy = list(map(int,input().split()))
    stars.append(star_xy)
#print(stars[1][0])

def check(x,y):
    star_cnt = 0
    for i in range(k):
        star_x = stars[i][0]
        star_y = stars[i][1]

        #print(star_x,star_y)
        if x<=star_x and star_x <= x+l and y <= star_y and star_y <= y+l: 
            star_cnt += 1
    return star_cnt

def solution(k,stars):
    max_star = 0
    #좌상단
    for i in range(k):
        #우상단.
        for j in range(k):
            x,y = stars[i][0],stars[j][1]
            #print(x,y)
            max_star = max(max_star,check(x,y))
    return k-max_star
#solution(k,stars)
print(solution(k,stars))